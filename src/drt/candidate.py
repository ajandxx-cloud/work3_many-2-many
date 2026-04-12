"""
candidate.py — HEUR-01: Top-k candidate meeting point generation.

Filters meeting points by walking radius (rho_p = ρ^P for pickup,
rho_d = ρ^D for dropoff), ranks by Euclidean distance, returns top-k.
"""
from __future__ import annotations

import math

from drt.types import MeetingPoint, Request


def euclidean(a: tuple[float, float], b: tuple[float, float]) -> float:
    """Euclidean distance between two 2-D points."""
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)


def generate_candidates(
    request: Request,
    meeting_points: list[MeetingPoint],
    rho: float,
    k_top: int,
    side: str,  # 'pickup' or 'dropoff'
) -> list[MeetingPoint]:
    """
    HEUR-01: Filter meeting points by walking radius rho (ρ^P or ρ^D),
    rank by Euclidean distance from the relevant trip endpoint,
    return at most k_top candidates in ascending distance order.

    Parameters
    ----------
    request       : the incoming trip request r
    meeting_points: full set of candidate meeting points M
    rho           : maximum walking radius (ρ^P for pickup, ρ^D for dropoff)
    k_top         : maximum number of candidates to return (k^top)
    side          : 'pickup'  → reference point is request.origin  (o_r)
                    'dropoff' → reference point is request.destination (d_r)

    Returns
    -------
    List of MeetingPoint, length ≤ k_top, sorted by ascending distance.
    Empty list if no meeting point lies within rho.
    """
    if side == "pickup":
        ref = request.origin
    else:
        ref = request.destination

    within: list[tuple[float, MeetingPoint]] = [
        (euclidean(ref, mp.coords), mp)
        for mp in meeting_points
        if euclidean(ref, mp.coords) <= rho
    ]
    within.sort(key=lambda x: x[0])
    return [mp for _, mp in within[:k_top]]
