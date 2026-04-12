"""
tests/test_scenarios.py — Tests for experiment scenario generators.

Verifies:
  - generate_synthetic returns correct counts and coordinate bounds
  - generate_beijing returns correct meeting point count and coord bounds
  - Morning peak clustering in Beijing scenario
  - Reproducibility: same seed → same output
"""

import sys
import os

# Ensure project root is on path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest
from experiments.scenarios import generate_synthetic, generate_beijing, Scenario


class TestGenerateSynthetic:
    def test_returns_scenario_dataclass(self):
        s = generate_synthetic(50, 5, 42)
        assert isinstance(s, Scenario)

    def test_request_count(self):
        s = generate_synthetic(100, 10, 42)
        assert len(s.requests) == 100

    def test_vehicle_count(self):
        s = generate_synthetic(100, 10, 42)
        assert len(s.vehicles) == 10

    def test_meeting_point_count(self):
        s = generate_synthetic(100, 10, 42)
        assert len(s.meeting_points) == 100

    def test_request_origins_in_grid(self):
        s = generate_synthetic(100, 10, 42)
        for req in s.requests:
            x, y = req.origin
            assert 0 <= x <= 20000, f"origin x={x} out of [0, 20000]"
            assert 0 <= y <= 20000, f"origin y={y} out of [0, 20000]"

    def test_request_destinations_in_grid(self):
        s = generate_synthetic(100, 10, 42)
        for req in s.requests:
            x, y = req.destination
            assert 0 <= x <= 20000, f"destination x={x} out of [0, 20000]"
            assert 0 <= y <= 20000, f"destination y={y} out of [0, 20000]"

    def test_meeting_points_on_10x10_grid(self):
        s = generate_synthetic(100, 10, 42)
        # Expect 10x10 regular grid: x = i*2000, y = j*2000 for i,j in 0..9
        expected_xs = set(i * 2000 for i in range(10))
        expected_ys = set(j * 2000 for j in range(10))
        for mp in s.meeting_points:
            x, y = mp.coords
            assert x in expected_xs, f"MP x={x} not on 10x10 grid"
            assert y in expected_ys, f"MP y={y} not on 10x10 grid"

    def test_request_time_window_valid(self):
        s = generate_synthetic(100, 10, 42)
        for req in s.requests:
            assert 0 <= req.earliest <= 4 * 3600, f"earliest={req.earliest} out of range"
            assert req.latest > req.earliest, "latest must be > earliest"
            assert 5 * 60 <= req.latest - req.earliest <= 20 * 60, (
                f"window {req.latest - req.earliest}s not in [5min, 20min]"
            )

    def test_vehicle_capacity(self):
        s = generate_synthetic(100, 10, 42)
        for v in s.vehicles:
            assert v.capacity == 8

    def test_vehicle_positions_in_grid(self):
        s = generate_synthetic(100, 10, 42)
        for v in s.vehicles:
            x, y = v.current_position
            assert 0 <= x <= 20000
            assert 0 <= y <= 20000

    def test_reproducibility(self):
        s1 = generate_synthetic(100, 10, 42)
        s2 = generate_synthetic(100, 10, 42)
        # Same requests
        for r1, r2 in zip(s1.requests, s2.requests):
            assert r1.origin == r2.origin
            assert r1.destination == r2.destination
            assert r1.earliest == r2.earliest
        # Same vehicle positions
        for v1, v2 in zip(s1.vehicles, s2.vehicles):
            assert v1.current_position == v2.current_position

    def test_different_seeds_give_different_results(self):
        s1 = generate_synthetic(100, 10, 42)
        s2 = generate_synthetic(100, 10, 99)
        origins1 = [r.origin for r in s1.requests]
        origins2 = [r.origin for r in s2.requests]
        assert origins1 != origins2, "Different seeds should give different results"

    def test_area_km_attribute(self):
        s = generate_synthetic(100, 10, 42)
        assert s.area_km == 20.0

    def test_name_attribute(self):
        s = generate_synthetic(100, 10, 42)
        assert "synthetic" in s.name.lower()

    def test_n_requests_cap_raises(self):
        # Threat T-03-03: cap at 1000 to prevent OOM
        with pytest.raises(ValueError):
            generate_synthetic(1001, 10, 42)

    def test_max_ride_time(self):
        s = generate_synthetic(100, 10, 42)
        for req in s.requests:
            assert req.max_ride_time == 45 * 60


class TestGenerateBeijing:
    def test_returns_scenario_dataclass(self):
        s = generate_beijing(100, 10, 42)
        assert isinstance(s, Scenario)

    def test_meeting_point_count(self):
        s = generate_beijing(200, 15, 42)
        assert len(s.meeting_points) == 80

    def test_meeting_points_in_15km_grid(self):
        s = generate_beijing(200, 15, 42)
        for mp in s.meeting_points:
            x, y = mp.coords
            assert 0 <= x <= 15000, f"MP x={x} out of [0, 15000]"
            assert 0 <= y <= 15000, f"MP y={y} out of [0, 15000]"

    def test_request_count(self):
        s = generate_beijing(200, 15, 42)
        assert len(s.requests) == 200

    def test_vehicle_count(self):
        s = generate_beijing(200, 15, 42)
        assert len(s.vehicles) == 15

    def test_morning_peak_earliest_times(self):
        s = generate_beijing(200, 15, 42)
        for req in s.requests:
            assert 7 * 3600 <= req.earliest <= 9 * 3600, (
                f"earliest={req.earliest} not in morning peak [7h, 9h]"
            )

    def test_request_origins_in_15km_grid(self):
        s = generate_beijing(200, 15, 42)
        for req in s.requests:
            x, y = req.origin
            assert 0 <= x <= 15000, f"origin x={x} out of [0, 15000]"
            assert 0 <= y <= 15000, f"origin y={y} out of [0, 15000]"

    def test_destinations_in_15km_grid(self):
        s = generate_beijing(200, 15, 42)
        for req in s.requests:
            x, y = req.destination
            assert 0 <= x <= 15000, f"destination x={x} out of [0, 15000]"
            assert 0 <= y <= 15000, f"destination y={y} out of [0, 15000]"

    def test_vehicle_start_time(self):
        s = generate_beijing(200, 15, 42)
        for v in s.vehicles:
            assert v.current_time == 7 * 3600

    def test_reproducibility(self):
        s1 = generate_beijing(200, 15, 42)
        s2 = generate_beijing(200, 15, 42)
        for r1, r2 in zip(s1.requests, s2.requests):
            assert r1.origin == r2.origin
            assert r1.earliest == r2.earliest

    def test_area_km_attribute(self):
        s = generate_beijing(200, 15, 42)
        assert s.area_km == 15.0

    def test_name_attribute(self):
        s = generate_beijing(200, 15, 42)
        assert "beijing" in s.name.lower()

    def test_max_ride_time(self):
        s = generate_beijing(200, 15, 42)
        for req in s.requests:
            assert req.max_ride_time == 40 * 60

    def test_n_requests_cap_raises(self):
        # Threat T-03-03: cap applies to both generators
        with pytest.raises(ValueError):
            generate_beijing(1001, 10, 42)
