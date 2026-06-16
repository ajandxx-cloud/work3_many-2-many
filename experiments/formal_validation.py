"""Persisted artifact validation for Phase 6 formal synthetic experiments."""

from __future__ import annotations

import csv
import inspect
import json
import math
from pathlib import Path
from typing import Iterable

import pandas as pd

from experiments.pilot_validation import (
    NON_NEGATIVE_FIELDS,
    RATIO_FIELDS,
    REQUIRED_UTILITY_KEYS,
)
from experiments.variants import ALL_VARIANTS

REQUIRED_RAW_FIELDS = {
    "run_id",
    "config_id",
    "variant",
    "scale",
    "seed",
    "scenario",
    "method_label",
    "service_design",
    "choice_model",
    "reoptimization",
    "routing_solver",
    "evidence_family",
    "diagnostic_role",
    "status",
    "detailed_reason",
    "runtime_s",
    "error_message",
    "result_schema_version",
    "timestamp_utc",
    "artifact_dir",
    "git_commit_or_code_hash",
    "n_requests",
    "n_offered",
    "n_served",
    "total_vehicle_km",
}

QUARTET_METRIC_FIELDS = {
    "vehicle_km",
    "served_share",
    "vkm_per_served_trip",
    "vkm_per_original_request",
}

RERUN_LEDGER_COLUMNS = [
    "run_id",
    "config_id",
    "seed",
    "scale",
    "method",
    "status",
    "error",
    "reason",
    "fix",
    "rerun_result",
]


def _empty_result(results_dir: Path) -> dict:
    return {
        "passed": True,
        "schema_drift": False,
        "denominator_checks": {},
        "errors": [],
        "warnings": [],
        "row_counts": {},
        "checked_files": [],
        "results_dir": str(results_dir),
        "ledger_path": "",
    }


def _read_csv(path: Path, result: dict) -> pd.DataFrame | None:
    if not path.exists():
        result["errors"].append(f"missing required file: {path}")
        return None
    result["checked_files"].append(str(path))
    return pd.read_csv(path)


def _check_columns(df: pd.DataFrame, required: Iterable[str], label: str, result: dict) -> None:
    missing = sorted(set(required) - set(df.columns))
    if missing:
        result["schema_drift"] = True
        result["errors"].append(f"{label} missing required columns: {', '.join(missing)}")


def _check_numeric_field(df: pd.DataFrame, field: str, result: dict) -> pd.Series | None:
    if field not in df.columns:
        return None
    values = pd.to_numeric(df[field], errors="coerce")
    invalid_mask = values.isna() | ~values.map(math.isfinite)
    if invalid_mask.any():
        result["errors"].append(f"{field} contains NaN or infinity")
    return values


def _validate_numeric_ranges(df: pd.DataFrame, result: dict) -> None:
    for field in sorted(RATIO_FIELDS & set(df.columns)):
        values = _check_numeric_field(df, field, result)
        if values is not None and ((values < 0.0) | (values > 1.0)).any():
            result["errors"].append(f"{field} must be in [0, 1]")

    for field in sorted(NON_NEGATIVE_FIELDS & set(df.columns)):
        values = _check_numeric_field(df, field, result)
        if values is not None and (values < 0.0).any():
            result["errors"].append(f"{field} must be non-negative")


def _series_close(left: pd.Series, right: pd.Series, tolerance: float = 1e-6) -> pd.Series:
    return (left - right).abs() <= tolerance


def _validate_denominators(main: pd.DataFrame, result: dict) -> None:
    """Check Phase 2 metric-contract denominators on completed formal rows."""
    completed = main[main["status"] == "completed"].copy()
    if completed.empty:
        result["denominator_checks"] = {
            "served_share": "skipped_no_completed_rows",
            "vkm_per_served_trip": "skipped_no_completed_rows",
            "vkm_per_original_request": "skipped_no_completed_rows",
            "behavioral_acceptance_rate": "skipped_no_completed_rows",
        }
        return

    required = {
        "n_requests",
        "n_served",
        "served_share",
        "behavioral_acceptance_rate",
        "choice_rejection_rate",
        "feasibility_rejection_rate",
        "vehicle_km",
        "total_vehicle_km",
        "vkm_per_served_trip",
        "vkm_per_original_request",
    }
    if not required.issubset(completed.columns):
        result["denominator_checks"] = {"status": "skipped_missing_columns"}
        return

    n_requests = pd.to_numeric(completed["n_requests"], errors="coerce")
    n_served = pd.to_numeric(completed["n_served"], errors="coerce")
    vehicle_km = pd.to_numeric(completed["vehicle_km"], errors="coerce")
    total_vehicle_km = pd.to_numeric(completed["total_vehicle_km"], errors="coerce")
    safe_requests = n_requests.where(n_requests > 0)
    safe_served = n_served.where(n_served > 0)

    expected_served_share = (n_served / safe_requests).fillna(0.0)
    expected_vkm_original = (vehicle_km / safe_requests).fillna(0.0)
    expected_vkm_served = (vehicle_km / safe_served).fillna(0.0)
    expected_behavioral_acceptance = (
        1.0 - pd.to_numeric(completed["choice_rejection_rate"], errors="coerce")
    )
    rejection_sum = (
        pd.to_numeric(completed["served_share"], errors="coerce")
        + pd.to_numeric(completed["choice_rejection_rate"], errors="coerce")
        + pd.to_numeric(completed["feasibility_rejection_rate"], errors="coerce")
    )

    checks = {
        "served_share": _series_close(
            pd.to_numeric(completed["served_share"], errors="coerce"),
            expected_served_share,
        ),
        "vkm_per_original_request": _series_close(
            pd.to_numeric(completed["vkm_per_original_request"], errors="coerce"),
            expected_vkm_original,
        ),
        "vkm_per_served_trip": _series_close(
            pd.to_numeric(completed["vkm_per_served_trip"], errors="coerce"),
            expected_vkm_served,
        ),
        "behavioral_acceptance_rate": _series_close(
            pd.to_numeric(completed["behavioral_acceptance_rate"], errors="coerce"),
            expected_behavioral_acceptance,
        ),
        "rejection_partition": _series_close(rejection_sum, pd.Series(1.0, index=completed.index)),
        "total_vehicle_km_alias": _series_close(total_vehicle_km, vehicle_km),
    }
    result["denominator_checks"] = {
        name: "passed" if bool(mask.all()) else "failed"
        for name, mask in checks.items()
    }
    for name, mask in checks.items():
        if not bool(mask.all()):
            failures = int((~mask).sum())
            result["errors"].append(
                f"denominator check failed for {name}: {failures} completed rows"
            )


def ensure_rerun_ledger(path: str | Path) -> Path:
    ledger_path = Path(path)
    ledger_path.parent.mkdir(parents=True, exist_ok=True)
    if not ledger_path.exists():
        with ledger_path.open("w", newline="", encoding="utf-8") as handle:
            writer = csv.DictWriter(handle, fieldnames=RERUN_LEDGER_COLUMNS)
            writer.writeheader()
    return ledger_path


def _existing_ledger_keys(ledger_path: Path) -> set[tuple[str, str, str]]:
    if not ledger_path.exists():
        return set()
    with ledger_path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        return {
            (row.get("run_id", ""), row.get("config_id", ""), row.get("status", ""))
            for row in reader
        }


def append_unresolved_failures_to_ledger(raw: pd.DataFrame, path: str | Path) -> Path:
    """Append failed/timeout main rows to the durable rerun ledger."""
    ledger_path = ensure_rerun_ledger(path)
    existing = _existing_ledger_keys(ledger_path)
    unresolved = raw[raw["status"].isin({"failed", "timeout"})]
    rows = []
    for _, row in unresolved.iterrows():
        key = (str(row["run_id"]), str(row["config_id"]), str(row["status"]))
        if key in existing:
            continue
        rows.append(
            {
                "run_id": row["run_id"],
                "config_id": row["config_id"],
                "seed": row["seed"],
                "scale": row["scale"],
                "method": row["method_label"],
                "status": row["status"],
                "error": row.get("error_message", ""),
                "reason": row.get("detailed_reason", ""),
                "fix": "",
                "rerun_result": "",
            }
        )

    if rows:
        with ledger_path.open("a", newline="", encoding="utf-8") as handle:
            writer = csv.DictWriter(handle, fieldnames=RERUN_LEDGER_COLUMNS)
            writer.writerows(rows)
    return ledger_path


def check_label_implementation_gate() -> dict:
    """Block paper-facing RH/ALNS labels when the implementation is sequential."""
    result = {"passed": True, "errors": [], "warnings": []}
    for variant in ALL_VARIANTS:
        metadata = variant.method_metadata
        if metadata.get("method_label") != "BidirectionalMP_Choice_RH_ALNS":
            continue
        source = inspect.getsource(variant.__class__._solve)
        claims_rh_alns = (
            metadata.get("reoptimization") == "rolling_horizon"
            or metadata.get("routing_solver") == "alns"
        )
        uses_sequential_actual_offer = "_run_actual_offer_sequence" in source
        uses_rolling_horizon = "RollingHorizon" in source
        if claims_rh_alns and uses_sequential_actual_offer and not uses_rolling_horizon:
            result["passed"] = False
            result["errors"].append(
                "BidirectionalMP_Choice_RH_ALNS metadata claims rolling-horizon/ALNS, "
                "but FullModel._solve currently delegates to the common sequential "
                "actual-offer path. Correct implementation or metadata before formal runs."
            )
    return result


def _validate_expected_matrix(
    raw: pd.DataFrame,
    expected_seeds: Iterable[int],
    expected_scales: Iterable[int],
    expected_method_labels: Iterable[str],
    result: dict,
) -> pd.DataFrame:
    expected_seed_set = set(expected_seeds)
    expected_scale_set = set(expected_scales)
    expected_label_set = set(expected_method_labels)
    main = raw[
        raw["method_label"].isin(expected_label_set)
        & (raw["evidence_family"] == "behavioral_main")
    ].copy()
    result["row_counts"]["main_behavioral_rows"] = int(len(main))

    observed_scales = set(pd.to_numeric(raw["scale"], errors="coerce").dropna().astype(int))
    forbidden_scales = sorted(observed_scales - expected_scale_set)
    if forbidden_scales:
        result["errors"].append(
            f"formal outputs contain non-predeclared scales: {forbidden_scales}"
        )

    observed_labels = set(raw["method_label"].dropna())
    forbidden_labels = sorted(observed_labels - expected_label_set)
    if forbidden_labels:
        result["errors"].append(
            f"formal outputs contain non-main method labels: {forbidden_labels}"
        )

    non_behavioral = raw[
        raw["method_label"].isin(expected_label_set)
        & (raw["evidence_family"] != "behavioral_main")
    ]
    if not non_behavioral.empty:
        result["errors"].append("main method labels include non-behavioral evidence rows")

    completed = main[main["status"] == "completed"]
    expected_tuples = {
        (seed, scale, method)
        for seed in expected_seed_set
        for scale in expected_scale_set
        for method in expected_label_set
    }
    completed_tuples = {
        (int(row["seed"]), int(row["scale"]), row["method_label"])
        for _, row in completed.iterrows()
    }
    missing = sorted(expected_tuples - completed_tuples)
    if missing:
        preview = ", ".join(f"seed={s}/scale={c}/method={m}" for s, c, m in missing[:5])
        result["errors"].append(
            f"missing completed main matrix cells: {len(missing)} missing"
            + (f" ({preview})" if preview else "")
        )

    duplicate_counts = completed.groupby(["seed", "scale", "method_label"]).size()
    duplicates = duplicate_counts[duplicate_counts > 1]
    if not duplicates.empty:
        result["errors"].append(
            f"duplicate completed main matrix cells: {len(duplicates)} duplicate keys"
        )

    return main


def _validate_statuses(main: pd.DataFrame, result: dict) -> None:
    failed_count = int((main["status"] == "failed").sum())
    timeout_count = int((main["status"] == "timeout").sum())
    result["row_counts"]["failed_rows"] = failed_count
    result["row_counts"]["timeout_rows"] = timeout_count
    if failed_count:
        result["errors"].append(f"formal main matrix contains {failed_count} failed rows")
    if timeout_count:
        result["errors"].append(f"formal main matrix contains {timeout_count} timeout rows")


def _validate_utility_joinability(main: pd.DataFrame, utility: pd.DataFrame, result: dict) -> None:
    _check_columns(utility, REQUIRED_UTILITY_KEYS, "utility_components.csv", result)
    if not REQUIRED_UTILITY_KEYS.issubset(utility.columns):
        return

    completed = main[main["status"] == "completed"]
    for _, row in completed.iterrows():
        matches = utility[
            (utility["run_id"] == row["run_id"])
            & (utility["seed"].astype(str) == str(row["seed"]))
            & (utility["scenario"] == row["scenario"])
            & (utility["method"] == row["variant"])
        ]
        if matches.empty:
            result["errors"].append(
                "missing utility rows for completed run "
                f"{row['run_id']} ({row['method_label']}, seed={row['seed']})"
            )


def validate_phase06_main_outputs(
    results_dir,
    expected_seeds,
    expected_scales,
    expected_method_labels,
    ledger_path,
    write_json: bool = True,
    require_label_gate: bool = True,
) -> dict:
    """Validate persisted Phase 6 formal main CSV artifacts."""
    root = Path(results_dir)
    result = _empty_result(root)
    result["ledger_path"] = str(ledger_path)

    raw = _read_csv(root / "synthetic_results.csv", result)
    metrics = _read_csv(root / "metrics_table.csv", result)
    utility = _read_csv(root / "utility_components.csv", result)
    for manifest_name in ["formal_seed_manifest.json", "formal_config_manifest.json"]:
        manifest_path = root / manifest_name
        if manifest_path.exists():
            result["checked_files"].append(str(manifest_path))
        else:
            result["errors"].append(f"missing required file: {manifest_path}")

    if raw is None or metrics is None or utility is None:
        result["passed"] = False
        _write_validation_json(root, result, write_json)
        return result

    result["row_counts"].update(
        synthetic_results=int(len(raw)),
        metrics_table=int(len(metrics)),
        utility_components=int(len(utility)),
    )

    _check_columns(raw, REQUIRED_RAW_FIELDS | QUARTET_METRIC_FIELDS, "synthetic_results.csv", result)
    _check_columns(metrics, {"variant"}, "metrics_table.csv", result)
    if not (REQUIRED_RAW_FIELDS | QUARTET_METRIC_FIELDS).issubset(raw.columns):
        result["passed"] = False
        _write_validation_json(root, result, write_json)
        return result

    _validate_numeric_ranges(raw, result)
    _validate_numeric_ranges(metrics, result)
    main = _validate_expected_matrix(
        raw,
        expected_seeds=expected_seeds,
        expected_scales=expected_scales,
        expected_method_labels=expected_method_labels,
        result=result,
    )
    _validate_statuses(main, result)
    _validate_denominators(main, result)
    _validate_utility_joinability(main, utility, result)

    ledger = append_unresolved_failures_to_ledger(main, ledger_path)
    result["ledger_path"] = str(ledger)

    if require_label_gate:
        gate = check_label_implementation_gate()
        result["label_implementation_gate"] = gate
        result["errors"].extend(gate["errors"])
        result["warnings"].extend(gate["warnings"])

    result["passed"] = not result["errors"]
    _write_validation_json(root, result, write_json)
    return result


def _write_validation_json(root: Path, result: dict, enabled: bool) -> None:
    if not enabled:
        return
    root.mkdir(parents=True, exist_ok=True)
    path = root / "main_matrix_validation.json"
    if str(path) not in result["checked_files"]:
        result["checked_files"].append(str(path))
    path.write_text(json.dumps(result, indent=2, sort_keys=True), encoding="utf-8")
