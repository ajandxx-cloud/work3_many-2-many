"""
insertion.py — HEUR-02: Online insertion evaluator for many-to-many DRT.

For each incoming request, enumerates all (vehicle, pos_p, pos_d, mp_p, mp_d)
combinations, checks feasibility, computes incremental cost, and returns the
best feasible insertion.

Incremental cost components (notation from Phase 1):
  delta_C_op   — additional route distance (operational cost)
  delta_C_wait — max(0, pickup_time - request.earliest)  (wait time)
  delta_C_walk — d(origin, mp_p) + d(mp_d, destination)  (walk distance)
  delta_C_IVT  — d(mp_p, mp_d) / speed                   (in-vehicle time)

Weighted cost: alpha_op * delta_C_op + alpha_wait * delta_C_wait
             + alpha_walk * delta_C_walk + alpha_ivt * delta_C_IVT
"""
from __future__ import annotations

from dataclasses import dataclass

from drt.candidate import euclidean, generate_candidates
from drt.feasibility import check_feasibility
from drt.types import MeetingPoint, Request, Route, Vehicle


@dataclass
class InsertionResult:
    """Best feasible insertion found by evaluate_insertion."""

    vehicle_id: str
    pos_p: int           # insertion index for pickup stop
    pos_d: int           # insertion index for dropoff stop
    pickup_mp: MeetingPoint
    dropoff_mp: MeetingPoint
    incremental_cost: float


def _route_distance(
    stops: list,
    vehicle_pos: tuple[float, float],
) -> float:
    """Total Euclidean distance of route from vehicle current position."""
    if not stops:
        return 0.0
    pts = [vehicle_pos] + [mp.coords for mp, _ in stops]
    return sum(euclidean(pts[i], pts[i + 1]) for i in range(len(pts) - 1))


def evaluate_insertion(
    request: Request,
    routes: dict,          # vehicle_id -> Route
    vehicles: dict,        # vehicle_id -> Vehicle
    meeting_points: list[MeetingPoint],
    rho_p: float,          # rho^P — walking radius for pickup
    rho_d: float,          # rho^D — walking radius for dropoff
    k_top: int,            # k^top — max candidates per side
    cost_weights: tuple[float, float, float, float] = (1.0, 1.0, 1.0, 1.0),
    travel_speed: float = 1.0,
) -> InsertionResult | None:
    """
    HEUR-02: Enumerate all (vehicle, pos_p, pos_d, mp_p, mp_d) combinations,
    check feasibility, compute incremental cost, return best feasible insertion.

    Returns None if no feasible insertion exists (request rejected).
    """
    alpha_op, alpha_wait, alpha_walk, alpha_ivt = cost_weights
    best: InsertionResult | None = None

    pickup_candidates = generate_candidates(request, meeting_points, rho_p, k_top, "pickup")
    dropoff_candidates = generate_candidates(request, meeting_points, rho_d, k_top, "dropoff")

    # No candidates within walking radius — reject immediately
    if not pickup_candidates or not dropoff_candidates:
        return None

    for vid, vehicle in vehicles.items():
        route = routes.get(vid)
        if route is None:
            route = Route(vehicle_id=vid, stops=[])
        n = len(route.stops)
        dist_before = _route_distance(route.stops, vehicle.current_position)

        for mp_p in pickup_candidates:
            for mp_d in dropoff_candidates:
                for pos_p in range(n + 1):
                    for pos_d in range(pos_p + 1, n + 2):
                        ok, _ = check_feasibility(
                            route, request, mp_p, mp_d, pos_p, pos_d, vehicle, travel_speed
                        )
                        if not ok:
                            continue

                        # Build new stop list to compute pickup departure time
                        new_stops = list(route.stops)
                        new_stops.insert(pos_p, (mp_p, 0.0))
                        new_stops.insert(pos_d, (mp_d, 0.0))

                        # Recompute schedule to get pickup time
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
                        delta_walk = (
                            euclidean(request.origin, mp_p.coords)
                            + euclidean(mp_d.coords, request.destination)
                        )
                        delta_ivt = euclidean(mp_p.coords, mp_d.coords) / travel_speed

                        cost = (
                            alpha_op * delta_op
                            + alpha_wait * delta_wait
                            + alpha_walk * delta_walk
                            + alpha_ivt * delta_ivt
                        )

                        if best is None or cost < best.incremental_cost:
                            best = InsertionResult(
                                vehicle_id=vid,
                                pos_p=pos_p,
                                pos_d=pos_d,
                                pickup_mp=mp_p,
                                dropoff_mp=mp_d,
                                incremental_cost=cost,
                            )
    return best
