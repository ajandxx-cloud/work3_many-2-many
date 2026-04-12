"""
experiments/weight_sensitivity.py — REV-12: Weight sensitivity analysis.

Runs FullModel and DoorToDoor under three objective weight configurations
at scale=200 (3 seeds each) to verify that the qualitative conclusion
"bidirectional FullModel reduces vkm/served-trip vs DoorToDoor" holds
across weight configurations.

Weight configurations (alpha index order: [op, wait, walk, IVT]):
  efficiency-focused: alpha = [1.0, 0.5, 0.5, 2.0]  (prioritise low IVT)
  equity-focused:     alpha = [1.0, 2.0, 2.0, 0.5]  (prioritise low wait/walk)
  balanced:           alpha = [1.0, 1.0, 1.0, 1.0]  (baseline)

Note: alpha_5 (rejection penalty) is not part of cost_weights passed to
greedy_insertion / RollingHorizon; it is only used in the MNL utility.
The 4-element cost_weights tuple maps to (alpha_op, alpha_wait, alpha_walk, alpha_ivt).

Writes results to results/weight_sensitivity.json.
"""
from __future__ import annotations

import json
import os

from experiments.config import SEEDS, VEHICLE_COUNTS
from experiments.metrics import compute_metrics
from experiments.scenarios import generate_synthetic
from experiments.variants import DoorToDoor, FullModel

# ---------------------------------------------------------------------------
# Weight configurations for REV-12
# alpha index order: (alpha_op, alpha_wait, alpha_walk, alpha_ivt)
# ---------------------------------------------------------------------------

WEIGHT_CONFIGS = [
    {
        "name": "efficiency-focused",
        "alpha_weights": (1.0, 0.5, 0.5, 2.0),
        "description": "Prioritises low IVT (alpha_IVT=2.0); reduces walk/wait weight",
    },
    {
        "name": "equity-focused",
        "alpha_weights": (1.0, 2.0, 2.0, 0.5),
        "description": "Prioritises low wait and walk (alpha_wait=alpha_walk=2.0)",
    },
    {
        "name": "balanced",
        "alpha_weights": (1.0, 1.0, 1.0, 1.0),
        "description": "Baseline configuration (matches config.py ALPHA_WEIGHTS)",
    },
]


def run_weight_sensitivity(config: dict, n_requests: int, seed: int) -> dict:
    """Run FullModel and DoorToDoor under a single weight config. Return metrics.

    Args:
        config: One entry from WEIGHT_CONFIGS (name, alpha_weights, description).
        n_requests: Number of requests (use 200 for REV-12).
        seed: Random seed.

    Returns:
        Dict with config_name, seed, per-variant vkm and acceptance_rate,
        vkm_per_trip for each variant, and reduction_pct.
    """
    n_vehicles = VEHICLE_COUNTS[n_requests]
    scenario = generate_synthetic(n_requests, n_vehicles, seed)
    alpha = config["alpha_weights"]

    # Instantiate variants with the specified cost_weights
    fm_variant = FullModel(cost_weights=alpha)
    dd_variant = DoorToDoor(cost_weights=alpha)

    fm_result = fm_variant.run(scenario)
    dd_result = dd_variant.run(scenario)

    fm_metrics = compute_metrics(fm_result)
    dd_metrics = compute_metrics(dd_result)

    fm_vkm = fm_metrics.vehicle_km
    fm_acc = fm_metrics.acceptance_rate
    dd_vkm = dd_metrics.vehicle_km
    dd_acc = dd_metrics.acceptance_rate

    # vkm per served trip — normalises for coverage differences across configs
    # Guard: denominator > 0 (T-09-07 mitigation)
    fm_vpt = fm_vkm / fm_acc if fm_acc > 0 else float("inf")
    dd_vpt = dd_vkm / dd_acc if dd_acc > 0 else float("inf")
    reduction = (dd_vpt - fm_vpt) / dd_vpt * 100.0 if dd_vpt > 0 and dd_vpt != float("inf") else None

    return {
        "config_name": config["name"],
        "seed": seed,
        "fullmodel_vkm": fm_vkm,
        "fullmodel_accept": fm_acc,
        "fullmodel_vkm_per_trip": fm_vpt,
        "doorToDoor_vkm": dd_vkm,
        "doorToDoor_accept": dd_acc,
        "doorToDoor_vkm_per_trip": dd_vpt,
        "reduction_pct": reduction,
    }


def main() -> None:
    N = 200
    rows = []
    for cfg in WEIGHT_CONFIGS:
        for seed in SEEDS:
            print(f"  {cfg['name']}, seed={seed} ...", flush=True)
            row = run_weight_sensitivity(cfg, N, seed)
            rows.append(row)
            r = row["reduction_pct"]
            print(f"    FM vkm/trip={row['fullmodel_vkm_per_trip']:.1f}  "
                  f"DD vkm/trip={row['doorToDoor_vkm_per_trip']:.1f}  "
                  f"reduction={r:.1f}%" if r is not None else "    N/A")

    _results_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "results")
    os.makedirs(_results_dir, exist_ok=True)
    out_path = os.path.join(_results_dir, "weight_sensitivity.json")
    with open(out_path, "w") as f:
        json.dump(rows, f, indent=2)
    print(f"Wrote {out_path}")


if __name__ == "__main__":
    main()
