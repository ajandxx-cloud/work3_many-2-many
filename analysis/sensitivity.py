"""
analysis/sensitivity.py — Sensitivity sweep functions for policy analysis.

Two public functions:
  sweep_walking_tolerance() — vary walking radius rho across RHO_VALUES,
      run FullModel + DoorToDoor, collect metrics. Also adds city-tier
      comparison rows (POLICY-06) at rho=500 for low/high density scenarios.
  sweep_fleet_size() — vary n_vehicles across FLEET_VALUES with fixed
      n_requests=200, run FullModel + DoorToDoor, collect metrics.

Both functions write results to results/ and return list of row dicts.

Threat T-04-01 mitigation: rho injection uses constructor parameters
(not monkey-patching), so no global state is modified. Thread-safe.
"""
from __future__ import annotations

import csv
import os
from typing import Any

from experiments.metrics import compute_metrics
from experiments.scenarios import generate_synthetic
from experiments.variants import DoorToDoor, FullModel

# ---------------------------------------------------------------------------
# Sweep parameter grids
# ---------------------------------------------------------------------------

RHO_VALUES = [200, 300, 400, 500, 700, 1000]   # meters — POLICY-02
FLEET_VALUES = [5, 10, 15, 20, 25, 30]          # vehicles — POLICY-03

# Density tier scenarios for POLICY-06 city tier comparison (at rho=500)
_DENSITY_TIERS = [
    {"density_tier": "low",  "n_requests": 100, "n_vehicles": 10},
    {"density_tier": "high", "n_requests": 400, "n_vehicles": 20},
]

_RESULTS_DIR = os.path.join(os.path.dirname(__file__), "..", "results")


def _ensure_results_dir() -> str:
    """Return absolute path to results/ directory, creating it if needed."""
    path = os.path.abspath(_RESULTS_DIR)
    os.makedirs(path, exist_ok=True)
    return path


def sweep_walking_tolerance() -> list[dict[str, Any]]:
    """Run walking tolerance sensitivity sweep (POLICY-02 + POLICY-06).

    For each rho in RHO_VALUES, runs FullModel and DoorToDoor on
    generate_synthetic(200, 15, 42) and records four metrics.
    Then appends city-tier comparison rows at rho=500 for low/high density.

    Returns:
        List of row dicts with keys:
        rho, variant, acceptance_rate, vehicle_km, avg_walk, avg_wait, density_tier
    """
    rows: list[dict[str, Any]] = []

    # --- Main sweep: standard density (n=200, v=15) ---
    for rho in RHO_VALUES:
        scenario = generate_synthetic(200, 15, 42)
        for variant_cls, variant_name in [
            (lambda r: FullModel(rho_p=r, rho_d=r), "FullModel"),
            (lambda r: DoorToDoor(rho_p=r, rho_d=r), "DoorToDoor"),
        ]:
            variant = variant_cls(rho)
            result = variant.run(scenario)
            m = compute_metrics(result)
            rows.append({
                "rho": rho,
                "variant": variant_name,
                "acceptance_rate": round(m.acceptance_rate, 4),
                "vehicle_km": round(m.vehicle_km, 4),
                "avg_walk": round(m.avg_walk, 4),
                "avg_wait": round(m.avg_wait, 4),
                "density_tier": "standard",
            })

    # --- City tier rows: POLICY-06 (FullModel only, rho=500) ---
    for tier in _DENSITY_TIERS:
        scenario = generate_synthetic(tier["n_requests"], tier["n_vehicles"], 42)
        variant = FullModel(rho_p=500, rho_d=500)
        result = variant.run(scenario)
        m = compute_metrics(result)
        rows.append({
            "rho": 500,
            "variant": "FullModel",
            "acceptance_rate": round(m.acceptance_rate, 4),
            "vehicle_km": round(m.vehicle_km, 4),
            "avg_walk": round(m.avg_walk, 4),
            "avg_wait": round(m.avg_wait, 4),
            "density_tier": tier["density_tier"],
        })

    # Write CSV
    results_dir = _ensure_results_dir()
    out_path = os.path.join(results_dir, "sensitivity_walk.csv")
    fieldnames = ["rho", "variant", "acceptance_rate", "vehicle_km", "avg_walk", "avg_wait", "density_tier"]
    with open(out_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"sensitivity_walk.csv written: {len(rows)} rows -> {out_path}")
    return rows


def sweep_fleet_size() -> list[dict[str, Any]]:
    """Run fleet size sensitivity sweep (POLICY-03).

    For each n_vehicles in FLEET_VALUES, runs FullModel and DoorToDoor on
    generate_synthetic(200, n_vehicles, 42) and records three metrics.

    Returns:
        List of row dicts with keys:
        n_vehicles, variant, acceptance_rate, vehicle_km, avg_wait
    """
    rows: list[dict[str, Any]] = []

    for n_vehicles in FLEET_VALUES:
        scenario = generate_synthetic(200, n_vehicles, 42)
        for variant_cls, variant_name in [
            (FullModel, "FullModel"),
            (DoorToDoor, "DoorToDoor"),
        ]:
            variant = variant_cls()
            result = variant.run(scenario)
            m = compute_metrics(result)
            rows.append({
                "n_vehicles": n_vehicles,
                "variant": variant_name,
                "acceptance_rate": round(m.acceptance_rate, 4),
                "vehicle_km": round(m.vehicle_km, 4),
                "avg_wait": round(m.avg_wait, 4),
            })

    # Write CSV
    results_dir = _ensure_results_dir()
    out_path = os.path.join(results_dir, "sensitivity_fleet.csv")
    fieldnames = ["n_vehicles", "variant", "acceptance_rate", "vehicle_km", "avg_wait"]
    with open(out_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"sensitivity_fleet.csv written: {len(rows)} rows -> {out_path}")
    return rows


if __name__ == "__main__":
    sweep_walking_tolerance()
    sweep_fleet_size()
    print("Sensitivity sweeps complete.")
