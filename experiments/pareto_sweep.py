"""
experiments/pareto_sweep.py -- Gamma rejection-penalty sweep for FullModel.

Sweeps Gamma over GAMMA_VALUES using FullModel at scale=200, seeds [42,43,44].
Computes per-run (served_share, vkm_per_served_trip, social_welfare) and
saves results to results/pareto_gamma_sweep.csv.

Usage:
    python experiments/pareto_sweep.py

Output columns:
    gamma            : rejection penalty value
    seed             : random seed used
    served_share     : accepted_count / total_requests  in [0, 1]
    vkm_per_served_trip : total_vehicle_km / accepted_count  (km per trip)
    social_welfare   : sum_r[z_r*U_rb* - (1-z_r)*gamma]
"""
from __future__ import annotations

import csv
import os
import sys

# Allow running from project root
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from experiments.config import SEEDS, VEHICLE_COUNTS
from experiments.metrics import compute_social_welfare
from experiments.scenarios import generate_synthetic_scenario
from experiments.variants import FullModel

GAMMA_VALUES = [0, 5, 10, 20, 50, 100]
SWEEP_SCALE = 200
OUTPUT_PATH = os.path.join("results", "pareto_gamma_sweep.csv")


def run_sweep() -> list[dict]:
    """Run FullModel for each (gamma, seed) combination and return row dicts."""
    n_vehicles = VEHICLE_COUNTS[SWEEP_SCALE]
    rows = []

    for gamma in GAMMA_VALUES:
        for seed in SEEDS:
            print(f"  gamma={gamma:3d}  seed={seed}", flush=True)
            scenario = generate_synthetic_scenario(
                n_requests=SWEEP_SCALE,
                n_vehicles=n_vehicles,
                seed=seed,
            )
            model = FullModel(gamma=gamma)
            result = model.run(scenario)

            total_requests = len(result.records)
            accepted_count = sum(1 for r in result.records if r.accepted)
            served_share = accepted_count / total_requests if total_requests > 0 else 0.0
            vkm_per_served = (
                result.total_vehicle_km / accepted_count if accepted_count > 0 else 0.0
            )
            w = compute_social_welfare(result.records, gamma=gamma)

            rows.append(
                {
                    "gamma": gamma,
                    "seed": seed,
                    "served_share": round(served_share, 6),
                    "vkm_per_served_trip": round(vkm_per_served, 4),
                    "social_welfare": round(w, 4),
                }
            )

    return rows


def main() -> None:
    os.makedirs("results", exist_ok=True)
    print(f"Pareto sweep: scale={SWEEP_SCALE}, gamma={GAMMA_VALUES}, seeds={SEEDS}")
    rows = run_sweep()

    fieldnames = ["gamma", "seed", "served_share", "vkm_per_served_trip", "social_welfare"]
    with open(OUTPUT_PATH, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"Saved {len(rows)} rows to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
