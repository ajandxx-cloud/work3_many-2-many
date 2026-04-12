"""
analysis/test_sensitivity.py — Tests for sensitivity sweep functions.

TDD RED phase: these tests define the expected behavior of
sweep_walking_tolerance() and sweep_fleet_size().
"""
from __future__ import annotations

import csv
import os
import tempfile
import pytest


def test_sweep_walking_tolerance_row_count():
    """sweep_walking_tolerance() must return exactly 16 rows:
    6 rho_values * 2 variants (standard) + 2 density_tier rows (low/high).
    """
    from analysis.sensitivity import sweep_walking_tolerance, RHO_VALUES
    rows = sweep_walking_tolerance()
    assert len(rows) == len(RHO_VALUES) * 2 + 2, (
        f"Expected {len(RHO_VALUES) * 2 + 2} rows, got {len(rows)}"
    )


def test_sweep_walking_tolerance_required_keys():
    """Every row must have all required column keys."""
    from analysis.sensitivity import sweep_walking_tolerance
    rows = sweep_walking_tolerance()
    required = {"rho", "variant", "acceptance_rate", "vehicle_km", "avg_walk", "avg_wait", "density_tier"}
    for row in rows:
        assert required.issubset(row.keys()), f"Missing keys in row: {row}"


def test_sweep_walking_tolerance_non_negative_metrics():
    """All numeric metrics must be non-negative."""
    from analysis.sensitivity import sweep_walking_tolerance
    rows = sweep_walking_tolerance()
    for row in rows:
        assert row["acceptance_rate"] >= 0, f"Negative acceptance_rate: {row}"
        assert row["vehicle_km"] >= 0, f"Negative vehicle_km: {row}"
        assert row["avg_walk"] >= 0, f"Negative avg_walk: {row}"
        assert row["avg_wait"] >= 0, f"Negative avg_wait: {row}"


def test_sweep_walking_tolerance_density_tiers():
    """density_tier column must contain 'standard', 'low', and 'high' values."""
    from analysis.sensitivity import sweep_walking_tolerance
    rows = sweep_walking_tolerance()
    tiers = {row["density_tier"] for row in rows}
    assert "standard" in tiers, "Missing 'standard' density_tier rows"
    assert "low" in tiers, "Missing 'low' density_tier row"
    assert "high" in tiers, "Missing 'high' density_tier row"


def test_sweep_walking_tolerance_variants():
    """Standard rows must include both FullModel and DoorToDoor variants."""
    from analysis.sensitivity import sweep_walking_tolerance
    rows = sweep_walking_tolerance()
    standard_rows = [r for r in rows if r["density_tier"] == "standard"]
    variants = {r["variant"] for r in standard_rows}
    assert "FullModel" in variants
    assert "DoorToDoor" in variants


def test_sweep_fleet_size_row_count():
    """sweep_fleet_size() must return exactly 12 rows: 6 fleet sizes * 2 variants."""
    from analysis.sensitivity import sweep_fleet_size, FLEET_VALUES
    rows = sweep_fleet_size()
    assert len(rows) == len(FLEET_VALUES) * 2, (
        f"Expected {len(FLEET_VALUES) * 2} rows, got {len(rows)}"
    )


def test_sweep_fleet_size_required_keys():
    """Every fleet row must have all required column keys."""
    from analysis.sensitivity import sweep_fleet_size
    rows = sweep_fleet_size()
    required = {"n_vehicles", "variant", "acceptance_rate", "vehicle_km", "avg_wait"}
    for row in rows:
        assert required.issubset(row.keys()), f"Missing keys in row: {row}"


def test_sweep_fleet_size_non_negative_metrics():
    """All numeric metrics in fleet sweep must be non-negative."""
    from analysis.sensitivity import sweep_fleet_size
    rows = sweep_fleet_size()
    for row in rows:
        assert row["acceptance_rate"] >= 0
        assert row["vehicle_km"] >= 0
        assert row["avg_wait"] >= 0


def test_sensitivity_walk_csv_written():
    """sensitivity_walk.csv must exist after running sweep_walking_tolerance()."""
    from analysis.sensitivity import sweep_walking_tolerance
    sweep_walking_tolerance()
    csv_path = os.path.join(
        os.path.dirname(__file__), "..", "results", "sensitivity_walk.csv"
    )
    assert os.path.isfile(csv_path), f"CSV not found: {csv_path}"
    with open(csv_path, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    assert len(rows) >= 14, f"Expected >=14 rows in CSV, got {len(rows)}"


def test_sensitivity_fleet_csv_written():
    """sensitivity_fleet.csv must exist after running sweep_fleet_size()."""
    from analysis.sensitivity import sweep_fleet_size
    sweep_fleet_size()
    csv_path = os.path.join(
        os.path.dirname(__file__), "..", "results", "sensitivity_fleet.csv"
    )
    assert os.path.isfile(csv_path), f"CSV not found: {csv_path}"
    with open(csv_path, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    assert len(rows) == 12, f"Expected 12 rows in CSV, got {len(rows)}"
