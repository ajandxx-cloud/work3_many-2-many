"""Persisted artifact checks for Phase 5 pilot outputs."""

from __future__ import annotations

import math
from pathlib import Path
from typing import Iterable

import pandas as pd

REQUIRED_RAW_FIELDS = {
    "status",
    "error_message",
    "runtime_s",
    "config_id",
    "seed",
    "scenario",
    "method_label",
    "artifact_dir",
    "git_commit_or_code_hash",
}

RATIO_FIELDS = {
    "acceptance_rate",
    "served_share",
    "behavioral_acceptance_rate",
    "choice_rejection_rate",
    "feasibility_rejection_rate",
    "fairness_index",
}

NON_NEGATIVE_FIELDS = {
    "vehicle_km",
    "vkm_per_served_trip",
    "vkm_per_original_request",
    "avg_wait",
    "p95_wait",
    "avg_walk",
    "avg_ivt",
    "detour_ratio",
    "cpu_time",
    "runtime_s",
}

REQUIRED_UTILITY_KEYS = {"run_id", "seed", "scenario", "method", "request_id"}


def _empty_result(results_dir: Path) -> dict:
    return {
        "passed": True,
        "errors": [],
        "warnings": [],
        "row_counts": {},
        "checked_files": [],
        "results_dir": str(results_dir),
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


def _validate_expected_matrix(
    raw: pd.DataFrame,
    expected_seeds: Iterable[int],
    expected_method_labels: Iterable[str],
    expected_scale: int,
    result: dict,
) -> pd.DataFrame:
    expected_seed_set = set(expected_seeds)
    expected_label_set = set(expected_method_labels)
    main = raw[
        raw["method_label"].isin(expected_label_set)
        & (raw["evidence_family"] == "behavioral_main")
    ].copy()
    result["row_counts"]["main_behavioral_rows"] = int(len(main))

    observed_seeds = set(pd.to_numeric(main["seed"], errors="coerce").dropna().astype(int))
    observed_labels = set(main["method_label"].dropna())
    if observed_seeds != expected_seed_set:
        result["errors"].append(
            f"main behavioral seeds mismatch: expected {sorted(expected_seed_set)}, got {sorted(observed_seeds)}"
        )
    if observed_labels != expected_label_set:
        result["errors"].append(
            f"main behavioral method labels mismatch: expected {sorted(expected_label_set)}, got {sorted(observed_labels)}"
        )
    if "scale" in main.columns:
        observed_scales = set(pd.to_numeric(main["scale"], errors="coerce").dropna().astype(int))
        if observed_scales != {expected_scale}:
            result["errors"].append(
                f"main behavioral scale mismatch: expected {expected_scale}, got {sorted(observed_scales)}"
            )
    expected_rows = len(expected_seed_set) * len(expected_label_set)
    if len(main) != expected_rows:
        result["errors"].append(f"expected {expected_rows} main behavioral rows, got {len(main)}")
    return main


def _validate_statuses(main: pd.DataFrame, result: dict) -> None:
    failed_count = int((main["status"] == "failed").sum())
    timeout_count = int((main["status"] == "timeout").sum())
    result["row_counts"]["failed_rows"] = failed_count
    result["row_counts"]["timeout_rows"] = timeout_count
    if failed_count:
        result["errors"].append(f"main behavioral pilot contains {failed_count} failed rows")
    if timeout_count:
        result["errors"].append(f"main behavioral pilot contains {timeout_count} timeout rows")


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


def validate_phase05_outputs(
    results_dir,
    expected_seeds,
    expected_method_labels,
    expected_scale,
) -> dict:
    """Validate persisted Phase 5 pilot CSV artifacts."""
    root = Path(results_dir)
    result = _empty_result(root)
    raw = _read_csv(root / "synthetic_results.csv", result)
    metrics = _read_csv(root / "metrics_table.csv", result)
    utility = _read_csv(root / "utility_components.csv", result)
    for optional_name in [
        "matched_coverage_pilot.csv",
        "fixed_accepted_set_smoke.json",
    ]:
        optional_path = root / optional_name
        if optional_path.exists():
            result["checked_files"].append(str(optional_path))

    if raw is None or metrics is None or utility is None:
        result["passed"] = False
        return result

    result["row_counts"].update(
        synthetic_results=int(len(raw)),
        metrics_table=int(len(metrics)),
        utility_components=int(len(utility)),
    )

    _check_columns(raw, REQUIRED_RAW_FIELDS, "synthetic_results.csv", result)
    if not REQUIRED_RAW_FIELDS.issubset(raw.columns):
        result["passed"] = False
        return result

    _validate_numeric_ranges(raw, result)
    _validate_numeric_ranges(metrics, result)
    main = _validate_expected_matrix(
        raw,
        expected_seeds=expected_seeds,
        expected_method_labels=expected_method_labels,
        expected_scale=expected_scale,
        result=result,
    )
    _validate_statuses(main, result)
    _validate_utility_joinability(main, utility, result)

    result["passed"] = not result["errors"]
    return result
