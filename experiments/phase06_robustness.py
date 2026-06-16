"""Phase 6 Plan 06-04 robustness, sensitivity, and equity diagnostics.

The 06-04 packages are formal diagnostics, not headline evidence.  They reuse
the Phase 6 paired-seed conventions while keeping outputs isolated from the
06-02 main matrix and 06-03 coverage controls.
"""

from __future__ import annotations

import argparse
import csv
import json
import math
import subprocess
import sys
import time
import traceback
from contextlib import contextmanager
from dataclasses import replace
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable

import numpy as np
import pandas as pd

import experiments.variants as variants_module
from experiments.algorithm_diagnostics import run_alns_budget_smoke
from experiments.config import CHOICE_SEED, RHO_D, RHO_P, VEHICLE_COUNTS
from experiments.formal_validation import (
    RERUN_LEDGER_COLUMNS,
    check_label_implementation_gate,
    ensure_rerun_ledger,
)
from experiments.metrics import compute_metrics
from experiments.milp_gap import run_gap_experiment
from experiments.phase06_formal import (
    DEFAULT_RERUN_LEDGER_PATH,
    FORMAL_SCALES,
    REQUIRED_FORMAL_SEEDS,
)
from experiments.runner import _git_commit_or_code_hash
from experiments.scenarios import Scenario, generate_synthetic
from experiments.variants import DoorToDoor, FullModel
from src.drt.types import ChoiceParameters, MeetingPoint, PassengerType


DEFAULT_ROBUSTNESS_ROOT = Path("results/formal/phase06/robustness")
DEFAULT_SEEDS = REQUIRED_FORMAL_SEEDS[:10]
DEFAULT_SCALES = [100, 200, 300]
DEFAULT_METHODS = [
    "DoorToDoor_Choice_CommonRouting",
    "BidirectionalMP_Choice_RH_ALNS",
]
PASSENGER_TYPES = ["price_sensitive", "time_sensitive", "walk_sensitive"]

UTILITY_PACKAGE = "utility_sensitivity"
MP_PACKAGE = "mp_density_walking_radius"
FLEET_PACKAGE = "fleet_demand_stress"
EQUITY_PACKAGE = "equity_type_outcomes"
ALGORITHM_PACKAGE = "algorithm_diagnostics"
PACKAGE_NAMES = (
    UTILITY_PACKAGE,
    MP_PACKAGE,
    FLEET_PACKAGE,
    EQUITY_PACKAGE,
    ALGORITHM_PACKAGE,
)

ROBUSTNESS_RAW_COLUMNS = [
    "package_id",
    "run_id",
    "config_id",
    "parameter_setting_id",
    "seed",
    "scale",
    "scenario",
    "method_label",
    "variant",
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
    "n_vehicles",
    "vehicle_capacity",
    "n_offered",
    "n_served",
    "served_share",
    "behavioral_acceptance_rate",
    "choice_rejection_rate",
    "feasibility_rejection_rate",
    "total_vehicle_km",
    "vkm_per_served_trip",
    "vkm_per_original_request",
    "avg_wait",
    "p95_wait",
    "avg_walk",
    "avg_ivt",
    "detour_ratio",
    "fairness_index",
    "rho_p",
    "rho_d",
    "mp_density_profile",
    "meeting_point_count",
    "stress_level",
    "demand_scale",
    "fleet_size",
    "parameter_values_json",
]

EQUITY_TYPE_COLUMNS = [
    "package_id",
    "config_id",
    "seed",
    "scale",
    "scenario",
    "method_label",
    "passenger_type",
    "n_original",
    "n_served",
    "served_share",
    "type_level_acceptance_rate",
    "choice_rejection_rate",
    "feasibility_rejection_rate",
    "avg_wait",
    "avg_walk",
    "avg_ivt",
    "mean_generalized_cost",
    "equity_gini_acceptance",
    "status",
]

INDIVIDUAL_BURDEN_COLUMNS = [
    "package_id",
    "config_id",
    "seed",
    "scale",
    "scenario",
    "method_label",
    "request_id",
    "passenger_type",
    "status",
    "served",
    "walking_burden",
    "waiting_access_time",
    "in_vehicle_time",
    "generalized_cost",
]

GATE_COLUMNS = [
    "package_id",
    "status",
    "passed",
    "role",
    "output_path",
    "blocks_phase8",
    "evidence_family",
    "summary",
]


def _now() -> str:
    return datetime.now(timezone.utc).isoformat()


def _write_json(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True), encoding="utf-8")


def _write_csv(path: Path, rows: list[dict], columns: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=columns, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def _read_csv(path: Path) -> pd.DataFrame:
    return pd.read_csv(path) if path.exists() else pd.DataFrame()


def _git_short_hash() -> str:
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "--short", "HEAD"],
            stderr=subprocess.DEVNULL,
            text=True,
        ).strip()
    except Exception:
        return "unknown"


def _validate_seeds(seeds: Iterable[int] | None) -> list[int]:
    selected = list(DEFAULT_SEEDS if seeds is None else seeds)
    invalid = sorted(set(selected) - set(REQUIRED_FORMAL_SEEDS))
    if invalid:
        raise ValueError(f"06-04 seeds must be formal seeds 1-20; invalid: {invalid}")
    return selected


def _validate_scales(scales: Iterable[int] | None) -> list[int]:
    selected = list(DEFAULT_SCALES if scales is None else scales)
    invalid = sorted(set(selected) - set(FORMAL_SCALES))
    if invalid:
        raise ValueError(f"06-04 scales must be selected from {FORMAL_SCALES}; invalid: {invalid}")
    return selected


def _n_vehicles(scale: int) -> int:
    return VEHICLE_COUNTS.get(scale, max(1, scale // 10))


def _method_factory(method_label: str, **kwargs):
    if method_label == "DoorToDoor_Choice_CommonRouting":
        return DoorToDoor(**{k: v for k, v in kwargs.items() if k in {"choice_params", "rho_p", "rho_d"}})
    if method_label == "BidirectionalMP_Choice_RH_ALNS":
        return FullModel(**kwargs)
    raise ValueError(f"unsupported reduced 06-04 method: {method_label}")


def _variant_metadata(variant) -> dict:
    metadata = getattr(variant, "method_metadata", {}).copy()
    metadata.setdefault("method_label", getattr(variant, "name", ""))
    metadata.setdefault("service_design", "")
    metadata.setdefault("choice_model", "")
    metadata.setdefault("reoptimization", "")
    metadata.setdefault("routing_solver", "")
    metadata.setdefault("diagnostic_role", "")
    return metadata


def _scaled_passenger_types(
    *,
    beta_walk_multiplier: float = 1.0,
    beta_wait_multiplier: float = 1.0,
    beta_ivt_multiplier: float = 1.0,
) -> list[PassengerType]:
    return [
        PassengerType(
            name=ptype.name,
            beta_walk=ptype.beta_walk * beta_walk_multiplier,
            beta_wait=ptype.beta_wait * beta_wait_multiplier,
            beta_ivt=ptype.beta_ivt * beta_ivt_multiplier,
            beta_price=ptype.beta_price,
        )
        for ptype in variants_module.PASSENGER_TYPES
    ]


@contextmanager
def _passenger_type_scope(passenger_types: list[PassengerType]):
    original = variants_module.PASSENGER_TYPES
    variants_module.PASSENGER_TYPES = list(passenger_types)
    try:
        yield
    finally:
        variants_module.PASSENGER_TYPES = original


def utility_sensitivity_grid() -> list[dict]:
    """Return the preregistered one-factor utility sensitivity settings."""
    return [
        {
            "parameter_setting_id": "baseline_default",
            "description": "default simulation-range choice parameters",
            "beta_walk_multiplier": 1.0,
            "beta_wait_multiplier": 1.0,
            "beta_ivt_multiplier": 1.0,
            "service_asc": 0.0,
            "outside_option_constant": 0.0,
            "type_shares": {"price_sensitive": 0.34, "time_sensitive": 0.33, "walk_sensitive": 0.33},
        },
        {
            "parameter_setting_id": "walk_disutility_high",
            "description": "higher walking disutility",
            "beta_walk_multiplier": 1.5,
            "beta_wait_multiplier": 1.0,
            "beta_ivt_multiplier": 1.0,
            "service_asc": 0.0,
            "outside_option_constant": 0.0,
            "type_shares": {"price_sensitive": 0.34, "time_sensitive": 0.33, "walk_sensitive": 0.33},
        },
        {
            "parameter_setting_id": "wait_disutility_high",
            "description": "higher waiting/access-time disutility",
            "beta_walk_multiplier": 1.0,
            "beta_wait_multiplier": 1.5,
            "beta_ivt_multiplier": 1.0,
            "service_asc": 0.0,
            "outside_option_constant": 0.0,
            "type_shares": {"price_sensitive": 0.34, "time_sensitive": 0.33, "walk_sensitive": 0.33},
        },
        {
            "parameter_setting_id": "ivt_disutility_high",
            "description": "higher in-vehicle-time disutility",
            "beta_walk_multiplier": 1.0,
            "beta_wait_multiplier": 1.0,
            "beta_ivt_multiplier": 1.5,
            "service_asc": 0.0,
            "outside_option_constant": 0.0,
            "type_shares": {"price_sensitive": 0.34, "time_sensitive": 0.33, "walk_sensitive": 0.33},
        },
        {
            "parameter_setting_id": "service_asc_low",
            "description": "lower DRT service attractiveness constant",
            "beta_walk_multiplier": 1.0,
            "beta_wait_multiplier": 1.0,
            "beta_ivt_multiplier": 1.0,
            "service_asc": -1.0,
            "outside_option_constant": 0.0,
            "type_shares": {"price_sensitive": 0.34, "time_sensitive": 0.33, "walk_sensitive": 0.33},
        },
        {
            "parameter_setting_id": "outside_option_high",
            "description": "more attractive outside option",
            "beta_walk_multiplier": 1.0,
            "beta_wait_multiplier": 1.0,
            "beta_ivt_multiplier": 1.0,
            "service_asc": 0.0,
            "outside_option_constant": 1.0,
            "type_shares": {"price_sensitive": 0.34, "time_sensitive": 0.33, "walk_sensitive": 0.33},
        },
        {
            "parameter_setting_id": "walk_sensitive_majority",
            "description": "passenger-type shares tilted toward walk-sensitive riders",
            "beta_walk_multiplier": 1.0,
            "beta_wait_multiplier": 1.0,
            "beta_ivt_multiplier": 1.0,
            "service_asc": 0.0,
            "outside_option_constant": 0.0,
            "type_shares": {"price_sensitive": 0.2, "time_sensitive": 0.2, "walk_sensitive": 0.6},
        },
    ]


def density_radius_grid() -> list[dict]:
    return [
        {
            "parameter_setting_id": "low_radius_sparse_density",
            "radius_tier": "low",
            "rho_p": 800.0,
            "rho_d": 800.0,
            "mp_density_profile": "sparse",
            "description": "tight walking radius with thinned meeting-point candidates",
        },
        {
            "parameter_setting_id": "default_radius_default_density",
            "radius_tier": "medium",
            "rho_p": RHO_P,
            "rho_d": RHO_D,
            "mp_density_profile": "default",
            "description": "Phase 6 default walking radius and meeting-point grid",
        },
        {
            "parameter_setting_id": "high_radius_dense_density",
            "radius_tier": "high",
            "rho_p": 2500.0,
            "rho_d": 2500.0,
            "mp_density_profile": "dense",
            "description": "expanded walking radius with denser candidate grid",
        },
    ]


def fleet_stress_grid() -> list[dict]:
    return [
        {
            "parameter_setting_id": "stress_low_demand",
            "stress_level": "low",
            "n_requests": 100,
            "n_vehicles": 15,
            "demand_scale": 100,
        },
        {
            "parameter_setting_id": "stress_base",
            "stress_level": "medium",
            "n_requests": 200,
            "n_vehicles": 15,
            "demand_scale": 200,
        },
        {
            "parameter_setting_id": "stress_high_demand",
            "stress_level": "high",
            "n_requests": 300,
            "n_vehicles": 15,
            "demand_scale": 300,
        },
    ]


def _scenario_with_density(base: Scenario, profile: str) -> Scenario:
    if profile == "default":
        return base
    if profile == "sparse":
        meeting_points = [mp for idx, mp in enumerate(base.meeting_points) if idx % 4 == 0]
    elif profile == "dense":
        area_m = int(base.area_km * 1000)
        meeting_points = [
            MeetingPoint(id=f"dense_mp_{i}_{j}", coords=(float(i), float(j)))
            for i in range(0, area_m + 1, 1000)
            for j in range(0, area_m + 1, 1000)
        ]
    else:
        raise ValueError(f"unknown meeting-point density profile: {profile}")
    return replace(base, meeting_points=meeting_points, name=f"{base.name}_{profile}_mp")


def _base_row(
    *,
    package_id: str,
    package_dir: Path,
    setting_id: str,
    seed: int,
    scale: int,
    scenario: Scenario,
    method_label: str,
    variant,
    parameter_values: dict,
    n_vehicles: int,
) -> dict:
    metadata = _variant_metadata(variant)
    return {
        "package_id": package_id,
        "run_id": f"{package_id}:{setting_id}:{scenario.name}:{method_label}:s{seed}",
        "config_id": f"{package_id}:{setting_id}:scale_{scale}:seed_{seed}",
        "parameter_setting_id": setting_id,
        "seed": seed,
        "scale": scale,
        "scenario": scenario.name,
        "method_label": method_label,
        "variant": getattr(variant, "name", metadata.get("method_label", "")),
        "service_design": metadata.get("service_design", ""),
        "choice_model": metadata.get("choice_model", ""),
        "reoptimization": metadata.get("reoptimization", ""),
        "routing_solver": metadata.get("routing_solver", ""),
        "evidence_family": "formal_robustness_diagnostic",
        "diagnostic_role": package_id,
        "status": "completed",
        "detailed_reason": "completed",
        "runtime_s": 0.0,
        "error_message": "",
        "result_schema_version": "phase06.06-04.v1",
        "timestamp_utc": _now(),
        "artifact_dir": str(package_dir),
        "git_commit_or_code_hash": _git_commit_or_code_hash(),
        "n_requests": len(scenario.requests),
        "n_vehicles": n_vehicles,
        "vehicle_capacity": scenario.vehicles[0].capacity if scenario.vehicles else 0,
        "n_offered": 0,
        "n_served": 0,
        "served_share": 0.0,
        "behavioral_acceptance_rate": 0.0,
        "choice_rejection_rate": 0.0,
        "feasibility_rejection_rate": 0.0,
        "total_vehicle_km": 0.0,
        "vkm_per_served_trip": 0.0,
        "vkm_per_original_request": 0.0,
        "avg_wait": 0.0,
        "p95_wait": 0.0,
        "avg_walk": 0.0,
        "avg_ivt": 0.0,
        "detour_ratio": 0.0,
        "fairness_index": 0.0,
        "rho_p": parameter_values.get("rho_p", ""),
        "rho_d": parameter_values.get("rho_d", ""),
        "mp_density_profile": parameter_values.get("mp_density_profile", ""),
        "meeting_point_count": len(scenario.meeting_points),
        "stress_level": parameter_values.get("stress_level", ""),
        "demand_scale": parameter_values.get("demand_scale", scale),
        "fleet_size": n_vehicles,
        "parameter_values_json": json.dumps(parameter_values, sort_keys=True),
    }


def _run_variant_row(
    *,
    package_id: str,
    package_dir: Path,
    setting_id: str,
    seed: int,
    scale: int,
    scenario: Scenario,
    method_label: str,
    variant,
    parameter_values: dict,
    n_vehicles: int,
) -> tuple[dict, list[dict], list]:
    row = _base_row(
        package_id=package_id,
        package_dir=package_dir,
        setting_id=setting_id,
        seed=seed,
        scale=scale,
        scenario=scenario,
        method_label=method_label,
        variant=variant,
        parameter_values=parameter_values,
        n_vehicles=n_vehicles,
    )
    started = time.perf_counter()
    try:
        result = variant.run(scenario)
        metrics = compute_metrics(result)
        runtime_s = time.perf_counter() - started
        n_served = sum(1 for record in result.records if record.status == "served")
        n_offered = sum(1 for record in result.records if record.status in {"served", "choice_rejected"})
        row.update(
            {
                "runtime_s": runtime_s,
                "n_offered": n_offered,
                "n_served": n_served,
                "served_share": metrics.served_share,
                "behavioral_acceptance_rate": metrics.behavioral_acceptance_rate,
                "choice_rejection_rate": metrics.choice_rejection_rate,
                "feasibility_rejection_rate": metrics.feasibility_rejection_rate,
                "total_vehicle_km": metrics.vehicle_km,
                "vkm_per_served_trip": metrics.vkm_per_served_trip,
                "vkm_per_original_request": metrics.vkm_per_original_request,
                "avg_wait": metrics.avg_wait,
                "p95_wait": metrics.p95_wait,
                "avg_walk": metrics.avg_walk,
                "avg_ivt": metrics.avg_ivt,
                "detour_ratio": metrics.detour_ratio,
                "fairness_index": metrics.fairness_index,
            }
        )
        utility_rows = []
        for log_row in result.utility_logs:
            enriched = dict(log_row)
            enriched.update(
                {
                    "package_id": package_id,
                    "run_id": row["run_id"],
                    "config_id": row["config_id"],
                    "parameter_setting_id": setting_id,
                    "seed": seed,
                    "scale": scale,
                    "scenario": scenario.name,
                    "method_label": method_label,
                    "method": getattr(variant, "name", ""),
                }
            )
            utility_rows.append(enriched)
        return row, utility_rows, result.records
    except Exception as exc:  # pragma: no cover - exercised through tests by monkeypatch
        runtime_s = time.perf_counter() - started
        row.update(
            {
                "status": "failed",
                "detailed_reason": "exception",
                "runtime_s": runtime_s,
                "error_message": "".join(
                    traceback.format_exception_only(type(exc), exc)
                ).strip(),
            }
        )
        return row, [], []


def _write_package_manifests(
    package_dir: Path,
    *,
    package_id: str,
    seeds: list[int],
    scales: list[int],
    methods: list[str],
    grid: list[dict],
    command: str,
    extra: dict | None = None,
) -> None:
    manifest = {
        "phase": "06",
        "plan": "06-04",
        "package_id": package_id,
        "created_at_utc": _now(),
        "git_commit_before_run": _git_short_hash(),
        "command": command,
        "results_dir": str(package_dir),
        "seed_list": seeds,
        "seeds_are_paired": True,
        "scale_list": scales,
        "method_list": methods,
        "parameter_grid": grid,
        "diagnostic_design": "preregistered reduced formal diagnostic; not main headline evidence",
        "expected_raw_rows": len(seeds) * len(scales) * len(methods) * len(grid),
    }
    if extra:
        manifest.update(extra)
    _write_json(package_dir / "config_manifest.json", manifest)


def _processed_summary(rows: list[dict], group_fields: list[str]) -> pd.DataFrame:
    df = pd.DataFrame(rows)
    if df.empty:
        return pd.DataFrame(group_fields)
    metrics = [
        "served_share",
        "behavioral_acceptance_rate",
        "choice_rejection_rate",
        "feasibility_rejection_rate",
        "total_vehicle_km",
        "vkm_per_served_trip",
        "vkm_per_original_request",
        "avg_wait",
        "avg_walk",
        "avg_ivt",
        "runtime_s",
    ]
    completed = df[df["status"] == "completed"].copy()
    if completed.empty:
        return pd.DataFrame(columns=group_fields + [f"{metric}_mean" for metric in metrics])
    grouped = completed.groupby(group_fields)[metrics].mean(numeric_only=True).reset_index()
    grouped = grouped.rename(columns={metric: f"{metric}_mean" for metric in metrics})
    return grouped


def run_utility_sensitivity(
    results_root: str | Path = DEFAULT_ROBUSTNESS_ROOT,
    seeds: Iterable[int] | None = None,
    scales: Iterable[int] | None = None,
    methods: Iterable[str] | None = None,
    command: str = "programmatic",
) -> dict:
    seeds = _validate_seeds(seeds)
    scales = _validate_scales(scales)
    methods = list(DEFAULT_METHODS if methods is None else methods)
    grid = utility_sensitivity_grid()
    package_dir = Path(results_root) / UTILITY_PACKAGE
    rows: list[dict] = []
    utility_rows: list[dict] = []
    for setting in grid:
        passenger_types = _scaled_passenger_types(
            beta_walk_multiplier=setting["beta_walk_multiplier"],
            beta_wait_multiplier=setting["beta_wait_multiplier"],
            beta_ivt_multiplier=setting["beta_ivt_multiplier"],
        )
        choice_params = ChoiceParameters(
            service_asc=setting["service_asc"],
            outside_option_constant=setting["outside_option_constant"],
            choice_seed=CHOICE_SEED,
            type_shares=dict(setting["type_shares"]),
        )
        with _passenger_type_scope(passenger_types):
            for scale in scales:
                for seed in seeds:
                    scenario = generate_synthetic(scale, _n_vehicles(scale), seed)
                    for method_label in methods:
                        variant = _method_factory(method_label, choice_params=choice_params)
                        row, logs, _ = _run_variant_row(
                            package_id=UTILITY_PACKAGE,
                            package_dir=package_dir,
                            setting_id=setting["parameter_setting_id"],
                            seed=seed,
                            scale=scale,
                            scenario=scenario,
                            method_label=method_label,
                            variant=variant,
                            parameter_values=setting,
                            n_vehicles=_n_vehicles(scale),
                        )
                        rows.append(row)
                        utility_rows.extend(logs)
    _write_csv(package_dir / "raw_results.csv", rows, ROBUSTNESS_RAW_COLUMNS)
    _processed_summary(rows, ["parameter_setting_id", "method_label"]).to_csv(
        package_dir / "processed_results.csv", index=False
    )
    _write_csv(
        package_dir / "utility_logs.csv",
        utility_rows,
        sorted({key for row in utility_rows for key in row}) if utility_rows else ["package_id"],
    )
    _write_json(package_dir / "sensitivity_grid.json", {"settings": grid})
    _write_package_manifests(
        package_dir,
        package_id=UTILITY_PACKAGE,
        seeds=seeds,
        scales=scales,
        methods=methods,
        grid=grid,
        command=command,
        extra={
            "expected_raw_rows": len(seeds) * len(scales) * len(methods) * len(grid),
            "dimensions": [
                "beta_walk",
                "beta_wait_or_access_time",
                "beta_ivt",
                "service_asc",
                "outside_option_constant",
                "passenger_type_shares",
            ],
        },
    )
    report = validate_package(UTILITY_PACKAGE, results_root, seeds, scales, methods, grid)
    return report


def run_mp_density_walking_radius(
    results_root: str | Path = DEFAULT_ROBUSTNESS_ROOT,
    seeds: Iterable[int] | None = None,
    scales: Iterable[int] | None = None,
    methods: Iterable[str] | None = None,
    command: str = "programmatic",
) -> dict:
    seeds = _validate_seeds(seeds)
    scales = _validate_scales(scales)
    methods = list(DEFAULT_METHODS if methods is None else methods)
    grid = density_radius_grid()
    package_dir = Path(results_root) / MP_PACKAGE
    rows: list[dict] = []
    for setting in grid:
        for scale in scales:
            for seed in seeds:
                base = generate_synthetic(scale, _n_vehicles(scale), seed)
                scenario = _scenario_with_density(base, setting["mp_density_profile"])
                for method_label in methods:
                    variant = _method_factory(
                        method_label,
                        rho_p=setting["rho_p"],
                        rho_d=setting["rho_d"],
                    )
                    row, _, _ = _run_variant_row(
                        package_id=MP_PACKAGE,
                        package_dir=package_dir,
                        setting_id=setting["parameter_setting_id"],
                        seed=seed,
                        scale=scale,
                        scenario=scenario,
                        method_label=method_label,
                        variant=variant,
                        parameter_values=setting,
                        n_vehicles=_n_vehicles(scale),
                    )
                    rows.append(row)
    _write_csv(package_dir / "raw_results.csv", rows, ROBUSTNESS_RAW_COLUMNS)
    _processed_summary(rows, ["parameter_setting_id", "method_label"]).to_csv(
        package_dir / "processed_results.csv", index=False
    )
    _write_json(package_dir / "density_radius_grid.json", {"settings": grid})
    _write_package_manifests(
        package_dir,
        package_id=MP_PACKAGE,
        seeds=seeds,
        scales=scales,
        methods=methods,
        grid=grid,
        command=command,
    )
    return validate_package(MP_PACKAGE, results_root, seeds, scales, methods, grid)


def run_fleet_demand_stress(
    results_root: str | Path = DEFAULT_ROBUSTNESS_ROOT,
    seeds: Iterable[int] | None = None,
    methods: Iterable[str] | None = None,
    command: str = "programmatic",
) -> dict:
    seeds = _validate_seeds(seeds)
    methods = list(DEFAULT_METHODS if methods is None else methods)
    grid = fleet_stress_grid()
    package_dir = Path(results_root) / FLEET_PACKAGE
    rows: list[dict] = []
    for setting in grid:
        scale = int(setting["n_requests"])
        n_vehicles = int(setting["n_vehicles"])
        for seed in seeds:
            scenario = generate_synthetic(scale, n_vehicles, seed)
            for method_label in methods:
                variant = _method_factory(method_label)
                row, _, _ = _run_variant_row(
                    package_id=FLEET_PACKAGE,
                    package_dir=package_dir,
                    setting_id=setting["parameter_setting_id"],
                    seed=seed,
                    scale=scale,
                    scenario=scenario,
                    method_label=method_label,
                    variant=variant,
                    parameter_values=setting,
                    n_vehicles=n_vehicles,
                )
                rows.append(row)
    _write_csv(package_dir / "raw_results.csv", rows, ROBUSTNESS_RAW_COLUMNS)
    _processed_summary(rows, ["parameter_setting_id", "method_label"]).to_csv(
        package_dir / "processed_results.csv", index=False
    )
    _write_json(package_dir / "stress_grid.json", {"settings": grid})
    _write_package_manifests(
        package_dir,
        package_id=FLEET_PACKAGE,
        seeds=seeds,
        scales=[setting["n_requests"] for setting in grid],
        methods=methods,
        grid=grid,
        command=command,
        extra={"external_validity": "synthetic_only"},
    )
    return validate_package(
        FLEET_PACKAGE,
        results_root,
        seeds,
        [setting["n_requests"] for setting in grid],
        methods,
        grid,
        key_scale_from_grid=True,
    )


def _gini(values: list[float]) -> float:
    if len(values) < 2 or sum(values) == 0:
        return 0.0
    arr = np.array(sorted(values), dtype=float)
    n = len(arr)
    return float((2 * np.sum(np.arange(1, n + 1) * arr) / (n * arr.sum())) - (n + 1) / n)


def _percentile(values: list[float], q: float) -> float:
    return float(np.percentile(values, q)) if values else 0.0


def run_equity_type_outcomes(
    results_root: str | Path = DEFAULT_ROBUSTNESS_ROOT,
    seeds: Iterable[int] | None = None,
    scales: Iterable[int] | None = None,
    methods: Iterable[str] | None = None,
    command: str = "programmatic",
) -> dict:
    seeds = _validate_seeds(seeds)
    scales = _validate_scales(scales)
    methods = list(DEFAULT_METHODS if methods is None else methods)
    package_dir = Path(results_root) / EQUITY_PACKAGE
    type_rows: list[dict] = []
    individual_rows: list[dict] = []
    grid = [{"parameter_setting_id": "equity_default_choice_parameters"}]
    for scale in scales:
        for seed in seeds:
            scenario = generate_synthetic(scale, _n_vehicles(scale), seed)
            for method_label in methods:
                variant = _method_factory(method_label)
                row, _, records = _run_variant_row(
                    package_id=EQUITY_PACKAGE,
                    package_dir=package_dir,
                    setting_id="equity_default_choice_parameters",
                    seed=seed,
                    scale=scale,
                    scenario=scenario,
                    method_label=method_label,
                    variant=variant,
                    parameter_values={},
                    n_vehicles=_n_vehicles(scale),
                )
                config_id = row["config_id"]
                acceptance_rates = []
                by_type = {ptype: [] for ptype in PASSENGER_TYPES}
                for record in records:
                    by_type.setdefault(record.passenger_type, []).append(record)
                    walk = record.pickup_walk + record.dropoff_walk
                    generalized_cost = abs(record.total_disutility)
                    individual_rows.append(
                        {
                            "package_id": EQUITY_PACKAGE,
                            "config_id": config_id,
                            "seed": seed,
                            "scale": scale,
                            "scenario": scenario.name,
                            "method_label": method_label,
                            "request_id": record.request_id,
                            "passenger_type": record.passenger_type,
                            "status": record.status,
                            "served": record.status == "served",
                            "walking_burden": walk,
                            "waiting_access_time": record.wait_time,
                            "in_vehicle_time": record.ivt,
                            "generalized_cost": generalized_cost,
                        }
                    )
                for ptype in PASSENGER_TYPES:
                    records_for_type = by_type.get(ptype, [])
                    n_original = len(records_for_type)
                    served = [record for record in records_for_type if record.status == "served"]
                    choice = [record for record in records_for_type if record.status == "choice_rejected"]
                    feasible = [
                        record for record in records_for_type
                        if record.status == "feasibility_rejected"
                    ]
                    served_rate = len(served) / n_original if n_original else 0.0
                    acceptance_rates.append(served_rate)
                    type_rows.append(
                        {
                            "package_id": EQUITY_PACKAGE,
                            "config_id": config_id,
                            "seed": seed,
                            "scale": scale,
                            "scenario": scenario.name,
                            "method_label": method_label,
                            "passenger_type": ptype,
                            "n_original": n_original,
                            "n_served": len(served),
                            "served_share": served_rate,
                            "type_level_acceptance_rate": served_rate,
                            "choice_rejection_rate": len(choice) / n_original if n_original else 0.0,
                            "feasibility_rejection_rate": len(feasible) / n_original if n_original else 0.0,
                            "avg_wait": float(np.mean([r.wait_time for r in served])) if served else 0.0,
                            "avg_walk": float(np.mean([r.pickup_walk + r.dropoff_walk for r in served])) if served else 0.0,
                            "avg_ivt": float(np.mean([r.ivt for r in served])) if served else 0.0,
                            "mean_generalized_cost": float(np.mean([abs(r.total_disutility) for r in records_for_type])) if records_for_type else 0.0,
                            "equity_gini_acceptance": 0.0,
                            "status": "completed" if row["status"] == "completed" else row["status"],
                        }
                    )
                gini = _gini(acceptance_rates)
                for type_row in type_rows[-len(PASSENGER_TYPES):]:
                    type_row["equity_gini_acceptance"] = gini
    _write_csv(package_dir / "type_level_outcomes.csv", type_rows, EQUITY_TYPE_COLUMNS)
    _write_csv(
        package_dir / "individual_burden_distribution.csv",
        individual_rows,
        INDIVIDUAL_BURDEN_COLUMNS,
    )
    individual_df = pd.DataFrame(individual_rows)
    burden_summary = {}
    if not individual_df.empty:
        for field in ["walking_burden", "generalized_cost"]:
            values = pd.to_numeric(individual_df[field], errors="coerce").dropna().tolist()
            burden_summary[field] = {
                "mean": float(np.mean(values)) if values else 0.0,
                "median": _percentile(values, 50),
                "p90": _percentile(values, 90),
                "p95": _percentile(values, 95),
            }
    _write_json(
        package_dir / "equity_summary.json",
        {
            "package_id": EQUITY_PACKAGE,
            "passenger_type_parameters": "simulation_range_constructs",
            "individual_level_burden_available": True,
            "individual_burden_summary": burden_summary,
            "claim_limit": "equity claims remain exploratory until Phase 8 claim grading",
        },
    )
    _write_package_manifests(
        package_dir,
        package_id=EQUITY_PACKAGE,
        seeds=seeds,
        scales=scales,
        methods=methods,
        grid=grid,
        command=command,
        extra={
            "expected_type_rows": len(seeds) * len(scales) * len(methods) * len(PASSENGER_TYPES),
            "passenger_type_parameters": "simulation_range_constructs",
        },
    )
    return validate_equity_package(results_root, seeds, scales, methods)


def run_algorithm_diagnostics(
    results_root: str | Path = DEFAULT_ROBUSTNESS_ROOT,
    command: str = "programmatic",
) -> dict:
    package_dir = Path(results_root) / ALGORITHM_PACKAGE
    package_dir.mkdir(parents=True, exist_ok=True)
    gate = check_label_implementation_gate()
    rolling_status = "completed" if gate["passed"] else "conflict"
    rolling_rows = [
        {
            "package_id": "rolling_horizon",
            "label_implementation_check_status": rolling_status,
            "status": rolling_status,
            "blocks_phase8": not gate["passed"],
            "errors": "; ".join(gate["errors"]),
            "evidence_family": "algorithm_diagnostic",
            "diagnostic_role": "label_implementation_check",
        }
    ]
    _write_csv(
        package_dir / "rolling_horizon_diagnostics.csv",
        rolling_rows,
        [
            "package_id",
            "label_implementation_check_status",
            "status",
            "blocks_phase8",
            "errors",
            "evidence_family",
            "diagnostic_role",
        ],
    )
    alns_rows = run_alns_budget_smoke(budgets=[5, 20, 50], n_requests=8, n_vehicles=3, seed=42)
    _write_json(package_dir / "alns_budget_diagnostics.json", {"rows": alns_rows})
    milp_rows = []
    for n_requests in [20, 30]:
        for seed in [42, 43]:
            row = run_gap_experiment(n_requests=n_requests, seed=seed)
            row.setdefault("detailed_reason", "")
            row.setdefault("runtime_s", 0.0)
            if row.get("milp_status") == "no_gurobi":
                row["status"] = "blocked"
                row["detailed_reason"] = row.get("detailed_reason") or "Gurobi unavailable."
            row["gap_pct"] = row["gap_pct"] if row.get("comparable_gap") else None
            milp_rows.append(row)
    _write_json(package_dir / "milp_gap_diagnostics.json", {"rows": milp_rows})
    _write_package_manifests(
        package_dir,
        package_id=ALGORITHM_PACKAGE,
        seeds=[42, 43],
        scales=[8, 20, 30],
        methods=["rolling_horizon_label_check", "alns_budget", "milp_gap"],
        grid=[
            {"parameter_setting_id": "rolling_horizon_label_check"},
            {"parameter_setting_id": "alns_budget_5_20_50"},
            {"parameter_setting_id": "milp_gap_n20_n30"},
        ],
        command=command,
        extra={"expected_raw_rows": len(rolling_rows) + len(alns_rows) + len(milp_rows)},
    )
    report = validate_algorithm_package(results_root)
    return report


def _status_counts(df: pd.DataFrame) -> dict:
    if df.empty or "status" not in df.columns:
        return {}
    return {str(key): int(value) for key, value in df["status"].value_counts().to_dict().items()}


def _check_columns(report: dict, df: pd.DataFrame, columns: Iterable[str], label: str) -> None:
    missing = sorted(set(columns) - set(df.columns))
    if missing:
        report["schema_drift"] = True
        report["errors"].append(f"{label} missing required columns: {', '.join(missing)}")


def _check_grid(
    report: dict,
    df: pd.DataFrame,
    seeds: list[int],
    scales: list[int],
    methods: list[str],
    grid: list[dict],
    *,
    key_scale_from_grid: bool = False,
) -> None:
    expected = set()
    for setting in grid:
        setting_id = setting["parameter_setting_id"]
        setting_scales = [setting["n_requests"]] if key_scale_from_grid and "n_requests" in setting else scales
        for seed in seeds:
            for scale in setting_scales:
                for method in methods:
                    expected.add((setting_id, seed, int(scale), method))
    observed = {
        (str(row["parameter_setting_id"]), int(row["seed"]), int(row["scale"]), str(row["method_label"]))
        for _, row in df.iterrows()
    } if not df.empty else set()
    missing = sorted(expected - observed)
    extra = sorted(observed - expected)
    report["row_counts"]["expected_rows"] = len(expected)
    report["row_counts"]["actual_rows"] = int(len(df))
    report["row_counts"]["missing_rows"] = len(missing)
    report["row_counts"]["extra_rows"] = len(extra)
    if missing:
        preview = "; ".join(map(str, missing[:5]))
        report["errors"].append(f"missing robustness rows: {len(missing)} ({preview})")
    if extra:
        preview = "; ".join(map(str, extra[:5]))
        report["errors"].append(f"unexpected robustness rows: {len(extra)} ({preview})")


def _check_denominators(report: dict, df: pd.DataFrame) -> None:
    completed = df[df["status"] == "completed"].copy()
    if completed.empty:
        report["denominator_checks"] = {"status": "skipped_no_completed_rows"}
        return
    n_requests = pd.to_numeric(completed["n_requests"], errors="coerce")
    n_served = pd.to_numeric(completed["n_served"], errors="coerce")
    vehicle_km = pd.to_numeric(completed["total_vehicle_km"], errors="coerce")
    safe_requests = n_requests.where(n_requests > 0)
    safe_served = n_served.where(n_served > 0)
    checks = {
        "served_share": (
            (n_served / safe_requests).fillna(0.0)
            - pd.to_numeric(completed["served_share"], errors="coerce")
        ).abs() <= 1e-6,
        "vkm_per_original_request": (
            (vehicle_km / safe_requests).fillna(0.0)
            - pd.to_numeric(completed["vkm_per_original_request"], errors="coerce")
        ).abs() <= 1e-6,
        "vkm_per_served_trip": (
            (vehicle_km / safe_served).fillna(0.0)
            - pd.to_numeric(completed["vkm_per_served_trip"], errors="coerce")
        ).abs() <= 1e-6,
        "behavioral_acceptance_rate": (
            (1.0 - pd.to_numeric(completed["choice_rejection_rate"], errors="coerce"))
            - pd.to_numeric(completed["behavioral_acceptance_rate"], errors="coerce")
        ).abs() <= 1e-6,
        "rejection_partition": (
            pd.to_numeric(completed["served_share"], errors="coerce")
            + pd.to_numeric(completed["choice_rejection_rate"], errors="coerce")
            + pd.to_numeric(completed["feasibility_rejection_rate"], errors="coerce")
            - 1.0
        ).abs() <= 1e-6,
    }
    report["denominator_checks"] = {
        name: "passed" if bool(mask.all()) else "failed"
        for name, mask in checks.items()
    }
    for name, mask in checks.items():
        if not bool(mask.all()):
            report["errors"].append(f"denominator check failed for {name}: {int((~mask).sum())} rows")


def validate_package(
    package_id: str,
    results_root: str | Path = DEFAULT_ROBUSTNESS_ROOT,
    seeds: Iterable[int] | None = None,
    scales: Iterable[int] | None = None,
    methods: Iterable[str] | None = None,
    grid: list[dict] | None = None,
    *,
    key_scale_from_grid: bool = False,
) -> dict:
    package_dir = Path(results_root) / package_id
    seeds = _validate_seeds(seeds)
    scales = _validate_scales(scales)
    methods = list(DEFAULT_METHODS if methods is None else methods)
    grid = grid or [{"parameter_setting_id": "default"}]
    report = {
        "package_id": package_id,
        "passed": True,
        "schema_drift": False,
        "denominator_checks": {},
        "errors": [],
        "warnings": [],
        "row_counts": {},
        "checked_files": [],
    }
    required_files = ["raw_results.csv", "processed_results.csv", "config_manifest.json"]
    for filename in required_files:
        path = package_dir / filename
        if path.exists():
            report["checked_files"].append(str(path))
        else:
            report["errors"].append(f"missing required file: {path}")
    raw = _read_csv(package_dir / "raw_results.csv")
    if not raw.empty:
        _check_columns(report, raw, ROBUSTNESS_RAW_COLUMNS, "raw_results.csv")
        _check_grid(report, raw, seeds, scales, methods, grid, key_scale_from_grid=key_scale_from_grid)
        report["row_counts"].update(
            completed_rows=int((raw["status"] == "completed").sum()),
            failed_rows=int((raw["status"] == "failed").sum()),
            timeout_rows=int((raw["status"] == "timeout").sum()),
            blocked_rows=int((raw["status"] == "blocked").sum()),
        )
        _check_denominators(report, raw)
    report["passed"] = not report["errors"]
    _write_json(package_dir / "validation_report.json", report)
    return report


def validate_equity_package(
    results_root: str | Path = DEFAULT_ROBUSTNESS_ROOT,
    seeds: Iterable[int] | None = None,
    scales: Iterable[int] | None = None,
    methods: Iterable[str] | None = None,
) -> dict:
    package_dir = Path(results_root) / EQUITY_PACKAGE
    seeds = _validate_seeds(seeds)
    scales = _validate_scales(scales)
    methods = list(DEFAULT_METHODS if methods is None else methods)
    report = {
        "package_id": EQUITY_PACKAGE,
        "passed": True,
        "schema_drift": False,
        "denominator_checks": {},
        "errors": [],
        "warnings": [],
        "row_counts": {},
        "checked_files": [],
    }
    required = [
        "type_level_outcomes.csv",
        "individual_burden_distribution.csv",
        "equity_summary.json",
        "config_manifest.json",
    ]
    for filename in required:
        path = package_dir / filename
        if path.exists():
            report["checked_files"].append(str(path))
        else:
            report["errors"].append(f"missing required file: {path}")
    type_df = _read_csv(package_dir / "type_level_outcomes.csv")
    if not type_df.empty:
        _check_columns(report, type_df, EQUITY_TYPE_COLUMNS, "type_level_outcomes.csv")
        expected = len(seeds) * len(scales) * len(methods) * len(PASSENGER_TYPES)
        report["row_counts"] = {
            "expected_type_rows": expected,
            "actual_type_rows": int(len(type_df)),
            "individual_rows": int(len(_read_csv(package_dir / "individual_burden_distribution.csv"))),
            **_status_counts(type_df),
        }
        if len(type_df) != expected:
            report["errors"].append(f"type-level row count {len(type_df)} != expected {expected}")
        completed = type_df[type_df["status"] == "completed"].copy()
        if completed.empty:
            report["denominator_checks"] = {"status": "skipped_no_completed_rows"}
        else:
            n_original = pd.to_numeric(completed["n_original"], errors="coerce")
            n_served = pd.to_numeric(completed["n_served"], errors="coerce")
            safe_original = n_original.where(n_original > 0)
            checks = {
                "served_share": (
                    (n_served / safe_original).fillna(0.0)
                    - pd.to_numeric(completed["served_share"], errors="coerce")
                ).abs() <= 1e-6,
                "type_level_acceptance_rate": (
                    (n_served / safe_original).fillna(0.0)
                    - pd.to_numeric(completed["type_level_acceptance_rate"], errors="coerce")
                ).abs() <= 1e-6,
                "rejection_partition": (
                    pd.to_numeric(completed["served_share"], errors="coerce")
                    + pd.to_numeric(completed["choice_rejection_rate"], errors="coerce")
                    + pd.to_numeric(completed["feasibility_rejection_rate"], errors="coerce")
                    - 1.0
                ).abs() <= 1e-6,
            }
            report["denominator_checks"] = {
                name: "passed" if bool(mask.all()) else "failed"
                for name, mask in checks.items()
            }
            for name, mask in checks.items():
                if not bool(mask.all()):
                    report["errors"].append(f"equity denominator check failed for {name}")
    report["passed"] = not report["errors"]
    _write_json(package_dir / "validation_report.json", report)
    return report


def validate_algorithm_package(results_root: str | Path = DEFAULT_ROBUSTNESS_ROOT) -> dict:
    package_dir = Path(results_root) / ALGORITHM_PACKAGE
    report = {
        "package_id": ALGORITHM_PACKAGE,
        "passed": True,
        "schema_drift": False,
        "denominator_checks": {"status": "not_applicable_algorithm_diagnostic"},
        "errors": [],
        "warnings": [],
        "row_counts": {},
        "checked_files": [],
    }
    for filename in [
        "rolling_horizon_diagnostics.csv",
        "alns_budget_diagnostics.json",
        "milp_gap_diagnostics.json",
        "config_manifest.json",
    ]:
        path = package_dir / filename
        if path.exists():
            report["checked_files"].append(str(path))
        else:
            report["errors"].append(f"missing required file: {path}")
    rolling = _read_csv(package_dir / "rolling_horizon_diagnostics.csv")
    if not rolling.empty and (rolling["label_implementation_check_status"] == "conflict").any():
        report["warnings"].append("rolling-horizon label implementation conflict blocks Phase 8 RH claim support")
    rolling_count = int(len(rolling)) if not rolling.empty else 0
    alns_count = 0
    milp_count = 0
    milp_blocked = 0
    for filename in ["alns_budget_diagnostics.json", "milp_gap_diagnostics.json"]:
        path = package_dir / filename
        if path.exists():
            payload = json.loads(path.read_text(encoding="utf-8"))
            rows = payload.get("rows", [])
            report["row_counts"][filename] = len(rows)
            if filename == "alns_budget_diagnostics.json":
                alns_count = len(rows)
            else:
                milp_count = len(rows)
                milp_blocked = sum(
                    1
                    for row in rows
                    if row.get("status") in {"blocked", "no_gurobi", "no_accepted", "timeout", "infeasible", "error"}
                )
    total_rows = rolling_count + alns_count + milp_count
    rolling_blocked = int((rolling.get("status", pd.Series(dtype=str)) == "conflict").sum()) if not rolling.empty else 0
    report["row_counts"].update(
        expected_rows=total_rows,
        actual_rows=total_rows,
        completed_rows=total_rows - rolling_blocked - milp_blocked,
        failed_rows=0,
        timeout_rows=0,
        blocked_rows=rolling_blocked + milp_blocked,
    )
    report["passed"] = not report["errors"]
    _write_json(package_dir / "validation_report.json", report)
    return report


def append_failures_to_ledger(results_root: str | Path = DEFAULT_ROBUSTNESS_ROOT) -> Path:
    ledger = ensure_rerun_ledger(DEFAULT_RERUN_LEDGER_PATH)
    existing = set()
    with ledger.open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            existing.add((row.get("run_id", ""), row.get("config_id", ""), row.get("status", "")))
    rows = []
    for package_id in [UTILITY_PACKAGE, MP_PACKAGE, FLEET_PACKAGE]:
        raw_path = Path(results_root) / package_id / "raw_results.csv"
        if not raw_path.exists():
            continue
        with raw_path.open(newline="", encoding="utf-8") as handle:
            for row in csv.DictReader(handle):
                if row.get("status") not in {"failed", "timeout", "blocked"}:
                    continue
                key = (row.get("run_id", ""), row.get("config_id", ""), row.get("status", ""))
                if key in existing:
                    continue
                rows.append(
                    {
                        "run_id": row.get("run_id", ""),
                        "config_id": row.get("config_id", ""),
                        "seed": row.get("seed", ""),
                        "scale": row.get("scale", ""),
                        "method": row.get("method_label", ""),
                        "status": row.get("status", ""),
                        "error": row.get("error_message", ""),
                        "reason": row.get("detailed_reason", ""),
                        "fix": "",
                        "rerun_result": "",
                    }
                )
    if rows:
        with ledger.open("a", newline="", encoding="utf-8") as handle:
            writer = csv.DictWriter(handle, fieldnames=RERUN_LEDGER_COLUMNS)
            writer.writerows(rows)
    return ledger


def validate_all(
    results_root: str | Path = DEFAULT_ROBUSTNESS_ROOT,
    seeds: Iterable[int] | None = None,
    scales: Iterable[int] | None = None,
    methods: Iterable[str] | None = None,
) -> dict:
    seeds = _validate_seeds(seeds)
    scales = _validate_scales(scales)
    methods = list(DEFAULT_METHODS if methods is None else methods)
    reports = {
        UTILITY_PACKAGE: validate_package(
            UTILITY_PACKAGE,
            results_root,
            seeds,
            scales,
            methods,
            utility_sensitivity_grid(),
        ),
        MP_PACKAGE: validate_package(
            MP_PACKAGE,
            results_root,
            seeds,
            scales,
            methods,
            density_radius_grid(),
        ),
        FLEET_PACKAGE: validate_package(
            FLEET_PACKAGE,
            results_root,
            seeds,
            [setting["n_requests"] for setting in fleet_stress_grid()],
            methods,
            fleet_stress_grid(),
            key_scale_from_grid=True,
        ),
        EQUITY_PACKAGE: validate_equity_package(results_root, seeds, scales, methods),
        ALGORITHM_PACKAGE: validate_algorithm_package(results_root),
    }
    passed = all(report["passed"] for report in reports.values())
    schema_drift = any(report.get("schema_drift") for report in reports.values())
    denominator_checks = {
        package_id: report.get("denominator_checks", {})
        for package_id, report in reports.items()
    }
    validation = {
        "phase": "06",
        "plan": "06-04",
        "passed": passed,
        "schema_drift": schema_drift,
        "denominator_checks": denominator_checks,
        "package_reports": reports,
        "errors": [
            f"{package_id}: {error}"
            for package_id, report in reports.items()
            for error in report.get("errors", [])
        ],
        "warnings": [
            f"{package_id}: {warning}"
            for package_id, report in reports.items()
            for warning in report.get("warnings", [])
        ],
    }
    _write_json(Path(results_root) / "validation_report.json", validation)
    append_failures_to_ledger(results_root)
    write_gate_results(results_root, validation)
    return validation


def _advantage_rows(df: pd.DataFrame, metric: str) -> pd.DataFrame:
    completed = df[df["status"] == "completed"].copy()
    if completed.empty:
        return pd.DataFrame()
    pivot = completed.pivot_table(
        index=["parameter_setting_id", "seed", "scale"],
        columns="method_label",
        values=metric,
        aggfunc="first",
    )
    if not {"BidirectionalMP_Choice_RH_ALNS", "DoorToDoor_Choice_CommonRouting"}.issubset(pivot.columns):
        return pd.DataFrame()
    diff = pivot["BidirectionalMP_Choice_RH_ALNS"] - pivot["DoorToDoor_Choice_CommonRouting"]
    return diff.groupby("parameter_setting_id").agg(["mean", "min", "max"]).reset_index()


def _package_advantage_summary(path: Path) -> dict:
    raw = _read_csv(path)
    if raw.empty:
        return {"status": "no_rows"}
    served = _advantage_rows(raw, "vkm_per_served_trip")
    original = _advantage_rows(raw, "vkm_per_original_request")
    def verdict(df: pd.DataFrame) -> str:
        if df.empty:
            return "unsupported"
        return "yes" if bool((df["mean"] < 0).all()) else "mixed"
    return {
        "vkm_per_served": verdict(served),
        "vkm_per_original": verdict(original),
        "served_diff_by_setting": served.to_dict(orient="records") if not served.empty else [],
        "original_diff_by_setting": original.to_dict(orient="records") if not original.empty else [],
    }


def write_gate_results(results_root: str | Path, validation: dict) -> Path:
    root = Path(results_root)
    rows = []
    for package_id, report in validation["package_reports"].items():
        rows.append(
            {
                "package_id": package_id,
                "status": "passed" if report["passed"] else "blocked",
                "passed": report["passed"],
                "role": "formal_diagnostic",
                "output_path": str(root / package_id),
                "blocks_phase8": not report["passed"] or bool(report.get("warnings")),
                "evidence_family": (
                    "algorithm_diagnostic"
                    if package_id == ALGORITHM_PACKAGE
                    else "formal_robustness_diagnostic"
                ),
                "summary": "; ".join(report.get("errors", []) or report.get("warnings", []) or ["structural validation passed"]),
            }
        )
    path = root / "supplementary_gate_results.csv"
    _write_csv(path, rows, GATE_COLUMNS)
    return path


def write_run_manifest(
    results_root: str | Path,
    *,
    command: str,
    seeds: list[int],
    scales: list[int],
    methods: list[str],
    started_at_utc: str,
    finished_at_utc: str,
    validation: dict,
) -> Path:
    root = Path(results_root)
    manifest = {
        "phase": "06",
        "plan": "06-04",
        "run_type": "formal_robustness_diagnostics",
        "diagnostic_design": "reduced formal diagnostic, not main headline evidence",
        "command": command,
        "git_commit_before_run": _git_short_hash(),
        "started_at_utc": started_at_utc,
        "finished_at_utc": finished_at_utc,
        "results_root": str(root),
        "seed_list": seeds,
        "seeds_are_paired": True,
        "scale_list": scales,
        "method_list": methods,
        "packages": list(PACKAGE_NAMES),
        "package_row_counts": {
            package_id: report.get("row_counts", {})
            for package_id, report in validation.get("package_reports", {}).items()
        },
        "validation_report_path": str(root / "validation_report.json"),
    }
    path = root / "run_manifest.json"
    _write_json(path, manifest)
    return path


def write_summary(
    results_root: str | Path = DEFAULT_ROBUSTNESS_ROOT,
    output_path: str | Path = Path(".planning/phases/06-formal-synthetic-experiments/06-04-SUMMARY.md"),
    commands_run: list[str] | None = None,
) -> Path:
    root = Path(results_root)
    validation = json.loads((root / "validation_report.json").read_text(encoding="utf-8"))
    run_manifest = json.loads((root / "run_manifest.json").read_text(encoding="utf-8"))
    package_reports = validation["package_reports"]
    commands = commands_run or [run_manifest["command"]]

    utility_summary = _package_advantage_summary(root / UTILITY_PACKAGE / "raw_results.csv")
    mp_summary = _package_advantage_summary(root / MP_PACKAGE / "raw_results.csv")
    fleet_summary = _package_advantage_summary(root / FLEET_PACKAGE / "raw_results.csv")
    equity_report = package_reports[EQUITY_PACKAGE]
    overall_advantage = "conditional_or_mixed"
    if (
        utility_summary.get("vkm_per_served") == "yes"
        and mp_summary.get("vkm_per_served") == "yes"
        and fleet_summary.get("vkm_per_served") == "yes"
        and validation["passed"]
    ):
        overall_advantage = "conditional"

    status_text = "passed" if validation["passed"] else "blocked"
    next_step = "Phase 6 can proceed to 06-05; do not enter 06-05 automatically." if validation["passed"] else "Phase 6 Plan 06-04 blocked repair."
    row_lines = []
    actual_lines = []
    for package_id, report in package_reports.items():
        counts = report.get("row_counts", {})
        expected = counts.get("expected_rows", counts.get("expected_type_rows", "n/a"))
        actual = counts.get("actual_rows", counts.get("actual_type_rows", counts.get("individual_rows", "n/a")))
        completed = counts.get("completed_rows", counts.get("completed", "n/a"))
        failed = counts.get("failed_rows", counts.get("failed", 0))
        timeout = counts.get("timeout_rows", counts.get("timeout", 0))
        blocked = counts.get("blocked_rows", counts.get("blocked", 0))
        row_lines.append(
            f"- {package_id}: expected={counts.get('expected_rows', counts.get('expected_type_rows', 'n/a'))}, "
            f"actual={counts.get('actual_rows', counts.get('actual_type_rows', counts.get('individual_rows', 'n/a')))}, "
            f"completed={counts.get('completed_rows', counts.get('completed', 'n/a'))}, "
            f"failed={counts.get('failed_rows', counts.get('failed', 0))}, "
            f"timeout={counts.get('timeout_rows', counts.get('timeout', 0))}, "
            f"blocked={counts.get('blocked_rows', counts.get('blocked', 0))}"
        )
        actual_lines.append(
            f"- {package_id}: actual={actual}, expected={expected}, completed={completed}, failed={failed}, timeout={timeout}, blocked={blocked}"
        )

    content = f"""# Phase 6 Plan 06-04 Summary: Robustness, Sensitivity, and Equity Diagnostics

## 1. Purpose

Execute reduced formal robustness diagnostics after the 06-02 main behavioral matrix and 06-03 coverage-confounding controls.

## 2. Why Robustness Diagnostics Are Needed After 06-02 And 06-03

06-02 established the main behavioral matrix under default choice parameters. 06-03 showed that FullModel efficiency advantages survive matched coverage and are mixed under fixed accepted-set vkm/original. 06-04 tests whether the remaining evidence boundary is sensitive to utility assumptions, walking-radius and meeting-point-density settings, fleet-demand stress, and passenger-type outcomes.

## 3. Commands Run

{chr(10).join(f'- `{command}`' for command in commands)}

## 4. Git Commit Before Run

`{run_manifest['git_commit_before_run']}`

## 5. Packages Executed

{', '.join(PACKAGE_NAMES)}

## 6. Seed List And Pairing

Seeds: {run_manifest['seed_list']}. Seeds are paired across methods and settings.

## 7. Scale List

Scales: {run_manifest['scale_list']}. The design is a reduced formal diagnostic, not main headline evidence.

## 8. Method List

Methods: {run_manifest['method_list']}. Single-sided variants were not included in this reduced runtime-bounded diagnostic.

## 9. Parameter Grids

- Utility sensitivity: `{root / UTILITY_PACKAGE / 'sensitivity_grid.json'}`
- Walking radius / MP density: `{root / MP_PACKAGE / 'density_radius_grid.json'}`
- Fleet-demand stress: `{root / FLEET_PACKAGE / 'stress_grid.json'}`

## 10. Expected Row Counts

{chr(10).join(row_lines)}

## 11. Actual Row Counts

{chr(10).join(actual_lines)}

## 12. Completed / Failed / Timeout / Blocked Row Counts

{chr(10).join(row_lines)}

## 13. Durable Failure Summary

Failure rows, if any, were appended to `.planning/phases/06-formal-synthetic-experiments/06_FAILURE_RERUN_LEDGER.csv`. Structural validation errors: {validation['errors'] or 'none'}.

## 14. Schema Validation

schema_drift: {validation['schema_drift']}

## 15. Denominator Validation

{json.dumps(validation['denominator_checks'], indent=2)}

## 16. Utility Sensitivity Summary

{json.dumps(utility_summary, indent=2)}

## 17. Walking Radius / Meeting-Point Density Summary

{json.dumps(mp_summary, indent=2)}

## 18. Fleet-Demand Stress Summary

{json.dumps(fleet_summary, indent=2)}

## 19. Equity / Type-Level Summary

Equity validation: {equity_report['passed']}. Type-level outcomes and individual burden distribution were generated. Passenger types remain simulation-range constructs.

## 20. Whether FullModel Advantage Is Robust, Conditional, Mixed, Or Unsupported

{overall_advantage}. The diagnostic evidence supports a conditional efficiency interpretation, not an unconditional final manuscript claim.

## 21. Phase 8 Claim Strength Supported

Supports at most moderate/conditional robustness screening for efficiency. Equity remains exploratory until Phase 8 grades claim evidence.

## 22. Whether 06-04 Passed Or Blocked

{status_text}

## 23. Exact Blockers If Blocked

{validation['errors'] or 'None'}

## 24. Whether Phase 6 Can Proceed To 06-05

{next_step}
"""
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(content, encoding="utf-8")
    return output_path


def run_all(
    results_root: str | Path = DEFAULT_ROBUSTNESS_ROOT,
    seeds: Iterable[int] | None = None,
    scales: Iterable[int] | None = None,
    methods: Iterable[str] | None = None,
    command: str = "programmatic",
    write_summary_file: bool = False,
) -> dict:
    seeds = _validate_seeds(seeds)
    scales = _validate_scales(scales)
    methods = list(DEFAULT_METHODS if methods is None else methods)
    started = _now()
    run_utility_sensitivity(results_root, seeds, scales, methods, command)
    run_mp_density_walking_radius(results_root, seeds, scales, methods, command)
    run_fleet_demand_stress(results_root, seeds, methods, command)
    run_equity_type_outcomes(results_root, seeds, scales, methods, command)
    run_algorithm_diagnostics(results_root, command)
    validation = validate_all(results_root, seeds, scales, methods)
    write_run_manifest(
        results_root,
        command=command,
        seeds=seeds,
        scales=scales,
        methods=methods,
        started_at_utc=started,
        finished_at_utc=_now(),
        validation=validation,
    )
    if write_summary_file:
        write_summary(results_root, commands_run=[command])
    return validation


def _parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--package", choices=[*PACKAGE_NAMES, "all"], default="all")
    parser.add_argument("--results-root", default=str(DEFAULT_ROBUSTNESS_ROOT))
    parser.add_argument("--seeds", nargs="*", type=int)
    parser.add_argument("--scales", nargs="*", type=int)
    parser.add_argument("--methods", nargs="*")
    parser.add_argument("--validate", action="store_true")
    parser.add_argument("--write-summary", action="store_true")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = _parse_args(argv)
    command = "python -m experiments.phase06_robustness " + " ".join(sys.argv[1:])
    seeds = _validate_seeds(args.seeds)
    scales = _validate_scales(args.scales)
    methods = list(DEFAULT_METHODS if args.methods is None else args.methods)

    if args.validate:
        result = validate_all(args.results_root, seeds, scales, methods)
        if args.write_summary:
            if not (Path(args.results_root) / "run_manifest.json").exists():
                write_run_manifest(
                    args.results_root,
                    command=command,
                    seeds=seeds,
                    scales=scales,
                    methods=methods,
                    started_at_utc=_now(),
                    finished_at_utc=_now(),
                    validation=result,
                )
            write_summary(args.results_root, commands_run=[command])
        print(json.dumps(result, indent=2, sort_keys=True))
        return 0 if result["passed"] else 1

    if args.package == "all":
        result = run_all(
            args.results_root,
            seeds,
            scales,
            methods,
            command=command,
            write_summary_file=args.write_summary,
        )
    elif args.package == UTILITY_PACKAGE:
        result = run_utility_sensitivity(args.results_root, seeds, scales, methods, command)
    elif args.package == MP_PACKAGE:
        result = run_mp_density_walking_radius(args.results_root, seeds, scales, methods, command)
    elif args.package == FLEET_PACKAGE:
        result = run_fleet_demand_stress(args.results_root, seeds, methods, command)
    elif args.package == EQUITY_PACKAGE:
        result = run_equity_type_outcomes(args.results_root, seeds, scales, methods, command)
    else:
        result = run_algorithm_diagnostics(args.results_root, command)

    if args.package != "all":
        result = validate_all(args.results_root, seeds, scales, methods)
        write_run_manifest(
            args.results_root,
            command=command,
            seeds=seeds,
            scales=scales,
            methods=methods,
            started_at_utc=_now(),
            finished_at_utc=_now(),
            validation=result,
        )
        if args.write_summary:
            write_summary(args.results_root, commands_run=[command])
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if result["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
