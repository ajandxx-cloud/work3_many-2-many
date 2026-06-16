"""Compatibility CLI for Phase 6 supplementary diagnostics.

Plan 06-04 originally named the runner ``phase06_supplementary``.  The formal
06-04 implementation lives in ``phase06_robustness`` because the artifact
contract is organized around robustness/sensitivity/equity packages.
"""

from __future__ import annotations

import sys

from experiments.phase06_robustness import main as robustness_main


PACKAGE_ALIASES = {
    "mp_density_walking": "mp_density_walking_radius",
    "fleet_demand": "fleet_demand_stress",
    "equity": "equity_type_outcomes",
    "rolling_horizon": "algorithm_diagnostics",
    "alns_budget": "algorithm_diagnostics",
    "milp_gap": "algorithm_diagnostics",
}


def main(argv: list[str] | None = None) -> int:
    args = list(sys.argv[1:] if argv is None else argv)
    translated: list[str] = []
    skip_next = False
    for idx, arg in enumerate(args):
        if skip_next:
            skip_next = False
            continue
        if arg == "--results-dir":
            translated.append("--results-root")
            if idx + 1 < len(args):
                translated.append(args[idx + 1])
                skip_next = True
            continue
        if arg == "--package" and idx + 1 < len(args):
            translated.extend(["--package", PACKAGE_ALIASES.get(args[idx + 1], args[idx + 1])])
            skip_next = True
            continue
        translated.append(PACKAGE_ALIASES.get(arg, arg))
    return robustness_main(translated)


if __name__ == "__main__":
    raise SystemExit(main())
