"""Phase 6 coverage-confounding formal controls.

This module runs the two 06-03 control packages requested after the formal
06-02 main behavioral matrix:

* matched_coverage: cap each behavioral method to the same attainable served
  count within every seed x scale cell.
* fixed_accepted_set: route the same retained request set for every method as a
  diagnostic-only operating-efficiency comparison.

Outputs are intentionally isolated from 06-02 main evidence.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
import subprocess
import sys
import time
import traceback
from concurrent.futures import ThreadPoolExecutor, TimeoutError
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable

import pandas as pd

from experiments.config import (
    DELTA,
    H_WINDOW,
    K_TOP,
    RHO_D,
    RHO_P,
    VEHICLE_COUNTS,
)
from experiments.metrics import compute_metrics
from experiments.phase06_formal import (
    DEFAULT_MAIN_RESULTS_DIR,
    DEFAULT_RERUN_LEDGER_PATH,
    FORMAL_MAIN_METHOD_LABELS,
    FORMAL_SCALES,
    REQUIRED_FORMAL_SEEDS,
)
from experiments.runner import _git_commit_or_code_hash
from experiments.scenarios import Scenario, generate_synthetic
from experiments.variants import (
    DoorToDoor,
    FullModel,
    SingleSidedDropoff,
    SingleSidedPickup,
    TRAVEL_SPEED,
    _COST_WEIGHTS,
)
from src.drt.alns import ALNSState, RollingHorizon, greedy_insertion
from src.drt.types import MeetingPoint, Route


DEFAULT_COVERAGE_ROOT = Path("results/formal/phase06/coverage_controls")
MATCHED_PACKAGE = "matched_coverage"
FIXED_PACKAGE = "fixed_accepted_set"
PACKAGE_NAMES = (MATCHED_PACKAGE, FIXED_PACKAGE)
CONTROL_TIMEOUT_S = 120
MATCHED_COVERAGE_TOLERANCE_COUNT = 0

METHOD_LABEL_TO_VARIANT = {
    "DoorToDoor_Choice_CommonRouting": "DoorToDoor",
    "SingleSidedPickup_Choice_CommonRouting": "SingleSidedPickup",
    "SingleSidedDropoff_Choice_CommonRouting": "SingleSidedDropoff",
    "BidirectionalMP_Choice_RH_ALNS": "FullModel",
}

METHOD_LABEL_TO_SERVICE_DESIGN = {
    "DoorToDoor_Choice_CommonRouting": "door_to_door",
    "SingleSidedPickup_Choice_CommonRouting": "single_sided_pickup",
    "SingleSidedDropoff_Choice_CommonRouting": "single_sided_dropoff",
    "BidirectionalMP_Choice_RH_ALNS": "bidirectional_mp",
}

METHOD_LABEL_TO_REOPTIMIZATION = {
    "DoorToDoor_Choice_CommonRouting": "common_sequential_insertion",
    "SingleSidedPickup_Choice_CommonRouting": "common_sequential_insertion",
    "SingleSidedDropoff_Choice_CommonRouting": "common_sequential_insertion",
    "BidirectionalMP_Choice_RH_ALNS": "rolling_horizon",
}

METHOD_LABEL_TO_ROUTING_SOLVER = {
    "DoorToDoor_Choice_CommonRouting": "greedy_insertion",
    "SingleSidedPickup_Choice_CommonRouting": "greedy_insertion",
    "SingleSidedDropoff_Choice_CommonRouting": "greedy_insertion",
    "BidirectionalMP_Choice_RH_ALNS": "alns",
}


MATCHED_RAW_COLUMNS = [
    "package_id",
    "run_id",
    "config_id",
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
    "original_request_count",
    "attainable_served_count",
    "matched_target_served_count",
    "target_basis",
    "target_adjusted",
    "actual_served_count",
    "served_share",
    "coverage_gap_count",
    "coverage_gap_abs",
    "coverage_tolerance_count",
    "total_vehicle_km",
    "vkm_per_served_trip",
    "vkm_per_original_request",
    "avg_wait",
    "p95_wait",
    "avg_walk",
    "avg_ivt",
    "detour_ratio",
    "fairness_index",
]

FIXED_RAW_COLUMNS = [
    "package_id",
    "run_id",
    "config_id",
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
    "evidence_role",
    "diagnostic_role",
    "status",
    "detailed_reason",
    "runtime_s",
    "error_message",
    "result_schema_version",
    "timestamp_utc",
    "artifact_dir",
    "git_commit_or_code_hash",
    "construction_rule",
    "fallback_used",
    "retained_set_hash",
    "served_intersection_count",
    "serviceable_intersection_count",
    "candidate_serviceable_intersection_count",
    "retained_request_count",
    "retained_share",
    "deterministic_inserted_share",
    "served_count",
    "unserved_accepted_count",
    "original_request_count",
    "total_vehicle_km",
    "vkm_per_inserted_request",
    "vkm_per_served_request",
    "vkm_per_original_request",
    "avg_wait",
    "p95_wait",
    "avg_walk",
    "avg_ivt",
    "detour_ratio",
    "fairness_index",
]


@dataclass(frozen=True)
class ControlSelection:
    seeds: list[int]
    scales: list[int]
    methods: list[str]

    @property
    def expected_rows(self) -> int:
        return len(self.seeds) * len(self.scales) * len(self.methods)


class _MatchedDoorToDoor(DoorToDoor):
    def __init__(self, max_served_count: int):
        super().__init__()
        self._max_served_count = max_served_count

    def _solve(self, scenario: Scenario) -> ALNSState:
        return self._run_actual_offer_sequence(
            scenario=scenario,
            service_design="DoorToDoor",
            meeting_points_for_request=lambda request: [
                MeetingPoint(id=f"dtd_pu_{request.id}", coords=request.origin),
                MeetingPoint(id=f"dtd_do_{request.id}", coords=request.destination),
            ],
            rho_p=0.0,
            rho_d=0.0,
            k_top=1,
            cost_weights=_COST_WEIGHTS,
            max_served_count=self._max_served_count,
        )


class _MatchedSingleSidedPickup(SingleSidedPickup):
    def __init__(self, max_served_count: int):
        super().__init__()
        self._max_served_count = max_served_count

    def _solve(self, scenario: Scenario) -> ALNSState:
        return self._run_actual_offer_sequence(
            scenario=scenario,
            service_design="SingleSidedPickup",
            meeting_points_for_request=lambda request: list(scenario.meeting_points)
            + [MeetingPoint(id=f"ssp_do_{request.id}", coords=request.destination)],
            rho_p=RHO_P,
            rho_d=0.0,
            k_top=K_TOP,
            cost_weights=_COST_WEIGHTS,
            max_served_count=self._max_served_count,
        )


class _MatchedSingleSidedDropoff(SingleSidedDropoff):
    def __init__(self, max_served_count: int):
        super().__init__()
        self._max_served_count = max_served_count

    def _solve(self, scenario: Scenario) -> ALNSState:
        return self._run_actual_offer_sequence(
            scenario=scenario,
            service_design="SingleSidedDropoff",
            meeting_points_for_request=lambda request: [
                MeetingPoint(id=f"ssd_pu_{request.id}", coords=request.origin)
            ]
            + list(scenario.meeting_points),
            rho_p=0.0,
            rho_d=RHO_D,
            k_top=K_TOP,
            cost_weights=_COST_WEIGHTS,
            max_served_count=self._max_served_count,
        )


class _FixedDoorToDoor(DoorToDoor):
    choice_model = "fixed_accepted_set"
    evidence_family = "algorithm_diagnostic"
    diagnostic_role = "fixed_accepted_set_routing"

    def _solve(self, scenario: Scenario) -> ALNSState:
        vehicles = self._vehicles_dict(scenario)
        state = self._initial_state(scenario)
        for request in scenario.requests:
            pickup_mp = MeetingPoint(id=f"fixed_dtd_pu_{request.id}", coords=request.origin)
            dropoff_mp = MeetingPoint(id=f"fixed_dtd_do_{request.id}", coords=request.destination)
            state.unassigned = [request]
            result_state = greedy_insertion(
                state,
                vehicles,
                [pickup_mp, dropoff_mp],
                rho_p=float("inf"),
                rho_d=float("inf"),
                k_top=1,
                cost_weights=_COST_WEIGHTS,
                travel_speed=TRAVEL_SPEED,
            )
            state.routes = result_state.routes
            state.unassigned = result_state.unassigned
        return state


class _FixedSingleSidedPickup(SingleSidedPickup):
    choice_model = "fixed_accepted_set"
    evidence_family = "algorithm_diagnostic"
    diagnostic_role = "fixed_accepted_set_routing"

    def _solve(self, scenario: Scenario) -> ALNSState:
        vehicles = self._vehicles_dict(scenario)
        state = self._initial_state(scenario)
        all_unassigned = []
        for request in scenario.requests:
            dropoff_mp = MeetingPoint(id=f"fixed_ssp_do_{request.id}", coords=request.destination)
            state.unassigned = [request]
            result_state = greedy_insertion(
                state,
                vehicles,
                list(scenario.meeting_points) + [dropoff_mp],
                rho_p=RHO_P,
                rho_d=float("inf"),
                k_top=K_TOP,
                cost_weights=_COST_WEIGHTS,
                travel_speed=TRAVEL_SPEED,
            )
            state.routes = result_state.routes
            all_unassigned.extend(result_state.unassigned)
        state.unassigned = all_unassigned
        return state


class _FixedSingleSidedDropoff(SingleSidedDropoff):
    choice_model = "fixed_accepted_set"
    evidence_family = "algorithm_diagnostic"
    diagnostic_role = "fixed_accepted_set_routing"

    def _solve(self, scenario: Scenario) -> ALNSState:
        vehicles = self._vehicles_dict(scenario)
        state = self._initial_state(scenario)
        all_unassigned = []
        for request in scenario.requests:
            pickup_mp = MeetingPoint(id=f"fixed_ssd_pu_{request.id}", coords=request.origin)
            state.unassigned = [request]
            result_state = greedy_insertion(
                state,
                vehicles,
                [pickup_mp] + list(scenario.meeting_points),
                rho_p=float("inf"),
                rho_d=RHO_D,
                k_top=K_TOP,
                cost_weights=_COST_WEIGHTS,
                travel_speed=TRAVEL_SPEED,
            )
            state.routes = result_state.routes
            all_unassigned.extend(result_state.unassigned)
        state.unassigned = all_unassigned
        return state


class _FixedBidirectionalRH(FullModel):
    choice_model = "fixed_accepted_set"
    evidence_family = "algorithm_diagnostic"
    diagnostic_role = "fixed_accepted_set_routing"

    def _solve(self, scenario: Scenario) -> ALNSState:
        vehicles = self._vehicles_dict(scenario)
        if not scenario.requests:
            return ALNSState(
                routes={v.id: Route(vehicle_id=v.id, stops=[]) for v in scenario.vehicles},
                unassigned=[],
                cost=0.0,
            )
        rh = RollingHorizon(
            vehicles=vehicles,
            meeting_points=scenario.meeting_points,
            rho_p=RHO_P,
            rho_d=RHO_D,
            k_top=K_TOP,
            H=H_WINDOW,
            delta=DELTA,
            cost_weights=_COST_WEIGHTS,
            travel_speed=TRAVEL_SPEED,
            alns_iterations=50,
            seed=42,
        )
        requests = sorted(scenario.requests, key=lambda request: request.earliest)
        rh.run_simulation(requests, [request.earliest for request in requests])
        assigned_ids = set(rh.completed_request_ids)
        for route in rh.routes.values():
            for stop in route.stops:
                if len(stop) >= 3:
                    assigned_ids.add(stop[2])
        return ALNSState(
            routes=rh.routes,
            unassigned=[request for request in scenario.requests if request.id not in assigned_ids],
            cost=0.0,
            completed_ids=set(rh.completed_request_ids),
            extra_vehicle_km=rh.accumulated_vehicle_km,
            pickup_times=dict(rh.pickup_times),
        )


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


def _selection(
    seeds: Iterable[int] | None = None,
    scales: Iterable[int] | None = None,
) -> ControlSelection:
    seed_list = list(REQUIRED_FORMAL_SEEDS if seeds is None else seeds)
    scale_list = list(FORMAL_SCALES if scales is None else scales)
    invalid_seeds = sorted(set(seed_list) - set(REQUIRED_FORMAL_SEEDS))
    invalid_scales = sorted(set(scale_list) - set(FORMAL_SCALES))
    if invalid_seeds:
        raise ValueError(f"06-03 controls require formal seeds; invalid: {invalid_seeds}")
    if invalid_scales:
        raise ValueError(f"06-03 controls require formal scales; invalid: {invalid_scales}")
    return ControlSelection(
        seeds=seed_list,
        scales=scale_list,
        methods=sorted(FORMAL_MAIN_METHOD_LABELS),
    )


def _package_dir(results_root: str | Path, package_id: str) -> Path:
    return Path(results_root) / package_id


def _n_vehicles(scale: int) -> int:
    return VEHICLE_COUNTS.get(scale, max(1, scale // 10))


def _main_raw(main_results_dir: str | Path) -> pd.DataFrame:
    path = Path(main_results_dir) / "raw_results.csv"
    if not path.exists():
        path = Path(main_results_dir) / "synthetic_results.csv"
    return pd.read_csv(path)


def _utility_logs(main_results_dir: str | Path) -> pd.DataFrame:
    path = Path(main_results_dir) / "utility_logs.csv"
    if not path.exists():
        path = Path(main_results_dir) / "utility_components.csv"
    return pd.read_csv(path)


def _write_common_manifests(
    package_dir: Path,
    package_id: str,
    selection: ControlSelection,
    command: str,
    main_results_dir: str | Path,
    extra_config: dict | None = None,
) -> None:
    created_at = _now()
    seed_manifest = {
        "created_at_utc": created_at,
        "package_id": package_id,
        "selected_seeds": selection.seeds,
        "required_formal_seeds": REQUIRED_FORMAL_SEEDS,
        "seed_policy": "same paired seeds and synthetic demand realizations as 06-02",
    }
    config = {
        "created_at_utc": created_at,
        "phase": "06",
        "plan": "06-03",
        "package_id": package_id,
        "command": command,
        "git_commit_before_run": _git_commit_or_code_hash(),
        "main_results_dir": str(main_results_dir),
        "results_dir": str(package_dir),
        "scale_list": selection.scales,
        "method_list": selection.methods,
        "expected_rows": selection.expected_rows,
        "evidence_family": (
            "supplementary_control"
            if package_id == MATCHED_PACKAGE
            else "algorithm_diagnostic"
        ),
    }
    if extra_config:
        config.update(extra_config)
    _write_json(package_dir / "seed_manifest.json", seed_manifest)
    _write_json(package_dir / "config_manifest.json", config)


def matched_targets_from_main(raw: pd.DataFrame, selection: ControlSelection) -> dict[tuple[int, int], dict]:
    targets: dict[tuple[int, int], dict] = {}
    for seed in selection.seeds:
        for scale in selection.scales:
            cell = raw[
                (pd.to_numeric(raw["seed"], errors="coerce").astype("Int64") == seed)
                & (pd.to_numeric(raw["scale"], errors="coerce").astype("Int64") == scale)
                & (raw["method_label"].isin(selection.methods))
                & (raw["status"] == "completed")
            ]
            counts = {
                method: int(
                    pd.to_numeric(
                        cell[cell["method_label"] == method]["n_served"],
                        errors="coerce",
                    ).iloc[0]
                )
                for method in selection.methods
                if len(cell[cell["method_label"] == method]) == 1
            }
            if len(counts) != len(selection.methods):
                targets[(seed, scale)] = {
                    "status": "blocked",
                    "reason": "06-02 completed main rows missing for target construction",
                    "target_count": 0,
                    "counts": counts,
                    "basis": "blocked_missing_main_rows",
                }
                continue
            min_count = min(counts.values())
            limiting_methods = sorted(
                method for method, count in counts.items() if count == min_count
            )
            targets[(seed, scale)] = {
                "status": "ready",
                "reason": "target is min completed 06-02 served count across comparison methods",
                "target_count": min_count,
                "counts": counts,
                "basis": "min_attainable_served_count_all_methods",
                "limiting_methods": limiting_methods,
            }
    return targets


def _matched_variant(method_label: str, target_count: int, attainable_count: int):
    if method_label == "DoorToDoor_Choice_CommonRouting":
        return _MatchedDoorToDoor(target_count)
    if method_label == "SingleSidedPickup_Choice_CommonRouting":
        return _MatchedSingleSidedPickup(target_count)
    if method_label == "SingleSidedDropoff_Choice_CommonRouting":
        return _MatchedSingleSidedDropoff(target_count)
    if method_label == "BidirectionalMP_Choice_RH_ALNS":
        return FullModel() if target_count == attainable_count else FullModel(
            max_served_count=target_count
        )
    raise ValueError(f"unknown method label: {method_label}")


def _fixed_variant(method_label: str):
    if method_label == "DoorToDoor_Choice_CommonRouting":
        return _FixedDoorToDoor()
    if method_label == "SingleSidedPickup_Choice_CommonRouting":
        return _FixedSingleSidedPickup()
    if method_label == "SingleSidedDropoff_Choice_CommonRouting":
        return _FixedSingleSidedDropoff()
    if method_label == "BidirectionalMP_Choice_RH_ALNS":
        return _FixedBidirectionalRH()
    raise ValueError(f"unknown method label: {method_label}")


def _empty_matched_row(
    package_dir: Path,
    seed: int,
    scale: int,
    method_label: str,
    status: str,
    reason: str,
    target_info: dict,
) -> dict:
    target_count = int(target_info.get("target_count", 0))
    attainable = int(target_info.get("counts", {}).get(method_label, 0))
    return {
        "package_id": MATCHED_PACKAGE,
        "run_id": f"matched_coverage:synthetic_n{scale}_s{seed}:{method_label}",
        "config_id": f"matched_coverage:scale_{scale}:seed_{seed}",
        "seed": seed,
        "scale": scale,
        "scenario": f"synthetic_n{scale}_v{_n_vehicles(scale)}_s{seed}",
        "method_label": method_label,
        "variant": METHOD_LABEL_TO_VARIANT[method_label],
        "service_design": METHOD_LABEL_TO_SERVICE_DESIGN[method_label],
        "choice_model": "binary_logit_with_matched_coverage_cap",
        "reoptimization": METHOD_LABEL_TO_REOPTIMIZATION[method_label],
        "routing_solver": METHOD_LABEL_TO_ROUTING_SOLVER[method_label],
        "evidence_family": "supplementary_control",
        "diagnostic_role": "matched_coverage_control",
        "status": status,
        "detailed_reason": reason,
        "runtime_s": 0.0,
        "error_message": reason if status in {"failed", "timeout", "blocked"} else "",
        "result_schema_version": "phase06.06-03.v1",
        "timestamp_utc": _now(),
        "artifact_dir": str(package_dir.resolve()),
        "git_commit_or_code_hash": _git_commit_or_code_hash(),
        "original_request_count": scale,
        "attainable_served_count": attainable,
        "matched_target_served_count": target_count,
        "target_basis": target_info.get("basis", ""),
        "target_adjusted": attainable != target_count,
        "actual_served_count": 0,
        "served_share": 0.0,
        "coverage_gap_count": -target_count,
        "coverage_gap_abs": target_count,
        "coverage_tolerance_count": MATCHED_COVERAGE_TOLERANCE_COUNT,
        "total_vehicle_km": 0.0,
        "vkm_per_served_trip": 0.0,
        "vkm_per_original_request": 0.0,
        "avg_wait": 0.0,
        "p95_wait": 0.0,
        "avg_walk": 0.0,
        "avg_ivt": 0.0,
        "detour_ratio": 0.0,
        "fairness_index": 0.0,
    }


def _run_with_timeout(variant, scenario: Scenario, timeout_s: int = CONTROL_TIMEOUT_S):
    executor = ThreadPoolExecutor(max_workers=1)
    started = time.perf_counter()
    future = executor.submit(variant.run, scenario)
    try:
        result = future.result(timeout=timeout_s)
        executor.shutdown(wait=True)
        return "completed", result, time.perf_counter() - started, ""
    except TimeoutError:
        future.cancel()
        executor.shutdown(wait=False, cancel_futures=True)
        return "timeout", None, time.perf_counter() - started, f"timeout after {timeout_s}s"
    except Exception as exc:
        executor.shutdown(wait=True)
        return "failed", None, time.perf_counter() - started, "".join(
            traceback.format_exception_only(type(exc), exc)
        ).strip()


def _matched_completed_row(
    package_dir: Path,
    seed: int,
    scale: int,
    method_label: str,
    target_info: dict,
    result,
    runtime_s: float,
) -> dict:
    metrics = compute_metrics(result)
    actual_count = sum(1 for record in result.records if record.status == "served")
    target_count = int(target_info["target_count"])
    attainable = int(target_info["counts"][method_label])
    gap = actual_count - target_count
    passed = abs(gap) <= MATCHED_COVERAGE_TOLERANCE_COUNT
    return {
        "package_id": MATCHED_PACKAGE,
        "run_id": f"matched_coverage:synthetic_n{scale}_s{seed}:{method_label}",
        "config_id": f"matched_coverage:scale_{scale}:seed_{seed}",
        "seed": seed,
        "scale": scale,
        "scenario": f"synthetic_n{scale}_v{_n_vehicles(scale)}_s{seed}",
        "method_label": method_label,
        "variant": METHOD_LABEL_TO_VARIANT[method_label],
        "service_design": METHOD_LABEL_TO_SERVICE_DESIGN[method_label],
        "choice_model": "binary_logit_with_matched_coverage_cap",
        "reoptimization": METHOD_LABEL_TO_REOPTIMIZATION[method_label],
        "routing_solver": METHOD_LABEL_TO_ROUTING_SOLVER[method_label],
        "evidence_family": "supplementary_control",
        "diagnostic_role": "matched_coverage_control",
        "status": "completed" if passed else "failed",
        "detailed_reason": (
            "actual served count equals matched target"
            if passed
            else f"actual served count differs from target by {gap}"
        ),
        "runtime_s": runtime_s,
        "error_message": "" if passed else f"coverage gap count {gap}",
        "result_schema_version": "phase06.06-03.v1",
        "timestamp_utc": _now(),
        "artifact_dir": str(package_dir.resolve()),
        "git_commit_or_code_hash": _git_commit_or_code_hash(),
        "original_request_count": scale,
        "attainable_served_count": attainable,
        "matched_target_served_count": target_count,
        "target_basis": target_info["basis"],
        "target_adjusted": attainable != target_count,
        "actual_served_count": actual_count,
        "served_share": actual_count / scale if scale else 0.0,
        "coverage_gap_count": gap,
        "coverage_gap_abs": abs(gap),
        "coverage_tolerance_count": MATCHED_COVERAGE_TOLERANCE_COUNT,
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


def run_matched_coverage_controls(
    results_root: str | Path = DEFAULT_COVERAGE_ROOT,
    main_results_dir: str | Path = DEFAULT_MAIN_RESULTS_DIR,
    seeds: Iterable[int] | None = None,
    scales: Iterable[int] | None = None,
    command: str = "programmatic",
) -> dict:
    selection = _selection(seeds, scales)
    package_dir = _package_dir(results_root, MATCHED_PACKAGE)
    raw = _main_raw(main_results_dir)
    target_map = matched_targets_from_main(raw, selection)
    _write_common_manifests(
        package_dir,
        MATCHED_PACKAGE,
        selection,
        command,
        main_results_dir,
        extra_config={
            "target_rule": "per seed x scale min completed 06-02 served count across all comparison methods",
            "coverage_tolerance_count": MATCHED_COVERAGE_TOLERANCE_COUNT,
            "pilot_logic_reused_as_evidence": False,
        },
    )

    rows: list[dict] = []
    for scale in selection.scales:
        for seed in selection.seeds:
            scenario = generate_synthetic(scale, _n_vehicles(scale), seed)
            target_info = target_map[(seed, scale)]
            for method_label in selection.methods:
                if target_info["status"] != "ready":
                    rows.append(
                        _empty_matched_row(
                            package_dir,
                            seed,
                            scale,
                            method_label,
                            "blocked",
                            str(target_info["reason"]),
                            target_info,
                        )
                    )
                    continue
                target_count = int(target_info["target_count"])
                attainable = int(target_info["counts"][method_label])
                variant = _matched_variant(method_label, target_count, attainable)
                status, result, runtime_s, error = _run_with_timeout(variant, scenario)
                if status != "completed":
                    rows.append(
                        _empty_matched_row(
                            package_dir,
                            seed,
                            scale,
                            method_label,
                            status,
                            error,
                            target_info,
                        )
                    )
                    rows[-1]["runtime_s"] = runtime_s
                    continue
                rows.append(
                    _matched_completed_row(
                        package_dir,
                        seed,
                        scale,
                        method_label,
                        target_info,
                        result,
                        runtime_s,
                    )
                )

    _write_csv(package_dir / "raw_results.csv", rows, MATCHED_RAW_COLUMNS)
    _write_matched_processed(package_dir, rows)
    report = validate_matched_coverage_outputs(package_dir, selection, write_json=True)
    append_control_failures_to_ledger(package_dir / "raw_results.csv", DEFAULT_RERUN_LEDGER_PATH)
    return report


def _write_matched_processed(package_dir: Path, rows: list[dict]) -> None:
    df = pd.DataFrame(rows)
    if df.empty:
        _write_csv(package_dir / "processed_results.csv", [], ["method_label"])
        return
    numeric = [
        "attainable_served_count",
        "matched_target_served_count",
        "actual_served_count",
        "served_share",
        "coverage_gap_abs",
        "total_vehicle_km",
        "vkm_per_served_trip",
        "vkm_per_original_request",
        "runtime_s",
    ]
    for field in numeric:
        df[field] = pd.to_numeric(df[field], errors="coerce")
    grouped = (
        df.groupby("method_label", dropna=False)
        .agg(
            row_count=("method_label", "size"),
            completed_rows=("status", lambda s: int((s == "completed").sum())),
            failed_rows=("status", lambda s: int((s == "failed").sum())),
            timeout_rows=("status", lambda s: int((s == "timeout").sum())),
            blocked_rows=("status", lambda s: int((s == "blocked").sum())),
            mean_target_served_count=("matched_target_served_count", "mean"),
            mean_actual_served_count=("actual_served_count", "mean"),
            mean_served_share=("served_share", "mean"),
            max_coverage_gap_abs=("coverage_gap_abs", "max"),
            mean_total_vehicle_km=("total_vehicle_km", "mean"),
            mean_vkm_per_served_trip=("vkm_per_served_trip", "mean"),
            mean_vkm_per_original_request=("vkm_per_original_request", "mean"),
            mean_runtime_s=("runtime_s", "mean"),
        )
        .reset_index()
    )
    grouped.to_csv(package_dir / "processed_results.csv", index=False)


def _method_rows(utility: pd.DataFrame, seed: int, scenario: str, method_label: str) -> pd.DataFrame:
    method = METHOD_LABEL_TO_VARIANT[method_label]
    return utility[
        (pd.to_numeric(utility["seed"], errors="coerce").astype("Int64") == seed)
        & (utility["scenario"] == scenario)
        & (utility["method"] == method)
    ]


def _intersect_request_ids(utility: pd.DataFrame, seed: int, scenario: str, method_labels: list[str], statuses: set[str]) -> set[str]:
    sets = []
    for method_label in method_labels:
        rows = _method_rows(utility, seed, scenario, method_label)
        sets.append(set(rows[rows["status"].isin(statuses)]["request_id"]))
    if not sets:
        return set()
    return set.intersection(*sets)


def _common_candidate_serviceable_request_ids(
    utility: pd.DataFrame,
    seed: int,
    scenario: str,
    method_labels: list[str],
) -> set[str]:
    sets = []
    for method_label in method_labels:
        rows = _method_rows(utility, seed, scenario, method_label)
        if "detailed_reason" not in rows.columns:
            return set()
        serviceable = rows[rows["detailed_reason"] != "no_candidate_mp"]
        sets.append(set(serviceable["request_id"]))
    if not sets:
        return set()
    return set.intersection(*sets)


def fixed_set_for_cell(
    utility: pd.DataFrame,
    seed: int,
    scale: int,
    method_labels: list[str],
) -> dict:
    scenario = f"synthetic_n{scale}_v{_n_vehicles(scale)}_s{seed}"
    served_ids = _intersect_request_ids(utility, seed, scenario, method_labels, {"served"})
    serviceable_ids = _intersect_request_ids(
        utility,
        seed,
        scenario,
        method_labels,
        {"served", "choice_rejected"},
    )
    candidate_ids = _common_candidate_serviceable_request_ids(
        utility,
        seed,
        scenario,
        method_labels,
    )
    if served_ids:
        retained = served_ids
        rule = "common_served"
        fallback = False
    elif serviceable_ids:
        retained = serviceable_ids
        rule = "common_actual_offer_serviceable"
        fallback = False
    elif candidate_ids:
        retained = candidate_ids
        rule = "common_candidate_serviceable"
        fallback = True
    else:
        retained = set()
        rule = "empty_intersection"
        fallback = False
    retained_sorted = sorted(retained)
    digest = hashlib.sha256("\n".join(retained_sorted).encode("utf-8")).hexdigest()
    return {
        "scenario": scenario,
        "retained_request_ids": retained_sorted,
        "retained_set_hash": digest,
        "construction_rule": rule,
        "fallback_used": fallback,
        "served_intersection_count": len(served_ids),
        "serviceable_intersection_count": len(serviceable_ids),
        "candidate_serviceable_intersection_count": len(candidate_ids),
    }


def _fixed_scenario(scale: int, seed: int, retained_ids: list[str]) -> Scenario:
    scenario = generate_synthetic(scale, _n_vehicles(scale), seed)
    retained = set(retained_ids)
    return Scenario(
        requests=[request for request in scenario.requests if request.id in retained],
        vehicles=scenario.vehicles,
        meeting_points=scenario.meeting_points,
        area_km=scenario.area_km,
        name=f"{scenario.name}_fixed_accepted_set",
    )


def _empty_fixed_row(
    package_dir: Path,
    seed: int,
    scale: int,
    method_label: str,
    fixed_set: dict,
    status: str,
    reason: str,
) -> dict:
    retained = int(len(fixed_set["retained_request_ids"]))
    return {
        "package_id": FIXED_PACKAGE,
        "run_id": f"fixed_accepted_set:synthetic_n{scale}_s{seed}:{method_label}",
        "config_id": f"fixed_accepted_set:scale_{scale}:seed_{seed}",
        "seed": seed,
        "scale": scale,
        "scenario": fixed_set["scenario"],
        "method_label": method_label,
        "variant": METHOD_LABEL_TO_VARIANT[method_label],
        "service_design": METHOD_LABEL_TO_SERVICE_DESIGN[method_label],
        "choice_model": "fixed_accepted_set",
        "reoptimization": METHOD_LABEL_TO_REOPTIMIZATION[method_label],
        "routing_solver": METHOD_LABEL_TO_ROUTING_SOLVER[method_label],
        "evidence_family": "algorithm_diagnostic",
        "evidence_role": "diagnostic_only",
        "diagnostic_role": "fixed_accepted_set_routing",
        "status": status,
        "detailed_reason": reason,
        "runtime_s": 0.0,
        "error_message": reason if status in {"failed", "timeout", "blocked"} else "",
        "result_schema_version": "phase06.06-03.v1",
        "timestamp_utc": _now(),
        "artifact_dir": str(package_dir.resolve()),
        "git_commit_or_code_hash": _git_commit_or_code_hash(),
        "construction_rule": fixed_set["construction_rule"],
        "fallback_used": fixed_set["fallback_used"],
        "retained_set_hash": fixed_set["retained_set_hash"],
        "served_intersection_count": fixed_set["served_intersection_count"],
        "serviceable_intersection_count": fixed_set["serviceable_intersection_count"],
        "candidate_serviceable_intersection_count": fixed_set[
            "candidate_serviceable_intersection_count"
        ],
        "retained_request_count": retained,
        "retained_share": retained / scale if scale else 0.0,
        "deterministic_inserted_share": 0.0,
        "served_count": 0,
        "unserved_accepted_count": retained,
        "original_request_count": scale,
        "total_vehicle_km": 0.0,
        "vkm_per_inserted_request": 0.0,
        "vkm_per_served_request": 0.0,
        "vkm_per_original_request": 0.0,
        "avg_wait": 0.0,
        "p95_wait": 0.0,
        "avg_walk": 0.0,
        "avg_ivt": 0.0,
        "detour_ratio": 0.0,
        "fairness_index": 0.0,
    }


def _fixed_completed_row(
    package_dir: Path,
    seed: int,
    scale: int,
    method_label: str,
    fixed_set: dict,
    result,
    runtime_s: float,
) -> dict:
    metrics = compute_metrics(result)
    retained = int(len(fixed_set["retained_request_ids"]))
    served = sum(1 for record in result.records if record.status == "served")
    unserved = max(0, retained - served)
    inserted_share = served / retained if retained else 0.0
    return {
        **_empty_fixed_row(
            package_dir,
            seed,
            scale,
            method_label,
            fixed_set,
            "completed",
            "fixed accepted-set deterministic routing completed",
        ),
        "runtime_s": runtime_s,
        "deterministic_inserted_share": inserted_share,
        "served_count": served,
        "unserved_accepted_count": unserved,
        "total_vehicle_km": metrics.vehicle_km,
        "vkm_per_inserted_request": metrics.vehicle_km / served if served else 0.0,
        "vkm_per_served_request": metrics.vehicle_km / served if served else 0.0,
        "vkm_per_original_request": metrics.vehicle_km / scale if scale else 0.0,
        "avg_wait": metrics.avg_wait,
        "p95_wait": metrics.p95_wait,
        "avg_walk": metrics.avg_walk,
        "avg_ivt": metrics.avg_ivt,
        "detour_ratio": metrics.detour_ratio,
        "fairness_index": metrics.fairness_index,
    }


def run_fixed_accepted_set_controls(
    results_root: str | Path = DEFAULT_COVERAGE_ROOT,
    main_results_dir: str | Path = DEFAULT_MAIN_RESULTS_DIR,
    seeds: Iterable[int] | None = None,
    scales: Iterable[int] | None = None,
    command: str = "programmatic",
) -> dict:
    selection = _selection(seeds, scales)
    package_dir = _package_dir(results_root, FIXED_PACKAGE)
    utility = _utility_logs(main_results_dir)
    _write_common_manifests(
        package_dir,
        FIXED_PACKAGE,
        selection,
        command,
        main_results_dir,
        extra_config={
            "construction_rule": "common_served, then common_actual_offer_serviceable, then documented common_candidate_serviceable fallback",
            "interpretation": "routing diagnostic only; not behavioral main evidence",
        },
    )

    fixed_sets: list[dict] = []
    rows: list[dict] = []
    for scale in selection.scales:
        for seed in selection.seeds:
            fixed_set = fixed_set_for_cell(utility, seed, scale, selection.methods)
            fixed_sets.append(
                {
                    key: value
                    for key, value in fixed_set.items()
                    if key != "retained_request_ids"
                }
                | {
                    "seed": seed,
                    "scale": scale,
                    "retained_request_count": len(fixed_set["retained_request_ids"]),
                    "retained_share": len(fixed_set["retained_request_ids"]) / scale if scale else 0.0,
                }
            )
            for method_label in selection.methods:
                if not fixed_set["retained_request_ids"]:
                    rows.append(
                        _empty_fixed_row(
                            package_dir,
                            seed,
                            scale,
                            method_label,
                            fixed_set,
                            "blocked",
                            "common accepted/serviceable request intersection is empty",
                        )
                    )
                    continue
                scenario = _fixed_scenario(scale, seed, fixed_set["retained_request_ids"])
                variant = _fixed_variant(method_label)
                status, result, runtime_s, error = _run_with_timeout(variant, scenario)
                if status != "completed":
                    rows.append(
                        _empty_fixed_row(
                            package_dir,
                            seed,
                            scale,
                            method_label,
                            fixed_set,
                            status,
                            error,
                        )
                    )
                    rows[-1]["runtime_s"] = runtime_s
                    continue
                rows.append(
                    _fixed_completed_row(
                        package_dir,
                        seed,
                        scale,
                        method_label,
                        fixed_set,
                        result,
                        runtime_s,
                    )
                )

    _write_csv(package_dir / "raw_results.csv", rows, FIXED_RAW_COLUMNS)
    _write_fixed_processed(package_dir, rows)
    _write_json(
        package_dir / "retained_set_manifest.json",
        {
            "package_id": FIXED_PACKAGE,
            "created_at_utc": _now(),
            "sets": fixed_sets,
        },
    )
    report = validate_fixed_accepted_set_outputs(package_dir, selection, write_json=True)
    append_control_failures_to_ledger(package_dir / "raw_results.csv", DEFAULT_RERUN_LEDGER_PATH)
    return report


def _write_fixed_processed(package_dir: Path, rows: list[dict]) -> None:
    df = pd.DataFrame(rows)
    if df.empty:
        _write_csv(package_dir / "processed_results.csv", [], ["method_label"])
        return
    numeric = [
        "retained_request_count",
        "retained_share",
        "deterministic_inserted_share",
        "served_count",
        "unserved_accepted_count",
        "total_vehicle_km",
        "vkm_per_inserted_request",
        "vkm_per_served_request",
        "vkm_per_original_request",
        "runtime_s",
    ]
    for field in numeric:
        df[field] = pd.to_numeric(df[field], errors="coerce")
    grouped = (
        df.groupby("method_label", dropna=False)
        .agg(
            row_count=("method_label", "size"),
            completed_rows=("status", lambda s: int((s == "completed").sum())),
            failed_rows=("status", lambda s: int((s == "failed").sum())),
            timeout_rows=("status", lambda s: int((s == "timeout").sum())),
            blocked_rows=("status", lambda s: int((s == "blocked").sum())),
            fallback_rows=("fallback_used", lambda s: int(sum(bool(v) for v in s))),
            mean_retained_request_count=("retained_request_count", "mean"),
            mean_retained_share=("retained_share", "mean"),
            mean_deterministic_inserted_share=("deterministic_inserted_share", "mean"),
            mean_served_count=("served_count", "mean"),
            mean_unserved_accepted_count=("unserved_accepted_count", "mean"),
            mean_total_vehicle_km=("total_vehicle_km", "mean"),
            mean_vkm_per_served_request=("vkm_per_served_request", "mean"),
            mean_vkm_per_original_request=("vkm_per_original_request", "mean"),
            mean_runtime_s=("runtime_s", "mean"),
        )
        .reset_index()
    )
    grouped.to_csv(package_dir / "processed_results.csv", index=False)


def _validation_base(package_dir: Path, package_id: str) -> dict:
    return {
        "package_id": package_id,
        "results_dir": str(package_dir),
        "passed": True,
        "schema_drift": False,
        "denominator_checks": {},
        "errors": [],
        "warnings": [],
        "row_counts": {},
        "checked_files": [],
    }


def _check_required_files(report: dict, package_dir: Path, files: list[str]) -> bool:
    ok = True
    for name in files:
        path = package_dir / name
        if path.exists():
            report["checked_files"].append(str(path))
        else:
            ok = False
            report["errors"].append(f"missing required file: {path}")
    return ok


def _check_columns(report: dict, df: pd.DataFrame, required: list[str], label: str) -> None:
    missing = sorted(set(required) - set(df.columns))
    if missing:
        report["schema_drift"] = True
        report["errors"].append(f"{label} missing required columns: {', '.join(missing)}")


def _finite_numeric(series: pd.Series) -> pd.Series:
    values = pd.to_numeric(series, errors="coerce")
    return values.map(lambda value: math.isfinite(value) if pd.notna(value) else False)


def _validate_expected_grid(report: dict, df: pd.DataFrame, selection: ControlSelection) -> None:
    expected = {
        (seed, scale, method)
        for seed in selection.seeds
        for scale in selection.scales
        for method in selection.methods
    }
    observed = {
        (int(row.seed), int(row.scale), row.method_label)
        for row in df[["seed", "scale", "method_label"]].itertuples(index=False)
    }
    missing = sorted(expected - observed)
    extra = sorted(observed - expected)
    if missing:
        report["errors"].append(f"missing control rows: {len(missing)}")
    if extra:
        report["errors"].append(f"unexpected control rows: {len(extra)}")
    duplicates = df.groupby(["seed", "scale", "method_label"]).size()
    duplicate_keys = duplicates[duplicates > 1]
    if not duplicate_keys.empty:
        report["errors"].append(f"duplicate control rows: {len(duplicate_keys)}")


def validate_matched_coverage_outputs(
    package_dir: str | Path,
    selection: ControlSelection | None = None,
    write_json: bool = True,
) -> dict:
    package_dir = Path(package_dir)
    selection = selection or _selection()
    report = _validation_base(package_dir, MATCHED_PACKAGE)
    if not _check_required_files(
        report,
        package_dir,
        [
            "raw_results.csv",
            "processed_results.csv",
            "config_manifest.json",
            "seed_manifest.json",
        ],
    ):
        report["passed"] = False
        _write_validation(package_dir, report, write_json)
        return report

    raw = pd.read_csv(package_dir / "raw_results.csv")
    processed = pd.read_csv(package_dir / "processed_results.csv")
    report["row_counts"] = {
        "expected_rows": selection.expected_rows,
        "actual_rows": int(len(raw)),
        "processed_rows": int(len(processed)),
        "completed_rows": int((raw["status"] == "completed").sum()),
        "failed_rows": int((raw["status"] == "failed").sum()),
        "timeout_rows": int((raw["status"] == "timeout").sum()),
        "blocked_rows": int((raw["status"] == "blocked").sum()),
    }
    _check_columns(report, raw, MATCHED_RAW_COLUMNS, "matched raw_results.csv")
    _validate_expected_grid(report, raw, selection)
    if len(raw) != selection.expected_rows:
        report["errors"].append(
            f"matched raw row count {len(raw)} != expected {selection.expected_rows}"
        )
    if set(raw["evidence_family"]) != {"supplementary_control"}:
        report["errors"].append("matched rows must be supplementary_control only")
    if not _finite_numeric(raw["total_vehicle_km"]).all():
        report["errors"].append("matched total_vehicle_km contains non-finite values")

    completed = raw[raw["status"] == "completed"].copy()
    if completed.empty:
        report["denominator_checks"] = {"status": "skipped_no_completed_rows"}
    else:
        original = pd.to_numeric(completed["original_request_count"], errors="coerce")
        actual = pd.to_numeric(completed["actual_served_count"], errors="coerce")
        target = pd.to_numeric(completed["matched_target_served_count"], errors="coerce")
        vehicle_km = pd.to_numeric(completed["total_vehicle_km"], errors="coerce")
        served_share = pd.to_numeric(completed["served_share"], errors="coerce")
        vkm_served = pd.to_numeric(completed["vkm_per_served_trip"], errors="coerce")
        vkm_original = pd.to_numeric(completed["vkm_per_original_request"], errors="coerce")
        gap_abs = pd.to_numeric(completed["coverage_gap_abs"], errors="coerce")
        checks = {
            "served_share": ((actual / original).fillna(0.0) - served_share).abs() <= 1e-6,
            "vkm_per_original_request": ((vehicle_km / original).fillna(0.0) - vkm_original).abs() <= 1e-6,
            "vkm_per_served_trip": (
                (vehicle_km / actual.where(actual > 0)).fillna(0.0) - vkm_served
            ).abs() <= 1e-6,
            "coverage_gap": ((actual - target).abs() - gap_abs).abs() <= 1e-6,
            "coverage_tolerance": gap_abs <= MATCHED_COVERAGE_TOLERANCE_COUNT,
        }
        report["denominator_checks"] = {
            name: "passed" if bool(mask.all()) else "failed"
            for name, mask in checks.items()
        }
        for name, mask in checks.items():
            if not bool(mask.all()):
                report["errors"].append(
                    f"matched denominator check failed for {name}: {int((~mask).sum())} rows"
                )
    report["passed"] = not report["errors"]
    _write_validation(package_dir, report, write_json)
    return report


def validate_fixed_accepted_set_outputs(
    package_dir: str | Path,
    selection: ControlSelection | None = None,
    write_json: bool = True,
) -> dict:
    package_dir = Path(package_dir)
    selection = selection or _selection()
    report = _validation_base(package_dir, FIXED_PACKAGE)
    if not _check_required_files(
        report,
        package_dir,
        [
            "raw_results.csv",
            "processed_results.csv",
            "config_manifest.json",
            "seed_manifest.json",
        ],
    ):
        report["passed"] = False
        _write_validation(package_dir, report, write_json)
        return report

    raw = pd.read_csv(package_dir / "raw_results.csv")
    processed = pd.read_csv(package_dir / "processed_results.csv")
    report["row_counts"] = {
        "expected_rows": selection.expected_rows,
        "actual_rows": int(len(raw)),
        "processed_rows": int(len(processed)),
        "completed_rows": int((raw["status"] == "completed").sum()),
        "failed_rows": int((raw["status"] == "failed").sum()),
        "timeout_rows": int((raw["status"] == "timeout").sum()),
        "blocked_rows": int((raw["status"] == "blocked").sum()),
        "fallback_rows": int(raw["fallback_used"].astype(str).str.lower().isin({"true", "1"}).sum()),
    }
    _check_columns(report, raw, FIXED_RAW_COLUMNS, "fixed raw_results.csv")
    _validate_expected_grid(report, raw, selection)
    if len(raw) != selection.expected_rows:
        report["errors"].append(
            f"fixed raw row count {len(raw)} != expected {selection.expected_rows}"
        )
    if set(raw["evidence_role"]) != {"diagnostic_only"}:
        report["errors"].append("fixed accepted-set rows must be diagnostic_only")

    completed = raw[raw["status"] == "completed"].copy()
    if completed.empty:
        report["denominator_checks"] = {"status": "skipped_no_completed_rows"}
    else:
        retained = pd.to_numeric(completed["retained_request_count"], errors="coerce")
        served = pd.to_numeric(completed["served_count"], errors="coerce")
        unserved = pd.to_numeric(completed["unserved_accepted_count"], errors="coerce")
        original = pd.to_numeric(completed["original_request_count"], errors="coerce")
        vehicle_km = pd.to_numeric(completed["total_vehicle_km"], errors="coerce")
        inserted_share = pd.to_numeric(completed["deterministic_inserted_share"], errors="coerce")
        vkm_served = pd.to_numeric(completed["vkm_per_served_request"], errors="coerce")
        vkm_original = pd.to_numeric(completed["vkm_per_original_request"], errors="coerce")
        checks = {
            "deterministic_inserted_share": ((served / retained).fillna(0.0) - inserted_share).abs() <= 1e-6,
            "unserved_accepted_count": (retained - served - unserved).abs() <= 1e-6,
            "vkm_per_served_request": (
                (vehicle_km / served.where(served > 0)).fillna(0.0) - vkm_served
            ).abs() <= 1e-6,
            "vkm_per_original_request": ((vehicle_km / original).fillna(0.0) - vkm_original).abs() <= 1e-6,
        }
        report["denominator_checks"] = {
            name: "passed" if bool(mask.all()) else "failed"
            for name, mask in checks.items()
        }
        for name, mask in checks.items():
            if not bool(mask.all()):
                report["errors"].append(
                    f"fixed denominator check failed for {name}: {int((~mask).sum())} rows"
                )
    report["passed"] = not report["errors"]
    _write_validation(package_dir, report, write_json)
    return report


def _write_validation(package_dir: Path, report: dict, write_json: bool) -> None:
    if write_json:
        _write_json(package_dir / "validation_report.json", report)


def validate_all(
    results_root: str | Path = DEFAULT_COVERAGE_ROOT,
    seeds: Iterable[int] | None = None,
    scales: Iterable[int] | None = None,
) -> dict:
    selection = _selection(seeds, scales)
    matched = validate_matched_coverage_outputs(
        _package_dir(results_root, MATCHED_PACKAGE),
        selection,
        write_json=True,
    )
    fixed = validate_fixed_accepted_set_outputs(
        _package_dir(results_root, FIXED_PACKAGE),
        selection,
        write_json=True,
    )
    return {
        "passed": bool(matched["passed"] and fixed["passed"]),
        "matched_coverage": matched,
        "fixed_accepted_set": fixed,
    }


def append_control_failures_to_ledger(raw_path: str | Path, ledger_path: str | Path) -> None:
    from experiments.formal_validation import RERUN_LEDGER_COLUMNS, ensure_rerun_ledger

    raw_path = Path(raw_path)
    if not raw_path.exists():
        return
    ledger_path = ensure_rerun_ledger(ledger_path)
    existing: set[tuple[str, str, str]] = set()
    with ledger_path.open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            existing.add((row.get("run_id", ""), row.get("config_id", ""), row.get("status", "")))
    rows = []
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
        with ledger_path.open("a", newline="", encoding="utf-8") as handle:
            writer = csv.DictWriter(handle, fieldnames=RERUN_LEDGER_COLUMNS)
            writer.writerows(rows)


def _metric_summary(df: pd.DataFrame, fields: list[str]) -> dict:
    summary = {}
    for field in fields:
        values = pd.to_numeric(df[field], errors="coerce")
        summary[field] = {
            "mean": float(values.mean()) if len(values) else 0.0,
            "min": float(values.min()) if len(values) else 0.0,
            "max": float(values.max()) if len(values) else 0.0,
        }
    return summary


def _paired_differences(df: pd.DataFrame, value_field: str) -> pd.DataFrame:
    completed = df[df["status"] == "completed"].copy()
    pivot = completed.pivot_table(
        index=["seed", "scale"],
        columns="method_label",
        values=value_field,
        aggfunc="first",
    )
    full = pivot.get("BidirectionalMP_Choice_RH_ALNS")
    rows = []
    if full is None:
        return pd.DataFrame(rows)
    for baseline in [
        "DoorToDoor_Choice_CommonRouting",
        "SingleSidedPickup_Choice_CommonRouting",
        "SingleSidedDropoff_Choice_CommonRouting",
    ]:
        if baseline not in pivot:
            continue
        diff = full - pivot[baseline]
        rows.append(
            {
                "metric": value_field,
                "baseline": baseline,
                "mean_full_minus_baseline": float(diff.mean()),
                "min_full_minus_baseline": float(diff.min()),
                "max_full_minus_baseline": float(diff.max()),
                "full_better_share": float((diff < 0).mean()),
            }
        )
    return pd.DataFrame(rows)


def _markdown_table(df: pd.DataFrame) -> str:
    if df.empty:
        return "No complete paired differences available."
    columns = list(df.columns)
    lines = [
        "| " + " | ".join(columns) + " |",
        "| " + " | ".join("---" for _ in columns) + " |",
    ]
    for _, row in df.iterrows():
        values = []
        for column in columns:
            value = row[column]
            if isinstance(value, float):
                values.append(f"{value:.6g}")
            else:
                values.append(str(value))
        lines.append("| " + " | ".join(values) + " |")
    return "\n".join(lines)


def _advantage_text(served_diff: pd.DataFrame, original_diff: pd.DataFrame) -> str:
    served = (
        "yes"
        if not served_diff.empty
        and bool((served_diff["mean_full_minus_baseline"] < 0).all())
        else "no_or_mixed"
    )
    original = (
        "yes"
        if not original_diff.empty
        and bool((original_diff["mean_full_minus_baseline"] < 0).all())
        else "no_or_mixed"
    )
    return f"vkm_per_served: {served}; vkm_per_original: {original}"


def write_summary(
    results_root: str | Path = DEFAULT_COVERAGE_ROOT,
    main_results_dir: str | Path = DEFAULT_MAIN_RESULTS_DIR,
    output_path: str | Path = Path(".planning/phases/06-formal-synthetic-experiments/06-03-SUMMARY.md"),
    commands_run: list[str] | None = None,
) -> Path:
    results_root = Path(results_root)
    output_path = Path(output_path)
    matched_dir = _package_dir(results_root, MATCHED_PACKAGE)
    fixed_dir = _package_dir(results_root, FIXED_PACKAGE)
    matched = pd.read_csv(matched_dir / "raw_results.csv")
    fixed = pd.read_csv(fixed_dir / "raw_results.csv")
    matched_report = json.loads((matched_dir / "validation_report.json").read_text(encoding="utf-8"))
    fixed_report = json.loads((fixed_dir / "validation_report.json").read_text(encoding="utf-8"))
    selection = _selection()

    fallback_count = int(
        fixed.drop_duplicates(["seed", "scale"])["fallback_used"]
        .astype(str)
        .str.lower()
        .isin({"true", "1"})
        .sum()
    )
    matched_counts = matched["status"].value_counts().to_dict()
    fixed_counts = fixed["status"].value_counts().to_dict()
    matched_diff_vkm_served = _paired_differences(matched, "vkm_per_served_trip")
    matched_diff_vkm_original = _paired_differences(matched, "vkm_per_original_request")
    fixed_diff_vkm_served = _paired_differences(fixed, "vkm_per_served_request")
    fixed_diff_vkm_original = _paired_differences(fixed, "vkm_per_original_request")

    matched_advantage = _advantage_text(
        matched_diff_vkm_served,
        matched_diff_vkm_original,
    )
    fixed_advantage = _advantage_text(
        fixed_diff_vkm_served,
        fixed_diff_vkm_original,
    )
    passed = bool(matched_report["passed"] and fixed_report["passed"])
    next_step = "Phase 6 Plan 06-04 ready" if passed else "Phase 6 Plan 06-03 blocked repair"

    commands = commands_run or [
        "python -m experiments.phase06_coverage_controls --package all",
        "python -m experiments.phase06_coverage_controls --validate --package all",
    ]
    git_before = subprocess.check_output(
        ["git", "rev-parse", "--short", "HEAD"],
        text=True,
    ).strip()

    content = f"""# Phase 6 Plan 06-03 Summary: Coverage-Confounding Formal Controls

## 1. Task Purpose

Run formal coverage-confounding controls after the 06-02 main behavioral matrix to test whether the observed FullModel vehicle-km advantage survives comparable served-count and fixed accepted-set comparisons.

## 2. Why This Control Is Necessary

The 06-02 main behavioral matrix completed, but FullModel also had lower served share than DoorToDoor and the single-sided baselines. That means lower vehicle-km and lower vkm denominators can be coverage-confounded. 06-03 therefore isolates matched coverage and fixed accepted-set routing before any final manuscript claim is allowed.

## 3. Commands Run

{chr(10).join(f'- `{command}`' for command in commands)}

## 4. Git Commit Before Run

`{git_before}`

## 5. Seed List

{selection.seeds}

## 6. Scale List

{selection.scales}

## 7. Method List

{selection.methods}

## 8. Matched-Coverage Construction Rule

For each seed x scale cell, the target served count is the minimum completed 06-02 served count across all four comparison methods. Each method is rerun on the same formal synthetic demand realization with a deterministic served-count cap. Rows record the attainable count, matched target, actual served count, served share, coverage gap, total vehicle-km, vkm/served, and vkm/original.

## 9. Fixed Accepted-Set Construction Rule

For each seed x scale cell, retained requests are selected by common served intersection first, common actual-offer serviceable intersection second, and the Phase 5 `common_candidate_serviceable` fallback only when both strict intersections are empty. The same retained set is routed for every method under diagnostic-only deterministic routing.

## 10. Fallback Rule And Fallback Count

Fallback rule: use `common_candidate_serviceable` only when `common_served` and `common_actual_offer_serviceable` are empty. Fallback seed x scale cells: {fallback_count}.

## 11. Expected Rows

- Matched coverage: {selection.expected_rows}
- Fixed accepted set: {selection.expected_rows}

## 12. Actual Rows

- Matched coverage: {len(matched)}
- Fixed accepted set: {len(fixed)}

## 13. Completed / Failed / Timeout / Blocked Row Counts

- Matched coverage: completed={matched_counts.get('completed', 0)}, failed={matched_counts.get('failed', 0)}, timeout={matched_counts.get('timeout', 0)}, blocked={matched_counts.get('blocked', 0)}
- Fixed accepted set: completed={fixed_counts.get('completed', 0)}, failed={fixed_counts.get('failed', 0)}, timeout={fixed_counts.get('timeout', 0)}, blocked={fixed_counts.get('blocked', 0)}

## 14. Method x Seed x Scale Completeness

- Matched coverage validator row count: {matched_report['row_counts']}
- Fixed accepted-set validator row count: {fixed_report['row_counts']}

## 15. Schema Validation

- Matched coverage schema_drift: {matched_report['schema_drift']}
- Fixed accepted set schema_drift: {fixed_report['schema_drift']}

## 16. Denominator Validation

- Matched coverage: {matched_report['denominator_checks']}
- Fixed accepted set: {fixed_report['denominator_checks']}

## 17. Matched Target Served Count Summary

{json.dumps(_metric_summary(matched, ['matched_target_served_count']), indent=2)}

## 18. Actual Served Count Summary

{json.dumps(_metric_summary(matched, ['actual_served_count']), indent=2)}

## 19. Coverage Gap Summary

{json.dumps(_metric_summary(matched, ['coverage_gap_abs']), indent=2)}

## 20. Vehicle-Km Summary

Matched coverage:

{json.dumps(_metric_summary(matched, ['total_vehicle_km', 'vkm_per_served_trip', 'vkm_per_original_request']), indent=2)}

Fixed accepted set:

{json.dumps(_metric_summary(fixed, ['total_vehicle_km', 'vkm_per_served_request', 'vkm_per_original_request']), indent=2)}

## 21. Paired Differences Versus Baselines

Matched coverage vkm/served:

{_markdown_table(matched_diff_vkm_served)}

Matched coverage vkm/original:

{_markdown_table(matched_diff_vkm_original)}

Fixed accepted set vkm/served:

{_markdown_table(fixed_diff_vkm_served)}

Fixed accepted set vkm/original:

{_markdown_table(fixed_diff_vkm_original)}

## 22. Whether FullModel Advantage Persists Under Matched Coverage

{matched_advantage}

## 23. Whether FullModel Advantage Persists Under Fixed Accepted Set

{fixed_advantage}

## 24. Whether 06-03 Passed Or Blocked

{"passed" if passed else "blocked"}

## 25. Exact Blockers If Blocked

Matched coverage errors: {matched_report['errors']}

Fixed accepted-set errors: {fixed_report['errors']}

## 26. Whether Phase 6 Can Proceed To 06-04

{next_step}. Do not enter 06-04 automatically.
"""
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(content, encoding="utf-8")
    return output_path


def _parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--package", choices=[*PACKAGE_NAMES, "all"], default="all")
    parser.add_argument("--results-root", default=str(DEFAULT_COVERAGE_ROOT))
    parser.add_argument("--main-results-dir", default=str(DEFAULT_MAIN_RESULTS_DIR))
    parser.add_argument("--seeds", nargs="*", type=int)
    parser.add_argument("--scales", nargs="*", type=int)
    parser.add_argument("--validate", action="store_true")
    parser.add_argument("--write-summary", action="store_true")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = _parse_args(argv)
    command = "python -m experiments.phase06_coverage_controls " + " ".join(sys.argv[1:])
    if args.validate:
        if args.package == MATCHED_PACKAGE:
            result = validate_matched_coverage_outputs(
                _package_dir(args.results_root, MATCHED_PACKAGE),
                _selection(args.seeds, args.scales),
                write_json=True,
            )
        elif args.package == FIXED_PACKAGE:
            result = validate_fixed_accepted_set_outputs(
                _package_dir(args.results_root, FIXED_PACKAGE),
                _selection(args.seeds, args.scales),
                write_json=True,
            )
        else:
            result = validate_all(args.results_root, args.seeds, args.scales)
        if args.write_summary:
            write_summary(
                args.results_root,
                args.main_results_dir,
                commands_run=[command],
            )
        print(json.dumps(result, indent=2, sort_keys=True))
        return 0 if result["passed"] else 1

    if args.package in {MATCHED_PACKAGE, "all"}:
        run_matched_coverage_controls(
            args.results_root,
            args.main_results_dir,
            args.seeds,
            args.scales,
            command=command,
        )
    if args.package in {FIXED_PACKAGE, "all"}:
        run_fixed_accepted_set_controls(
            args.results_root,
            args.main_results_dir,
            args.seeds,
            args.scales,
            command=command,
        )
    if args.write_summary:
        write_summary(args.results_root, args.main_results_dir, commands_run=[command])
    result = validate_all(args.results_root, args.seeds, args.scales)
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if result["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
