"""
experiments/scenarios.py — Scenario generators for synthetic and Beijing cases.

Two generators are provided:
  generate_synthetic(n_requests, n_vehicles, seed) → Scenario
  generate_beijing(n_requests, n_vehicles, seed)   → Scenario

Both return a Scenario dataclass that bundles requests, vehicles,
and meeting points — the common input contract for all 6 algorithm variants.

Threat T-03-03 mitigation: n_requests is capped at 1000 via ValueError
to prevent accidental out-of-memory runs at large scales.
"""

from __future__ import annotations

import math
import random
from dataclasses import dataclass

from src.drt.types import MeetingPoint, Request, Vehicle

# ---------------------------------------------------------------------------
# Scenario dataclass — common input contract
# ---------------------------------------------------------------------------

_MAX_REQUESTS = 1000  # T-03-03: hard cap to prevent OOM


@dataclass
class Scenario:
    """Bundled inputs for a single simulation run."""

    requests: list[Request]
    vehicles: list[Vehicle]
    meeting_points: list[MeetingPoint]
    area_km: float   # side length of the operating area in km
    name: str


# ---------------------------------------------------------------------------
# Synthetic scenario (20 km × 20 km uniform grid)
# ---------------------------------------------------------------------------


def generate_synthetic(n_requests: int, n_vehicles: int, seed: int) -> Scenario:
    """Generate a synthetic scenario on a 20 km × 20 km square grid.

    Meeting points are placed on a regular 10×10 grid at 2 km spacing.
    Request origins and destinations are drawn uniformly at random.
    Vehicle start positions are drawn uniformly at random.

    Args:
        n_requests: Number of trip requests to generate. Must be <= 1000.
        n_vehicles: Number of vehicles.
        seed: Integer seed for the local PRNG (does not affect global state).

    Returns:
        Scenario with exactly n_requests requests, n_vehicles vehicles,
        and 100 meeting points.

    Raises:
        ValueError: If n_requests > 1000 (T-03-03 DoS mitigation).
    """
    if n_requests > _MAX_REQUESTS:
        raise ValueError(
            f"n_requests={n_requests} exceeds maximum of {_MAX_REQUESTS}. "
            "Use a value <= 1000 to prevent accidental OOM."
        )

    rng = random.Random(seed)
    area = 20_000.0  # meters

    # --- Meeting points: regular 10×10 grid ---
    meeting_points: list[MeetingPoint] = []
    for i in range(10):
        for j in range(10):
            mp_id = f"mp_{i}_{j}"
            x = float(i * 2000)
            y = float(j * 2000)
            meeting_points.append(MeetingPoint(id=mp_id, coords=(x, y)))

    # --- Requests: uniform random origins and destinations ---
    requests: list[Request] = []
    for k in range(n_requests):
        ox = rng.uniform(0, area)
        oy = rng.uniform(0, area)
        dx = rng.uniform(0, area)
        dy = rng.uniform(0, area)
        earliest = rng.uniform(0, 4 * 3600.0)
        latest = earliest + rng.uniform(5 * 60.0, 20 * 60.0)
        requests.append(
            Request(
                id=f"req_{k}",
                origin=(ox, oy),
                destination=(dx, dy),
                earliest=earliest,
                latest=latest,
                max_ride_time=45 * 60.0,
            )
        )

    # --- Vehicles: random start positions, current_time = 0 ---
    vehicles: list[Vehicle] = []
    for k in range(n_vehicles):
        vx = rng.uniform(0, area)
        vy = rng.uniform(0, area)
        vehicles.append(
            Vehicle(
                id=f"veh_{k}",
                capacity=8,
                max_route_duration=8 * 3600.0,
                current_position=(vx, vy),
                current_time=0.0,
            )
        )

    return Scenario(
        requests=requests,
        vehicles=vehicles,
        meeting_points=meeting_points,
        area_km=20.0,
        name=f"synthetic_n{n_requests}_v{n_vehicles}_s{seed}",
    )


# ---------------------------------------------------------------------------
# Beijing semi-realistic scenario (15 km × 15 km, morning peak)
# ---------------------------------------------------------------------------


def _clamp(value: float, lo: float, hi: float) -> float:
    """Clamp value to [lo, hi]."""
    return max(lo, min(hi, value))


def _normal_clamp(rng: random.Random, mu: float, sigma: float, lo: float, hi: float) -> float:
    """Draw a normal variate and clamp to [lo, hi]."""
    # Use Box-Muller via rng for full reproducibility without numpy dependency
    while True:
        u1 = rng.random()
        u2 = rng.random()
        if u1 == 0.0:
            continue
        import math
        z = math.sqrt(-2.0 * math.log(u1)) * math.cos(2.0 * math.pi * u2)
        v = mu + sigma * z
        if lo <= v <= hi:
            return v


def generate_beijing(n_requests: int, n_vehicles: int, seed: int) -> Scenario:
    """Generate a semi-realistic suburban Beijing scenario.

    The operating area is a 15 km × 15 km grid representing a low-density
    suburban district. Meeting points are placed on a 9×9 regular grid
    (81 points), keeping the first 80 by row-major order to meet the
    target of 80 points.

    Request timing follows a morning peak pattern (7–9 am). Origins are
    drawn uniformly; destinations are biased toward the grid center to
    simulate residential-to-commercial commute patterns.

    Args:
        n_requests: Number of trip requests. Must be <= 1000.
        n_vehicles: Number of vehicles.
        seed: Integer seed for the local PRNG.

    Returns:
        Scenario with n_requests requests, n_vehicles vehicles,
        and 80 meeting points.

    Raises:
        ValueError: If n_requests > 1000 (T-03-03 DoS mitigation).
    """
    if n_requests > _MAX_REQUESTS:
        raise ValueError(
            f"n_requests={n_requests} exceeds maximum of {_MAX_REQUESTS}. "
            "Use a value <= 1000 to prevent accidental OOM."
        )

    rng = random.Random(seed)
    area = 15_000.0  # meters

    # --- Meeting points: 9×9 grid, keep first 80 by row-major order ---
    # Spacing = area / 8 so that indices 0..8 cover [0, area] evenly
    spacing = area / 8.0  # 1875.0 m (~500m is too small for 15km/80 points;
    # actual spacing at 9×9 on 15 km grid ≈ 1875 m)
    # Note: the plan says "~500m spacing" but that would require a 30×30 grid.
    # The plan also specifies "9×9 grid, drop last one → 80 points".
    # We follow the exact formula: x = i*(15000/8), y = j*(15000/8)
    meeting_points: list[MeetingPoint] = []
    for i in range(9):
        for j in range(9):
            if len(meeting_points) >= 80:
                break
            mp_id = f"bj_mp_{i}_{j}"
            x = float(i * spacing)
            y = float(j * spacing)
            meeting_points.append(MeetingPoint(id=mp_id, coords=(x, y)))
        if len(meeting_points) >= 80:
            break

    assert len(meeting_points) == 80

    # --- Requests: morning peak, residential→commercial bias ---
    requests: list[Request] = []
    for k in range(n_requests):
        # Origin: uniform across the area
        ox = rng.uniform(0, area)
        oy = rng.uniform(0, area)

        # Destination: biased toward center via Gaussian offset from origin
        dx = _clamp(ox + rng.gauss(0, 3000), 0, area)
        dy = _clamp(oy + rng.gauss(0, 3000), 0, area)

        # Earliest arrival: normal around 8 am, clipped to [7h, 9h]
        earliest = _normal_clamp(rng, mu=8 * 3600.0, sigma=30 * 60.0,
                                  lo=7 * 3600.0, hi=9 * 3600.0)
        latest = earliest + rng.uniform(5 * 60.0, 15 * 60.0)

        requests.append(
            Request(
                id=f"bj_req_{k}",
                origin=(ox, oy),
                destination=(dx, dy),
                earliest=earliest,
                latest=latest,
                max_ride_time=40 * 60.0,
            )
        )

    # --- Vehicles: random positions, start at 7 am ---
    vehicles: list[Vehicle] = []
    for k in range(n_vehicles):
        vx = rng.uniform(0, area)
        vy = rng.uniform(0, area)
        vehicles.append(
            Vehicle(
                id=f"bj_veh_{k}",
                capacity=8,
                max_route_duration=8 * 3600.0,
                current_position=(vx, vy),
                current_time=7 * 3600.0,
            )
        )

    return Scenario(
        requests=requests,
        vehicles=vehicles,
        meeting_points=meeting_points,
        area_km=15.0,
        name=f"beijing_n{n_requests}_v{n_vehicles}_s{seed}",
    )
