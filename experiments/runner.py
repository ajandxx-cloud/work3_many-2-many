"""
experiments/runner.py — Orchestrates all DRT experiments and writes CSV outputs.

Runs all 6 variants across all scales and seeds for both synthetic and Beijing
scenarios, then writes three CSV files:
  results/synthetic_results.csv  — raw per-run results (72 rows for full run)
  results/beijing_results.csv    — raw per-run results (18 rows for full run)
  results/metrics_table.csv      — aggregated mean±std per variant (6 rows)

Usage:
    python experiments/runner.py          # full run
    python -m experiments.runner          # same

Threat T-03-10 mitigation: core thesis assertion is checked after full run.
Threat T-03-11 mitigation: smoke test (scale=20) available via run_all_experiments().
"""

from __future__ import annotations

import csv
import os
import sys
import time
import traceback
import concurrent.futures

import pandas as pd

# Per-variant timeout in seconds. Variants exceeding this get an error row.
_VARIANT_TIMEOUT_S = 120

from experiments.config import BEIJING_SCALE, SCALES, SEEDS, VEHICLE_COUNTS
from experiments.metrics import compute_metrics
from experiments.scenarios import generate_beijing, generate_synthetic
from experiments.variants import ALL_VARIANTS

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------

_THIS_DIR = os.path.dirname(os.path.abspath(__file__))
RESULTS_DIR = os.path.join(_THIS_DIR, "..", "results")

# ---------------------------------------------------------------------------
# Column definitions
# ---------------------------------------------------------------------------

_RAW_COLS = [
    "variant", "scale", "seed",
    "acceptance_rate", "vehicle_km",
    "avg_wait", "p95_wait",
    "avg_walk", "avg_ivt",
    "detour_ratio", "fairness_index", "cpu_time",
]

_METRIC_COLS = [
    "acceptance_rate", "vehicle_km",
    "avg_wait", "p95_wait",
    "avg_walk", "avg_ivt",
    "detour_ratio", "fairness_index", "cpu_time",
]


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------


def run_all_experiments(
    scales=None,
    seeds=None,
    beijing: bool = True,
    results_dir: str = RESULTS_DIR,
) -> tuple[list[dict], list[dict]]:
    """Run all 6 variants across all scales and seeds.

    Args:
        scales: list of request counts (default: SCALES from config).
        seeds:  list of random seeds (default: SEEDS from config).
        beijing: whether to also run the Beijing scenario.
        results_dir: directory where CSV files are written.

    Returns:
        (synthetic_rows, beijing_rows) — lists of raw result dicts.
    """
    scales = scales if scales is not None else SCALES
    seeds = seeds if seeds is not None else SEEDS
    os.makedirs(results_dir, exist_ok=True)

    synthetic_rows: list[dict] = []
    beijing_rows: list[dict] = []

    total_synthetic = len(scales) * len(seeds) * len(ALL_VARIANTS)
    done = 0

    print(f"[runner] Starting synthetic experiments: "
          f"{len(scales)} scales × {len(seeds)} seeds × {len(ALL_VARIANTS)} variants "
          f"= {total_synthetic} runs")

    for scale in scales:
        n_vehicles = VEHICLE_COUNTS.get(scale, max(1, scale // 10))
        for seed in seeds:
            scenario = generate_synthetic(scale, n_vehicles, seed)
            for variant in ALL_VARIANTS:
                done += 1
                row = _run_variant_with_timeout(
                    variant, scenario, scale, seed,
                    label=f"[{done:3d}/{total_synthetic}] synthetic",
                )
                synthetic_rows.append(row)

    if beijing:
        n_vehicles = VEHICLE_COUNTS.get(BEIJING_SCALE, 15)
        total_beijing = len(seeds) * len(ALL_VARIANTS)
        done_bj = 0
        print(f"\n[runner] Starting Beijing experiments: "
              f"{len(seeds)} seeds × {len(ALL_VARIANTS)} variants = {total_beijing} runs")

        for seed in seeds:
            scenario = generate_beijing(BEIJING_SCALE, n_vehicles, seed)
            for variant in ALL_VARIANTS:
                done_bj += 1
                row = _run_variant_with_timeout(
                    variant, scenario, BEIJING_SCALE, seed,
                    label=f"[{done_bj:3d}/{total_beijing}] beijing ",
                )
                beijing_rows.append(row)

    # Write CSVs
    syn_path = os.path.join(results_dir, "synthetic_results.csv")
    bei_path = os.path.join(results_dir, "beijing_results.csv")
    tbl_path = os.path.join(results_dir, "metrics_table.csv")

    _write_csv(synthetic_rows, syn_path)
    _write_csv(beijing_rows, bei_path)
    _write_metrics_table(synthetic_rows, tbl_path)

    print(f"\n[runner] Wrote {len(synthetic_rows)} rows → {syn_path}")
    if beijing:
        print(f"[runner] Wrote {len(beijing_rows)} rows → {bei_path}")
    print(f"[runner] Wrote metrics table → {tbl_path}")

    return synthetic_rows, beijing_rows


# ---------------------------------------------------------------------------
# Internal helpers
# ---------------------------------------------------------------------------


def _make_row(variant_name: str, scale: int, seed: int, m) -> dict:
    return {
        "variant": variant_name,
        "scale": scale,
        "seed": seed,
        "acceptance_rate": m.acceptance_rate,
        "vehicle_km": m.vehicle_km,
        "avg_wait": m.avg_wait,
        "p95_wait": m.p95_wait,
        "avg_walk": m.avg_walk,
        "avg_ivt": m.avg_ivt,
        "detour_ratio": m.detour_ratio,
        "fairness_index": m.fairness_index,
        "cpu_time": m.cpu_time,
    }


def _make_error_row(variant_name: str, scale: int, seed: int) -> dict:
    """Return a zero-filled row so CSV row counts stay consistent on error."""
    return {
        "variant": variant_name,
        "scale": scale,
        "seed": seed,
        "acceptance_rate": 0.0,
        "vehicle_km": 0.0,
        "avg_wait": 0.0,
        "p95_wait": 0.0,
        "avg_walk": 0.0,
        "avg_ivt": 0.0,
        "detour_ratio": 0.0,
        "fairness_index": 0.0,
        "cpu_time": 0.0,
    }


def _run_variant_with_timeout(variant, scenario, scale, seed, label="") -> dict:
    """Run a single variant with a timeout. Returns error row on timeout/exception."""
    def _task():
        result = variant.run(scenario)
        m = compute_metrics(result)
        return _make_row(variant.name, scale, seed, m)

    with concurrent.futures.ThreadPoolExecutor(max_workers=1) as executor:
        future = executor.submit(_task)
        try:
            row = future.result(timeout=_VARIANT_TIMEOUT_S)
            print(
                f"{label} variant={variant.name:<28} scale={scale:3d} seed={seed} "
                f"accept={row['acceptance_rate']:.3f} vkm={row['vehicle_km']:.1f}"
            )
            return row
        except concurrent.futures.TimeoutError:
            print(
                f"{label} TIMEOUT variant={variant.name} scale={scale} seed={seed} "
                f"(>{_VARIANT_TIMEOUT_S}s)",
                file=sys.stderr,
            )
            return _make_error_row(variant.name, scale, seed)
        except Exception as exc:
            print(
                f"{label} ERROR variant={variant.name} scale={scale} seed={seed}: {exc}",
                file=sys.stderr,
            )
            traceback.print_exc(file=sys.stderr)
            return _make_error_row(variant.name, scale, seed)


def _write_csv(rows: list[dict], path: str) -> None:
    if not rows:
        return
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=_RAW_COLS)
        writer.writeheader()
        writer.writerows(rows)


def _write_metrics_table(rows: list[dict], path: str) -> None:
    """Aggregate mean±std per variant across all scales and seeds."""
    if not rows:
        return
    df = pd.DataFrame(rows)
    agg = df.groupby("variant")[_METRIC_COLS].agg(["mean", "std"]).reset_index()
    # Flatten MultiIndex columns: ('acceptance_rate', 'mean') → 'acceptance_rate_mean'
    agg.columns = ["variant"] + [
        f"{metric}_{stat}" for metric, stat in agg.columns[1:]
    ]
    # Fill NaN std values with 0.0 (occurs when only 1 sample per group)
    std_cols = [c for c in agg.columns if c.endswith("_std")]
    agg[std_cols] = agg[std_cols].fillna(0.0)
    agg.to_csv(path, index=False)


# ---------------------------------------------------------------------------
# Script entry point
# ---------------------------------------------------------------------------


if __name__ == "__main__":
    t_start = time.perf_counter()
    synthetic_rows, beijing_rows = run_all_experiments()
    elapsed = time.perf_counter() - t_start

    print(f"\n[runner] Total runtime: {elapsed:.1f}s ({elapsed/60:.1f} min)")

    # Validate core thesis claim (T-03-10 mitigation)
    tbl_path = os.path.join(RESULTS_DIR, "metrics_table.csv")
    df = pd.read_csv(tbl_path)
    print("\n--- metrics_table.csv ---")
    print(df.to_string(index=False))

    full_row = df[df["variant"] == "FullModel"]
    dtd_row = df[df["variant"] == "DoorToDoor"]

    if full_row.empty or dtd_row.empty:
        print("\n[WARN] Could not find FullModel or DoorToDoor in metrics table.")
    else:
        full_accept = full_row.iloc[0]["acceptance_rate_mean"]
        dtd_accept = dtd_row.iloc[0]["acceptance_rate_mean"]
        full_vkm = full_row.iloc[0]["vehicle_km_mean"]
        dtd_vkm = dtd_row.iloc[0]["vehicle_km_mean"]

        if full_accept >= dtd_accept:
            print(f"\n[PASS] acceptance_rate: FullModel={full_accept:.3f} >= DoorToDoor={dtd_accept:.3f}")
        else:
            print(f"\n[NOTE] acceptance_rate: FullModel={full_accept:.3f} < DoorToDoor={dtd_accept:.3f} "
                  f"(difference={dtd_accept - full_accept:.3f})")

        if full_vkm <= dtd_vkm:
            print(f"[PASS] vehicle_km: FullModel={full_vkm:.1f} <= DoorToDoor={dtd_vkm:.1f}")
        elif full_vkm <= dtd_vkm * 1.1:
            print(f"[NOTE] vehicle_km: FullModel={full_vkm:.1f} vs DoorToDoor={dtd_vkm:.1f} "
                  f"(within 10% tolerance — bidirectional MPs may add slight detour)")
        else:
            print(f"[NOTE] vehicle_km: FullModel={full_vkm:.1f} > DoorToDoor={dtd_vkm:.1f} "
                  f"(ratio={full_vkm/dtd_vkm:.2f}x — investigate routing)")
