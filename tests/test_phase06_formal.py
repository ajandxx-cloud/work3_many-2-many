from __future__ import annotations

import csv
import json
import os
import sys
from pathlib import Path

import pandas as pd

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import experiments.phase06_formal as phase06  # noqa: E402
import experiments.runner as runner_module  # noqa: E402
from experiments.formal_validation import (  # noqa: E402
    RERUN_LEDGER_COLUMNS,
    check_label_implementation_gate,
    ensure_rerun_ledger,
    validate_phase06_main_outputs,
)


VARIANT_BY_LABEL = {
    "DoorToDoor_Choice_CommonRouting": "DoorToDoor",
    "SingleSidedPickup_Choice_CommonRouting": "SingleSidedPickup",
    "SingleSidedDropoff_Choice_CommonRouting": "SingleSidedDropoff",
    "BidirectionalMP_Choice_RH_ALNS": "FullModel",
}


def _raw_row(tmp_path: Path, seed: int, scale: int, label: str, status: str = "completed"):
    variant = VARIANT_BY_LABEL[label]
    run_id = f"synthetic_{scale}:{label}:s{seed}"
    return {
        "run_id": run_id,
        "config_id": f"synthetic_{scale}:scale_{scale}:seed_{seed}",
        "variant": variant,
        "scale": scale,
        "seed": seed,
        "scenario": f"synthetic_{scale}",
        "method_label": label,
        "service_design": "test",
        "choice_model": "binary_logit",
        "reoptimization": "test",
        "routing_solver": "test",
        "evidence_family": "behavioral_main",
        "diagnostic_role": "test",
        "legacy_class": variant,
        "status": status,
        "detailed_reason": "completed" if status == "completed" else status,
        "runtime_s": 0.1,
        "error_message": "" if status == "completed" else f"{status} fixture",
        "result_schema_version": "phase04.v1",
        "timestamp_utc": "2026-06-15T00:00:00+00:00",
        "artifact_dir": str(tmp_path),
        "git_commit_or_code_hash": "abc123",
        "n_requests": 8,
        "n_offered": 4,
        "n_served": 3,
        "acceptance_rate": 0.375,
        "vehicle_km": 1.0,
        "total_vehicle_km": 1.0,
        "served_share": 0.375,
        "behavioral_acceptance_rate": 0.75,
        "choice_rejection_rate": 0.25,
        "feasibility_rejection_rate": 0.375,
        "vkm_per_served_trip": 1.0 / 3.0,
        "vkm_per_original_request": 0.125,
        "avg_wait": 1.0,
        "p95_wait": 1.0,
        "avg_walk": 1.0,
        "avg_ivt": 1.0,
        "detour_ratio": 1.0,
        "fairness_index": 0.0,
        "cpu_time": 0.1,
    }


def _write_valid_outputs(tmp_path: Path, seeds=(1,), scales=(100,)):
    rows = []
    utility_rows = []
    for seed in seeds:
        for scale in scales:
            for label in sorted(phase06.FORMAL_MAIN_METHOD_LABELS):
                row = _raw_row(tmp_path, seed, scale, label)
                rows.append(row)
                utility_rows.append(
                    {
                        "run_id": row["run_id"],
                        "seed": seed,
                        "scenario": row["scenario"],
                        "method": row["variant"],
                        "request_id": "req_0",
                        "status": "served",
                    }
                )
    raw = pd.DataFrame(rows)
    raw.to_csv(tmp_path / "synthetic_results.csv", index=False)
    raw.groupby("variant")[["served_share", "vehicle_km", "runtime_s"]].mean().to_csv(
        tmp_path / "metrics_table.csv"
    )
    pd.DataFrame(utility_rows).to_csv(tmp_path / "utility_components.csv", index=False)
    phase06.write_formal_manifests(results_dir=tmp_path, scales=scales, seeds=seeds)
    return raw


def test_phase06_formal_constants_are_predeclared():
    assert phase06.REQUIRED_FORMAL_SEEDS == list(range(1, 21))
    assert phase06.OPTIONAL_EXTENSION_SEEDS == list(range(21, 31))
    assert phase06.FORMAL_SCALES == [100, 200, 300, 500]
    assert phase06.FORMAL_MAIN_METHOD_LABELS == set(VARIANT_BY_LABEL)


def test_manifest_writer_records_required_optional_and_selected_seeds(tmp_path):
    seed_path, config_path = phase06.write_formal_manifests(
        results_dir=tmp_path,
        scales=[100],
        seeds=[1],
    )

    seed_manifest = pd.read_json(seed_path, typ="series")
    config_manifest = pd.read_json(config_path, typ="series")

    assert seed_manifest["required_seeds"] == list(range(1, 21))
    assert seed_manifest["optional_extension_seeds"] == list(range(21, 31))
    assert seed_manifest["selected_seeds"] == [1]
    assert config_manifest["formal_scales"] == [100]
    assert "results/synthetic_results.csv" in config_manifest["legacy_result_paths_forbidden"]
    assert str(tmp_path) not in {"results/synthetic_results.csv", "results/pilot/phase05"}


def test_formal_main_variants_are_exact_behavioral_main_set():
    variants = phase06.formal_main_variants()
    labels = {variant.method_metadata["method_label"] for variant in variants}
    families = {variant.method_metadata["evidence_family"] for variant in variants}

    assert len(variants) == 4
    assert labels == phase06.FORMAL_MAIN_METHOD_LABELS
    assert families == {"behavioral_main"}
    assert not any(
        variant.method_metadata["evidence_family"]
        in {"supplementary_control", "deterministic_diagnostic", "algorithm_diagnostic"}
        for variant in variants
    )


def test_run_phase06_main_scopes_runner_and_writes_to_supplied_directory(tmp_path, monkeypatch):
    captured = {}

    def fake_run_all_experiments(scales, seeds, beijing, results_dir):
        captured["variant_labels"] = [
            variant.method_metadata["method_label"] for variant in runner_module.ALL_VARIANTS
        ]
        captured["scales"] = list(scales)
        captured["seeds"] = list(seeds)
        captured["beijing"] = beijing
        _write_valid_outputs(Path(results_dir), seeds=seeds, scales=scales)
        return [], []

    monkeypatch.setattr(runner_module, "run_all_experiments", fake_run_all_experiments)

    phase06.run_phase06_main(results_dir=tmp_path, scales=[100], seeds=[1])

    assert sorted(captured["variant_labels"]) == sorted(phase06.FORMAL_MAIN_METHOD_LABELS)
    assert captured["scales"] == [100]
    assert captured["seeds"] == [1]
    assert captured["beijing"] is False
    assert (tmp_path / "synthetic_results.csv").exists()
    assert (tmp_path / "metrics_table.csv").exists()
    assert (tmp_path / "utility_components.csv").exists()
    assert (tmp_path / "raw_results.csv").exists()
    assert (tmp_path / "processed_results.csv").exists()
    assert (tmp_path / "utility_logs.csv").exists()
    assert (tmp_path / "run_manifest.json").exists()
    manifest = json.loads((tmp_path / "run_manifest.json").read_text(encoding="utf-8"))
    assert manifest["expected_row_count"] == 4
    assert manifest["actual_raw_row_count"] == 4
    assert manifest["formal_seed_count"] == 1
    assert manifest["optional_extension_status"] == "not_attempted"
    assert manifest["status_counts"] == {"completed": 4}
    assert len(pd.read_csv(tmp_path / "synthetic_results.csv")) == 4


def test_validate_phase06_main_outputs_accepts_complete_matrix_without_label_gate(tmp_path):
    _write_valid_outputs(tmp_path, seeds=[1], scales=[100])

    result = validate_phase06_main_outputs(
        tmp_path,
        expected_seeds=[1],
        expected_scales=[100],
        expected_method_labels=phase06.FORMAL_MAIN_METHOD_LABELS,
        ledger_path=tmp_path / "ledger.csv",
        require_label_gate=False,
    )

    assert result["passed"] is True
    assert result["schema_drift"] is False
    assert set(result["denominator_checks"].values()) == {"passed"}
    assert (tmp_path / "main_matrix_validation.json").exists()
    assert result["ledger_path"].endswith("ledger.csv")


def test_validate_phase06_main_outputs_blocks_denominator_drift(tmp_path):
    raw = _write_valid_outputs(tmp_path, seeds=[1], scales=[100])
    raw.loc[0, "served_share"] = 0.99
    raw.to_csv(tmp_path / "synthetic_results.csv", index=False)

    result = validate_phase06_main_outputs(
        tmp_path,
        expected_seeds=[1],
        expected_scales=[100],
        expected_method_labels=phase06.FORMAL_MAIN_METHOD_LABELS,
        ledger_path=tmp_path / "ledger.csv",
        require_label_gate=False,
    )

    assert result["passed"] is False
    assert result["denominator_checks"]["served_share"] == "failed"
    assert any("denominator check failed for served_share" in error for error in result["errors"])


def test_validate_phase06_main_outputs_blocks_missing_cells(tmp_path):
    raw = _write_valid_outputs(tmp_path, seeds=[1], scales=[100])
    raw.iloc[:-1].to_csv(tmp_path / "synthetic_results.csv", index=False)

    result = validate_phase06_main_outputs(
        tmp_path,
        expected_seeds=[1],
        expected_scales=[100],
        expected_method_labels=phase06.FORMAL_MAIN_METHOD_LABELS,
        ledger_path=tmp_path / "ledger.csv",
        require_label_gate=False,
    )

    assert result["passed"] is False
    assert any("missing completed main matrix cells" in error for error in result["errors"])


def test_validate_phase06_main_outputs_blocks_failed_and_timeout_rows(tmp_path):
    raw = _write_valid_outputs(tmp_path, seeds=[1], scales=[100])
    raw.loc[0, "status"] = "failed"
    raw.loc[1, "status"] = "timeout"
    raw.to_csv(tmp_path / "synthetic_results.csv", index=False)

    result = validate_phase06_main_outputs(
        tmp_path,
        expected_seeds=[1],
        expected_scales=[100],
        expected_method_labels=phase06.FORMAL_MAIN_METHOD_LABELS,
        ledger_path=tmp_path / "ledger.csv",
        require_label_gate=False,
    )

    assert result["passed"] is False
    assert any("failed rows" in error for error in result["errors"])
    assert any("timeout rows" in error for error in result["errors"])
    ledger = pd.read_csv(tmp_path / "ledger.csv")
    assert set(ledger["status"]) == {"failed", "timeout"}
    assert "replacement_seed" not in ledger.columns


def test_validate_phase06_main_outputs_blocks_missing_utility_rows(tmp_path):
    _write_valid_outputs(tmp_path, seeds=[1], scales=[100])
    utility = pd.read_csv(tmp_path / "utility_components.csv")
    utility.iloc[1:].to_csv(tmp_path / "utility_components.csv", index=False)

    result = validate_phase06_main_outputs(
        tmp_path,
        expected_seeds=[1],
        expected_scales=[100],
        expected_method_labels=phase06.FORMAL_MAIN_METHOD_LABELS,
        ledger_path=tmp_path / "ledger.csv",
        require_label_gate=False,
    )

    assert result["passed"] is False
    assert any("missing utility rows" in error for error in result["errors"])


def test_validate_phase06_main_outputs_blocks_forbidden_scale_20(tmp_path):
    _write_valid_outputs(tmp_path, seeds=[1], scales=[100])
    raw = pd.read_csv(tmp_path / "synthetic_results.csv")
    raw.loc[0, "scale"] = 20
    raw.to_csv(tmp_path / "synthetic_results.csv", index=False)

    result = validate_phase06_main_outputs(
        tmp_path,
        expected_seeds=[1],
        expected_scales=[100],
        expected_method_labels=phase06.FORMAL_MAIN_METHOD_LABELS,
        ledger_path=tmp_path / "ledger.csv",
        require_label_gate=False,
    )

    assert result["passed"] is False
    assert any("non-predeclared scales" in error for error in result["errors"])


def test_label_implementation_gate_reports_current_bidirectional_status():
    gate = check_label_implementation_gate()

    assert gate["passed"] is True
    assert gate["errors"] == []


def test_rerun_ledger_header_is_exact(tmp_path):
    ledger_path = ensure_rerun_ledger(tmp_path / "ledger.csv")

    with ledger_path.open(newline="", encoding="utf-8") as handle:
        reader = csv.reader(handle)
        header = next(reader)

    assert header == RERUN_LEDGER_COLUMNS
    assert "replacement_seed" not in header
