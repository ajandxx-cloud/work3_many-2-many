"""Phase 5 pilot harness for readiness-only behavioral runs."""

from __future__ import annotations

from contextlib import contextmanager
from pathlib import Path

import experiments.runner as runner_module
from experiments.variants import ALL_VARIANTS

PILOT_SCALE = 20
PILOT_SEEDS = [42, 43, 44]
PILOT_RESULTS_DIR = "results/pilot/phase05"
MAIN_BEHAVIORAL_METHOD_LABELS = {
    "DoorToDoor_Choice_CommonRouting",
    "SingleSidedPickup_Choice_CommonRouting",
    "SingleSidedDropoff_Choice_CommonRouting",
    "BidirectionalMP_Choice_RH_ALNS",
}


def main_behavioral_variants():
    """Return exactly the Phase 5 behavioral-main pilot variants."""
    variants = [
        variant
        for variant in ALL_VARIANTS
        if variant.method_metadata.get("method_label") in MAIN_BEHAVIORAL_METHOD_LABELS
        and variant.method_metadata.get("evidence_family") == "behavioral_main"
    ]
    return sorted(variants, key=lambda variant: variant.method_metadata["method_label"])


@contextmanager
def _runner_variant_scope(variants):
    original = runner_module.ALL_VARIANTS
    runner_module.ALL_VARIANTS = list(variants)
    try:
        yield
    finally:
        runner_module.ALL_VARIANTS = original


def run_phase05_pilot(
    results_dir: str | Path = PILOT_RESULTS_DIR,
    scale: int = PILOT_SCALE,
    seeds: list[int] | tuple[int, ...] = PILOT_SEEDS,
):
    """Run the isolated Phase 5 synthetic pilot matrix."""
    variants = main_behavioral_variants()
    with _runner_variant_scope(variants):
        return runner_module.run_all_experiments(
            scales=[scale],
            seeds=list(seeds),
            beijing=False,
            results_dir=str(results_dir),
        )


if __name__ == "__main__":
    run_phase05_pilot()
