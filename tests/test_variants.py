"""
tests/test_variants.py — Tests for all 6 model variant classes.

Tests
-----
test_all_variants_run          : each variant returns SimulationResult on a small scenario
test_all_variants_list_length  : ALL_VARIANTS has exactly 6 entries
test_all_variants_unique_names : all variant names are unique non-empty strings
test_door_to_door_no_walking   : DoorToDoor produces pickup_walk=0, dropoff_walk=0
test_single_sided_no_dropoff_walk : SingleSidedPickup produces dropoff_walk=0
test_acceptance_rate_in_range  : acceptance_rate in [0, 1] for all variants
test_cpu_time_positive         : cpu_time > 0 for all variants
"""
from __future__ import annotations

import os
import sys

import pytest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import experiments.variants as variants_module
from experiments.metrics import SimulationResult, compute_metrics
from experiments.scenarios import generate_synthetic
from experiments.variants import (
    ALL_VARIANTS,
    AblationNoChoice,
    AblationNoRollingHorizon,
    BidirectionalNoChoice,
    DoorToDoor,
    FullModel,
    SingleSidedDropoff,
    SingleSidedPickup,
)
from drt.types import ChoiceParameters

# ---------------------------------------------------------------------------
# Shared fixture
# ---------------------------------------------------------------------------

SMALL_SCENARIO = generate_synthetic(n_requests=10, n_vehicles=3, seed=42)
MEDIUM_SCENARIO = generate_synthetic(n_requests=20, n_vehicles=3, seed=42)


# ---------------------------------------------------------------------------
# Registry tests
# ---------------------------------------------------------------------------


def test_all_variants_list_length():
    assert len(ALL_VARIANTS) == 8


def test_all_variants_unique_names():
    names = [v.name for v in ALL_VARIANTS]
    assert len(names) == len(set(names)), f"Duplicate names: {names}"
    for name in names:
        assert isinstance(name, str) and len(name) > 0


# ---------------------------------------------------------------------------
# Run tests — each variant must return SimulationResult without exception
# ---------------------------------------------------------------------------


def test_all_variants_run():
    """Each variant runs on a 10-request, 3-vehicle scenario without exception."""
    for variant in ALL_VARIANTS:
        result = variant.run(SMALL_SCENARIO)
        assert isinstance(result, SimulationResult), (
            f"{variant.name} did not return SimulationResult"
        )
        assert result.records is not None
        assert len(result.records) == len(SMALL_SCENARIO.requests)


def test_cpu_time_positive():
    """All variants produce cpu_time > 0."""
    for variant in ALL_VARIANTS:
        result = variant.run(SMALL_SCENARIO)
        assert result.cpu_time > 0, f"{variant.name} has cpu_time={result.cpu_time}"


def test_acceptance_rate_in_range():
    """acceptance_rate in [0, 1] for all variants."""
    for variant in ALL_VARIANTS:
        result = variant.run(MEDIUM_SCENARIO)
        metrics = compute_metrics(result)
        assert 0.0 <= metrics.acceptance_rate <= 1.0, (
            f"{variant.name} acceptance_rate={metrics.acceptance_rate} out of range"
        )


# ---------------------------------------------------------------------------
# DoorToDoor-specific tests
# ---------------------------------------------------------------------------


def test_door_to_door_no_walking():
    """DoorToDoor: all accepted passengers have pickup_walk=0 and dropoff_walk=0."""
    result = DoorToDoor().run(MEDIUM_SCENARIO)
    for rec in result.records:
        if rec.accepted:
            assert rec.pickup_walk == pytest.approx(0.0, abs=1e-6), (
                f"DoorToDoor request {rec.request_id} has pickup_walk={rec.pickup_walk}"
            )
            assert rec.dropoff_walk == pytest.approx(0.0, abs=1e-6), (
                f"DoorToDoor request {rec.request_id} has dropoff_walk={rec.dropoff_walk}"
            )


# ---------------------------------------------------------------------------
# SingleSidedPickup-specific tests
# ---------------------------------------------------------------------------


def test_single_sided_no_dropoff_walk():
    """SingleSidedPickup: all accepted passengers have dropoff_walk=0."""
    result = SingleSidedPickup().run(MEDIUM_SCENARIO)
    for rec in result.records:
        if rec.accepted:
            assert rec.dropoff_walk == pytest.approx(0.0, abs=1e-6), (
                f"SingleSidedPickup request {rec.request_id} has dropoff_walk={rec.dropoff_walk}"
            )


def test_single_sided_dropoff_no_pickup_walk():
    """SingleSidedDropoff: all accepted passengers have pickup_walk=0."""
    result = SingleSidedDropoff().run(MEDIUM_SCENARIO)
    for rec in result.records:
        if rec.accepted:
            assert rec.pickup_walk == pytest.approx(0.0, abs=1e-6), (
                f"SingleSidedDropoff request {rec.request_id} has pickup_walk={rec.pickup_walk}"
            )


# ---------------------------------------------------------------------------
# Variant-specific structural tests
# ---------------------------------------------------------------------------


def test_bidirectional_no_choice_returns_result():
    result = BidirectionalNoChoice().run(SMALL_SCENARIO)
    assert isinstance(result, SimulationResult)


def test_full_model_returns_result():
    result = FullModel().run(SMALL_SCENARIO)
    assert isinstance(result, SimulationResult)


def test_single_sided_dropoff_returns_result():
    result = SingleSidedDropoff().run(SMALL_SCENARIO)
    assert isinstance(result, SimulationResult)


def test_ablation_no_rolling_horizon_returns_result():
    result = AblationNoRollingHorizon().run(SMALL_SCENARIO)
    assert isinstance(result, SimulationResult)


def test_ablation_no_choice_returns_result():
    result = AblationNoChoice().run(SMALL_SCENARIO)
    assert isinstance(result, SimulationResult)


# ---------------------------------------------------------------------------
# Phase 3 actual-offer choice integration
# ---------------------------------------------------------------------------


def test_full_model_emits_actual_offer_utility_logs():
    result = FullModel().run(SMALL_SCENARIO)

    assert len(result.utility_logs) == len(SMALL_SCENARIO.requests)
    for row in result.utility_logs:
        assert row["status"] in {"served", "choice_rejected", "feasibility_rejected"}
        assert row["detailed_reason"]
        assert row["passenger_type"]
        if row["status"] == "feasibility_rejected":
            assert "total_utility" not in row
            assert "pickup_mp_id" not in row
        else:
            assert row["pickup_mp_id"] is not None
            assert row["dropoff_mp_id"] is not None
            assert row["vehicle_id"] is not None
            assert "total_utility" in row
            assert "outside_utility" in row
            assert 0.0 <= row["acceptance_probability"] <= 1.0
            assert 0.0 <= row["random_draw"] <= 1.0


def test_choice_rejected_offers_are_not_inserted():
    for variant in [
        DoorToDoor(choice_params=ChoiceParameters(service_asc=-1000.0)),
        SingleSidedPickup(choice_params=ChoiceParameters(service_asc=-1000.0)),
        SingleSidedDropoff(choice_params=ChoiceParameters(service_asc=-1000.0)),
        FullModel(choice_params=ChoiceParameters(service_asc=-1000.0)),
    ]:
        state = variant._solve(SMALL_SCENARIO)
        assigned_ids = variant._assigned_request_ids(state)
        declined_ids = {
            request_id
            for request_id, evaluation in state.choice_evaluations.items()
            if evaluation.status == "choice_rejected"
        }

        assert declined_ids, f"{variant.name} did not produce declined requests"
        assert assigned_ids.isdisjoint(declined_ids)
        assert len(state.choice_evaluations) == len(SMALL_SCENARIO.requests)


def test_mnl_proxy_filter_is_not_used_by_behavioral_variants(monkeypatch):
    def fail_if_called(*args, **kwargs):
        raise AssertionError("_mnl_filter_requests should not run in Phase 3 paths")

    monkeypatch.setattr(variants_module, "_mnl_filter_requests", fail_if_called)

    for variant in [
        DoorToDoor(),
        SingleSidedPickup(),
        SingleSidedDropoff(),
        FullModel(),
        AblationNoRollingHorizon(),
    ]:
        result = variant.run(SMALL_SCENARIO)
        assert isinstance(result, SimulationResult)


def test_type_assignment_stable_across_service_designs():
    door_to_door = DoorToDoor().run(SMALL_SCENARIO)
    single_sided_pickup = SingleSidedPickup().run(SMALL_SCENARIO)
    single_sided_dropoff = SingleSidedDropoff().run(SMALL_SCENARIO)
    full_model = FullModel().run(SMALL_SCENARIO)

    dtd_types = {row["request_id"]: row["passenger_type"] for row in door_to_door.utility_logs}
    pickup_types = {row["request_id"]: row["passenger_type"] for row in single_sided_pickup.utility_logs}
    dropoff_types = {row["request_id"]: row["passenger_type"] for row in single_sided_dropoff.utility_logs}
    full_types = {row["request_id"]: row["passenger_type"] for row in full_model.utility_logs}

    assert dtd_types == full_types
    assert pickup_types == full_types
    assert dropoff_types == full_types


def test_type_share_hook_forces_deterministic_type_assignment():
    params = ChoiceParameters(type_shares={
        "price_sensitive": 1.0,
        "time_sensitive": 0.0,
        "walk_sensitive": 0.0,
    })

    result = FullModel(choice_params=params).run(SMALL_SCENARIO)

    assert {row["passenger_type"] for row in result.utility_logs} == {"price_sensitive"}


def test_service_asc_hook_changes_acceptance_probability_direction():
    def first_offered_probability(result):
        for row in result.utility_logs:
            if row["status"] != "feasibility_rejected":
                return row["acceptance_probability"]
        pytest.fail("Expected at least one feasible offer in the sensitivity scenario")

    low = DoorToDoor(choice_params=ChoiceParameters(service_asc=-100.0)).run(SMALL_SCENARIO)
    high = DoorToDoor(choice_params=ChoiceParameters(service_asc=100.0)).run(SMALL_SCENARIO)

    assert first_offered_probability(high) > first_offered_probability(low)


def test_behavioral_variants_have_concept_metadata():
    behavioral = [DoorToDoor(), SingleSidedPickup(), SingleSidedDropoff(), FullModel()]

    for variant in behavioral:
        metadata = variant.method_metadata
        for key in [
            "method_label",
            "service_design",
            "choice_model",
            "reoptimization",
            "routing_solver",
            "evidence_family",
            "diagnostic_role",
        ]:
            assert metadata[key]
        assert metadata["evidence_family"] == "behavioral_main"
        assert metadata["method_label"] not in {"FullModel", "AblationNoChoice"}

    full_metadata = FullModel().method_metadata
    assert "BidirectionalMP" in full_metadata["method_label"]
    assert full_metadata["legacy_class"] == "FullModel"


def test_deterministic_diagnostics_are_not_behavioral_main():
    behavioral_role = FullModel().method_metadata["diagnostic_role"]

    for variant in [BidirectionalNoChoice(), AblationNoChoice()]:
        metadata = variant.method_metadata
        assert metadata["evidence_family"] == "deterministic_diagnostic"
        assert metadata["diagnostic_role"] != behavioral_role
