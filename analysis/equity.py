"""
analysis/equity.py — Equity analysis across passenger types for the FullModel.

Runs FullModel on synthetic(200, 15, seed) for seeds [42, 43, 44], groups
PassengerRecord objects by passenger_type, computes per-type service metrics,
and calculates the Gini coefficient of acceptance rates across the 3 types.

Output: results/equity_table.csv
"""
from __future__ import annotations

import csv
import os
from pathlib import Path

from experiments.config import SEEDS
from experiments.scenarios import generate_synthetic
from experiments.variants import FullModel

# Canonical passenger type labels (must match PassengerRecord.passenger_type values)
PASSENGER_TYPES = ["price_sensitive", "time_sensitive", "walk_sensitive"]

# Output path relative to project root
_RESULTS_DIR = Path(__file__).parent.parent / "results"
_OUTPUT_CSV = _RESULTS_DIR / "equity_table.csv"


def _gini_three(values: list[float]) -> float:
    """Gini coefficient for exactly 3 non-negative values."""
    arr = sorted(values)
    n = len(arr)
    s = sum(arr)
    if s == 0:
        return 0.0
    return (2 * sum((i + 1) * v for i, v in enumerate(arr)) / (n * s)) - (n + 1) / n


def run_equity_analysis() -> dict:
    """Run FullModel across 3 seeds and compute per-type equity metrics.

    Returns:
        dict with keys:
          "rows"  — list of 3 dicts, one per passenger type, each containing:
                    passenger_type, acceptance_rate, avg_wait, avg_walk,
                    avg_ivt, gini_acceptance
          "gini"  — float, Gini coefficient of acceptance rates across types
    """
    model = FullModel()

    # Accumulate records across all seeds
    all_records = []
    for seed in SEEDS:
        scenario = generate_synthetic(200, 15, seed)
        result = model.run(scenario)
        all_records.extend(result.records)

    # Group by passenger_type
    grouped: dict[str, list] = {pt: [] for pt in PASSENGER_TYPES}
    for record in all_records:
        if record.passenger_type in grouped:
            grouped[record.passenger_type].append(record)

    # Compute per-type metrics
    rows = []
    acceptance_rates = []
    for pt in PASSENGER_TYPES:
        records = grouped[pt]
        total = len(records)
        accepted = [r for r in records if r.accepted]
        n_accepted = len(accepted)

        acceptance_rate = n_accepted / total if total > 0 else 0.0
        acceptance_rates.append(acceptance_rate)

        if accepted:
            avg_wait = sum(r.wait_time for r in accepted) / n_accepted
            avg_walk = sum(r.pickup_walk + r.dropoff_walk for r in accepted) / n_accepted
            avg_ivt = sum(r.ivt for r in accepted) / n_accepted
        else:
            avg_wait = 0.0
            avg_walk = 0.0
            avg_ivt = 0.0

        rows.append({
            "passenger_type": pt,
            "acceptance_rate": acceptance_rate,
            "avg_wait": avg_wait,
            "avg_walk": avg_walk,
            "avg_ivt": avg_ivt,
        })

    gini_value = _gini_three(acceptance_rates)

    # Attach gini_acceptance to every row (system-level value, same for all)
    for row in rows:
        row["gini_acceptance"] = gini_value

    # Write CSV
    _RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    fieldnames = ["passenger_type", "acceptance_rate", "avg_wait", "avg_walk", "avg_ivt", "gini_acceptance"]
    with open(_OUTPUT_CSV, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    return {"rows": rows, "gini": gini_value}


if __name__ == "__main__":
    result = run_equity_analysis()
    print(f"Gini of acceptance rates: {result['gini']:.4f}")
    for row in result["rows"]:
        print(row)
