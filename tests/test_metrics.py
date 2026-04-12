"""
tests/test_metrics.py — Tests for metrics computation module.

Verifies:
  - MetricsResult has all 9 required fields
  - compute_metrics on empty result returns all-zero MetricsResult (no division by zero)
  - acceptance_rate computed correctly
  - vehicle_km passed through correctly
  - Gini coefficient = 0 when all passengers have equal disutility
  - Gini coefficient > 0 when disutility values differ
  - p95_wait correctly computes 95th percentile
  - detour_ratio = avg_ivt / avg_direct_time
  - cpu_time passed through from SimulationResult
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import math
import pytest
from experiments.metrics import (
    PassengerRecord,
    SimulationResult,
    MetricsResult,
    compute_metrics,
)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def make_record(
    request_id: str = "req_0",
    passenger_type: str = "time_sensitive",
    accepted: bool = True,
    wait_time: float = 300.0,
    pickup_walk: float = 200.0,
    dropoff_walk: float = 150.0,
    ivt: float = 900.0,
    direct_time: float = 600.0,
    total_disutility: float = -5.0,
) -> PassengerRecord:
    return PassengerRecord(
        request_id=request_id,
        passenger_type=passenger_type,
        accepted=accepted,
        wait_time=wait_time,
        pickup_walk=pickup_walk,
        dropoff_walk=dropoff_walk,
        ivt=ivt,
        direct_time=direct_time,
        total_disutility=total_disutility,
    )


def make_result(records=None, total_vehicle_km=10.0, cpu_time=1.5) -> SimulationResult:
    return SimulationResult(
        records=records if records is not None else [],
        total_vehicle_km=total_vehicle_km,
        cpu_time=cpu_time,
    )


# ---------------------------------------------------------------------------
# MetricsResult structure
# ---------------------------------------------------------------------------

class TestMetricsResultStructure:
    def test_has_all_9_fields(self):
        m = MetricsResult(
            acceptance_rate=0.0,
            vehicle_km=0.0,
            avg_wait=0.0,
            p95_wait=0.0,
            avg_walk=0.0,
            avg_ivt=0.0,
            detour_ratio=0.0,
            fairness_index=0.0,
            cpu_time=0.0,
        )
        assert hasattr(m, "acceptance_rate")
        assert hasattr(m, "vehicle_km")
        assert hasattr(m, "avg_wait")
        assert hasattr(m, "p95_wait")
        assert hasattr(m, "avg_walk")
        assert hasattr(m, "avg_ivt")
        assert hasattr(m, "detour_ratio")
        assert hasattr(m, "fairness_index")
        assert hasattr(m, "cpu_time")

    def test_no_none_fields_on_compute(self):
        result = make_result([make_record()])
        m = compute_metrics(result)
        for field_name in [
            "acceptance_rate", "vehicle_km", "avg_wait", "p95_wait",
            "avg_walk", "avg_ivt", "detour_ratio", "fairness_index", "cpu_time"
        ]:
            assert getattr(m, field_name) is not None, f"Field {field_name} is None"


# ---------------------------------------------------------------------------
# Empty result (0 records)
# ---------------------------------------------------------------------------

class TestEmptyResult:
    def test_no_error_on_empty(self):
        result = make_result(records=[])
        m = compute_metrics(result)
        assert isinstance(m, MetricsResult)

    def test_acceptance_rate_zero(self):
        m = compute_metrics(make_result(records=[]))
        assert m.acceptance_rate == 0.0

    def test_vehicle_km_passthrough(self):
        m = compute_metrics(make_result(records=[], total_vehicle_km=42.5))
        assert m.vehicle_km == 42.5

    def test_avg_wait_zero(self):
        m = compute_metrics(make_result(records=[]))
        assert m.avg_wait == 0.0

    def test_p95_wait_zero(self):
        m = compute_metrics(make_result(records=[]))
        assert m.p95_wait == 0.0

    def test_avg_walk_zero(self):
        m = compute_metrics(make_result(records=[]))
        assert m.avg_walk == 0.0

    def test_avg_ivt_zero(self):
        m = compute_metrics(make_result(records=[]))
        assert m.avg_ivt == 0.0

    def test_detour_ratio_zero(self):
        m = compute_metrics(make_result(records=[]))
        assert m.detour_ratio == 0.0

    def test_fairness_index_zero(self):
        m = compute_metrics(make_result(records=[]))
        assert m.fairness_index == 0.0

    def test_cpu_time_passthrough(self):
        m = compute_metrics(make_result(records=[], cpu_time=3.14))
        assert m.cpu_time == 3.14


# ---------------------------------------------------------------------------
# All rejected (no accepted records)
# ---------------------------------------------------------------------------

class TestAllRejected:
    def test_acceptance_rate_zero_when_all_rejected(self):
        records = [make_record(f"req_{i}", accepted=False) for i in range(5)]
        m = compute_metrics(make_result(records=records))
        assert m.acceptance_rate == 0.0

    def test_no_error_when_all_rejected(self):
        records = [make_record(f"req_{i}", accepted=False) for i in range(10)]
        m = compute_metrics(make_result(records=records))
        assert isinstance(m, MetricsResult)
        assert m.avg_wait == 0.0
        assert m.avg_ivt == 0.0


# ---------------------------------------------------------------------------
# Single accepted passenger
# ---------------------------------------------------------------------------

class TestSinglePassenger:
    def setup_method(self):
        self.record = make_record(
            wait_time=180.0,
            pickup_walk=100.0,
            dropoff_walk=50.0,
            ivt=600.0,
            direct_time=400.0,
            total_disutility=-3.0,
        )
        self.result = make_result(records=[self.record], cpu_time=2.0)
        self.m = compute_metrics(self.result)

    def test_acceptance_rate_one(self):
        assert self.m.acceptance_rate == 1.0

    def test_avg_wait(self):
        assert abs(self.m.avg_wait - 180.0) < 1e-9

    def test_p95_wait(self):
        # Only one data point; p95 = that value
        assert abs(self.m.p95_wait - 180.0) < 1e-9

    def test_avg_walk(self):
        # pickup_walk + dropoff_walk = 150
        assert abs(self.m.avg_walk - 150.0) < 1e-9

    def test_avg_ivt(self):
        assert abs(self.m.avg_ivt - 600.0) < 1e-9

    def test_detour_ratio(self):
        # ivt / direct_time = 600 / 400 = 1.5
        assert abs(self.m.detour_ratio - 1.5) < 1e-9

    def test_fairness_index_zero_single(self):
        # Gini with 1 passenger is undefined → return 0.0
        assert self.m.fairness_index == 0.0

    def test_cpu_time(self):
        assert self.m.cpu_time == 2.0


# ---------------------------------------------------------------------------
# Acceptance rate
# ---------------------------------------------------------------------------

class TestAcceptanceRate:
    def test_partial_acceptance(self):
        records = (
            [make_record(f"a_{i}", accepted=True) for i in range(3)]
            + [make_record(f"r_{i}", accepted=False) for i in range(7)]
        )
        m = compute_metrics(make_result(records=records))
        assert abs(m.acceptance_rate - 0.3) < 1e-9

    def test_full_acceptance(self):
        records = [make_record(f"req_{i}", accepted=True) for i in range(10)]
        m = compute_metrics(make_result(records=records))
        assert abs(m.acceptance_rate - 1.0) < 1e-9


# ---------------------------------------------------------------------------
# Gini coefficient (fairness index)
# ---------------------------------------------------------------------------

class TestGiniCoefficient:
    def test_gini_zero_when_equal_disutility(self):
        # All passengers have exactly the same |total_disutility| → Gini = 0
        records = [
            make_record(f"req_{i}", accepted=True, total_disutility=-5.0)
            for i in range(5)
        ]
        m = compute_metrics(make_result(records=records))
        assert abs(m.fairness_index) < 1e-9, f"Expected Gini=0, got {m.fairness_index}"

    def test_gini_zero_when_single_accepted(self):
        records = [make_record("req_0", accepted=True, total_disutility=-5.0)]
        m = compute_metrics(make_result(records=records))
        assert m.fairness_index == 0.0

    def test_gini_positive_when_unequal(self):
        # Max inequality: one person at 10, rest at 1 → Gini > 0
        records = [
            make_record("req_0", accepted=True, total_disutility=-10.0),
        ] + [
            make_record(f"req_{i}", accepted=True, total_disutility=-1.0)
            for i in range(1, 5)
        ]
        m = compute_metrics(make_result(records=records))
        assert m.fairness_index > 0.0, "Unequal disutility should give Gini > 0"

    def test_gini_in_range_zero_to_one(self):
        # Gini should be in [0, 1]
        records = [
            make_record(f"req_{i}", accepted=True, total_disutility=float(-(i + 1)))
            for i in range(10)
        ]
        m = compute_metrics(make_result(records=records))
        assert 0.0 <= m.fairness_index <= 1.0

    def test_gini_known_value_two_passengers(self):
        # Two passengers: disutility 1 and 3 (absolute values)
        # Gini = |1-3| / (2 * 2^2 * mean(1,3)) = 2 / (2*4*2) = 2/16 = 0.125
        records = [
            make_record("req_0", accepted=True, total_disutility=-1.0),
            make_record("req_1", accepted=True, total_disutility=-3.0),
        ]
        m = compute_metrics(make_result(records=records))
        # G = sum_i sum_j |xi - xj| / (2 * n^2 * mean)
        # absolute values: x0=1, x1=3; mean=2; n=2
        # sum |xi - xj| = |1-1| + |1-3| + |3-1| + |3-3| = 0 + 2 + 2 + 0 = 4
        # G = 4 / (2 * 4 * 2) = 4/16 = 0.25
        assert abs(m.fairness_index - 0.25) < 1e-9, f"Expected 0.25, got {m.fairness_index}"


# ---------------------------------------------------------------------------
# p95 wait time
# ---------------------------------------------------------------------------

class TestP95Wait:
    def test_p95_with_20_passengers(self):
        # wait times: 0, 60, 120, ..., 1140 (20 values, step 60)
        wait_times = [i * 60.0 for i in range(20)]
        records = [
            make_record(f"req_{i}", accepted=True, wait_time=w)
            for i, w in enumerate(wait_times)
        ]
        m = compute_metrics(make_result(records=records))
        # numpy percentile with linear interpolation
        import numpy as np
        expected = float(np.percentile(wait_times, 95))
        assert abs(m.p95_wait - expected) < 1e-6, f"Expected {expected}, got {m.p95_wait}"

    def test_p95_greater_or_equal_avg(self):
        records = [
            make_record(f"req_{i}", accepted=True, wait_time=float(i * 30))
            for i in range(10)
        ]
        m = compute_metrics(make_result(records=records))
        assert m.p95_wait >= m.avg_wait


# ---------------------------------------------------------------------------
# detour_ratio
# ---------------------------------------------------------------------------

class TestDetourRatio:
    def test_no_detour_when_ivt_equals_direct(self):
        records = [
            make_record(f"req_{i}", accepted=True, ivt=600.0, direct_time=600.0)
            for i in range(5)
        ]
        m = compute_metrics(make_result(records=records))
        assert abs(m.detour_ratio - 1.0) < 1e-9

    def test_detour_ratio_computed_per_passenger_then_averaged(self):
        # r0: ivt=600, direct=400 → ratio 1.5
        # r1: ivt=900, direct=600 → ratio 1.5
        # mean = 1.5
        records = [
            make_record("req_0", accepted=True, ivt=600.0, direct_time=400.0),
            make_record("req_1", accepted=True, ivt=900.0, direct_time=600.0),
        ]
        m = compute_metrics(make_result(records=records))
        assert abs(m.detour_ratio - 1.5) < 1e-9

    def test_zero_direct_time_skipped(self):
        # Passengers with direct_time=0 must be excluded from detour_ratio
        records = [
            make_record("req_0", accepted=True, ivt=600.0, direct_time=0.0),
            make_record("req_1", accepted=True, ivt=600.0, direct_time=400.0),
        ]
        m = compute_metrics(make_result(records=records))
        # Only req_1 contributes: 600/400 = 1.5
        assert abs(m.detour_ratio - 1.5) < 1e-9
