"""Phase 5 readiness diagnostics for coverage and fixed accepted sets."""

from __future__ import annotations

import csv
import json
import time
from pathlib import Path

import pandas as pd

from experiments.config import VEHICLE_COUNTS
from experiments.metrics import compute_metrics
from experiments.phase05_pilot import (
    MAIN_BEHAVIORAL_METHOD_LABELS,
    PILOT_RESULTS_DIR,
    PILOT_SCALE,
    PILOT_SEEDS,
    run_phase05_pilot,
)
from experiments.scenarios import Scenario, generate_synthetic
from experiments.variants import DoorToDoorCapped, FullModel, GreedyInsertionBaseline


def _n_vehicles(scale: int) -> int:
    return VEHICLE_COUNTS.get(scale, max(1, scale // 10))


def _served_share_for_variant(variant, scale: int, seed: int) -> tuple[float, float]:
    scenario = generate_synthetic(scale, _n_vehicles(scale), seed)
    started = time.perf_counter()
    metrics = compute_metrics(variant.run(scenario))
    return metrics.served_share, time.perf_counter() - started


def run_matched_coverage_pilot(
    results_dir: str | Path = PILOT_RESULTS_DIR,
    scale: int = PILOT_SCALE,
    seeds: list[int] | tuple[int, ...] = PILOT_SEEDS,
    tolerance: float = 0.03,
) -> dict:
    """Run a pilot-scale matched-coverage diagnostic and persist rows."""
    root = Path(results_dir)
    root.mkdir(parents=True, exist_ok=True)
    seed_list = list(seeds)

    target_rows = []
    for seed in seed_list:
        served_share, runtime_s = _served_share_for_variant(FullModel(), scale, seed)
        target_rows.append(
            {
                "diagnostic_id": "phase05_matched_coverage",
                "seed": seed,
                "method_label": "BidirectionalMP_Choice_RH_ALNS",
                "target_served_share": served_share,
                "achieved_served_share": served_share,
                "abs_gap": 0.0,
                "tolerance": tolerance,
                "status": "target",
                "detailed_reason": "target behavioral-main served share",
                "runtime_s": runtime_s,
                "evidence_family": "supplementary_control",
                "diagnostic_role": "matched_coverage_target",
            }
        )

    target_share = (
        sum(row["target_served_share"] for row in target_rows) / len(target_rows)
        if target_rows
        else 0.0
    )
    capped_rows = []
    for seed in seed_list:
        served_share, runtime_s = _served_share_for_variant(
            DoorToDoorCapped(cap_share=target_share),
            scale,
            seed,
        )
        gap = abs(served_share - target_share)
        passed = gap <= tolerance
        capped_rows.append(
            {
                "diagnostic_id": "phase05_matched_coverage",
                "seed": seed,
                "method_label": "DoorToDoor_Capped_MatchedCoverage",
                "target_served_share": target_share,
                "achieved_served_share": served_share,
                "abs_gap": gap,
                "tolerance": tolerance,
                "status": "passed" if passed else "failed",
                "detailed_reason": (
                    "achieved served_share within tolerance"
                    if passed
                    else "achieved served_share outside tolerance"
                ),
                "runtime_s": runtime_s,
                "evidence_family": "supplementary_control",
                "diagnostic_role": "matched_coverage_control",
            }
        )

    rows = target_rows + capped_rows
    output_path = root / "matched_coverage_pilot.csv"
    with output_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)

    achieved_mean = (
        sum(row["achieved_served_share"] for row in capped_rows) / len(capped_rows)
        if capped_rows
        else 0.0
    )
    abs_gap = abs(achieved_mean - target_share)
    return {
        "passed": abs_gap <= tolerance,
        "target_served_share": target_share,
        "achieved_served_share": achieved_mean,
        "abs_gap": abs_gap,
        "tolerance": tolerance,
        "output_path": str(output_path),
        "row_count": len(rows),
    }


def _ensure_pilot_outputs(results_dir: Path, scale: int, seeds: list[int]) -> None:
    required = [
        results_dir / "synthetic_results.csv",
        results_dir / "utility_components.csv",
    ]
    if not all(path.exists() for path in required):
        run_phase05_pilot(results_dir=results_dir, scale=scale, seeds=seeds)


def _common_served_request_ids(utility: pd.DataFrame, seed: int) -> set[str]:
    seed_rows = utility[utility["seed"].astype(str) == str(seed)]
    served_by_method = []
    for method_label in MAIN_BEHAVIORAL_METHOD_LABELS:
        method_token = method_label.split("_Choice")[0]
        if method_label == "BidirectionalMP_Choice_RH_ALNS":
            method_names = {"FullModel"}
        elif method_token == "DoorToDoor":
            method_names = {"DoorToDoor"}
        elif method_token == "SingleSidedPickup":
            method_names = {"SingleSidedPickup"}
        elif method_token == "SingleSidedDropoff":
            method_names = {"SingleSidedDropoff"}
        else:
            method_names = set()
        method_rows = seed_rows[
            seed_rows["method"].isin(method_names) & (seed_rows["status"] == "served")
        ]
        served_by_method.append(set(method_rows["request_id"]))
    if not served_by_method:
        return set()
    return set.intersection(*served_by_method)


def _run_greedy_fixed_set(scale: int, seed: int, retained_ids: set[str]) -> dict:
    scenario = generate_synthetic(scale, _n_vehicles(scale), seed)
    retained_requests = [request for request in scenario.requests if request.id in retained_ids]
    fixed_scenario = Scenario(
        requests=retained_requests,
        vehicles=scenario.vehicles,
        meeting_points=scenario.meeting_points,
        area_km=scenario.area_km,
        name=f"{scenario.name}_fixed_set",
    )
    started = time.perf_counter()
    metrics = compute_metrics(GreedyInsertionBaseline().run(fixed_scenario))
    return {
        "routing_diagnostic": "GreedyInsertionBaseline",
        "routing_status": "completed",
        "routing_runtime_s": time.perf_counter() - started,
        "routing_vehicle_km": metrics.vehicle_km,
        "routing_served_share": metrics.served_share,
    }


def _optional_milp_row(scale: int, seed: int, include_milp: bool) -> dict:
    if not include_milp:
        return {
            "milp_status": "skipped",
            "milp_non_blocking": True,
            "milp_detailed_reason": "optional MILP diagnostic skipped for pilot fixed-set smoke",
        }
    from experiments.milp_gap import run_gap_experiment

    row = run_gap_experiment(scale, seed)
    return {
        "milp_status": row.get("status", row.get("milp_status", "unknown")),
        "milp_non_blocking": row.get("status") == "no_gurobi",
        "milp_detailed_reason": row.get("detailed_reason", ""),
        "milp_gap_pct": row.get("gap_pct"),
        "milp_comparable_gap": row.get("comparable_gap", False),
    }


def run_fixed_accepted_set_smoke(
    results_dir: str | Path = PILOT_RESULTS_DIR,
    scale: int = PILOT_SCALE,
    seed: int = 42,
    include_milp: bool = False,
) -> dict:
    """Persist a minimal fixed accepted-set diagnostic JSON artifact."""
    root = Path(results_dir)
    root.mkdir(parents=True, exist_ok=True)
    _ensure_pilot_outputs(root, scale, [seed])

    utility = pd.read_csv(root / "utility_components.csv")
    retained_ids = _common_served_request_ids(utility, seed)
    retained_share = len(retained_ids) / scale if scale else 0.0

    if retained_ids:
        routing = _run_greedy_fixed_set(scale, seed, retained_ids)
        status = "passed"
        detailed_reason = "fixed accepted-set greedy diagnostic completed"
    else:
        routing = {
            "routing_diagnostic": "GreedyInsertionBaseline",
            "routing_status": "skipped_empty_intersection",
            "routing_runtime_s": 0.0,
            "routing_vehicle_km": 0.0,
            "routing_served_share": 0.0,
        }
        status = "empty_intersection"
        detailed_reason = "common accepted request intersection is empty"

    payload = {
        "status": status,
        "detailed_reason": detailed_reason,
        "retained_request_count": len(retained_ids),
        "retained_share": retained_share,
        "retained_request_ids": sorted(retained_ids),
        "diagnostic_role": "fixed_accepted_set_smoke",
        "evidence_family": "algorithm_diagnostic",
        "seed": seed,
        "scale": scale,
        **routing,
        **_optional_milp_row(scale, seed, include_milp),
    }
    output_path = root / "fixed_accepted_set_smoke.json"
    output_path.write_text(json.dumps(payload, indent=2, sort_keys=True), encoding="utf-8")
    payload["output_path"] = str(output_path)
    payload["passed"] = True
    return payload


def main() -> None:
    matched = run_matched_coverage_pilot()
    fixed = run_fixed_accepted_set_smoke()
    print(json.dumps({"matched_coverage": matched, "fixed_accepted_set": fixed}, indent=2))


if __name__ == "__main__":
    main()
