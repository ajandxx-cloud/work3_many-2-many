"""Phase 6 formal synthetic experiment harness.

This module keeps formal outputs isolated from pilot and legacy result files,
predeclares the required main matrix, and exposes a small CLI for manifest
creation, smoke runs, and persisted-artifact validation.
"""

from __future__ import annotations

import argparse
import json
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
DEFAULT_MAIN_RESULTS_DIR = DEFAULT_PHASE06_ROOT / "main"
DEFAULT_RERUN_LEDGER_PATH = (
    Path(".planning/phases/06-formal-synthetic-experiments")
    / "06_FAILURE_RERUN_LEDGER.csv"
)


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
):
    """Run the isolated Phase 6 formal synthetic main matrix."""
    selected_scales = _validate_formal_scales(_as_int_list(scales, FORMAL_SCALES))
    selected_seeds = selected_formal_seeds(seeds, include_optional_extension)
    write_formal_manifests(
        results_dir=results_dir,
        scales=selected_scales,
        seeds=selected_seeds,
        include_optional_extension=include_optional_extension,
    )
    ensure_rerun_ledger()
    variants = formal_main_variants()
    with _runner_variant_scope(variants):
        return runner_module.run_all_experiments(
            scales=selected_scales,
            seeds=selected_seeds,
            beijing=False,
            results_dir=str(results_dir),
        )


def validate_phase06_main(
    results_dir: str | Path = DEFAULT_MAIN_RESULTS_DIR,
    scales: Iterable[int] | None = None,
    seeds: Iterable[int] | None = None,
    include_optional_extension: bool = False,
):
    """Validate persisted Phase 6 formal main outputs and write JSON gate result."""
    from experiments.formal_validation import validate_phase06_main_outputs

    return validate_phase06_main_outputs(
        results_dir=results_dir,
        expected_seeds=selected_formal_seeds(seeds, include_optional_extension),
        expected_scales=_validate_formal_scales(_as_int_list(scales, FORMAL_SCALES)),
        expected_method_labels=FORMAL_MAIN_METHOD_LABELS,
        ledger_path=DEFAULT_RERUN_LEDGER_PATH,
        write_json=True,
        require_label_gate=True,
    )


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
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
