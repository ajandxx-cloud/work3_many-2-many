"""
alns.py — HEUR-04/05/06: Rolling horizon controller and ALNS operators.

HEUR-04: RollingHorizon class — triggers re-optimization every delta minutes
         on active requests within the planning horizon [t, t+H].
HEUR-05: Five ALNS destroy/repair operators:
         Destroy: random_removal, worst_removal, related_removal
         Repair:  greedy_insertion, regret_insertion
HEUR-06: benchmark() — 200-request, 15-vehicle timing validation (< 1s avg).
"""
from __future__ import annotations

import math
import random
import time
from copy import deepcopy
from dataclasses import dataclass, field

from drt.candidate import euclidean
from drt.feasibility import check_feasibility
from drt.insertion import InsertionResult, evaluate_insertion
from drt.types import MeetingPoint, Request, Route, Vehicle


# ---------------------------------------------------------------------------
# State container
# ---------------------------------------------------------------------------

@dataclass
class ALNSState:
    """Mutable ALNS solution state."""
    routes: dict        # vehicle_id -> Route
    unassigned: list    # list[Request] removed by destroy operators
    cost: float = 0.0
    completed_ids: set = field(default_factory=set)  # IDs of requests already served (pruned from routes)
    extra_vehicle_km: float = 0.0  # km driven in completed (pruned) trips, for RollingHorizon variants
    pickup_times: dict = field(default_factory=dict)  # request_id -> actual scheduled pickup time


# ---------------------------------------------------------------------------
# Internal helpers
# ---------------------------------------------------------------------------

def _route_cost(routes: dict, vehicles: dict, travel_speed: float = 1.0) -> float:
    """Sum of total route distances across all vehicles."""
    total = 0.0
    for vid, route in routes.items():
        v = vehicles[vid]
        prev = v.current_position
        for stop in route.stops:
            mp = stop[0]  # first element is always MeetingPoint
            total += euclidean(prev, mp.coords) / travel_speed
            prev = mp.coords
    return total


def _request_cost(request: Request, route: Route, vehicle: Vehicle,
                  travel_speed: float = 1.0) -> float:
    """Approximate cost contribution of a request already in a route."""
    stops = route.stops
    # Find pickup and dropoff positions by request id stored in stop metadata.
    # Since stops only store (MeetingPoint, time), we use a simple proxy:
    # cost = IVT proxy (distance between consecutive stops attributed to request)
    # For simplicity, use walk distance from origin/destination to nearest stop.
    if not stops:
        return 0.0
    # Proxy: distance from origin to nearest stop + distance from nearest stop to destination
    min_pu = min(euclidean(request.origin, mp.coords) for mp, _ in stops)
    min_do = min(euclidean(request.destination, mp.coords) for mp, _ in stops)
    return min_pu + min_do


def _find_request_stops(request: Request, routes: dict) -> tuple[str | None, int, int]:
    """
    Find which vehicle and stop indices contain request's pickup/dropoff.
    Returns (vehicle_id, pickup_idx, dropoff_idx) or (None, -1, -1).

    Since stops don't carry request IDs, we use a tag stored in the stop tuple.
    Stops inserted by ALNS are tagged as (MeetingPoint, time, request_id, role).
    Legacy stops (from evaluate_insertion) are (MeetingPoint, time).
    """
    for vid, route in routes.items():
        pu_idx = -1
        do_idx = -1
        for i, stop in enumerate(route.stops):
            if len(stop) >= 3 and stop[2] == request.id:
                if len(stop) >= 4:
                    if stop[3] == 'pickup':
                        pu_idx = i
                    elif stop[3] == 'dropoff':
                        do_idx = i
                else:
                    if pu_idx == -1:
                        pu_idx = i
                    else:
                        do_idx = i
        if pu_idx != -1 and do_idx != -1:
            return vid, pu_idx, do_idx
    return None, -1, -1


def _apply_insertion(state: ALNSState, result: InsertionResult, request: Request,
                     vehicles: dict | None = None, travel_speed: float = 1.0) -> None:
    """Apply an InsertionResult to state.routes in-place, tagging stops with request id.

    If vehicles is provided, compute and store actual scheduled arrival times.
    Otherwise stores 0.0 as placeholder times.
    """
    route = state.routes.get(result.vehicle_id)
    if route is None:
        route = Route(vehicle_id=result.vehicle_id, stops=[])
        state.routes[result.vehicle_id] = route

    # Insert pickup then dropoff (pos_d is relative to list after pickup inserted)
    route.stops.insert(result.pos_p, (result.pickup_mp, 0.0, request.id, 'pickup'))
    route.stops.insert(result.pos_d, (result.dropoff_mp, 0.0, request.id, 'dropoff'))

    # Recompute scheduled times for all stops if vehicle info available
    if vehicles is not None:
        vehicle = vehicles.get(result.vehicle_id)
        if vehicle is not None:
            t = vehicle.current_time
            prev = vehicle.current_position
            new_stops = []
            for stop in route.stops:
                mp = stop[0]
                t += euclidean(prev, mp.coords) / travel_speed
                if len(stop) >= 4:
                    new_stops.append((mp, t, stop[2], stop[3]))
                elif len(stop) >= 3:
                    new_stops.append((mp, t, stop[2]))
                else:
                    new_stops.append((mp, t))
                prev = mp.coords
            route.stops = new_stops


def _remove_request(state: ALNSState, request: Request) -> bool:
    """Remove a request's pickup and dropoff stops from routes. Returns True if found."""
    vid, pu_idx, do_idx = _find_request_stops(request, state.routes)
    if vid is None:
        return False
    route = state.routes[vid]
    # Remove higher index first to preserve lower index
    high, low = (pu_idx, do_idx) if pu_idx > do_idx else (do_idx, pu_idx)
    del route.stops[high]
    del route.stops[low]
    state.unassigned.append(request)
    return True


def _assigned_requests(state: ALNSState) -> list[Request]:
    """Collect all Request objects currently assigned (tagged in stops)."""
    seen: dict[str, Request] = {}
    for route in state.routes.values():
        for stop in route.stops:
            if len(stop) >= 3:
                rid = stop[2]
                if rid not in seen:
                    # We only have the id; store a sentinel — caller must pass request map
                    pass
    # This helper is only useful when we have a request registry; see callers.
    return []


# ---------------------------------------------------------------------------
# Destroy operators
# ---------------------------------------------------------------------------

def random_removal(state: ALNSState, k: int, rng: random.Random,
                   request_registry: dict) -> ALNSState:
    """
    HEUR-05 Destroy 1: Remove k random assigned requests.

    Parameters
    ----------
    state            : current ALNS state (will be deep-copied)
    k                : number of requests to remove
    rng              : seeded Random instance
    request_registry : dict[request_id -> Request] for lookup
    """
    new_state = deepcopy(state)
    assigned_ids = _get_assigned_ids(new_state)
    if not assigned_ids:
        return new_state
    to_remove = rng.sample(assigned_ids, min(k, len(assigned_ids)))
    for rid in to_remove:
        req = request_registry[rid]
        _remove_request(new_state, req)
    return new_state


def worst_removal(state: ALNSState, k: int, request_registry: dict,
                  vehicles: dict, travel_speed: float = 1.0) -> ALNSState:
    """
    HEUR-05 Destroy 2: Remove k requests with highest cost contribution.
    Cost proxy: walk distance from origin/destination to assigned meeting points.
    """
    new_state = deepcopy(state)
    assigned_ids = _get_assigned_ids(new_state)
    if not assigned_ids:
        return new_state

    costs = []
    for rid in assigned_ids:
        req = request_registry[rid]
        vid, pu_idx, do_idx = _find_request_stops(req, new_state.routes)
        if vid is None:
            continue
        route = new_state.routes[vid]
        pu_mp = route.stops[pu_idx][0]
        do_mp = route.stops[do_idx][0]
        c = (euclidean(req.origin, pu_mp.coords)
             + euclidean(req.destination, do_mp.coords)
             + euclidean(pu_mp.coords, do_mp.coords) / travel_speed)
        costs.append((c, rid))

    costs.sort(reverse=True)
    for _, rid in costs[:k]:
        req = request_registry[rid]
        _remove_request(new_state, req)
    return new_state


def related_removal(state: ALNSState, k: int, rng: random.Random,
                    request_registry: dict, travel_speed: float = 1.0) -> ALNSState:
    """
    HEUR-05 Destroy 3: Remove k spatially/temporally related requests.
    Relatedness = euclidean(origin_i, origin_j) + |earliest_i - earliest_j|.
    Lower score = more similar = more related.
    """
    new_state = deepcopy(state)
    assigned_ids = _get_assigned_ids(new_state)
    if not assigned_ids:
        return new_state

    seed_id = rng.choice(assigned_ids)
    seed_req = request_registry[seed_id]

    others = [rid for rid in assigned_ids if rid != seed_id]
    if not others:
        _remove_request(new_state, seed_req)
        return new_state

    scores = []
    for rid in others:
        r = request_registry[rid]
        relatedness = (euclidean(seed_req.origin, r.origin)
                       + abs(seed_req.earliest - r.earliest))
        scores.append((relatedness, rid))
    scores.sort()  # ascending: most related first

    to_remove = [seed_id] + [rid for _, rid in scores[:k - 1]]
    for rid in to_remove:
        req = request_registry[rid]
        _remove_request(new_state, req)
    return new_state


# ---------------------------------------------------------------------------
# Repair operators
# ---------------------------------------------------------------------------

def greedy_insertion(state: ALNSState, vehicles: dict, meeting_points: list,
                     rho_p: float, rho_d: float, k_top: int,
                     cost_weights: tuple, travel_speed: float = 1.0,
                     rng: random.Random | None = None) -> ALNSState:
    """
    HEUR-05 Repair 1: Reinsert unassigned requests in random order using
    minimum incremental cost (calls evaluate_insertion).
    """
    new_state = deepcopy(state)
    pending = list(new_state.unassigned)
    if rng:
        rng.shuffle(pending)
    new_state.unassigned = []

    # Build routes dict with plain (MeetingPoint, time) stops for evaluate_insertion
    plain_routes = _to_plain_routes(new_state.routes)

    for req in pending:
        result = evaluate_insertion(
            req, plain_routes, vehicles, meeting_points,
            rho_p, rho_d, k_top, cost_weights, travel_speed
        )
        if result is not None:
            _apply_insertion(new_state, result, req, vehicles, travel_speed)
            # Keep plain_routes in sync
            plain_routes = _to_plain_routes(new_state.routes)
        else:
            new_state.unassigned.append(req)

    return new_state


def regret_insertion(state: ALNSState, vehicles: dict, meeting_points: list,
                     rho_p: float, rho_d: float, k_top: int,
                     cost_weights: tuple, travel_speed: float = 1.0) -> ALNSState:
    """
    HEUR-05 Repair 2: Regret-2 heuristic.
    For each unassigned request, compute best and second-best insertion cost.
    regret_value = second_best - best (higher = insert now).
    Insert highest-regret request first; repeat.
    """
    new_state = deepcopy(state)
    pending = list(new_state.unassigned)
    new_state.unassigned = []

    while pending:
        plain_routes = _to_plain_routes(new_state.routes)
        best_regret = -math.inf
        best_req = None
        best_result = None

        for req in pending:
            # Collect all feasible insertion costs across vehicles
            all_costs = _all_insertion_costs(
                req, plain_routes, vehicles, meeting_points,
                rho_p, rho_d, k_top, cost_weights, travel_speed
            )
            if not all_costs:
                continue
            all_costs.sort(key=lambda x: x[0])
            c1 = all_costs[0][0]
            c2 = all_costs[1][0] if len(all_costs) > 1 else c1 + 1e9
            regret = c2 - c1
            if regret > best_regret:
                best_regret = regret
                best_req = req
                best_result = all_costs[0][1]

        if best_req is None:
            # No feasible insertion for any remaining request
            new_state.unassigned.extend(pending)
            break

        _apply_insertion(new_state, best_result, best_req, vehicles, travel_speed)
        pending.remove(best_req)

    return new_state


# ---------------------------------------------------------------------------
# Internal helpers for repair operators
# ---------------------------------------------------------------------------

def _to_plain_routes(routes: dict) -> dict:
    """Convert tagged routes to plain (MeetingPoint, time) format for evaluate_insertion."""
    plain = {}
    for vid, route in routes.items():
        plain_stops = [(stop[0], stop[1]) for stop in route.stops]
        plain[vid] = Route(vehicle_id=vid, stops=plain_stops)
    return plain


def _get_assigned_ids(state: ALNSState) -> list[str]:
    """Return list of request IDs currently assigned in routes."""
    ids = []
    seen = set()
    for route in state.routes.values():
        for stop in route.stops:
            if len(stop) >= 3:
                rid = stop[2]
                if rid not in seen:
                    seen.add(rid)
                    ids.append(rid)
    return ids


def _all_insertion_costs(
    request: Request, plain_routes: dict, vehicles: dict,
    meeting_points: list, rho_p: float, rho_d: float, k_top: int,
    cost_weights: tuple, travel_speed: float
) -> list[tuple[float, InsertionResult]]:
    """Return list of (cost, InsertionResult) for all feasible insertions."""
    from drt.candidate import generate_candidates
    alpha_op, alpha_wait, alpha_walk, alpha_ivt = cost_weights
    results = []

    pickup_cands = generate_candidates(request, meeting_points, rho_p, k_top, 'pickup')
    dropoff_cands = generate_candidates(request, meeting_points, rho_d, k_top, 'dropoff')
    if not pickup_cands or not dropoff_cands:
        return results

    for vid, vehicle in vehicles.items():
        route = plain_routes.get(vid, Route(vehicle_id=vid, stops=[]))
        n = len(route.stops)
        from drt.insertion import _route_distance
        dist_before = _route_distance(route.stops, vehicle.current_position)

        for mp_p in pickup_cands:
            for mp_d in dropoff_cands:
                for pos_p in range(n + 1):
                    for pos_d in range(pos_p + 1, n + 2):
                        ok, _ = check_feasibility(
                            route, request, mp_p, mp_d, pos_p, pos_d, vehicle, travel_speed
                        )
                        if not ok:
                            continue
                        new_stops = list(route.stops)
                        new_stops.insert(pos_p, (mp_p, 0.0))
                        new_stops.insert(pos_d, (mp_d, 0.0))
                        t = vehicle.current_time
                        prev = vehicle.current_position
                        pickup_time = 0.0
                        for i, (mp, _) in enumerate(new_stops):
                            t += euclidean(prev, mp.coords) / travel_speed
                            if i == pos_p:
                                pickup_time = t
                            prev = mp.coords
                        dist_after = _route_distance(new_stops, vehicle.current_position)
                        delta_op = dist_after - dist_before
                        delta_wait = max(0.0, pickup_time - request.earliest)
                        delta_walk = (euclidean(request.origin, mp_p.coords)
                                      + euclidean(mp_d.coords, request.destination))
                        delta_ivt = euclidean(mp_p.coords, mp_d.coords) / travel_speed
                        cost = (alpha_op * delta_op + alpha_wait * delta_wait
                                + alpha_walk * delta_walk + alpha_ivt * delta_ivt)
                        ir = InsertionResult(
                            vehicle_id=vid, pos_p=pos_p, pos_d=pos_d,
                            pickup_mp=mp_p, dropoff_mp=mp_d, incremental_cost=cost
                        )
                        results.append((cost, ir))
    return results


# ---------------------------------------------------------------------------
# RollingHorizon controller
# ---------------------------------------------------------------------------

class RollingHorizon:
    """
    HEUR-04: Online rolling horizon controller for many-to-many DRT.

    Maintains an active request set and triggers ALNS re-optimization
    every delta minutes over a planning horizon of H minutes.
    """

    def __init__(
        self,
        vehicles: dict,           # vehicle_id -> Vehicle
        meeting_points: list,     # list[MeetingPoint]
        rho_p: float,             # pickup walking radius
        rho_d: float,             # dropoff walking radius
        k_top: int,               # max candidates per side
        H: float,                 # horizon window (minutes)
        delta: float,             # re-optimization interval (minutes)
        cost_weights: tuple = (1.0, 1.0, 1.0, 1.0),
        travel_speed: float = 1.0,
        alns_iterations: int = 50,
        destroy_fraction: float = 0.3,
        seed: int = 42,
        collect_diagnostics: bool = False,
    ):
        self.vehicles = vehicles
        self.meeting_points = meeting_points
        self.rho_p = rho_p
        self.rho_d = rho_d
        self.k_top = k_top
        self.H = H
        self.delta = delta
        self.cost_weights = cost_weights
        self.travel_speed = travel_speed
        self.alns_iterations = alns_iterations
        self.destroy_fraction = destroy_fraction
        self.rng = random.Random(seed)
        self.collect_diagnostics = collect_diagnostics
        self.diagnostic_trace: list[dict] = []
        self.operator_counts: dict[str, int] = {}
        self.improvement_counts: dict[str, int] = {}

        # Current solution state
        self.routes: dict = {vid: Route(vehicle_id=vid, stops=[]) for vid in vehicles}
        self.active_requests: dict = {}   # request_id -> Request
        self.request_registry: dict = {}  # request_id -> Request (all ever seen)
        self.completed_request_ids: set = set()  # IDs of requests already served
        self.accumulated_vehicle_km: float = 0.0  # total km driven including completed trips
        self.pickup_times: dict = {}  # request_id -> actual scheduled pickup time

    def add_request(self, request: Request, current_time: float) -> None:
        """Add a new incoming request to the active set."""
        self.active_requests[request.id] = request
        self.request_registry[request.id] = request

    def reoptimize(self, current_time: float) -> dict:
        """
        HEUR-04: Run ALNS on active requests in window [current_time, current_time + H].
        Returns dict with keys: routes, unassigned, cost, time_ms, objective, n_accepted.
        """
        t0 = time.perf_counter()

        # Advance vehicle state to current_time:
        # - Update current_time to simulation time
        # - Update current_position to last completed stop (stops with scheduled time <= current_time)
        # - Remove completed stops from routes so feasibility checks work correctly
        vehicles_at_t = {}
        pruned_routes = {}
        for vid, v in self.vehicles.items():
            route = self.routes.get(vid, Route(vehicle_id=vid, stops=[]))
            # Separate completed stops (scheduled time <= current_time) from future stops
            # Stop time is stored at index 1 in tagged stops (mp, time, req_id, role)
            # or index 1 in plain stops (mp, time). Use index 1 for both.
            completed = [s for s in route.stops if len(s) >= 2 and s[1] <= current_time]
            future = [s for s in route.stops if len(s) >= 2 and s[1] > current_time]
            # Vehicle position is last completed stop, or initial position if none
            if completed:
                last_pos = completed[-1][0].coords
                # Track completed request IDs so they aren't re-inserted
                for s in completed:
                    if len(s) >= 3:
                        self.completed_request_ids.add(s[2])
                        # Record pickup time for wait-time tracking
                        if len(s) >= 4 and s[3] == 'pickup':
                            self.pickup_times[s[2]] = s[1]
                # Accumulate vehicle_km for completed stops
                prev = v.current_position
                for s in completed:
                    mp = s[0]
                    self.accumulated_vehicle_km += euclidean(prev, mp.coords) / 1000.0
                    prev = mp.coords
            else:
                last_pos = v.current_position
            vehicles_at_t[vid] = Vehicle(
                id=v.id,
                capacity=v.capacity,
                max_route_duration=v.max_route_duration,
                current_position=last_pos,
                current_time=max(v.current_time, current_time),
            )
            pruned_routes[vid] = Route(vehicle_id=vid, stops=future)

        # Use pruned routes (future stops only) for ALNS
        self.routes = pruned_routes

        # Filter active requests within horizon
        horizon_requests = {
            rid: req for rid, req in self.active_requests.items()
            if req.earliest <= current_time + self.H
        }

        if not horizon_requests:
            elapsed_ms = (time.perf_counter() - t0) * 1000
            result = {
                'routes': self.routes,
                'unassigned': [],
                'cost': 0.0,
                'time_ms': elapsed_ms,
                'objective': 0.0,
                'n_accepted': 0,
            }
            if self.collect_diagnostics:
                result['diagnostic_trace'] = list(self.diagnostic_trace)
                result['operator_counts'] = dict(self.operator_counts)
                result['improvement_counts'] = dict(self.improvement_counts)
            return result

        # Build initial state from current routes
        # Add unassigned horizon requests so repair operators can insert them
        # Use completed_request_ids + currently-in-route IDs to avoid re-inserting
        already_assigned = self.completed_request_ids | set(_get_assigned_ids(ALNSState(
            routes=deepcopy(self.routes), unassigned=[], cost=0.0
        )))
        unassigned_horizon = [
            req for rid, req in horizon_requests.items()
            if rid not in already_assigned
        ]
        current_state = ALNSState(
            routes=deepcopy(self.routes),
            unassigned=unassigned_horizon,
            cost=_route_cost(self.routes, vehicles_at_t, self.travel_speed),
        )

        # Determine k for destroy operators
        n_assigned = len(_get_assigned_ids(current_state))
        k_destroy = max(1, int(n_assigned * self.destroy_fraction))

        best_state = deepcopy(current_state)

        destroy_ops = [
            ("random_removal", lambda s: random_removal(s, k_destroy, self.rng, self.request_registry)),
            ("worst_removal", lambda s: worst_removal(s, k_destroy, self.request_registry,
                                                      vehicles_at_t, self.travel_speed)),
            ("related_removal", lambda s: related_removal(s, k_destroy, self.rng,
                                                          self.request_registry, self.travel_speed)),
        ]

        for iteration in range(self.alns_iterations):
            iter_t0 = time.perf_counter()
            # Select destroy operator uniformly
            destroy_name, destroy_fn = self.rng.choice(destroy_ops)
            destroyed = destroy_fn(best_state)

            # Select repair operator (alternate greedy / regret)
            if iteration % 2 == 0:
                repair_name = "greedy_insertion"
                repaired = greedy_insertion(
                    destroyed, vehicles_at_t, self.meeting_points,
                    self.rho_p, self.rho_d, self.k_top,
                    self.cost_weights, self.travel_speed, self.rng
                )
            else:
                repair_name = "regret_insertion"
                repaired = regret_insertion(
                    destroyed, vehicles_at_t, self.meeting_points,
                    self.rho_p, self.rho_d, self.k_top,
                    self.cost_weights, self.travel_speed
                )

            repaired.cost = _route_cost(repaired.routes, vehicles_at_t, self.travel_speed)

            # Acceptance: prefer fewer unassigned (more accepted), break ties by cost
            repaired_unassigned = len(repaired.unassigned)
            best_unassigned = len(best_state.unassigned)
            previous_best_cost = best_state.cost
            previous_best_unassigned = best_unassigned
            improved = (
                repaired_unassigned < previous_best_unassigned or
                (repaired_unassigned == previous_best_unassigned and
                 repaired.cost < previous_best_cost)
            )
            accepted_candidate = False
            if (repaired_unassigned < best_unassigned or
                    (repaired_unassigned == best_unassigned and
                     repaired.cost <= best_state.cost)):
                best_state = repaired
                accepted_candidate = True

            if self.collect_diagnostics:
                self.operator_counts[destroy_name] = self.operator_counts.get(destroy_name, 0) + 1
                self.operator_counts[repair_name] = self.operator_counts.get(repair_name, 0) + 1
                if improved:
                    self.improvement_counts[destroy_name] = self.improvement_counts.get(destroy_name, 0) + 1
                    self.improvement_counts[repair_name] = self.improvement_counts.get(repair_name, 0) + 1
                self.diagnostic_trace.append({
                    "iteration": iteration,
                    "objective": repaired.cost,
                    "best_objective": best_state.cost,
                    "runtime_ms": (time.perf_counter() - iter_t0) * 1000,
                    "accepted_count": len(_get_assigned_ids(repaired)),
                    "unassigned_count": len(repaired.unassigned),
                    "destroy_operator": destroy_name,
                    "repair_operator": repair_name,
                    "improved": improved,
                    "accepted_improvement": accepted_candidate and improved,
                    "accepted": accepted_candidate,
                })

        # Update controller state
        self.routes = best_state.routes
        # Remove accepted requests from active set and track them
        accepted_ids = set(_get_assigned_ids(best_state))
        n_accepted = len(accepted_ids)
        for rid in accepted_ids:
            self.active_requests.pop(rid, None)
            self.completed_request_ids.add(rid)

        elapsed_ms = (time.perf_counter() - t0) * 1000

        result = {
            'routes': self.routes,
            'unassigned': best_state.unassigned,
            'cost': best_state.cost,
            'time_ms': elapsed_ms,
            'objective': best_state.cost,
            'n_accepted': n_accepted,
        }
        if self.collect_diagnostics:
            result['diagnostic_trace'] = list(self.diagnostic_trace)
            result['operator_counts'] = dict(self.operator_counts)
            result['improvement_counts'] = dict(self.improvement_counts)
        return result

    def run_simulation(
        self, requests: list[Request], arrival_times: list[float]
    ) -> dict:
        """
        Run full rolling horizon simulation.
        Processes requests in arrival order, triggers reoptimize() every delta minutes.
        Returns final routes, total cost, and timing stats.
        """
        t_start = time.perf_counter()
        decision_times: list[float] = []

        # Sort by arrival time
        events = sorted(zip(arrival_times, requests), key=lambda x: x[0])

        current_time = 0.0
        next_reopt = self.delta
        event_idx = 0

        while event_idx < len(events):
            arr_time, req = events[event_idx]

            # Advance time to next event or next reopt trigger
            if arr_time <= next_reopt:
                current_time = arr_time
                self.add_request(req, current_time)
                event_idx += 1
            else:
                current_time = next_reopt
                t0 = time.perf_counter()
                self.reoptimize(current_time)
                decision_times.append(time.perf_counter() - t0)
                next_reopt += self.delta

        # Final reoptimize after all requests arrive
        t0 = time.perf_counter()
        final_result = self.reoptimize(current_time)
        decision_times.append(time.perf_counter() - t0)

        total_time = time.perf_counter() - t_start
        avg_time = sum(decision_times) / len(decision_times) if decision_times else 0.0

        return {
            'routes': self.routes,
            'cost': final_result['cost'],
            'n_accepted': final_result['n_accepted'],
            'n_unassigned': len(final_result.get('unassigned', [])),
            'total_time_s': total_time,
            'avg_reopt_time_s': avg_time,
            'n_reoptimizations': len(decision_times),
            'diagnostic_trace': final_result.get('diagnostic_trace', []),
            'operator_counts': final_result.get('operator_counts', {}),
            'improvement_counts': final_result.get('improvement_counts', {}),
        }


# ---------------------------------------------------------------------------
# HEUR-06: Timing benchmark
# ---------------------------------------------------------------------------

def benchmark(
    n_requests: int = 200,
    n_vehicles: int = 15,
    n_meeting_points: int = 20,
    rho: float = 10.0,
    k_top: int = 5,
    seed: int = 42,
) -> dict:
    """
    HEUR-06: Generate n_requests random requests and run rolling horizon.
    Returns {'avg_time_per_request_s': float, 'total_time_s': float, 'n_requests': int}.

    Grid: [0, 100]^2 coordinate space.
    Vehicles: capacity=8, max_route_duration=300 minutes.
    Meeting points: uniform grid.
    """
    rng = random.Random(seed)

    # Generate meeting points on a grid
    grid_side = math.ceil(math.sqrt(n_meeting_points))
    step = 100.0 / max(grid_side - 1, 1)
    meeting_points = []
    for i in range(grid_side):
        for j in range(grid_side):
            if len(meeting_points) >= n_meeting_points:
                break
            mp = MeetingPoint(
                id=f"mp_{i}_{j}",
                coords=(i * step, j * step),
            )
            meeting_points.append(mp)
        if len(meeting_points) >= n_meeting_points:
            break

    # Generate vehicles
    vehicles = {}
    for i in range(n_vehicles):
        v = Vehicle(
            id=f"v{i}",
            capacity=8,
            max_route_duration=300.0,
            current_position=(rng.uniform(0, 100), rng.uniform(0, 100)),
            current_time=0.0,
        )
        vehicles[v.id] = v

    # Generate requests
    requests = []
    arrival_times = []
    for i in range(n_requests):
        origin = (rng.uniform(0, 100), rng.uniform(0, 100))
        destination = (rng.uniform(0, 100), rng.uniform(0, 100))
        earliest = rng.uniform(0, 120)
        latest = earliest + rng.uniform(10, 30)
        arr_time = rng.uniform(0, 100)
        req = Request(
            id=f"r{i}",
            origin=origin,
            destination=destination,
            earliest=earliest,
            latest=latest,
            max_ride_time=60.0,
        )
        requests.append(req)
        arrival_times.append(arr_time)

    # Run rolling horizon
    rh = RollingHorizon(
        vehicles=vehicles,
        meeting_points=meeting_points,
        rho_p=rho,
        rho_d=rho,
        k_top=k_top,
        H=60.0,
        delta=10.0,
        cost_weights=(1.0, 1.0, 1.0, 1.0),
        travel_speed=1.0,
        alns_iterations=50,
        destroy_fraction=0.3,
        seed=seed,
    )

    t0 = time.perf_counter()
    result = rh.run_simulation(requests, arrival_times)
    total_time = time.perf_counter() - t0

    avg_time_per_request = total_time / n_requests

    return {
        'avg_time_per_request_s': avg_time_per_request,
        'total_time_s': total_time,
        'n_requests': n_requests,
        'n_accepted': result.get('n_accepted', 0),
        'n_reoptimizations': result.get('n_reoptimizations', 0),
    }
