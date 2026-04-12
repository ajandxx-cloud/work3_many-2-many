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

import pytest

from experiments.metrics import SimulationResult, compute_metrics
from experiments.scenarios import generate_synthetic
from experiments.variants import (
    ALL_VARIANTS,
    AblationNoChoice,
    AblationNoRollingHorizon,
    BidirectionalNoChoice,
    DoorToDoor,
    FullModel,
    SingleSidedPickup,
)

# ---------------------------------------------------------------------------
# Shared fixture
# ---------------------------------------------------------------------------

SMALL_SCENARIO = generate_synthetic(n_requests=10, n_vehicles=3, seed=42)
MEDIUM_SCENARIO = generate_synthetic(n_requests=20, n_vehicles=3, seed=42)


# ---------------------------------------------------------------------------
# Registry tests
# ---------------------------------------------------------------------------


def test_all_variants_list_length():
    assert len(ALL_VARIANTS) == 6


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


# ---------------------------------------------------------------------------
# Variant-specific structural tests
# ---------------------------------------------------------------------------


def test_bidirectional_no_choice_returns_result():
    result = BidirectionalNoChoice().run(SMALL_SCENARIO)
    assert isinstance(result, SimulationResult)


def test_full_model_returns_result():
    result = FullModel().run(SMALL_SCENARIO)
    assert isinstance(result, SimulationResult)


def test_ablation_no_rolling_horizon_returns_result():
    result = AblationNoRollingHorizon().run(SMALL_SCENARIO)
    assert isinstance(result, SimulationResult)


def test_ablation_no_choice_returns_result():
    result = AblationNoChoice().run(SMALL_SCENARIO)
    assert isinstance(result, SimulationResult)
