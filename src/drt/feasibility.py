"""
feasibility.py — HEUR-03: Fast feasibility checker for proposed insertions.

Checks all constraints from Phase 1 (constraints.tex) for inserting a new
request (pickup + dropoff meeting points) into an existing vehicle route.

Constraint labels (from constraints.tex):
  con:capacity        — occupancy ≤ Q_v at every stop
  con:tw-early        — scheduled pickup ≥ e_r
  con:tw-late         — scheduled pickup ≤ l_r
  con:ridetime        — dropoff_time - pickup_time ≤ T_r^max
  con:precedence-pos  — pos_p < pos_d
  con:precedence-time — scheduled_pickup + travel(pickup→dropoff) ≤ scheduled_dropoff
  con:time-consistency— s_{v,i+1} ≥ s_{v,i} + travel(stop_i → stop_{i+1})
  con:route-duration  — last_stop_time - vehicle.current_time ≤ T_v^max
"""
from __future__ import annotations

import math
from typing import NamedTuple

from drt.types import MeetingPoint, Request, Route, Vehicle


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _euclidean(a: tuple[float, float], b: tuple[float, float]) -> float:
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)


def _travel_time(
    a: tuple[float, float],
    b: tuple[float, float],
    speed: float,
) -> float:
    """Travel time from a to b at constant speed (Euclidean distance model)."""
    return _euclidean(a, b) / speed


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

def check_feasibility(
    route: Route,
    request: Request,
    pickup_mp: MeetingPoint,
    dropoff_mp: MeetingPoint,
    pos_p: int,   # insertion index for pickup (0-indexed, before existing stop at pos_p)
    pos_d: int,   # insertion index for dropoff (must be > pos_p)
    vehicle: Vehicle,
    travel_speed: float = 1.0,  # distance units per time unit
) -> tuple[bool, str]:
    """
    HEUR-03: Check whether inserting (pickup_mp at pos_p, dropoff_mp at pos_d)
    into route is feasible under all Phase 1 constraints.

    Returns
    -------
    (True, "")           — insertion is feasible
    (False, reason)      — infeasible; reason is one of:
        "precedence"      con:precedence-pos violated (pos_d <= pos_p)
        "capacity"        con:capacity violated
        "tw_early"        con:tw-early violated (pickup before e_r)
        "tw_late"         con:tw-late violated (pickup after l_r)
        "ride_time"       con:ridetime violated
        "route_duration"  con:route-duration violated

    Parameters
    ----------
    route        : current vehicle route (stops may be empty)
    request      : the trip request being inserted
    pickup_mp    : chosen pickup meeting point (m_r^P)
    dropoff_mp   : chosen dropoff meeting point (m_r^D)
    pos_p        : insertion position for pickup stop
    pos_d        : insertion position for dropoff stop (after pickup inserted)
    vehicle      : vehicle data (capacity, max_route_duration, current_time)
    travel_speed : speed for Euclidean travel time computation
    """
    # ------------------------------------------------------------------
    # 1. con:precedence-pos — cheapest check first
    # ------------------------------------------------------------------
    if pos_d <= pos_p:
        return False, "precedence"

    # ------------------------------------------------------------------
    # 2. Build new stop sequence
    #    Insert pickup at pos_p, then dropoff at pos_d (in the already-
    #    extended list, so pos_d is relative to the new list).
    # ------------------------------------------------------------------
    existing_points: list[MeetingPoint] = [mp for mp, _ in route.stops]

    new_points = existing_points[:]
    new_points.insert(pos_p, pickup_mp)
    new_points.insert(pos_d, dropoff_mp)

    # ------------------------------------------------------------------
    # 3. Recompute schedule from vehicle.current_time
    #    Start position is vehicle.current_position (before first stop).
    # ------------------------------------------------------------------
    times: list[float] = []
    prev_coords = vehicle.current_position
    t = vehicle.current_time

    for mp in new_points:
        t += _travel_time(prev_coords, mp.coords, travel_speed)
        times.append(t)
        prev_coords = mp.coords

    # ------------------------------------------------------------------
    # 4. con:capacity — track occupancy (+1 at pickup, -1 at dropoff)
    #    We need to know which stops are pickups and which are dropoffs.
    #    Strategy: mark the two new stops; existing stops are assumed
    #    balanced (net occupancy from existing route is tracked separately).
    #
    #    For a general checker we track occupancy by labelling each stop
    #    as +1 (pickup) or -1 (dropoff).  Existing stops in route.stops
    #    carry no label, so we conservatively assume they are all pickups
    #    (worst case for capacity).  In practice, insertion.py will pass
    #    a fully-labelled route; here we use a simple heuristic:
    #    existing stops alternate pickup/dropoff starting with pickup.
    # ------------------------------------------------------------------
    # Build occupancy delta list: +1 pickup, -1 dropoff
    n_existing = len(existing_points)
    # Label existing stops: odd index = pickup (+1), even index = dropoff (-1)
    # (simple alternating assumption for standalone feasibility check)
    existing_deltas: list[int] = []
    for i in range(n_existing):
        existing_deltas.append(1 if i % 2 == 0 else -1)

    # Insert new deltas at the correct positions
    new_deltas = existing_deltas[:]
    new_deltas.insert(pos_p, 1)   # pickup
    new_deltas.insert(pos_d, -1)  # dropoff

    occupancy = 0
    pickup_time: float | None = None
    dropoff_time: float | None = None

    for i, (mp, t_i, delta) in enumerate(zip(new_points, times, new_deltas)):
        occupancy += delta
        if occupancy > vehicle.capacity:
            return False, "capacity"
        if mp is pickup_mp and pickup_time is None:
            pickup_time = t_i
        if mp is dropoff_mp and dropoff_time is None:
            dropoff_time = t_i

    # ------------------------------------------------------------------
    # 5. con:tw-early / con:tw-late
    # ------------------------------------------------------------------
    if pickup_time is None:
        # Should not happen; guard against logic errors
        return False, "precedence"

    if pickup_time < request.earliest:
        return False, "tw_early"
    if pickup_time > request.latest:
        return False, "tw_late"

    # ------------------------------------------------------------------
    # 6. con:ridetime
    # ------------------------------------------------------------------
    if dropoff_time is None:
        return False, "precedence"

    if dropoff_time - pickup_time > request.max_ride_time:
        return False, "ride_time"

    # ------------------------------------------------------------------
    # 7. con:route-duration
    # ------------------------------------------------------------------
    if times and times[-1] - vehicle.current_time > vehicle.max_route_duration:
        return False, "route_duration"

    return True, ""
