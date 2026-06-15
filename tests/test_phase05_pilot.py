from __future__ import annotations

import os
import sys
from pathlib import Path

import pandas as pd

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from experiments.phase05_pilot import (  # noqa: E402
    MAIN_BEHAVIORAL_METHOD_LABELS,
    PILOT_RESULTS_DIR,
    main_behavioral_variants,
    run_phase05_pilot,
)
from experiments.pilot_validation import validate_phase05_outputs  # noqa: E402


def _valid_rows(tmp_path: Path):
    rows = []
    utility_rows = []
    for seed in [42]:
        for variant, label in [
            ("DoorToDoor", "DoorToDoor_Choice_CommonRouting"),
            ("SingleSidedPickup", "SingleSidedPickup_Choice_CommonRouting"),
            ("SingleSidedDropoff", "SingleSidedDropoff_Choice_CommonRouting"),
            ("FullModel", "BidirectionalMP_Choice_RH_ALNS"),
        ]:
            run_id = f"synthetic_8:{label}:s{seed}"
            rows.append(
                {
                    "run_id": run_id,
                    "config_id": f"synthetic_8:scale_8:seed_{seed}",
                    "variant": variant,
                    "scale": 8,
                    "seed": seed,
                    "scenario": "synthetic_8",
                    "method_label": label,
                    "service_design": "test",
                    "choice_model": "binary_logit",
                    "reoptimization": "test",
                    "routing_solver": "test",
                    "evidence_family": "behavioral_main",
                    "diagnostic_role": "test",
                    "status": "completed",
                    "detailed_reason": "completed",
                    "runtime_s": 0.1,
                    "error_message": "",
                    "result_schema_version": "phase04.v1",
                    "timestamp_utc": "2026-06-15T00:00:00+00:00",
                    "artifact_dir": str(tmp_path),
                    "git_commit_or_code_hash": "abc123",
                    "n_requests": 8,
                    "n_offered": 4,
                    "n_served": 3,
                    "acceptance_rate": 0.375,
                    "vehicle_km": 1.0,
                    "served_share": 0.375,
                    "behavioral_acceptance_rate": 0.75,
                    "choice_rejection_rate": 0.25,
                    "feasibility_rejection_rate": 0.375,
                    "vkm_per_served_trip": 0.333,
                    "vkm_per_original_request": 0.125,
                    "avg_wait": 1.0,
                    "p95_wait": 1.0,
                    "avg_walk": 1.0,
                    "avg_ivt": 1.0,
                    "detour_ratio": 1.0,
                    "fairness_index": 0.0,
                    "cpu_time": 0.1,
                }
            )
            utility_rows.append(
                {
                    "run_id": run_id,
                    "seed": seed,
                    "scenario": "synthetic_8",
                    "method": variant,
                    "request_id": "req_0",
                    "status": "served",
                }
            )
    return pd.DataFrame(rows), pd.DataFrame(utility_rows)


def _write_valid_outputs(tmp_path: Path):
    raw, utility = _valid_rows(tmp_path)
    raw.to_csv(tmp_path / "synthetic_results.csv", index=False)
    raw.groupby("variant")[["served_share", "vehicle_km", "runtime_s"]].mean().to_csv(
        tmp_path / "metrics_table.csv"
    )
    utility.to_csv(tmp_path / "utility_components.csv", index=False)
    return raw, utility


def test_main_behavioral_variants_are_exact_phase05_matrix():
    variants = main_behavioral_variants()
    labels = {variant.method_metadata["method_label"] for variant in variants}

    assert len(variants) == 4
    assert labels == MAIN_BEHAVIORAL_METHOD_LABELS
    assert {
        variant.method_metadata["evidence_family"] for variant in variants
    } == {"behavioral_main"}


def test_phase05_results_dir_is_isolated():
    assert PILOT_RESULTS_DIR == "results/pilot/phase05"


def test_run_phase05_pilot_writes_to_supplied_directory(tmp_path):
    run_phase05_pilot(results_dir=tmp_path, scale=8, seeds=[42])

    assert (tmp_path / "synthetic_results.csv").exists()
    assert (tmp_path / "metrics_table.csv").exists()
    assert (tmp_path / "utility_components.csv").exists()


def test_validate_phase05_outputs_accepts_valid_temp_pilot_output(tmp_path):
    _write_valid_outputs(tmp_path)

    result = validate_phase05_outputs(
        tmp_path,
        expected_seeds=[42],
        expected_method_labels=MAIN_BEHAVIORAL_METHOD_LABELS,
        expected_scale=8,
    )

    assert result["passed"] is True


def test_validate_phase05_outputs_blocks_failed_and_timeout_rows(tmp_path):
    raw, utility = _write_valid_outputs(tmp_path)
    raw.loc[0, "status"] = "failed"
    raw.loc[1, "status"] = "timeout"
    raw.to_csv(tmp_path / "synthetic_results.csv", index=False)

    result = validate_phase05_outputs(
        tmp_path,
        expected_seeds=[42],
        expected_method_labels=MAIN_BEHAVIORAL_METHOD_LABELS,
        expected_scale=8,
    )

    assert result["passed"] is False
    assert any("failed" in error for error in result["errors"])
    assert any("timeout" in error for error in result["errors"])


def test_validate_phase05_outputs_blocks_metric_range_errors(tmp_path):
    raw, utility = _write_valid_outputs(tmp_path)
    raw.loc[0, "served_share"] = 1.2
    raw.loc[1, "vehicle_km"] = -1.0
    raw.to_csv(tmp_path / "synthetic_results.csv", index=False)

    result = validate_phase05_outputs(
        tmp_path,
        expected_seeds=[42],
        expected_method_labels=MAIN_BEHAVIORAL_METHOD_LABELS,
        expected_scale=8,
    )

    assert result["passed"] is False
    assert any("served_share" in error for error in result["errors"])
    assert any("vehicle_km" in error for error in result["errors"])


def test_validate_phase05_outputs_blocks_missing_provenance(tmp_path):
    raw, utility = _write_valid_outputs(tmp_path)
    raw = raw.drop(columns=["git_commit_or_code_hash"])
    raw.to_csv(tmp_path / "synthetic_results.csv", index=False)

    result = validate_phase05_outputs(
        tmp_path,
        expected_seeds=[42],
        expected_method_labels=MAIN_BEHAVIORAL_METHOD_LABELS,
        expected_scale=8,
    )

    assert result["passed"] is False
    assert any("git_commit_or_code_hash" in error for error in result["errors"])


def test_validate_phase05_outputs_checks_utility_joinability(tmp_path):
    raw, utility = _write_valid_outputs(tmp_path)
    utility = utility.iloc[1:]
    utility.to_csv(tmp_path / "utility_components.csv", index=False)

    result = validate_phase05_outputs(
        tmp_path,
        expected_seeds=[42],
        expected_method_labels=MAIN_BEHAVIORAL_METHOD_LABELS,
        expected_scale=8,
    )

    assert result["passed"] is False
    assert any("missing utility rows" in error for error in result["errors"])
