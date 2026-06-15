from __future__ import annotations

import os
import sys
from pathlib import Path

import pandas as pd
import pytest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from experiments.phase05_pilot import (  # noqa: E402
    MAIN_BEHAVIORAL_METHOD_LABELS,
    PILOT_RESULTS_DIR,
    main_behavioral_variants,
    run_phase05_pilot,
)
from experiments.pilot_validation import validate_phase05_outputs  # noqa: E402
from experiments.phase05_coverage_smoke import (  # noqa: E402
    run_fixed_accepted_set_smoke,
    run_matched_coverage_pilot,
)


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


def test_matched_coverage_output_columns(tmp_path):
    result = run_matched_coverage_pilot(tmp_path, scale=8, seeds=[42], tolerance=0.20)

    path = tmp_path / "matched_coverage_pilot.csv"
    assert path.exists()
    df = pd.read_csv(path)
    for column in [
        "original_fullmodel_served_share",
        "target_count",
        "target_basis",
        "target_adjusted",
        "target_served_share",
        "achieved_served_share",
        "abs_gap",
        "tolerance",
        "status",
        "detailed_reason",
    ]:
        assert column in df.columns
    assert set(df["evidence_family"]) == {"supplementary_control"}
    assert isinstance(result["passed"], bool)


def test_matched_coverage_default_scale20_closes_prior_seed_failures(tmp_path):
    result = run_matched_coverage_pilot(
        tmp_path,
        scale=20,
        seeds=[42, 43, 44],
        tolerance=0.03,
    )

    df = pd.read_csv(tmp_path / "matched_coverage_pilot.csv")
    capped = df[df["method_label"].eq("DoorToDoor_Capped_MatchedCoverage")]

    assert result["passed"] is True
    assert set(capped["seed"].astype(int)) == {42, 43, 44}
    assert set(capped["status"]) == {"passed"}
    assert (capped["abs_gap"].astype(float) <= capped["tolerance"].astype(float)).all()
    assert set(capped["target_basis"]).issubset(
        {
            "fullmodel_served_count",
            "uncapped_doortodoor_serviceable_count",
        }
    )


def test_matched_coverage_tolerance_failure_blocks(tmp_path, monkeypatch):
    import experiments.phase05_coverage_smoke as smoke

    def fake_served_stats(variant, scale, seed):
        if variant.__class__.__name__ == "FullModel":
            return 4, 0.50, 0.01
        if getattr(variant, "_cap_share", None) == 1.0:
            return 4, 0.50, 0.01
        return 1, 0.125, 0.01

    monkeypatch.setattr(smoke, "_served_stats_for_variant", fake_served_stats)

    result = run_matched_coverage_pilot(tmp_path, scale=8, seeds=[42], tolerance=0.03)

    assert result["passed"] is False
    df = pd.read_csv(tmp_path / "matched_coverage_pilot.csv")
    capped = df[df["method_label"].eq("DoorToDoor_Capped_MatchedCoverage")]
    assert "failed" in set(capped["status"])
    assert capped.iloc[0]["target_count"] == 4
    assert "target_count=4" in capped.iloc[0]["detailed_reason"]
    assert "achieved_count=1" in capped.iloc[0]["detailed_reason"]


def test_fixed_accepted_set_smoke_durability(tmp_path):
    _write_valid_outputs(tmp_path)

    result = run_fixed_accepted_set_smoke(tmp_path, scale=8, seed=42)

    path = tmp_path / "fixed_accepted_set_smoke.json"
    assert path.exists()
    assert "served_intersection_count" in result
    assert "serviceable_intersection_count" in result
    assert "construction_rule" in result
    assert "retained_request_count" in result
    assert "retained_share" in result
    assert result["evidence_family"] != "behavioral_main"
    assert result["diagnostic_role"] == "fixed_accepted_set_smoke"
    assert result["construction_rule"] == "common_served"


def test_fixed_accepted_set_smoke_uses_serviceable_fallback(tmp_path, monkeypatch):
    raw, utility = _write_valid_outputs(tmp_path)
    utility["status"] = "choice_rejected"
    utility.to_csv(tmp_path / "utility_components.csv", index=False)

    import experiments.phase05_coverage_smoke as smoke

    routed = {}

    def fake_greedy(scale, seed, retained_ids):
        routed["retained_ids"] = set(retained_ids)
        return {
            "routing_diagnostic": "GreedyInsertionBaseline",
            "routing_status": "completed",
            "routing_runtime_s": 0.01,
            "routing_vehicle_km": 1.0,
            "routing_served_share": 1.0,
        }

    monkeypatch.setattr(smoke, "_run_greedy_fixed_set", fake_greedy)

    result = run_fixed_accepted_set_smoke(tmp_path, scale=8, seed=42)

    assert result["status"] == "passed"
    assert result["construction_rule"] == "common_serviceable"
    assert result["served_intersection_count"] == 0
    assert result["serviceable_intersection_count"] > 0
    assert result["retained_request_count"] > 0
    assert result["routing_status"] == "completed"
    assert routed["retained_ids"] == {"req_0"}
    assert result["passed"] is True


def test_fixed_accepted_set_default_seed42_routes_retained_set(tmp_path):
    result = run_fixed_accepted_set_smoke(tmp_path, scale=20, seed=42)

    assert result["status"] == "passed"
    assert result["routing_status"] == "completed"
    assert result["retained_request_count"] > 0
    assert result["construction_rule"] in {
        "common_served",
        "common_serviceable",
        "common_candidate_serviceable",
    }
    if result["construction_rule"] == "common_candidate_serviceable":
        assert result["candidate_serviceable_intersection_count"] > 0
    assert result["evidence_family"] == "algorithm_diagnostic"


def test_fixed_accepted_set_no_gurobi_is_non_blocking(tmp_path, monkeypatch):
    _write_valid_outputs(tmp_path)

    import experiments.milp_gap as milp_gap

    def fake_gap(scale, seed):
        return {
            "status": "no_gurobi",
            "detailed_reason": "Gurobi unavailable in test",
            "gap_pct": None,
            "comparable_gap": False,
        }

    monkeypatch.setattr(milp_gap, "run_gap_experiment", fake_gap)

    result = run_fixed_accepted_set_smoke(tmp_path, scale=8, seed=42, include_milp=True)

    assert result["milp_status"] == "no_gurobi"
    assert result["milp_non_blocking"] is True
