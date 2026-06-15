# Phase 5 Pattern Map

**Phase:** 05 - Pilot Experiments
**Date:** 2026-06-15

## Purpose

Map Phase 5 plan files to nearby implementation patterns so executor agents can make focused edits instead of inventing a new experiment stack.

## Candidate Files and Analogs

| Target | Role | Closest analog | Pattern to reuse |
|---|---|---|---|
| `experiments/phase05_pilot.py` | Pilot orchestration wrapper | `experiments/runner.py` | Use `run_all_experiments`-style CSV writing, row schema, `results_dir`, seed/scale arguments, and module entry point |
| `experiments/pilot_validation.py` | Persisted artifact validator | `tests/test_runner.py`, `experiments/metrics.py` | Check required columns, valid statuses, range constraints, non-negative values, and utility-log joinability |
| `experiments/phase05_coverage_smoke.py` | Matched-coverage and fixed accepted-set diagnostics | `experiments/endogenous_matched_coverage.py`, `experiments/milp_gap.py` | Emit durable diagnostic rows with target/achieved coverage, tolerance, status, detailed reason, and no-Gurobi handling |
| `tests/test_phase05_pilot.py` | Focused Phase 5 tests | `tests/test_runner.py`, `tests/test_variants.py`, `tests/test_metrics.py` | Use temp result directories, generated synthetic scenarios, exact column assertions, range assertions, and monkeypatched failure fixtures |
| `.planning/phases/05-pilot-experiments/05_PILOT_RESULTS.md` | Gate report | `04_BASELINE_VALIDATION.md`, `04_ALGORITHM_VALIDATION.md` | Record purpose, schema checks, pass/fail gates, command outputs, bugs, reruns, and limitations without paper-facing claims |
| `results/pilot/phase05/` | Isolated pilot output directory | `results/` runner output pattern | Keep pilot files outside formal result filenames and include provenance in every row |

## Existing Behaviors to Preserve

- `experiments/runner.py` persists timeout and failed rows instead of dropping them.
- `ALL_VARIANTS` contains more than the main behavioral methods; Phase 5 must filter before running the main pilot.
- Behavioral method identity is stored in `method_metadata`, not inferred from class names.
- `utility_components.csv` is enriched with `run_id`, `seed`, `scenario`, `method`, and `request_id`.
- `milp_gap.py` defers Gurobi import and records `no_gurobi` rows.

## Data Flow

1. Pilot wrapper selects exact behavioral variants.
2. Synthetic scenarios run at one small scale and three seeds.
3. Runner-compatible rows and utility logs write to `results/pilot/phase05/`.
4. Validator checks status, schema, ranges, joinability, and REP-03 fields.
5. Coverage diagnostic writes matched-coverage and fixed-set smoke rows.
6. Gate report and bug ledger summarize readiness for Phase 6.

## Landmines

- Do not rely on legacy `variant` names for paper-facing method identity.
- Do not write pilot results to `results/synthetic_results.csv` used by older scripts.
- Do not treat abnormal served-share patterns as automatic failures unless they reveal schema, status, crash, timeout, or metric-range problems.
- Do not fail Phase 5 solely because Gurobi is absent.
- Do not create win/loss plots or manuscript-facing comparison figures from pilot data.

