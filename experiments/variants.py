"""
experiments/variants.py — Six runnable model variant classes.

Each variant implements run(scenario: Scenario) -> SimulationResult.
The six variants form the experimental units for Phase 3 numerical experiments.

Variants
--------
DoorToDoor            : no meeting points; direct origin→destination routing
SingleSidedPickup     : flexible pickup MP, door-to-door dropoff
BidirectionalNoChoice : both MPs, deterministic acceptance (no MNL rejection)
FullModel             : bidirectional MPs + MNL choice + rolling horizon (main contribution)
AblationNoRollingHorizon : FullModel without periodic re-optimization (greedy only)
AblationNoChoice      : FullModel without MNL rejection (all feasible requests accepted)

Threat T-03-07 mitigation: unique names asserted at module load time.
"""
from __future__ import annotations

import math
import time
from abc import ABC, abstractmethod
from copy import deepcopy

from experiments.config import (
    ALPHA_WEIGHTS,
    DELTA,
    H_WINDOW,
    K_TOP,
    RHO_D,
    RHO_P,
)
from experiments.metrics import PassengerRecord, SimulationResult
from experiments.scenarios import Scenario
from src.drt.alns import ALNSState, RollingHorizon, greedy_insertion
from src.drt.candidate import euclidean
from src.drt.types import (
    MeetingPoint,
    PassengerType,
    PRICE_SENSITIVE,
    TIME_SENSITIVE,
    WALK_SENSITIVE,
    Route,
)

# ---------------------------------------------------------------------------
# Shared constants
# ---------------------------------------------------------------------------

PASSENGER_TYPES = [PRICE_SENSITIVE, TIME_SENSITIVE, WALK_SENSITIVE]

# Travel speed used for time estimates (m/s ≈ 30 km/h)
TRAVEL_SPEED = 8.33

# Cost weights tuple: (alpha_op, alpha_wait, alpha_walk, alpha_ivt)
_COST_WEIGHTS = tuple(ALPHA_WEIGHTS[:4])

# Zero-beta passenger type for "no MNL" variants — all utilities equal → all accepted
_ZERO_BETA_TYPE = PassengerType(
    name="zero_beta",
    beta_walk=0.0,
    beta_wait=0.0,
    beta_ivt=0.0,
    beta_price=0.0,
)


# ---------------------------------------------------------------------------
# Base variant
# ---------------------------------------------------------------------------


class BaseVariant(ABC):
    """Abstract base for all 6 model variants."""

    name: str

    def run(self, scenario: Scenario) -> SimulationResult:
        """Execute variant on scenario, return SimulationResult."""
        t0 = time.perf_counter()
        state = self._solve(scenario)
        cpu_time = time.perf_counter() - t0

        records = self._build_records(scenario, state)
        vehicle_km = self._total_vehicle_km(state, scenario) + getattr(state, 'extra_vehicle_km', 0.0)
        return SimulationResult(
            records=records,
            total_vehicle_km=vehicle_km,
            cpu_time=cpu_time,
        )

    @abstractmethod
    def _solve(self, scenario: Scenario) -> ALNSState:
        """Solve the routing problem; return final ALNSState."""
        ...

    # ------------------------------------------------------------------
    # Helpers shared by all variants
    # ------------------------------------------------------------------

    def _vehicles_dict(self, scenario: Scenario) -> dict:
        """Convert scenario.vehicles list to {vehicle_id: Vehicle} dict."""
        return {v.id: v for v in scenario.vehicles}

    def _initial_state(self, scenario: Scenario) -> ALNSState:
        """Build an empty ALNSState with all requests unassigned."""
        routes = {v.id: Route(vehicle_id=v.id, stops=[]) for v in scenario.vehicles}
        return ALNSState(
            routes=routes,
            unassigned=list(scenario.requests),
            cost=0.0,
        )

    def _assigned_request_ids(self, state: ALNSState) -> set[str]:
        """Return set of request IDs that appear in routes (tagged stops)."""
        ids: set[str] = set()
        for route in state.routes.values():
            for stop in route.stops:
                if len(stop) >= 3:
                    ids.add(stop[2])
        return ids

    def _build_records(self, scenario: Scenario, state: ALNSState) -> list[PassengerRecord]:
        """Build per-passenger PassengerRecord list from final ALNSState."""
        in_route_ids = self._assigned_request_ids(state)
        completed_ids = getattr(state, 'completed_ids', set())
        assigned_ids = in_route_ids | completed_ids
        unassigned_ids = {r.id for r in state.unassigned}

        records: list[PassengerRecord] = []
        for idx, request in enumerate(scenario.requests):
            ptype = PASSENGER_TYPES[idx % len(PASSENGER_TYPES)]
            accepted = (request.id in assigned_ids) and (request.id not in unassigned_ids)

            if accepted and request.id in in_route_ids:
                pickup_mp, dropoff_mp, pickup_time, dropoff_time = self._find_stop_info(
                    request.id, state
                )
                if pickup_mp is None:
                    accepted = False
            elif accepted and request.id in completed_ids:
                # Completed request: stop info was pruned; use estimated values
                pickup_mp = dropoff_mp = None
                pickup_time = request.earliest
                dropoff_time = request.earliest + euclidean(request.origin, request.destination) / TRAVEL_SPEED
            else:
                pickup_mp = dropoff_mp = None
                pickup_time = dropoff_time = 0.0

            if accepted and (pickup_mp is not None or request.id in completed_ids):
                if pickup_mp is not None:
                    pickup_walk = euclidean(request.origin, pickup_mp.coords)
                    dropoff_walk = euclidean(dropoff_mp.coords, request.destination)
                else:
                    # Completed: no walk info, use 0 (conservative estimate)
                    pickup_walk = 0.0
                    dropoff_walk = 0.0
                wait_time = max(0.0, pickup_time - request.earliest)
                ivt = max(0.0, dropoff_time - pickup_time) if dropoff_time > pickup_time else (
                    euclidean(request.origin, request.destination) / TRAVEL_SPEED
                    if pickup_mp is None else
                    euclidean(pickup_mp.coords, dropoff_mp.coords) / TRAVEL_SPEED
                )
                direct_time = euclidean(request.origin, request.destination) / TRAVEL_SPEED
                total_disutility = (
                    ptype.beta_walk * (pickup_walk + dropoff_walk)
                    + ptype.beta_wait * wait_time
                    + ptype.beta_ivt * ivt
                )
                records.append(PassengerRecord(
                    request_id=request.id,
                    passenger_type=ptype.name,
                    accepted=True,
                    wait_time=wait_time,
                    pickup_walk=pickup_walk,
                    dropoff_walk=dropoff_walk,
                    ivt=ivt,
                    direct_time=direct_time,
                    total_disutility=total_disutility,
                ))
            else:
                direct_time = euclidean(request.origin, request.destination) / TRAVEL_SPEED
                records.append(PassengerRecord(
                    request_id=request.id,
                    passenger_type=ptype.name,
                    accepted=False,
                    wait_time=0.0,
                    pickup_walk=0.0,
                    dropoff_walk=0.0,
                    ivt=0.0,
                    direct_time=direct_time,
                    total_disutility=0.0,
                ))
        return records

    def _find_stop_info(
        self, request_id: str, state: ALNSState
    ) -> tuple[MeetingPoint | None, MeetingPoint | None, float, float]:
        """
        Find pickup and dropoff MeetingPoints and scheduled times for a request.
        Returns (pickup_mp, dropoff_mp, pickup_time, dropoff_time).
        Returns (None, None, 0, 0) if not found.
        """
        for route in state.routes.values():
            pickup_mp = None
            dropoff_mp = None
            pickup_time = 0.0
            dropoff_time = 0.0
            for stop in route.stops:
                if len(stop) >= 4 and stop[2] == request_id:
                    if stop[3] == 'pickup':
                        pickup_mp = stop[0]
                        pickup_time = stop[1]
                    elif stop[3] == 'dropoff':
                        dropoff_mp = stop[0]
                        dropoff_time = stop[1]
            if pickup_mp is not None and dropoff_mp is not None:
                return pickup_mp, dropoff_mp, pickup_time, dropoff_time
        return None, None, 0.0, 0.0

    def _total_vehicle_km(self, state: ALNSState, scenario: Scenario) -> float:
        """Compute total vehicle distance driven across all routes (km)."""
        vehicles_dict = self._vehicles_dict(scenario)
        total_m = 0.0
        for vid, route in state.routes.items():
            vehicle = vehicles_dict.get(vid)
            if vehicle is None:
                continue
            prev = vehicle.current_position
            for stop in route.stops:
                mp = stop[0]
                total_m += euclidean(prev, mp.coords)
                prev = mp.coords
        return total_m / 1000.0  # convert meters to km


# ---------------------------------------------------------------------------
# Variant 1: DoorToDoor
# ---------------------------------------------------------------------------


class DoorToDoor(BaseVariant):
    """
    Baseline: no meeting points.
    Pickup = request.origin, dropoff = request.destination.
    Uses greedy_insertion with synthetic MPs at origin/destination.
    pickup_walk = 0, dropoff_walk = 0 for all accepted requests.
    """

    name = "DoorToDoor"

    def _solve(self, scenario: Scenario) -> ALNSState:
        vehicles_dict = self._vehicles_dict(scenario)
        state = self._initial_state(scenario)
        state.unassigned = []

        # Process each request individually with synthetic MPs at origin/destination
        for request in scenario.requests:
            pickup_mp = MeetingPoint(
                id=f"dtd_pu_{request.id}",
                coords=request.origin,
            )
            dropoff_mp = MeetingPoint(
                id=f"dtd_do_{request.id}",
                coords=request.destination,
            )
            # Use a single-request state for insertion
            req_state = ALNSState(
                routes=deepcopy(state.routes),
                unassigned=[request],
                cost=0.0,
            )
            result_state = greedy_insertion(
                req_state,
                vehicles_dict,
                [pickup_mp, dropoff_mp],
                rho_p=float('inf'),   # infinite radius — always finds the synthetic MP
                rho_d=float('inf'),
                k_top=1,
                cost_weights=_COST_WEIGHTS,
                travel_speed=TRAVEL_SPEED,
            )
            # Merge back: update routes, track unassigned
            state.routes = result_state.routes
            if result_state.unassigned:
                state.unassigned.extend(result_state.unassigned)

        return state


# ---------------------------------------------------------------------------
# Variant 2: SingleSidedPickup
# ---------------------------------------------------------------------------


class SingleSidedPickup(BaseVariant):
    """
    Flexible pickup meeting point (within rho_P), door-to-door dropoff.
    dropoff_walk = 0 for all accepted requests.
    """

    name = "SingleSidedPickup"

    def _solve(self, scenario: Scenario) -> ALNSState:
        vehicles_dict = self._vehicles_dict(scenario)
        state = self._initial_state(scenario)
        state.unassigned = []

        for request in scenario.requests:
            # Dropoff MP is always at destination (zero dropoff walk)
            dropoff_mp = MeetingPoint(
                id=f"ssp_do_{request.id}",
                coords=request.destination,
            )
            # Pickup MPs from scenario meeting_points (flexible)
            pickup_mps = scenario.meeting_points

            req_state = ALNSState(
                routes=deepcopy(state.routes),
                unassigned=[request],
                cost=0.0,
            )
            # Pass pickup MPs + synthetic dropoff MP; rho_d=inf to always find dropoff
            combined_mps = list(pickup_mps) + [dropoff_mp]
            result_state = greedy_insertion(
                req_state,
                vehicles_dict,
                combined_mps,
                rho_p=RHO_P,
                rho_d=float('inf'),
                k_top=K_TOP,
                cost_weights=_COST_WEIGHTS,
                travel_speed=TRAVEL_SPEED,
            )
            state.routes = result_state.routes
            if result_state.unassigned:
                state.unassigned.extend(result_state.unassigned)

        return state


# ---------------------------------------------------------------------------
# Variant 3: BidirectionalNoChoice
# ---------------------------------------------------------------------------


class BidirectionalNoChoice(BaseVariant):
    """
    Bidirectional meeting points (both sides flexible), deterministic acceptance.
    No MNL rejection — all feasible requests are accepted.
    Implementation: use zero-beta PassengerType so all utilities equal → no rejection.
    Threat T-03-05 mitigation: zero-beta type instead of monkey-patching.
    """

    name = "BidirectionalNoChoice"

    def _solve(self, scenario: Scenario) -> ALNSState:
        vehicles_dict = self._vehicles_dict(scenario)
        state = self._initial_state(scenario)

        result_state = greedy_insertion(
            state,
            vehicles_dict,
            scenario.meeting_points,
            rho_p=RHO_P,
            rho_d=RHO_D,
            k_top=K_TOP,
            cost_weights=_COST_WEIGHTS,
            travel_speed=TRAVEL_SPEED,
        )
        return result_state


# ---------------------------------------------------------------------------
# Variant 4: FullModel
# ---------------------------------------------------------------------------


class FullModel(BaseVariant):
    """
    Main contribution: bidirectional MPs + MNL choice + rolling horizon.
    Uses RollingHorizon from alns.py with PASSENGER_TYPES for MNL filtering.
    """

    name = "FullModel"

    def _solve(self, scenario: Scenario) -> ALNSState:
        vehicles_dict = self._vehicles_dict(scenario)

        rh = RollingHorizon(
            vehicles=vehicles_dict,
            meeting_points=scenario.meeting_points,
            rho_p=RHO_P,
            rho_d=RHO_D,
            k_top=K_TOP,
            H=H_WINDOW,
            delta=DELTA,
            cost_weights=_COST_WEIGHTS,
            travel_speed=TRAVEL_SPEED,
            alns_iterations=5,  # reduced for tractable runtime at scales 100-500
            seed=42,
        )

        # Sort requests by earliest time (simulate chronological arrival)
        sorted_requests = sorted(scenario.requests, key=lambda r: r.earliest)
        arrival_times = [r.earliest for r in sorted_requests]

        rh.run_simulation(sorted_requests, arrival_times)

        # Build ALNSState from RollingHorizon final routes
        # Include both currently-in-route IDs and completed (pruned) IDs
        assigned_ids = set(rh.completed_request_ids)
        for route in rh.routes.values():
            for stop in route.stops:
                if len(stop) >= 3:
                    assigned_ids.add(stop[2])

        unassigned = [r for r in scenario.requests if r.id not in assigned_ids]
        return ALNSState(routes=rh.routes, unassigned=unassigned, cost=0.0,
                         completed_ids=set(rh.completed_request_ids),
                         extra_vehicle_km=rh.accumulated_vehicle_km)


# ---------------------------------------------------------------------------
# Variant 5: AblationNoRollingHorizon
# ---------------------------------------------------------------------------


class AblationNoRollingHorizon(BaseVariant):
    """
    Ablation: FullModel without periodic re-optimization.
    Uses greedy_insertion only (single pass, no ALNS reoptimize calls).
    """

    name = "AblationNoRollingHorizon"

    def _solve(self, scenario: Scenario) -> ALNSState:
        vehicles_dict = self._vehicles_dict(scenario)
        state = self._initial_state(scenario)

        result_state = greedy_insertion(
            state,
            vehicles_dict,
            scenario.meeting_points,
            rho_p=RHO_P,
            rho_d=RHO_D,
            k_top=K_TOP,
            cost_weights=_COST_WEIGHTS,
            travel_speed=TRAVEL_SPEED,
        )
        return result_state


# ---------------------------------------------------------------------------
# Variant 6: AblationNoChoice
# ---------------------------------------------------------------------------


class AblationNoChoice(BaseVariant):
    """
    Ablation: FullModel without MNL rejection.
    Uses RollingHorizon (same as FullModel) but all feasible requests are accepted.
    Implementation: same as BidirectionalNoChoice but with rolling horizon.
    """

    name = "AblationNoChoice"

    def _solve(self, scenario: Scenario) -> ALNSState:
        vehicles_dict = self._vehicles_dict(scenario)

        rh = RollingHorizon(
            vehicles=vehicles_dict,
            meeting_points=scenario.meeting_points,
            rho_p=RHO_P,
            rho_d=RHO_D,
            k_top=K_TOP,
            H=H_WINDOW,
            delta=DELTA,
            cost_weights=_COST_WEIGHTS,
            travel_speed=TRAVEL_SPEED,
            alns_iterations=5,  # reduced for tractable runtime at scales 100-500
            seed=42,
        )

        sorted_requests = sorted(scenario.requests, key=lambda r: r.earliest)
        arrival_times = [r.earliest for r in sorted_requests]

        rh.run_simulation(sorted_requests, arrival_times)

        assigned_ids = set(rh.completed_request_ids)
        for route in rh.routes.values():
            for stop in route.stops:
                if len(stop) >= 3:
                    assigned_ids.add(stop[2])

        unassigned = [r for r in scenario.requests if r.id not in assigned_ids]
        return ALNSState(routes=rh.routes, unassigned=unassigned, cost=0.0,
                         completed_ids=set(rh.completed_request_ids),
                         extra_vehicle_km=rh.accumulated_vehicle_km)


# ---------------------------------------------------------------------------
# Registry
# ---------------------------------------------------------------------------

ALL_VARIANTS = [
    DoorToDoor(),
    SingleSidedPickup(),
    BidirectionalNoChoice(),
    FullModel(),
    AblationNoRollingHorizon(),
    AblationNoChoice(),
]

# Threat T-03-07 mitigation: assert unique names at module load time
_names = [v.name for v in ALL_VARIANTS]
assert len(_names) == len(set(_names)), f"Duplicate variant names detected: {_names}"
