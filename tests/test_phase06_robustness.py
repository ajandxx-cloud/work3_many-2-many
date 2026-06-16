from __future__ import annotations

import json
import os
import sys
from pathlib import Path

import pandas as pd

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from experiments import phase06_robustness as robustness


def test_utility_sensitivity_grid_covers_required_dimensions():
    grid = robustness.utility_sensitivity_grid()
    ids = {setting["parameter_setting_id"] for setting in grid}

    assert "walk_disutility_high" in ids
    assert "wait_disutility_high" in ids
    assert "ivt_disutility_high" in ids
    assert "service_asc_low" in ids
    assert "outside_option_high" in ids
    assert "walk_sensitive_majority" in ids


def _raw_row(tmp_path: Path, setting: str, seed: int, scale: int, method: str) -> dict:
    return {
        "package_id": robustness.UTILITY_PACKAGE,
        "run_id": f"utility:{setting}:{scale}:{seed}:{method}",
        "config_id": f"utility:{setting}:scale_{scale}:seed_{seed}",
        "parameter_setting_id": setting,
        "seed": seed,
        "scale": scale,
        "scenario": f"synthetic_n{scale}_v10_s{seed}",
        "method_label": method,
        "variant": "FullModel" if "Bidirectional" in method else "DoorToDoor",
        "service_design": "test",
        "choice_model": "binary_logit",
        "reoptimization": "test",
        "routing_solver": "test",
        "evidence_family": "formal_robustness_diagnostic",
        "diagnostic_role": robustness.UTILITY_PACKAGE,
        "status": "completed",
        "detailed_reason": "completed",
        "runtime_s": 0.1,
        "error_message": "",
        "result_schema_version": "phase06.06-04.v1",
        "timestamp_utc": "2026-06-16T00:00:00+00:00",
        "artifact_dir": str(tmp_path),
        "git_commit_or_code_hash": "abc123",
        "n_requests": 10,
        "n_vehicles": 3,
        "vehicle_capacity": 8,
        "n_offered": 5,
        "n_served": 4,
        "served_share": 0.4,
        "behavioral_acceptance_rate": 0.7,
        "choice_rejection_rate": 0.3,
        "feasibility_rejection_rate": 0.3,
        "total_vehicle_km": 20.0,
        "vkm_per_served_trip": 5.0,
        "vkm_per_original_request": 2.0,
        "avg_wait": 1.0,
        "p95_wait": 1.0,
        "avg_walk": 1.0,
        "avg_ivt": 1.0,
        "detour_ratio": 1.0,
        "fairness_index": 0.0,
        "rho_p": "",
        "rho_d": "",
        "mp_density_profile": "",
        "meeting_point_count": 100,
        "stress_level": "",
        "demand_scale": scale,
        "fleet_size": 3,
        "parameter_values_json": "{}",
    }


def test_validate_package_accepts_complete_reduced_fixture(tmp_path):
    package_dir = tmp_path / robustness.UTILITY_PACKAGE
    package_dir.mkdir()
    seeds = [1]
    scales = [100]
    methods = list(robustness.DEFAULT_METHODS)
    grid = [{"parameter_setting_id": "baseline_default"}]
    rows = [
        _raw_row(package_dir, "baseline_default", seed, scale, method)
        for seed in seeds
        for scale in scales
        for method in methods
    ]
    pd.DataFrame(rows, columns=robustness.ROBUSTNESS_RAW_COLUMNS).to_csv(
        package_dir / "raw_results.csv", index=False
    )
    pd.DataFrame({"method_label": methods}).to_csv(package_dir / "processed_results.csv", index=False)
    (package_dir / "config_manifest.json").write_text(json.dumps({"package_id": robustness.UTILITY_PACKAGE}))

    report = robustness.validate_package(
        robustness.UTILITY_PACKAGE,
        tmp_path,
        seeds=seeds,
        scales=scales,
        methods=methods,
        grid=grid,
    )

    assert report["passed"] is True
    assert report["schema_drift"] is False
    assert set(report["denominator_checks"].values()) == {"passed"}


def test_validate_package_blocks_silent_missing_row(tmp_path):
    package_dir = tmp_path / robustness.UTILITY_PACKAGE
    package_dir.mkdir()
    methods = list(robustness.DEFAULT_METHODS)
    row = _raw_row(package_dir, "baseline_default", 1, 100, methods[0])
    pd.DataFrame([row], columns=robustness.ROBUSTNESS_RAW_COLUMNS).to_csv(
        package_dir / "raw_results.csv", index=False
    )
    pd.DataFrame({"method_label": [methods[0]]}).to_csv(package_dir / "processed_results.csv", index=False)
    (package_dir / "config_manifest.json").write_text(json.dumps({"package_id": robustness.UTILITY_PACKAGE}))

    report = robustness.validate_package(
        robustness.UTILITY_PACKAGE,
        tmp_path,
        seeds=[1],
        scales=[100],
        methods=methods,
        grid=[{"parameter_setting_id": "baseline_default"}],
    )

    assert report["passed"] is False
    assert any("missing robustness rows" in error for error in report["errors"])


def test_validate_equity_package_accepts_type_and_individual_outputs(tmp_path):
    package_dir = tmp_path / robustness.EQUITY_PACKAGE
    package_dir.mkdir()
    type_rows = []
    individual_rows = []
    for passenger_type in robustness.PASSENGER_TYPES:
        type_rows.append(
            {
                "package_id": robustness.EQUITY_PACKAGE,
                "config_id": "equity:scale_100:seed_1",
                "seed": 1,
                "scale": 100,
                "scenario": "synthetic_n100_v10_s1",
                "method_label": robustness.DEFAULT_METHODS[0],
                "passenger_type": passenger_type,
                "n_original": 10,
                "n_served": 4,
                "served_share": 0.4,
                "type_level_acceptance_rate": 0.4,
                "choice_rejection_rate": 0.3,
                "feasibility_rejection_rate": 0.3,
                "avg_wait": 1.0,
                "avg_walk": 1.0,
                "avg_ivt": 1.0,
                "mean_generalized_cost": 1.0,
                "equity_gini_acceptance": 0.0,
                "status": "completed",
            }
        )
        individual_rows.append(
            {
                "package_id": robustness.EQUITY_PACKAGE,
                "config_id": "equity:scale_100:seed_1",
                "seed": 1,
                "scale": 100,
                "scenario": "synthetic_n100_v10_s1",
                "method_label": robustness.DEFAULT_METHODS[0],
                "request_id": f"req_{passenger_type}",
                "passenger_type": passenger_type,
                "status": "served",
                "served": True,
                "walking_burden": 1.0,
                "waiting_access_time": 1.0,
                "in_vehicle_time": 1.0,
                "generalized_cost": 1.0,
            }
        )
    pd.DataFrame(type_rows, columns=robustness.EQUITY_TYPE_COLUMNS).to_csv(
        package_dir / "type_level_outcomes.csv", index=False
    )
    pd.DataFrame(individual_rows, columns=robustness.INDIVIDUAL_BURDEN_COLUMNS).to_csv(
        package_dir / "individual_burden_distribution.csv", index=False
    )
    (package_dir / "equity_summary.json").write_text(json.dumps({"ok": True}))
    (package_dir / "config_manifest.json").write_text(json.dumps({"ok": True}))

    report = robustness.validate_equity_package(
        tmp_path,
        seeds=[1],
        scales=[100],
        methods=[robustness.DEFAULT_METHODS[0]],
    )

    assert report["passed"] is True
    assert set(report["denominator_checks"].values()) == {"passed"}
