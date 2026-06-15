"""
tests/test_runner.py — Smoke tests for experiments/runner.py.

Tests run a minimal scale (n=20, 1 seed) to verify the runner completes
without exception and produces valid CSV outputs.

Uses a session-scoped fixture to run the experiment once and share results
across all tests (avoids re-running the slow FullModel variant 8 times).
"""

from __future__ import annotations

import os
import sys
import tempfile

import pandas as pd
import pytest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import experiments.runner as runner_module
from experiments.runner import run_all_experiments, _write_metrics_table, _make_row
from experiments.variants import ALL_VARIANTS


# ---------------------------------------------------------------------------
# Session-scoped fixture: run once, share across all tests
# ---------------------------------------------------------------------------


@pytest.fixture(scope="session")
def smoke_results(tmp_path_factory):
    """Run smoke experiment once; return (syn_rows, bei_rows, tmp_path)."""
    tmp_path = tmp_path_factory.mktemp("runner_smoke")
    syn_rows, bei_rows = run_all_experiments(
        scales=[8],
        seeds=[42],
        beijing=False,
        results_dir=str(tmp_path),
    )
    return syn_rows, bei_rows, tmp_path


# ---------------------------------------------------------------------------
# Smoke test: minimal scale
# ---------------------------------------------------------------------------


def test_run_all_experiments_smoke(smoke_results):
    """run_all_experiments(scales=[20], seeds=[42], beijing=False) completes."""
    syn_rows, bei_rows, tmp_path = smoke_results
    assert len(syn_rows) == len(ALL_VARIANTS), (
        f"Expected {len(ALL_VARIANTS)} rows, got {len(syn_rows)}"
    )


def test_synthetic_results_csv_exists(smoke_results):
    """synthetic_results.csv is created and has > 0 rows."""
    syn_rows, bei_rows, tmp_path = smoke_results
    csv_path = tmp_path / "synthetic_results.csv"
    assert csv_path.exists(), "synthetic_results.csv not created"
    df = pd.read_csv(csv_path)
    assert len(df) > 0, "synthetic_results.csv is empty"


def test_synthetic_results_columns(smoke_results):
    """synthetic_results.csv has all required columns."""
    syn_rows, bei_rows, tmp_path = smoke_results
    df = pd.read_csv(tmp_path / "synthetic_results.csv")
    required = [
        "variant", "scale", "seed",
        "acceptance_rate", "vehicle_km",
        "served_share", "behavioral_acceptance_rate",
        "choice_rejection_rate", "feasibility_rejection_rate",
        "avg_wait", "p95_wait",
        "avg_walk", "avg_ivt",
        "detour_ratio", "fairness_index", "cpu_time",
    ]
    for col in required:
        assert col in df.columns, f"Missing column: {col}"


def test_metrics_table_has_6_rows(smoke_results):
    """metrics_table.csv has exactly 6 rows (one per variant)."""
    syn_rows, bei_rows, tmp_path = smoke_results
    df = pd.read_csv(tmp_path / "metrics_table.csv")
    assert len(df) == len(ALL_VARIANTS), (
        f"Expected {len(ALL_VARIANTS)} rows in metrics_table.csv, got {len(df)}"
    )


def test_metrics_table_no_nan(smoke_results):
    """metrics_table.csv has no NaN values in numeric columns."""
    syn_rows, bei_rows, tmp_path = smoke_results
    df = pd.read_csv(tmp_path / "metrics_table.csv")
    numeric_cols = [c for c in df.columns if c != "variant"]
    nan_mask = df[numeric_cols].isnull()
    assert not nan_mask.any().any(), (
        f"NaN values found in metrics_table.csv:\n{df[numeric_cols][nan_mask.any(axis=1)]}"
    )


def test_metrics_table_columns(smoke_results):
    """metrics_table.csv has all 19 required columns."""
    syn_rows, bei_rows, tmp_path = smoke_results
    df = pd.read_csv(tmp_path / "metrics_table.csv")
    metric_cols = [
        "acceptance_rate", "vehicle_km",
        "served_share", "behavioral_acceptance_rate",
        "choice_rejection_rate", "feasibility_rejection_rate",
        "avg_wait", "p95_wait",
        "avg_walk", "avg_ivt", "detour_ratio", "fairness_index", "cpu_time",
    ]
    for m in metric_cols:
        assert f"{m}_mean" in df.columns, f"Missing column: {m}_mean"
        assert f"{m}_std" in df.columns, f"Missing column: {m}_std"


def test_acceptance_rate_in_range(smoke_results):
    """All acceptance_rate values are in [0, 1]."""
    syn_rows, bei_rows, tmp_path = smoke_results
    df = pd.read_csv(tmp_path / "synthetic_results.csv")
    assert (df["acceptance_rate"] >= 0.0).all(), "acceptance_rate < 0 found"
    assert (df["acceptance_rate"] <= 1.0).all(), "acceptance_rate > 1 found"


def test_beijing_scenario_runs(smoke_results):
    """Primary smoke fixture skips Beijing; targeted test covers it separately."""
    syn_rows, bei_rows, tmp_path = smoke_results
    assert bei_rows == []


def test_small_beijing_scenario_runs(tmp_path, monkeypatch):
    """Beijing scenario runs without exception at a unit-test scale."""
    monkeypatch.setattr(runner_module, "BEIJING_SCALE", 8)
    syn_rows, bei_rows = run_all_experiments(
        scales=[],
        seeds=[42],
        beijing=True,
        results_dir=str(tmp_path),
    )

    assert len(bei_rows) == len(ALL_VARIANTS), (
        f"Expected {len(ALL_VARIANTS)} beijing rows, got {len(bei_rows)}"
    )
    csv_path = tmp_path / "beijing_results.csv"
    assert csv_path.exists(), "beijing_results.csv not created"


def test_utility_components_csv_exists(smoke_results):
    syn_rows, bei_rows, tmp_path = smoke_results
    csv_path = tmp_path / "utility_components.csv"

    assert csv_path.exists(), "utility_components.csv not created"
    df = pd.read_csv(csv_path)
    assert len(df) > 0, "utility_components.csv is empty"


def test_utility_components_columns_and_join_keys(smoke_results):
    syn_rows, bei_rows, tmp_path = smoke_results
    df = pd.read_csv(tmp_path / "utility_components.csv")
    required = [
        "run_id", "seed", "scenario", "method", "request_id",
        "status", "detailed_reason", "passenger_type",
        "pickup_walk", "dropoff_walk", "wait_time", "ivt", "fare",
        "service_design", "pickup_mp_id", "dropoff_mp_id", "vehicle_id",
        "scheduled_pickup", "scheduled_dropoff",
        "walk_utility", "wait_utility", "ivt_utility", "fare_utility",
        "service_asc", "outside_option_constant", "total_utility",
        "outside_utility", "acceptance_probability", "random_draw",
    ]

    for col in required:
        assert col in df.columns, f"Missing utility column: {col}"
    assert df[["run_id", "seed", "scenario", "method", "request_id"]].notna().all().all()


def test_feasibility_rejections_do_not_fabricate_utility(smoke_results):
    syn_rows, bei_rows, tmp_path = smoke_results
    df = pd.read_csv(tmp_path / "utility_components.csv")
    feasibility = df[df["status"] == "feasibility_rejected"]

    if not feasibility.empty:
        assert feasibility["total_utility"].isna().all()
        assert feasibility["acceptance_probability"].isna().all()
