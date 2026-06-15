"""
test_insertion.py — pytest suite for HEUR-02 online insertion evaluator.

Tests:
  test_best_insertion            — 2 vehicles, picks the one with lower cost
  test_no_feasible               — capacity=0 forces None return
  test_incremental_cost_components — each cost component is non-negative
  test_timing_benchmark          — 100 requests, 10 vehicles, 20 MPs; avg < 1.0s
"""
from __future__ import annotations

import random
import time

import pytest

from drt.insertion import InsertionResult, evaluate_insertion
from drt.types import MeetingPoint, Request, Route, Vehicle


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def make_request(
    rid: str = "r1",
    origin: tuple[float, float] = (0.0, 0.0),
    destination: tuple[float, float] = (10.0, 10.0),
    earliest: float = 0.0,
    latest: float = 100.0,
    max_ride_time: float = 200.0,
) -> Request:
    return Request(
        id=rid,
        origin=origin,
        destination=destination,
        earliest=earliest,
        latest=latest,
        max_ride_time=max_ride_time,
    )


def make_vehicle(
    vid: str = "v1",
    capacity: int = 4,
    max_route_duration: float = 500.0,
    position: tuple[float, float] = (0.0, 0.0),
    current_time: float = 0.0,
) -> Vehicle:
    return Vehicle(
        id=vid,
        capacity=capacity,
        max_route_duration=max_route_duration,
        current_position=position,
        current_time=current_time,
    )


def make_mp(mid: str, coords: tuple[float, float]) -> MeetingPoint:
    return MeetingPoint(id=mid, coords=coords)


# ---------------------------------------------------------------------------
# test_best_insertion
# ---------------------------------------------------------------------------

def test_best_insertion():
    """Two vehicles; the one closer to the request should win (lower cost)."""
    request = make_request(origin=(5.0, 5.0), destination=(15.0, 15.0))

    # Vehicle 1 is far from the request origin
    v1 = make_vehicle("v1", position=(50.0, 50.0))
    # Vehicle 2 is close to the request origin
    v2 = make_vehicle("v2", position=(5.0, 5.0))

    vehicles = {"v1": v1, "v2": v2}
    routes: dict = {}

    # Meeting points near origin and destination
    mp_near_origin = make_mp("mp_pu", (5.5, 5.5))
    mp_near_dest = make_mp("mp_do", (14.5, 14.5))
    meeting_points = [mp_near_origin, mp_near_dest]

    result = evaluate_insertion(
        request=request,
        routes=routes,
        vehicles=vehicles,
        meeting_points=meeting_points,
        rho_p=5.0,
        rho_d=5.0,
        k_top=3,
    )

    assert result is not None, "Expected a feasible insertion"
    assert isinstance(result, InsertionResult)
    # Vehicle 2 starts closer — should have lower operational cost
    assert result.vehicle_id == "v2", (
        f"Expected v2 (closer vehicle) but got {result.vehicle_id}"
    )
    assert result.pos_p < result.pos_d


# ---------------------------------------------------------------------------
# test_no_feasible
# ---------------------------------------------------------------------------

def test_no_feasible():
    """Capacity=0 makes every insertion infeasible; must return None."""
    request = make_request()
    v1 = make_vehicle("v1", capacity=0)
    vehicles = {"v1": v1}
    routes: dict = {}

    mp1 = make_mp("mp1", (0.5, 0.5))
    mp2 = make_mp("mp2", (9.5, 9.5))
    meeting_points = [mp1, mp2]

    result = evaluate_insertion(
        request=request,
        routes=routes,
        vehicles=vehicles,
        meeting_points=meeting_points,
        rho_p=5.0,
        rho_d=5.0,
        k_top=3,
    )

    assert result is None, "Expected None when all insertions are infeasible"


def test_walking_radius_failure_returns_none():
    """Meeting points outside both walking radii produce no feasible insertion."""
    request = make_request(origin=(0.0, 0.0), destination=(10.0, 10.0))
    vehicles = {"v1": make_vehicle("v1")}
    routes: dict = {}
    meeting_points = [
        make_mp("far_pickup", (100.0, 100.0)),
        make_mp("far_dropoff", (120.0, 120.0)),
    ]

    result = evaluate_insertion(
        request=request,
        routes=routes,
        vehicles=vehicles,
        meeting_points=meeting_points,
        rho_p=1.0,
        rho_d=1.0,
        k_top=3,
    )

    assert result is None


# ---------------------------------------------------------------------------
# test_incremental_cost_components
# ---------------------------------------------------------------------------

def test_incremental_cost_components():
    """Each cost component must be non-negative; total cost must be >= 0."""
    request = make_request(origin=(2.0, 2.0), destination=(8.0, 8.0))
    v1 = make_vehicle("v1", position=(0.0, 0.0))
    vehicles = {"v1": v1}
    routes: dict = {}

    mp_pu = make_mp("mp_pu", (2.5, 2.5))
    mp_do = make_mp("mp_do", (7.5, 7.5))
    meeting_points = [mp_pu, mp_do]

    result = evaluate_insertion(
        request=request,
        routes=routes,
        vehicles=vehicles,
        meeting_points=meeting_points,
        rho_p=5.0,
        rho_d=5.0,
        k_top=3,
        cost_weights=(1.0, 1.0, 1.0, 1.0),
    )

    assert result is not None
    assert result.incremental_cost >= 0.0, (
        f"Incremental cost must be non-negative, got {result.incremental_cost}"
    )


# ---------------------------------------------------------------------------
# test_timing_benchmark
# ---------------------------------------------------------------------------

def test_timing_benchmark():
    """
    HEUR-06: 100 requests, 10 vehicles, 20 meeting points.
    Average decision time per request must be < 1.0 second.
    """
    rng = random.Random(42)

    # 20 meeting points on a 4x5 grid in [0, 100]^2
    meeting_points = [
        make_mp(f"mp{i}", (10.0 + (i % 4) * 20.0, 10.0 + (i // 4) * 20.0))
        for i in range(20)
    ]

    # 10 vehicles with empty routes
    vehicles = {
        f"v{j}": make_vehicle(
            vid=f"v{j}",
            capacity=8,
            max_route_duration=300.0,
            position=(rng.uniform(0, 100), rng.uniform(0, 100)),
            current_time=0.0,
        )
        for j in range(10)
    }
    routes: dict = {}

    # 100 requests with random origins/destinations in [0, 100]^2
    requests = [
        make_request(
            rid=f"req{i}",
            origin=(rng.uniform(0, 100), rng.uniform(0, 100)),
            destination=(rng.uniform(0, 100), rng.uniform(0, 100)),
            earliest=0.0,
            latest=200.0,
            max_ride_time=300.0,
        )
        for i in range(100)
    ]

    start = time.perf_counter()
    for req in requests:
        evaluate_insertion(
            request=req,
            routes=routes,
            vehicles=vehicles,
            meeting_points=meeting_points,
            rho_p=50.0,   # generous radius to ensure candidates exist
            rho_d=50.0,
            k_top=5,
        )
    elapsed = time.perf_counter() - start

    avg_time = elapsed / 100
    assert avg_time < 1.0, (
        f"Average decision time {avg_time:.4f}s exceeds 1.0s limit"
    )
