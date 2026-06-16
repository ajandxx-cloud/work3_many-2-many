from __future__ import annotations

import json
import os
import sys
from pathlib import Path

import pandas as pd

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from experiments.phase06_coverage_controls import (
    FIXED_PACKAGE,
    MATCHED_PACKAGE,
    FIXED_RAW_COLUMNS,
    MATCHED_RAW_COLUMNS,
    METHOD_LABEL_TO_VARIANT,
    _selection,
    fixed_set_for_cell,
    matched_targets_from_main,
    validate_fixed_accepted_set_outputs,
    validate_matched_coverage_outputs,
)


METHODS = sorted(METHOD_LABEL_TO_VARIANT)


def _main_fixture() -> pd.DataFrame:
    rows = []
    served_counts = {
        "BidirectionalMP_Choice_RH_ALNS": 2,
        "DoorToDoor_Choice_CommonRouting": 5,
        "SingleSidedDropoff_Choice_CommonRouting": 4,
        "SingleSidedPickup_Choice_CommonRouting": 3,
    }
    for method, count in served_counts.items():
        rows.append(
            {
                "seed": 1,
                "scale": 100,
                "method_label": method,
                "status": "completed",
                "n_served": count,
            }
        )
    return pd.DataFrame(rows)


def test_matched_targets_use_min_attainable_served_count():
    selection = _selection(seeds=[1], scales=[100])
    targets = matched_targets_from_main(_main_fixture(), selection)

    target = targets[(1, 100)]

    assert target["status"] == "ready"
    assert target["target_count"] == 2
    assert target["basis"] == "min_attainable_served_count_all_methods"
    assert target["limiting_methods"] == ["BidirectionalMP_Choice_RH_ALNS"]


def test_fixed_set_falls_back_to_candidate_serviceable_when_strict_sets_empty():
    rows = []
    scenario = "synthetic_n100_v10_s1"
    for method_label, variant in METHOD_LABEL_TO_VARIANT.items():
        rows.extend(
            [
                {
                    "seed": 1,
                    "scenario": scenario,
                    "method": variant,
                    "request_id": "req_common",
                    "status": "feasibility_rejected",
                    "detailed_reason": "no_feasible_route",
                },
                {
                    "seed": 1,
                    "scenario": scenario,
                    "method": variant,
                    "request_id": f"req_only_{variant}",
                    "status": "served",
                    "detailed_reason": "accepted",
                },
            ]
        )
    utility = pd.DataFrame(rows)

    fixed = fixed_set_for_cell(utility, 1, 100, METHODS)

    assert fixed["construction_rule"] == "common_candidate_serviceable"
    assert fixed["fallback_used"] is True
    assert fixed["retained_request_ids"] == ["req_common"]


def _write_manifests(root: Path, package_id: str) -> None:
    (root / "config_manifest.json").write_text(
        json.dumps({"package_id": package_id}),
        encoding="utf-8",
    )
    (root / "seed_manifest.json").write_text(
        json.dumps({"selected_seeds": [1]}),
        encoding="utf-8",
    )


def test_validate_matched_coverage_outputs_accepts_complete_fixture(tmp_path):
    selection = _selection(seeds=[1], scales=[100])
    rows = []
    for method in METHODS:
        rows.append(
            {
                "package_id": MATCHED_PACKAGE,
                "run_id": f"matched:{method}",
                "config_id": "matched:scale_100:seed_1",
                "seed": 1,
                "scale": 100,
                "scenario": "synthetic_n100_v10_s1",
                "method_label": method,
                "variant": METHOD_LABEL_TO_VARIANT[method],
                "service_design": "test",
                "choice_model": "binary_logit_with_matched_coverage_cap",
                "reoptimization": "test",
                "routing_solver": "test",
                "evidence_family": "supplementary_control",
                "diagnostic_role": "matched_coverage_control",
                "status": "completed",
                "detailed_reason": "ok",
                "runtime_s": 0.1,
                "error_message": "",
                "result_schema_version": "phase06.06-03.v1",
                "timestamp_utc": "2026-06-16T00:00:00+00:00",
                "artifact_dir": str(tmp_path),
                "git_commit_or_code_hash": "abc123",
                "original_request_count": 100,
                "attainable_served_count": 5,
                "matched_target_served_count": 2,
                "target_basis": "min_attainable_served_count_all_methods",
                "target_adjusted": True,
                "actual_served_count": 2,
                "served_share": 0.02,
                "coverage_gap_count": 0,
                "coverage_gap_abs": 0,
                "coverage_tolerance_count": 0,
                "total_vehicle_km": 10.0,
                "vkm_per_served_trip": 5.0,
                "vkm_per_original_request": 0.1,
                "avg_wait": 0.0,
                "p95_wait": 0.0,
                "avg_walk": 0.0,
                "avg_ivt": 0.0,
                "detour_ratio": 0.0,
                "fairness_index": 0.0,
            }
        )
    pd.DataFrame(rows, columns=MATCHED_RAW_COLUMNS).to_csv(tmp_path / "raw_results.csv", index=False)
    pd.DataFrame({"method_label": METHODS}).to_csv(tmp_path / "processed_results.csv", index=False)
    _write_manifests(tmp_path, MATCHED_PACKAGE)

    report = validate_matched_coverage_outputs(tmp_path, selection)

    assert report["passed"] is True
    assert report["schema_drift"] is False
    assert set(report["denominator_checks"].values()) == {"passed"}


def test_validate_fixed_accepted_set_outputs_blocks_missing_rows(tmp_path):
    selection = _selection(seeds=[1], scales=[100])
    rows = []
    for method in METHODS[:-1]:
        rows.append(
            {
                "package_id": FIXED_PACKAGE,
                "run_id": f"fixed:{method}",
                "config_id": "fixed:scale_100:seed_1",
                "seed": 1,
                "scale": 100,
                "scenario": "synthetic_n100_v10_s1",
                "method_label": method,
                "variant": METHOD_LABEL_TO_VARIANT[method],
                "service_design": "test",
                "choice_model": "fixed_accepted_set",
                "reoptimization": "test",
                "routing_solver": "test",
                "evidence_family": "algorithm_diagnostic",
                "evidence_role": "diagnostic_only",
                "diagnostic_role": "fixed_accepted_set_routing",
                "status": "completed",
                "detailed_reason": "ok",
                "runtime_s": 0.1,
                "error_message": "",
                "result_schema_version": "phase06.06-03.v1",
                "timestamp_utc": "2026-06-16T00:00:00+00:00",
                "artifact_dir": str(tmp_path),
                "git_commit_or_code_hash": "abc123",
                "construction_rule": "common_served",
                "fallback_used": False,
                "retained_set_hash": "abc123",
                "served_intersection_count": 2,
                "serviceable_intersection_count": 2,
                "candidate_serviceable_intersection_count": 2,
                "retained_request_count": 2,
                "retained_share": 0.02,
                "deterministic_inserted_share": 1.0,
                "served_count": 2,
                "unserved_accepted_count": 0,
                "original_request_count": 100,
                "total_vehicle_km": 10.0,
                "vkm_per_inserted_request": 5.0,
                "vkm_per_served_request": 5.0,
                "vkm_per_original_request": 0.1,
                "avg_wait": 0.0,
                "p95_wait": 0.0,
                "avg_walk": 0.0,
                "avg_ivt": 0.0,
                "detour_ratio": 0.0,
                "fairness_index": 0.0,
            }
        )
    pd.DataFrame(rows, columns=FIXED_RAW_COLUMNS).to_csv(tmp_path / "raw_results.csv", index=False)
    pd.DataFrame({"method_label": METHODS[:-1]}).to_csv(tmp_path / "processed_results.csv", index=False)
    _write_manifests(tmp_path, FIXED_PACKAGE)

    report = validate_fixed_accepted_set_outputs(tmp_path, selection)

    assert report["passed"] is False
    assert any("missing control rows" in error for error in report["errors"])
