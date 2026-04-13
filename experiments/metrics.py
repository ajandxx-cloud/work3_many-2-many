"""
experiments/metrics.py — Metric computation for DRT simulation results.

Defines three dataclasses:
  PassengerRecord  — per-passenger simulation outcome
  SimulationResult — aggregated result from one simulation run
  MetricsResult    — 9 computed performance metrics

The main entry point is:
  compute_metrics(result: SimulationResult) -> MetricsResult

All metrics return 0.0 when no passengers were accepted, so callers
never encounter division-by-zero errors.

Metric definitions
------------------
acceptance_rate : fraction of requests accepted ∈ [0, 1]
vehicle_km      : total distance driven by all vehicles (km)
avg_wait        : mean wait time for accepted passengers (seconds)
p95_wait        : 95th-percentile wait time for accepted passengers (seconds)
avg_walk        : mean total walking distance (pickup + dropoff) in meters
avg_ivt         : mean in-vehicle travel time (seconds)
detour_ratio    : mean (ivt / direct_time) for passengers with direct_time > 0
fairness_index  : Gini coefficient of |total_disutility| across accepted passengers
cpu_time        : wall-clock seconds for the simulation run (passed through)
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np


# ---------------------------------------------------------------------------
# Dataclasses
# ---------------------------------------------------------------------------


@dataclass
class PassengerRecord:
    """Per-passenger outcome from one simulation run."""

    request_id: str
    passenger_type: str        # "price_sensitive" | "time_sensitive" | "walk_sensitive"
    accepted: bool
    wait_time: float           # seconds from request arrival to scheduled pickup (0 if rejected)
    pickup_walk: float         # meters walked to pickup meeting point
    dropoff_walk: float        # meters walked from dropoff meeting point
    ivt: float                 # in-vehicle travel time (seconds)
    direct_time: float         # Euclidean origin→destination distance / speed (seconds)
    total_disutility: float    # MNL utility value (typically negative)


@dataclass
class SimulationResult:
    """Aggregated outcome from a complete simulation run."""

    records: list[PassengerRecord]
    total_vehicle_km: float    # total vehicle distance driven (km)
    cpu_time: float            # wall-clock seconds for the simulation


@dataclass
class MetricsResult:
    """Ten performance metrics computed from a SimulationResult."""

    acceptance_rate: float     # ∈ [0, 1]
    vehicle_km: float          # km
    avg_wait: float            # seconds
    p95_wait: float            # seconds
    avg_walk: float            # meters
    avg_ivt: float             # seconds
    detour_ratio: float        # dimensionless (≥ 1 when service adds detour)
    fairness_index: float      # Gini coefficient ∈ [0, 1]
    cpu_time: float            # seconds
    social_welfare: float = 0.0  # W = sum_r[z_r*U_rb* - (1-z_r)*gamma]; default 0.0


# ---------------------------------------------------------------------------
# Gini coefficient helper
# ---------------------------------------------------------------------------


def _gini(values: list[float]) -> float:
    """Compute the Gini coefficient of a list of non-negative values.

    Uses the standard pairwise-sum formula:
        G = Σ_i Σ_j |x_i - x_j| / (2 · n² · mean(x))

    Returns 0.0 if fewer than 2 values or mean is zero.
    """
    n = len(values)
    if n < 2:
        return 0.0
    arr = np.array(values, dtype=float)
    mean_val = arr.mean()
    if mean_val == 0.0:
        return 0.0
    # Efficient O(n log n) Gini via sorted-array formula
    arr_sorted = np.sort(arr)
    # Gini = (2 * Σ i*x_i / (n * sum)) - (n+1)/n
    # Equivalent to pairwise formula but O(n log n)
    indices = np.arange(1, n + 1, dtype=float)
    gini = (2.0 * np.sum(indices * arr_sorted) / (n * arr_sorted.sum())) - (n + 1.0) / n
    return float(np.clip(gini, 0.0, 1.0))


# ---------------------------------------------------------------------------
# Main computation
# ---------------------------------------------------------------------------


def compute_metrics(result: SimulationResult) -> MetricsResult:
    """Compute all 9 performance metrics from a SimulationResult.

    Args:
        result: Completed simulation output.

    Returns:
        MetricsResult with all fields populated (no None values).
        All time-based statistics return 0.0 when no passengers were accepted.
    """
    records = result.records
    accepted = [r for r in records if r.accepted]

    # 1. Acceptance rate
    if records:
        acceptance_rate = len(accepted) / len(records)
    else:
        acceptance_rate = 0.0

    # 2. Vehicle km — passed through directly
    vehicle_km = result.total_vehicle_km

    # 3. Average and p95 wait time
    if accepted:
        wait_times = [r.wait_time for r in accepted]
        avg_wait = float(np.mean(wait_times))
        p95_wait = float(np.percentile(wait_times, 95))
    else:
        avg_wait = 0.0
        p95_wait = 0.0

    # 4. Average total walk distance (pickup + dropoff)
    if accepted:
        avg_walk = float(np.mean([r.pickup_walk + r.dropoff_walk for r in accepted]))
    else:
        avg_walk = 0.0

    # 5. Average in-vehicle time
    if accepted:
        avg_ivt = float(np.mean([r.ivt for r in accepted]))
    else:
        avg_ivt = 0.0

    # 6. Detour ratio — per-passenger ivt/direct_time, skip zero direct_time
    eligible = [r for r in accepted if r.direct_time > 0.0]
    if eligible:
        detour_ratio = float(np.mean([r.ivt / r.direct_time for r in eligible]))
    else:
        detour_ratio = 0.0

    # 7. Fairness index — Gini of |total_disutility| across accepted passengers
    if len(accepted) >= 2:
        disutilities = [abs(r.total_disutility) for r in accepted]
        fairness_index = _gini(disutilities)
    else:
        fairness_index = 0.0

    # 8. CPU time — passed through directly
    cpu_time = result.cpu_time

    return MetricsResult(
        acceptance_rate=acceptance_rate,
        vehicle_km=vehicle_km,
        avg_wait=avg_wait,
        p95_wait=p95_wait,
        avg_walk=avg_walk,
        avg_ivt=avg_ivt,
        detour_ratio=detour_ratio,
        fairness_index=fairness_index,
        cpu_time=cpu_time,
    )


def vkm_per_trip(vehicle_km: float, n_requests: int, acceptance_rate: float) -> float:
    """Compute vehicle-km per accepted trip.

    Correct denominator: n_requests * acceptance_rate = accepted trip count.
    This is dimensionally consistent: km / trip.

    Args:
        vehicle_km: Total vehicle distance driven (km).
        n_requests: Total number of requests in the scenario (before MNL filtering).
        acceptance_rate: Fraction of requests accepted in [0, 1].

    Returns:
        float: vkm per accepted trip, or 0.0 if no trips were accepted.
    """
    accepted_trips = n_requests * acceptance_rate
    if accepted_trips <= 0.0:
        return 0.0
    return vehicle_km / accepted_trips


def compute_social_welfare(records: list[PassengerRecord], gamma: float) -> float:
    """Compute social welfare W = sum_r[z_r * U_rb* - (1-z_r) * gamma].

    Accepted passengers (z_r=1) contribute total_disutility (U_rb*, typically
    negative -- utility relative to outside option).
    Rejected passengers (z_r=0) contribute -gamma (rejection penalty).
    At gamma=0 rejected passengers contribute 0.

    Args:
        records: Per-passenger records from one SimulationResult.
        gamma: Non-negative rejection penalty (the sweep parameter Gamma).

    Returns:
        float: Social welfare sum. Higher is better; typically negative.
    """
    total = 0.0
    for r in records:
        if r.accepted:
            total += r.total_disutility   # z_r * U_rb*
        else:
            total -= gamma                # -(1 - z_r) * gamma
    return total
