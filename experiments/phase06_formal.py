"""Phase 6 formal synthetic experiment harness.

This module keeps formal outputs isolated from pilot and legacy result files,
predeclares the required main matrix, and exposes a small CLI for manifest
creation, smoke runs, and persisted-artifact validation.
"""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
from contextlib import contextmanager
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable

import experiments.runner as runner_module
from experiments.variants import ALL_VARIANTS

REQUIRED_FORMAL_SEEDS = list(range(1, 21))
OPTIONAL_EXTENSION_SEEDS = list(range(21, 31))
FORMAL_SCALES = [100, 200, 300, 500]
FORMAL_MAIN_METHOD_LABELS = {
    "DoorToDoor_Choice_CommonRouting",
    "SingleSidedPickup_Choice_CommonRouting",
    "SingleSidedDropoff_Choice_CommonRouting",
    "BidirectionalMP_Choice_RH_ALNS",
}

DEFAULT_PHASE06_ROOT = Path("results/formal/phase06")
DEFAULT_MAIN_RESULTS_DIR = DEFAULT_PHASE06_ROOT / "main_behavioral"
DEFAULT_RERUN_LEDGER_PATH = (
    Path(".planning/phases/06-formal-synthetic-experiments")
    / "06_FAILURE_RERUN_LEDGER.csv"
)

ARTIFACT_ALIASES = {
    "synthetic_results.csv": "raw_results.csv",
    "metrics_table.csv": "processed_results.csv",
    "utility_components.csv": "utility_logs.csv",
    "formal_seed_manifest.json": "seed_manifest.json",
    "formal_config_manifest.json": "config_manifest.json",
    "formal_run_manifest.json": "run_manifest.json",
    "main_matrix_validation.json": "validation_report.json",
}


def _as_int_list(values: Iterable[int] | None, default: list[int]) -> list[int]:
    return list(default if values is None else values)


def _validate_formal_scales(scales: Iterable[int]) -> list[int]:
    selected = list(scales)
    invalid = sorted(set(selected) - set(FORMAL_SCALES))
    if invalid:
        raise ValueError(
            "Phase 6 formal main scales must be drawn from "
            f"{FORMAL_SCALES}; got invalid scales {invalid}"
        )
    return selected


def selected_formal_seeds(
    seeds: Iterable[int] | None = None,
    include_optional_extension: bool = False,
) -> list[int]:
    """Return predeclared formal seed IDs for required or extension runs."""
    if seeds is not None:
        selected = list(seeds)
    else:
        selected = list(REQUIRED_FORMAL_SEEDS)
        if include_optional_extension:
            selected.extend(OPTIONAL_EXTENSION_SEEDS)

    allowed = set(REQUIRED_FORMAL_SEEDS) | set(OPTIONAL_EXTENSION_SEEDS)
    invalid = sorted(set(selected) - allowed)
    if invalid:
        raise ValueError(
            "Phase 6 formal seeds must be predeclared required or optional "
            f"extension seeds; got invalid seeds {invalid}"
        )
    return selected


def formal_main_variants():
    """Return exactly the approved Phase 6 behavioral-main variants."""
    variants = [
        variant
        for variant in ALL_VARIANTS
        if variant.method_metadata.get("method_label") in FORMAL_MAIN_METHOD_LABELS
        and variant.method_metadata.get("evidence_family") == "behavioral_main"
    ]
    variants = sorted(variants, key=lambda variant: variant.method_metadata["method_label"])
    labels = {variant.method_metadata["method_label"] for variant in variants}
    families = {variant.method_metadata["evidence_family"] for variant in variants}
    if labels != FORMAL_MAIN_METHOD_LABELS or families != {"behavioral_main"} or len(variants) != 4:
        raise RuntimeError(
            "Phase 6 formal main variant filter is not exact: "
            f"labels={sorted(labels)}, families={sorted(families)}, count={len(variants)}"
        )
    return variants


@contextmanager
def _runner_variant_scope(variants):
    original = runner_module.ALL_VARIANTS
    runner_module.ALL_VARIANTS = list(variants)
    try:
        yield
    finally:
        runner_module.ALL_VARIANTS = original


def _write_json(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True), encoding="utf-8")


def _git_short_hash() -> str:
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "--short", "HEAD"],
            stderr=subprocess.DEVNULL,
            text=True,
        ).strip()
    except Exception:
        return "unknown"


def write_artifact_aliases(results_dir: str | Path = DEFAULT_MAIN_RESULTS_DIR) -> dict[str, str]:
    """Write the 06-02 external artifact names without dropping legacy names."""
    root = Path(results_dir)
    written: dict[str, str] = {}
    for source_name, alias_name in ARTIFACT_ALIASES.items():
        source = root / source_name
        alias = root / alias_name
        if not source.exists():
            continue
        if source.resolve() == alias.resolve():
            written[source_name] = str(alias)
            continue
        shutil.copyfile(source, alias)
        written[source_name] = str(alias)
    return written


def _status_counts(rows: list[dict]) -> dict[str, int]:
    counts: dict[str, int] = {}
    for row in rows:
        status = str(row.get("status", ""))
        counts[status] = counts.get(status, 0) + 1
    return counts


def _read_row_count(path: Path) -> int:
    if not path.exists():
        return 0
    with path.open(newline="", encoding="utf-8") as handle:
        return max(0, sum(1 for _ in handle) - 1)


def _read_status_counts(path: Path) -> dict[str, int]:
    if not path.exists():
        return {}
    import csv

    counts: dict[str, int] = {}
    with path.open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            status = row.get("status", "")
            counts[status] = counts.get(status, 0) + 1
    return counts


def _run_manifest_path(results_dir: str | Path) -> Path:
    return Path(results_dir) / "formal_run_manifest.json"


def _write_run_manifest(
    results_dir: str | Path,
    *,
    command: str,
    selected_scales: list[int],
    selected_seeds: list[int],
    method_labels: list[str],
    seed_manifest_path: Path,
    config_manifest_path: Path,
    started_at_utc: str,
    finished_at_utc: str | None,
    status: str,
    synthetic_rows: list[dict] | None = None,
    validation_result: dict | None = None,
) -> Path:
    root = Path(results_dir)
    raw_rows = synthetic_rows or []
    manifest = {
        "phase": "06",
        "plan": "06-02",
        "run_type": "formal_main_behavioral",
        "results_dir": str(root),
        "command": command,
        "git_commit_before_run": _git_short_hash(),
        "started_at_utc": started_at_utc,
        "finished_at_utc": finished_at_utc,
        "status": status,
        "seed_list": selected_seeds,
        "formal_seed_count": len(selected_seeds),
        "optional_extension_attempted": any(seed in OPTIONAL_EXTENSION_SEEDS for seed in selected_seeds),
        "optional_extension_status": (
            "attempted" if any(seed in OPTIONAL_EXTENSION_SEEDS for seed in selected_seeds)
            else "not_attempted"
        ),
        "scale_list": selected_scales,
        "method_list": method_labels,
        "expected_row_count": len(selected_seeds) * len(selected_scales) * len(method_labels),
        "actual_raw_row_count": len(raw_rows) if raw_rows else _read_row_count(root / "synthetic_results.csv"),
        "utility_log_count": _read_row_count(root / "utility_components.csv"),
        "status_counts": (
            _status_counts(raw_rows)
            if raw_rows
            else _read_status_counts(root / "synthetic_results.csv")
        ),
        "seed_manifest_path": str(seed_manifest_path),
        "config_manifest_path": str(config_manifest_path),
        "validation_report_path": str(root / "main_matrix_validation.json"),
        "alias_artifacts": {
            legacy: alias for legacy, alias in ARTIFACT_ALIASES.items()
        },
    }
    if validation_result is not None:
        manifest["validator_passed"] = bool(validation_result.get("passed"))
        manifest["validator_errors"] = validation_result.get("errors", [])
        manifest["validator_warnings"] = validation_result.get("warnings", [])
        manifest["validator_row_counts"] = validation_result.get("row_counts", {})
    path = _run_manifest_path(root)
    _write_json(path, manifest)
    write_artifact_aliases(root)
    return path


def write_formal_manifests(
    results_dir: str | Path = DEFAULT_MAIN_RESULTS_DIR,
    scales: Iterable[int] | None = None,
    seeds: Iterable[int] | None = None,
    include_optional_extension: bool = False,
) -> tuple[Path, Path]:
    """Write seed and config manifests before any formal run starts."""
    root = Path(results_dir)
    root.mkdir(parents=True, exist_ok=True)
    selected_scales = _validate_formal_scales(_as_int_list(scales, FORMAL_SCALES))
    selected_seeds = selected_formal_seeds(seeds, include_optional_extension)
    variants = formal_main_variants()
    method_labels = sorted(FORMAL_MAIN_METHOD_LABELS)
    created_at = datetime.now(timezone.utc).isoformat()

    seed_manifest = {
        "created_at_utc": created_at,
        "required_seeds": REQUIRED_FORMAL_SEEDS,
        "optional_extension_seeds": OPTIONAL_EXTENSION_SEEDS,
        "selected_seeds": selected_seeds,
        "include_optional_extension": include_optional_extension,
        "minimum_completion_rule": "required seeds 1-20 must complete as paired cells",
        "optional_extension_rule": (
            "seeds 21-30 upgrade evidence only if every optional paired cell completes"
        ),
        "replacement_seed_policy": "replacement seeds are forbidden",
    }
    config_manifest = {
        "created_at_utc": created_at,
        "phase": "06",
        "family": "main_behavioral_synthetic",
        "results_dir": str(root),
        "formal_scales": selected_scales,
        "pilot_scale_excluded": 20,
        "beijing": False,
        "method_labels": method_labels,
        "variant_names": [variant.name for variant in variants],
        "expected_completed_rows": (
            len(selected_scales) * len(selected_seeds) * len(method_labels)
        ),
        "runner": "experiments.runner.run_all_experiments",
        "legacy_result_paths_forbidden": [
            "results/synthetic_results.csv",
            "results/metrics_table.csv",
            "results/pilot/phase05",
        ],
    }

    seed_path = root / "formal_seed_manifest.json"
    config_path = root / "formal_config_manifest.json"
    _write_json(seed_path, seed_manifest)
    _write_json(config_path, config_manifest)
    write_artifact_aliases(root)
    return seed_path, config_path


def ensure_rerun_ledger(path: str | Path = DEFAULT_RERUN_LEDGER_PATH) -> Path:
    """Create the formal failure/rerun ledger header if needed."""
    from experiments.formal_validation import ensure_rerun_ledger as _ensure

    return _ensure(path)


def run_phase06_main(
    results_dir: str | Path = DEFAULT_MAIN_RESULTS_DIR,
    scales: Iterable[int] | None = None,
    seeds: Iterable[int] | None = None,
    include_optional_extension: bool = False,
    command: str = "programmatic",
):
    """Run the isolated Phase 6 formal synthetic main matrix."""
    selected_scales = _validate_formal_scales(_as_int_list(scales, FORMAL_SCALES))
    selected_seeds = selected_formal_seeds(seeds, include_optional_extension)
    started_at_utc = datetime.now(timezone.utc).isoformat()
    seed_manifest_path, config_manifest_path = write_formal_manifests(
        results_dir=results_dir,
        scales=selected_scales,
        seeds=selected_seeds,
        include_optional_extension=include_optional_extension,
    )
    ensure_rerun_ledger()
    variants = formal_main_variants()
    with _runner_variant_scope(variants):
        synthetic_rows, beijing_rows = runner_module.run_all_experiments(
            scales=selected_scales,
            seeds=selected_seeds,
            beijing=False,
            results_dir=str(results_dir),
        )
    _write_run_manifest(
        results_dir,
        command=command,
        selected_scales=selected_scales,
        selected_seeds=selected_seeds,
        method_labels=sorted(FORMAL_MAIN_METHOD_LABELS),
        seed_manifest_path=seed_manifest_path,
        config_manifest_path=config_manifest_path,
        started_at_utc=started_at_utc,
        finished_at_utc=datetime.now(timezone.utc).isoformat(),
        status="completed",
        synthetic_rows=synthetic_rows,
    )
    write_artifact_aliases(results_dir)
    return synthetic_rows, beijing_rows


def validate_phase06_main(
    results_dir: str | Path = DEFAULT_MAIN_RESULTS_DIR,
    scales: Iterable[int] | None = None,
    seeds: Iterable[int] | None = None,
    include_optional_extension: bool = False,
):
    """Validate persisted Phase 6 formal main outputs and write JSON gate result."""
    from experiments.formal_validation import validate_phase06_main_outputs

    selected_scales = _validate_formal_scales(_as_int_list(scales, FORMAL_SCALES))
    selected_seeds = selected_formal_seeds(seeds, include_optional_extension)
    result = validate_phase06_main_outputs(
        results_dir=results_dir,
        expected_seeds=selected_seeds,
        expected_scales=selected_scales,
        expected_method_labels=FORMAL_MAIN_METHOD_LABELS,
        ledger_path=DEFAULT_RERUN_LEDGER_PATH,
        write_json=True,
        require_label_gate=True,
    )
    root = Path(results_dir)
    existing_manifest = _run_manifest_path(root)
    command = "programmatic validation"
    started_at = datetime.now(timezone.utc).isoformat()
    if existing_manifest.exists():
        try:
            current = json.loads(existing_manifest.read_text(encoding="utf-8"))
            command = current.get("command", command)
            started_at = current.get("started_at_utc", started_at)
        except json.JSONDecodeError:
            pass
    _write_run_manifest(
        root,
        command=command,
        selected_scales=selected_scales,
        selected_seeds=selected_seeds,
        method_labels=sorted(FORMAL_MAIN_METHOD_LABELS),
        seed_manifest_path=root / "formal_seed_manifest.json",
        config_manifest_path=root / "formal_config_manifest.json",
        started_at_utc=started_at,
        finished_at_utc=datetime.now(timezone.utc).isoformat(),
        status="validated_passed" if result["passed"] else "validated_blocked",
        validation_result=result,
    )
    write_artifact_aliases(root)
    return result


def _parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--family", default="main", choices=["main"])
    parser.add_argument("--results-dir", default=str(DEFAULT_MAIN_RESULTS_DIR))
    parser.add_argument("--scales", nargs="*", type=int)
    parser.add_argument("--seeds", nargs="*", type=int)
    parser.add_argument("--include-optional-extension", action="store_true")
    parser.add_argument("--manifests-only", action="store_true")
    parser.add_argument("--init-ledger", action="store_true")
    parser.add_argument("--validate", action="store_true")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = _parse_args(argv)
    cli_command = "python -m experiments.phase06_formal " + " ".join(sys.argv[1:])
    if args.init_ledger:
        ensure_rerun_ledger()
    if args.manifests_only:
        write_formal_manifests(
            results_dir=args.results_dir,
            scales=args.scales,
            seeds=args.seeds,
            include_optional_extension=args.include_optional_extension,
        )
        return 0
    if args.validate:
        result = validate_phase06_main(
            results_dir=args.results_dir,
            scales=args.scales,
            seeds=args.seeds,
            include_optional_extension=args.include_optional_extension,
        )
        print(json.dumps(result, indent=2, sort_keys=True))
        return 0 if result["passed"] else 1

    run_phase06_main(
        results_dir=args.results_dir,
        scales=args.scales,
        seeds=args.seeds,
        include_optional_extension=args.include_optional_extension,
        command=cli_command,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
