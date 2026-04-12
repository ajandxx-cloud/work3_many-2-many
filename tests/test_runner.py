"""
tests/test_runner.py — Smoke tests for experiments/runner.py.

Tests run a minimal scale (n=20, 1 seed) to verify the runner completes
without exception and produces valid CSV outputs.
"""

from __future__ import annotations

import os
import tempfile

import pandas as pd
import pytest

from experiments.runner import run_all_experiments, _write_metrics_table, _make_row
from experiments.variants import ALL_VARIANTS


# ---------------------------------------------------------------------------
# Smoke test: minimal scale
# ---------------------------------------------------------------------------


def test_run_all_experiments_smoke(tmp_path):
    """run_all_experiments(scales=[20], seeds=[42], beijing=False) completes."""
    syn_rows, bei_rows = run_all_experiments(
        scales=[20],
        seeds=[42],
        beijing=False,
        results_dir=str(tmp_path),
    )
    assert len(syn_rows) == len(ALL_VARIANTS), (
        f"Expected {len(ALL_VARIANTS)} rows, got {len(syn_rows)}"
    )
    assert bei_rows == [], "beijing=False should produce no beijing rows"


def test_synthetic_results_csv_exists(tmp_path):
    """synthetic_results.csv is created and has > 0 rows."""
    run_all_experiments(scales=[20], seeds=[42], beijing=False, results_dir=str(tmp_path))
    csv_path = tmp_path / "synthetic_results.csv"
    assert csv_path.exists(), "synthetic_results.csv not created"
    df = pd.read_csv(csv_path)
    assert len(df) > 0, "synthetic_results.csv is empty"


def test_synthetic_results_columns(tmp_path):
    """synthetic_results.csv has all required columns."""
    run_all_experiments(scales=[20], seeds=[42], beijing=False, results_dir=str(tmp_path))
    df = pd.read_csv(tmp_path / "synthetic_results.csv")
    required = [
        "variant", "scale", "seed",
        "acceptance_rate", "vehicle_km",
        "avg_wait", "p95_wait",
        "avg_walk", "avg_ivt",
        "detour_ratio", "fairness_index", "cpu_time",
    ]
    for col in required:
        assert col in df.columns, f"Missing column: {col}"


def test_metrics_table_has_6_rows(tmp_path):
    """metrics_table.csv has exactly 6 rows (one per variant)."""
    run_all_experiments(scales=[20], seeds=[42], beijing=False, results_dir=str(tmp_path))
    df = pd.read_csv(tmp_path / "metrics_table.csv")
    assert len(df) == len(ALL_VARIANTS), (
        f"Expected {len(ALL_VARIANTS)} rows in metrics_table.csv, got {len(df)}"
    )


def test_metrics_table_no_nan(tmp_path):
    """metrics_table.csv has no NaN values in numeric columns."""
    run_all_experiments(scales=[20], seeds=[42], beijing=False, results_dir=str(tmp_path))
    df = pd.read_csv(tmp_path / "metrics_table.csv")
    numeric_cols = [c for c in df.columns if c != "variant"]
    nan_mask = df[numeric_cols].isnull()
    assert not nan_mask.any().any(), (
        f"NaN values found in metrics_table.csv:\n{df[numeric_cols][nan_mask.any(axis=1)]}"
    )


def test_metrics_table_columns(tmp_path):
    """metrics_table.csv has all 19 required columns."""
    run_all_experiments(scales=[20], seeds=[42], beijing=False, results_dir=str(tmp_path))
    df = pd.read_csv(tmp_path / "metrics_table.csv")
    metric_cols = [
        "acceptance_rate", "vehicle_km", "avg_wait", "p95_wait",
        "avg_walk", "avg_ivt", "detour_ratio", "fairness_index", "cpu_time",
    ]
    for m in metric_cols:
        assert f"{m}_mean" in df.columns, f"Missing column: {m}_mean"
        assert f"{m}_std" in df.columns, f"Missing column: {m}_std"


def test_acceptance_rate_in_range(tmp_path):
    """All acceptance_rate values are in [0, 1]."""
    run_all_experiments(scales=[20], seeds=[42], beijing=False, results_dir=str(tmp_path))
    df = pd.read_csv(tmp_path / "synthetic_results.csv")
    assert (df["acceptance_rate"] >= 0.0).all(), "acceptance_rate < 0 found"
    assert (df["acceptance_rate"] <= 1.0).all(), "acceptance_rate > 1 found"


def test_beijing_scenario_runs(tmp_path):
    """Beijing scenario runs without exception."""
    syn_rows, bei_rows = run_all_experiments(
        scales=[20],
        seeds=[42],
        beijing=True,
        results_dir=str(tmp_path),
    )
    assert len(bei_rows) == len(ALL_VARIANTS), (
        f"Expected {len(ALL_VARIANTS)} beijing rows, got {len(bei_rows)}"
    )
    csv_path = tmp_path / "beijing_results.csv"
    assert csv_path.exists(), "beijing_results.csv not created"
