"""
test_alns.py — HEUR-05/06 unit tests for ALNS operators and RollingHorizon.

Tests:
  test_all_operators_run       — 5-request, 2-vehicle instance; all 5 operators run without error
  test_reoptimize_returns_keys — RollingHorizon.reoptimize() returns required keys
  test_timing_benchmark        — 200-request, 15-vehicle benchmark; avg decision time < 1.0s
"""
from __future__ import annotations

import os
import random
import sys
import time

import pytest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, "src")

from experiments.algorithm_diagnostics import run_alns_budget_smoke
from drt.alns import (
    ALNSState,
    RollingHorizon,
    _apply_insertion,
    benchmark,
    greedy_insertion,
    random_removal,
    regret_insertion,
    related_removal,
    worst_removal,
)
from drt.types import MeetingPoint, Request, Route, Vehicle
from drt.insertion import evaluate_insertion


# ---------------------------------------------------------------------------
# Shared fixtures
# ---------------------------------------------------------------------------

def _make_meeting_points() -> list[MeetingPoint]:
    """6 meeting points on a 3x3 grid (skip center)."""
    coords = [
        (0.0, 0.0), (5.0, 0.0), (10.0, 0.0),
        (0.0, 5.0),              (10.0, 5.0),
        (5.0, 10.0),
    ]
    return [MeetingPoint(id=f"mp{i}", coords=c) for i, c in enumerate(coords)]


def _make_vehicles() -> dict:
    return {
        "v0": Vehicle(id="v0", capacity=4, max_route_duration=120.0,
                      current_position=(2.0, 2.0), current_time=0.0),
        "v1": Vehicle(id="v1", capacity=4, max_route_duration=120.0,
                      current_position=(8.0, 8.0), current_time=0.0),
    }


def _make_requests() -> list[Request]:
    return [
        Request(id="r0", origin=(0.5, 0.5), destination=(9.5, 9.5),
                earliest=0.0, latest=30.0, max_ride_time=60.0),
        Request(id="r1", origin=(1.0, 1.0), destination=(8.0, 8.0),
                earliest=2.0, latest=35.0, max_ride_time=60.0),
        Request(id="r2", origin=(4.0, 0.5), destination=(6.0, 9.5),
                earliest=1.0, latest=40.0, max_ride_time=60.0),
        Request(id="r3", origin=(0.5, 4.5), destination=(9.5, 5.0),
                earliest=3.0, latest=45.0, max_ride_time=60.0),
        Request(id="r4", origin=(5.0, 0.5), destination=(5.0, 9.5),
                earliest=0.5, latest=50.0, max_ride_time=60.0),
    ]


def _build_state_with_requests(requests, vehicles, meeting_points, rho=5.0, k_top=3):
    """Build an ALNSState with some requests inserted via greedy_insertion."""
    routes = {vid: Route(vehicle_id=vid, stops=[]) for vid in vehicles}
    registry = {r.id: r for r in requests}
    initial_state = ALNSState(routes=routes, unassigned=list(requests), cost=0.0)
    rng = random.Random(0)
    state = greedy_insertion(
        initial_state, vehicles, meeting_points,
        rho_p=rho, rho_d=rho, k_top=k_top,
        cost_weights=(1.0, 1.0, 1.0, 1.0), travel_speed=1.0, rng=rng
    )
    return state, registry


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

def test_all_operators_run():
    """
    HEUR-05: All 5 destroy/repair operators execute without exception
    on a 5-request, 2-vehicle instance.
    """
    meeting_points = _make_meeting_points()
    vehicles = _make_vehicles()
    requests = _make_requests()
    rng = random.Random(42)

    state, registry = _build_state_with_requests(requests, vehicles, meeting_points)

    # Destroy operator 1: random_removal
    s1 = random_removal(state, k=2, rng=rng, request_registry=registry)
    assert isinstance(s1, ALNSState), "random_removal must return ALNSState"

    # Destroy operator 2: worst_removal
    s2 = worst_removal(state, k=2, request_registry=registry,
                       vehicles=vehicles, travel_speed=1.0)
    assert isinstance(s2, ALNSState), "worst_removal must return ALNSState"

    # Destroy operator 3: related_removal
    s3 = related_removal(state, k=2, rng=rng, request_registry=registry,
                         travel_speed=1.0)
    assert isinstance(s3, ALNSState), "related_removal must return ALNSState"

    # Repair operator 4: greedy_insertion (on a destroyed state)
    s4 = greedy_insertion(s1, vehicles, meeting_points,
                          rho_p=5.0, rho_d=5.0, k_top=3,
                          cost_weights=(1.0, 1.0, 1.0, 1.0),
                          travel_speed=1.0, rng=rng)
    assert isinstance(s4, ALNSState), "greedy_insertion must return ALNSState"

    # Repair operator 5: regret_insertion (on a destroyed state)
    s5 = regret_insertion(s2, vehicles, meeting_points,
                          rho_p=5.0, rho_d=5.0, k_top=3,
                          cost_weights=(1.0, 1.0, 1.0, 1.0),
                          travel_speed=1.0)
    assert isinstance(s5, ALNSState), "regret_insertion must return ALNSState"


def test_reoptimize_returns_keys():
    """
    HEUR-04: RollingHorizon.reoptimize() returns dict with required keys:
    routes, unassigned, cost, time_ms, objective, n_accepted.
    """
    meeting_points = _make_meeting_points()
    vehicles = _make_vehicles()
    requests = _make_requests()

    rh = RollingHorizon(
        vehicles=vehicles,
        meeting_points=meeting_points,
        rho_p=5.0,
        rho_d=5.0,
        k_top=3,
        H=60.0,
        delta=10.0,
        cost_weights=(1.0, 1.0, 1.0, 1.0),
        travel_speed=1.0,
        alns_iterations=5,
        seed=42,
    )

    # Add all requests before reoptimizing
    for req in requests:
        rh.add_request(req, current_time=0.0)

    result = rh.reoptimize(current_time=0.0)

    required_keys = {'routes', 'unassigned', 'cost', 'time_ms', 'objective', 'n_accepted'}
    assert required_keys.issubset(result.keys()), (
        f"Missing keys: {required_keys - result.keys()}"
    )
    assert isinstance(result['routes'], dict)
    assert isinstance(result['objective'], float)
    assert isinstance(result['n_accepted'], int)
    assert result['time_ms'] >= 0.0


def test_reoptimize_collects_diagnostic_trace():
    meeting_points = _make_meeting_points()
    vehicles = _make_vehicles()
    requests = _make_requests()

    rh = RollingHorizon(
        vehicles=vehicles,
        meeting_points=meeting_points,
        rho_p=5.0,
        rho_d=5.0,
        k_top=3,
        H=60.0,
        delta=10.0,
        cost_weights=(1.0, 1.0, 1.0, 1.0),
        travel_speed=1.0,
        alns_iterations=4,
        seed=42,
        collect_diagnostics=True,
    )
    for req in requests:
        rh.add_request(req, current_time=0.0)

    result = rh.reoptimize(current_time=0.0)
    trace = result["diagnostic_trace"]

    assert len(trace) == 4
    for entry in trace:
        for key in [
            "iteration",
            "objective",
            "best_objective",
            "runtime_ms",
            "accepted_count",
            "unassigned_count",
            "destroy_operator",
            "repair_operator",
            "accepted_improvement",
        ]:
            assert key in entry
        assert isinstance(entry["accepted_improvement"], bool)
    assert result["operator_counts"]


def test_apply_insertion_preserves_tagged_request_ids_and_pickup_times():
    meeting_points = _make_meeting_points()
    vehicles = _make_vehicles()
    request = _make_requests()[0]
    state = ALNSState(
        routes={vid: Route(vehicle_id=vid, stops=[]) for vid in vehicles},
        unassigned=[],
    )
    result = evaluate_insertion(
        request,
        state.routes,
        vehicles,
        meeting_points,
        rho_p=5.0,
        rho_d=5.0,
        k_top=3,
        cost_weights=(1.0, 1.0, 1.0, 1.0),
        travel_speed=1.0,
    )

    assert result is not None
    _apply_insertion(state, result, request, vehicles, travel_speed=1.0)

    stops = state.routes[result.vehicle_id].stops
    tagged = [stop for stop in stops if len(stop) >= 4 and stop[2] == request.id]
    assert {stop[3] for stop in tagged} == {"pickup", "dropoff"}
    assert all(stop[1] > 0.0 for stop in tagged)


def test_rolling_horizon_pruning_preserves_completed_ids_and_pickup_times():
    meeting_points = _make_meeting_points()
    vehicles = _make_vehicles()
    request = _make_requests()[0]
    rh = RollingHorizon(
        vehicles=vehicles,
        meeting_points=meeting_points,
        rho_p=5.0,
        rho_d=5.0,
        k_top=3,
        H=60.0,
        delta=10.0,
        cost_weights=(1.0, 1.0, 1.0, 1.0),
        travel_speed=1.0,
        alns_iterations=1,
        seed=42,
    )
    rh.routes["v0"].stops = [
        (meeting_points[0], 1.0, request.id, "pickup"),
        (meeting_points[1], 2.0, request.id, "dropoff"),
    ]

    rh.reoptimize(current_time=3.0)

    assert request.id in rh.completed_request_ids
    assert rh.pickup_times[request.id] == 1.0
    assert rh.routes["v0"].stops == []


def test_algorithm_diagnostics_budget_smoke_default_rows():
    rows = run_alns_budget_smoke()

    assert [row["budget_iterations"] for row in rows] == [5, 20, 50]
    for row in rows:
        for key in [
            "budget_iterations",
            "best_objective",
            "runtime_s",
            "n_accepted",
            "n_unassigned",
            "operator_selection_counts",
            "improvement_counts",
        ]:
            assert key in row
        assert row["evidence_family"] == "algorithm_diagnostic"
        assert row["diagnostic_role"] == "alns_budget_smoke"


def test_timing_benchmark():
    """
    HEUR-06: 200-request, 15-vehicle benchmark must complete with
    avg decision time < 1.0s per request.
    """
    result = benchmark(n_requests=200, n_vehicles=15, n_meeting_points=20,
                       rho=10.0, k_top=5, seed=42)
    avg = result['avg_time_per_request_s']
    assert avg < 1.0, (
        f"Avg time per request {avg:.4f}s exceeds 1.0s requirement (HEUR-06)"
    )
    assert result['n_requests'] == 200
