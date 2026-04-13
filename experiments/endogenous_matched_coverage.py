"""
experiments/endogenous_matched_coverage.py — Endogenous matched-coverage experiment.

Replaces the post-hoc random rejection approach in matched_coverage.py with a
credible endogenous comparison: DoorToDoorCapped re-routes with a served-share cap
so that its served_share ≈ FullModel's mean served_share (~23.5%).

Strategy:
- Run FullModel (gamma=0) for seeds 42/43/44 → compute mean served_share (target).
- Run DoorToDoorCapped for each seed with cap_share=target_share.
  DoorToDoorCapped rejects requests once accepted_count/total >= cap_share,
  but continues optimizing routes for already-accepted passengers (endogenous re-routing).
- Assert ±3pp tolerance: abs(mean_dtdc_share - target_share) <= 0.03.
  If outside, print WARNING but still write CSV.

Output columns:
    variant      : "FullModel" or "DoorToDoorCapped"
    seed         : random seed
    served_share : accepted_count / n_requests
    vkm_per_trip : vkm / (n_requests * acceptance_rate)  [correct denominator]
"""
from __future__ import annotations

import csv
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from experiments.config import SEEDS, VEHICLE_COUNTS
from experiments.metrics import vkm_per_trip
from experiments.scenarios import generate_synthetic
from experiments.variants import DoorToDoorCapped, FullModel

SWEEP_SCALE = 200
OUTPUT_PATH = os.path.join("results", "endogenous_matched_coverage.csv")


def _run_fullmodel_baseline(seeds: list[int]) -> list[dict]:
    """Run FullModel at gamma=0 for each seed; return rows."""
    n_vehicles = VEHICLE_COUNTS[SWEEP_SCALE]
    rows = []
    for seed in seeds:
        scenario = generate_synthetic(
            n_requests=SWEEP_SCALE, n_vehicles=n_vehicles, seed=seed
        )
        model = FullModel(gamma=0.0)
        result = model.run(scenario)
        n = len(result.records)
        accepted = sum(1 for r in result.records if r.accepted)
        ar = accepted / n if n > 0 else 0.0
        rows.append({
            "variant": "FullModel",
            "seed": seed,
            "served_share": round(ar, 6),
            "vkm_per_trip": round(vkm_per_trip(result.total_vehicle_km, n, ar), 4),
        })
    return rows


def _run_doortodoor_capped(seed: int, cap_share: float, n_vehicles: int) -> dict:
    """
    Run DoorToDoorCapped with the given cap_share for one seed.

    DoorToDoorCapped endogenously rejects requests once the cap is reached,
    then continues optimizing routes for already-accepted passengers.
    """
    scenario = generate_synthetic(
        n_requests=SWEEP_SCALE, n_vehicles=n_vehicles, seed=seed
    )
    model = DoorToDoorCapped(cap_share=cap_share)
    result = model.run(scenario)
    n = len(result.records)
    accepted = sum(1 for r in result.records if r.accepted)
    ar = accepted / n if n > 0 else 0.0
    return {
        "variant": "DoorToDoorCapped",
        "seed": seed,
        "served_share": round(ar, 6),
        "vkm_per_trip": round(vkm_per_trip(result.total_vehicle_km, n, ar), 4),
    }


def endogenous_matched_coverage_experiment(seeds: list[int] = None) -> list[dict]:
    """
    Run endogenous matched-coverage experiment and return list of result dicts.

    Steps:
    1. Run FullModel for each seed → compute mean served_share (target).
    2. Run DoorToDoorCapped for each seed with cap_share=target_share.
    3. Assert ±3pp tolerance; warn if outside but still write CSV.
    4. Return fm_rows + dtdc_rows.
    """
    if seeds is None:
        seeds = SEEDS
    n_vehicles = VEHICLE_COUNTS[SWEEP_SCALE]

    print(f"Step 1: Running FullModel baseline (scale={SWEEP_SCALE}, seeds={seeds})")
    fm_rows = _run_fullmodel_baseline(seeds)
    target_share = sum(r["served_share"] for r in fm_rows) / len(fm_rows)
    print(f"  FullModel mean served_share = {target_share:.4f} (target for DoorToDoorCapped)")

    print(f"Step 2: Running DoorToDoorCapped with cap_share={target_share:.4f}")
    dtdc_rows = []
    for seed in seeds:
        row = _run_doortodoor_capped(seed, target_share, n_vehicles)
        print(f"  seed={seed}: DoorToDoorCapped served_share={row['served_share']:.4f}, "
              f"vkm/trip={row['vkm_per_trip']:.2f}")
        dtdc_rows.append(row)

    # Tolerance check
    mean_dtdc_share = sum(r["served_share"] for r in dtdc_rows) / len(dtdc_rows)
    tolerance_ok = abs(mean_dtdc_share - target_share) <= 0.03
    if not tolerance_ok:
        print(
            f"WARNING: DoorToDoorCapped mean served_share={mean_dtdc_share:.4f} "
            f"is outside ±3pp of target={target_share:.4f} "
            f"(diff={abs(mean_dtdc_share - target_share):.4f}). "
            f"Still writing CSV."
        )
    else:
        print(f"  Tolerance check PASSED: |{mean_dtdc_share:.4f} - {target_share:.4f}| <= 0.03")

    return fm_rows + dtdc_rows


def main() -> None:
    os.makedirs("results", exist_ok=True)
    rows = endogenous_matched_coverage_experiment()

    fieldnames = ["variant", "seed", "served_share", "vkm_per_trip"]
    with open(OUTPUT_PATH, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    # Print summary
    fm = [r for r in rows if r["variant"] == "FullModel"]
    dtdc = [r for r in rows if r["variant"] == "DoorToDoorCapped"]
    fm_mean_vkm = sum(r["vkm_per_trip"] for r in fm) / len(fm)
    dtdc_mean_vkm = sum(r["vkm_per_trip"] for r in dtdc) / len(dtdc)
    improvement = (dtdc_mean_vkm - fm_mean_vkm) / dtdc_mean_vkm * 100
    fm_mean_share = sum(r["served_share"] for r in fm) / len(fm)
    dtdc_mean_share = sum(r["served_share"] for r in dtdc) / len(dtdc)
    tolerance_ok = abs(dtdc_mean_share - fm_mean_share) <= 0.03

    print(f"\nEndogenous matched-coverage result:")
    print(f"  FullModel vkm/trip (mean): {fm_mean_vkm:.2f}")
    print(f"  DoorToDoorCapped vkm/trip (mean): {dtdc_mean_vkm:.2f}")
    print(f"  Improvement: {improvement:.1f}%")
    print(f"  FullModel served_share (mean): {fm_mean_share:.4f}")
    print(f"  DoorToDoorCapped served_share (mean): {dtdc_mean_share:.4f}")
    print(f"  Tolerance check (±3pp): {'PASSED' if tolerance_ok else 'FAILED'}")
    print(f"Saved {len(rows)} rows to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
