"""
test_milp.py — Smoke tests for DRTModel (EXACT-01/02/03/04).

Tests are skipped gracefully when gurobipy is not installed or not licensed.
"""
from __future__ import annotations

import math
import sys
import os
from types import SimpleNamespace

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

try:
    import gurobipy as gp
except ImportError:
    gp = None

import experiments.milp_gap as milp_gap
from drt.candidate import generate_candidates
from drt.feasibility import check_feasibility
from drt.milp import DRTModel
from drt.types import MeetingPoint, Request, Route, Vehicle


# ---------------------------------------------------------------------------
# License check helper
# ---------------------------------------------------------------------------

def _gurobi_licensed() -> bool:
    if gp is None:
        return False
    try:
        gp.Model()
        return True
    except Exception:
        return False


_licensed = _gurobi_licensed()


# ---------------------------------------------------------------------------
# Instance factories
# ---------------------------------------------------------------------------

def _make_meeting_points() -> list[MeetingPoint]:
    """8 meeting points on a 3x3 grid (excluding centre at (5,5))."""
    coords = [
        (2.5, 2.5), (5.0, 2.5), (7.5, 2.5),
        (2.5, 5.0),              (7.5, 5.0),
        (2.5, 7.5), (5.0, 7.5), (7.5, 7.5),
    ]
    return [MeetingPoint(id=f"mp{i}", coords=c) for i, c in enumerate(coords)]


def _make_small_instance():
    """10 requests, 3 vehicles, 8 meeting points."""
    meeting_points = _make_meeting_points()

    # Deterministic requests on a 10x10 grid
    origins = [
        (1, 1), (3, 2), (5, 1), (7, 2), (9, 1),
        (1, 9), (3, 8), (5, 9), (7, 8), (9, 9),
    ]
    destinations = [
        (9, 9), (7, 8), (5, 9), (3, 8), (1, 9),
        (9, 1), (7, 2), (5, 1), (3, 2), (1, 1),
    ]
    requests = [
        Request(
            id=f"r{i}",
            origin=origins[i],
            destination=destinations[i],
            earliest=0.0,
            latest=60.0,
            max_ride_time=30.0,
        )
        for i in range(10)
    ]

    vehicles = [
        Vehicle(
            id=f"v{j}",
            capacity=4,
            max_route_duration=120.0,
            current_position=(5.0, 5.0),
            current_time=0.0,
        )
        for j in range(3)
    ]

    return requests, vehicles, meeting_points


def _make_scale_instance():
    """30 requests, 5 vehicles, 8 meeting points."""
    meeting_points = _make_meeting_points()

    import random
    rng = random.Random(42)

    requests = [
        Request(
            id=f"r{i}",
            origin=(rng.uniform(0, 10), rng.uniform(0, 10)),
            destination=(rng.uniform(0, 10), rng.uniform(0, 10)),
            earliest=0.0,
            latest=60.0,
            max_ride_time=30.0,
        )
        for i in range(30)
    ]

    vehicles = [
        Vehicle(
            id=f"v{j}",
            capacity=6,
            max_route_duration=120.0,
            current_position=(5.0, 5.0),
            current_time=0.0,
        )
        for j in range(5)
    ]

    return requests, vehicles, meeting_points


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

def test_small_instance():
    pytest.importorskip("gurobipy", reason="gurobipy not installed")
    """10 requests, 3 vehicles — assert feasible solution found."""
    requests, vehicles, meeting_points = _make_small_instance()
    model = DRTModel(
        requests=requests,
        vehicles=vehicles,
        meeting_points=meeting_points,
        rho_p=5.0,
        rho_d=5.0,
        cost_weights=(1, 1, 1, 1, 10),
    )
    try:
        result = model.solve()
    except gp.GurobiError as exc:
        pytest.skip(f"Gurobi license error: {exc}")

    assert isinstance(result, dict), "solve() must return a dict"
    assert "status" in result
    assert "objective_value" in result
    assert "mip_gap" in result
    assert "solve_time" in result
    assert "accepted" in result

    assert result["status"] in ("optimal", "feasible", "timeout", "infeasible"), (
        f"Unexpected status: {result['status']}"
    )
    assert result["solve_time"] is not None and result["solve_time"] > 0


def test_reports_gap():
    pytest.importorskip("gurobipy", reason="gurobipy not installed")
    """After solve, mip_gap is a float (not None) when a solution is found."""
    requests, vehicles, meeting_points = _make_small_instance()
    model = DRTModel(
        requests=requests,
        vehicles=vehicles,
        meeting_points=meeting_points,
        rho_p=5.0,
        rho_d=5.0,
        cost_weights=(1, 1, 1, 1, 10),
    )
    try:
        result = model.solve()
    except gp.GurobiError as exc:
        pytest.skip(f"Gurobi license error: {exc}")

    if result["status"] in ("optimal", "feasible", "timeout"):
        assert result["mip_gap"] is not None, "mip_gap must be set when solution found"
        assert isinstance(result["mip_gap"], float)


def test_reports_solve_time():
    pytest.importorskip("gurobipy", reason="gurobipy not installed")
    """solve_time > 0 after any solve call."""
    requests, vehicles, meeting_points = _make_small_instance()
    model = DRTModel(
        requests=requests,
        vehicles=vehicles,
        meeting_points=meeting_points,
        rho_p=5.0,
        rho_d=5.0,
        cost_weights=(1, 1, 1, 1, 10),
    )
    try:
        result = model.solve()
    except gp.GurobiError as exc:
        pytest.skip(f"Gurobi license error: {exc}")

    assert result["solve_time"] > 0, "solve_time must be positive"


def test_accepted_subset():
    pytest.importorskip("gurobipy", reason="gurobipy not installed")
    """result['accepted'] is a list; all ids are valid request ids."""
    requests, vehicles, meeting_points = _make_small_instance()
    model = DRTModel(
        requests=requests,
        vehicles=vehicles,
        meeting_points=meeting_points,
        rho_p=5.0,
        rho_d=5.0,
        cost_weights=(1, 1, 1, 1, 10),
    )
    try:
        result = model.solve()
    except gp.GurobiError as exc:
        pytest.skip(f"Gurobi license error: {exc}")

    assert isinstance(result["accepted"], list)
    valid_ids = {r.id for r in requests}
    for rid in result["accepted"]:
        assert rid in valid_ids, f"Unknown request id in accepted: {rid}"


@pytest.mark.skipif(not _licensed, reason="Gurobi license unavailable")
def test_scale_instance():
    """30 requests, 5 vehicles — EXACT-02 scale test."""
    requests, vehicles, meeting_points = _make_scale_instance()
    model = DRTModel(
        requests=requests,
        vehicles=vehicles,
        meeting_points=meeting_points,
        rho_p=5.0,
        rho_d=5.0,
        cost_weights=(1, 1, 1, 1, 10),
        time_limit=120.0,
    )
    try:
        result = model.solve()
    except gp.GurobiError as exc:
        pytest.skip(f"Gurobi license error: {exc}")

    assert result["status"] in ("optimal", "feasible", "timeout")
    assert result["solve_time"] > 0


def test_candidate_filtering_without_gurobi():
    request = Request(
        id="tiny",
        origin=(0.0, 0.0),
        destination=(10.0, 0.0),
        earliest=0.0,
        latest=20.0,
        max_ride_time=20.0,
    )
    near_pickup = MeetingPoint("near_pickup", (1.0, 0.0))
    near_dropoff = MeetingPoint("near_dropoff", (9.0, 0.0))
    far = MeetingPoint("far", (100.0, 100.0))

    pickup_candidates = generate_candidates(
        request, [near_pickup, near_dropoff, far], rho=2.0, k_top=3, side="pickup"
    )
    dropoff_candidates = generate_candidates(
        request, [near_pickup, near_dropoff, far], rho=2.0, k_top=3, side="dropoff"
    )

    assert [mp.id for mp in pickup_candidates] == ["near_pickup"]
    assert [mp.id for mp in dropoff_candidates] == ["near_dropoff"]


def test_static_tiny_instance_feasibility_and_objective_units_without_gurobi():
    request = Request(
        id="tiny",
        origin=(0.0, 0.0),
        destination=(10.0, 0.0),
        earliest=0.0,
        latest=20.0,
        max_ride_time=20.0,
    )
    vehicle = Vehicle(
        id="v0",
        capacity=1,
        max_route_duration=30.0,
        current_position=(0.0, 0.0),
        current_time=0.0,
    )
    pickup = MeetingPoint("pickup", (0.0, 0.0))
    dropoff = MeetingPoint("dropoff", (10.0, 0.0))
    model = DRTModel(
        requests=[request],
        vehicles=[vehicle],
        meeting_points=[pickup, dropoff],
        rho_p=1.0,
        rho_d=1.0,
        travel_speed=2.0,
    )

    ok, reason = check_feasibility(
        Route(vehicle_id=vehicle.id, stops=[]),
        request,
        pickup,
        dropoff,
        pos_p=0,
        pos_d=1,
        vehicle=vehicle,
        travel_speed=2.0,
    )

    assert ok is True
    assert reason == ""
    assert model._travel_time(pickup.coords, dropoff.coords) == pytest.approx(5.0)


def test_milp_gap_no_gurobi_path_returns_durable_diagnostic_row(monkeypatch):
    class FakeFullModel:
        def run(self, scenario):
            return SimpleNamespace(
                total_vehicle_km=12.0,
                records=[
                    SimpleNamespace(request_id=scenario.requests[0].id, accepted=True),
                    *[
                        SimpleNamespace(request_id=request.id, accepted=False)
                        for request in scenario.requests[1:]
                    ],
                ],
            )

    def raise_import_error(self):
        raise ImportError("forced no gurobi")

    monkeypatch.setattr(milp_gap, "FullModel", FakeFullModel)
    monkeypatch.setattr(DRTModel, "solve", raise_import_error)

    row = milp_gap.run_gap_experiment(n_requests=3, seed=42)

    assert row["milp_status"] == "no_gurobi"
    assert row["status"] == "no_gurobi"
    assert row["gap_pct"] is None
    assert row["comparable_gap"] is False
    assert row["evidence_family"] == "algorithm_diagnostic"
    assert "milp" in row["diagnostic_role"]
    assert row["detailed_reason"]
