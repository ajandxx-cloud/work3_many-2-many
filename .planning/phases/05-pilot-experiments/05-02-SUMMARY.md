---
phase: 05-pilot-experiments
plan: 05-02
subsystem: experiments
tags: [phase05, matched-coverage, fixed-accepted-set, diagnostics]
requires:
  - phase: 05-pilot-experiments
    provides: Phase 5 pilot harness and generated main behavioral artifacts
provides:
  - pilot-scale matched-coverage diagnostic rows
  - fixed accepted-set smoke JSON artifact
  - validator visibility for diagnostic artifacts
affects: [phase05, phase06-formal-experiments, rep-03]
tech-stack:
  added: []
  patterns: [readiness diagnostics, non-main evidence family separation]
key-files:
  created:
    - experiments/phase05_coverage_smoke.py
    - results/pilot/phase05/matched_coverage_pilot.csv
    - results/pilot/phase05/fixed_accepted_set_smoke.json
  modified:
    - experiments/pilot_validation.py
    - tests/test_phase05_pilot.py
key-decisions:
  - "Matched-coverage tolerance failures are persisted as blocking diagnostic rows."
  - "The optional MILP path remains non-blocking; skipped/no_gurobi statuses do not block Phase 5 by themselves."
patterns-established:
  - "Diagnostic outputs use non-behavioral-main evidence families."
  - "Fixed accepted-set smoke writes durable output even when the common intersection is empty."
requirements-completed: [REP-03]
duration: 12 min
completed: 2026-06-15
---

# Phase 05 Plan 02: Coverage-Control and Fixed Accepted-Set Smokes Summary

**Matched-coverage and fixed accepted-set readiness diagnostics with durable blocker output**

## Performance

- **Duration:** 12 min
- **Started:** 2026-06-15T13:44:00Z
- **Completed:** 2026-06-15T13:56:00Z
- **Tasks:** 3
- **Files modified:** 5

## Accomplishments

- Added `experiments/phase05_coverage_smoke.py` with `run_matched_coverage_pilot(...)` and `run_fixed_accepted_set_smoke(...)`.
- Persisted `matched_coverage_pilot.csv` with target, achieved, gap, tolerance, status, evidence-family, and diagnostic-role fields.
- Persisted `fixed_accepted_set_smoke.json` with retained request count/share and non-main diagnostic metadata.
- Extended `validate_phase05_outputs(...)` so optional diagnostic artifacts appear in `checked_files`.
- Added tests for matched-coverage output columns, tolerance blocking, fixed-set durability, empty intersection handling, and no-Gurobi non-blocking behavior.

## Task Commits

1. **Task 1-3: Coverage and fixed-set diagnostics** - `ebba31c` (`feat(05-02)`)

## Files Created/Modified

- `experiments/phase05_coverage_smoke.py` - Phase 5 matched-coverage and fixed accepted-set diagnostic module.
- `experiments/pilot_validation.py` - Adds optional diagnostic artifacts to the checked-files summary.
- `tests/test_phase05_pilot.py` - Adds focused diagnostic tests.
- `results/pilot/phase05/matched_coverage_pilot.csv` - Generated matched-coverage readiness rows.
- `results/pilot/phase05/fixed_accepted_set_smoke.json` - Generated fixed-set smoke artifact.

## Decisions Made

- Kept the matched-coverage diagnostic separate from the main behavioral pilot by using `evidence_family = supplementary_control`.
- Kept fixed accepted-set output separate from behavioral evidence by using `evidence_family = algorithm_diagnostic`.
- Defaulted the optional MILP path to skipped for the pilot smoke; tests cover `no_gurobi` as durable and non-blocking.

## Deviations from Plan

None - plan executed exactly as written.

## Issues Encountered

- The real matched-coverage pilot found a blocker: achieved mean served share `0.1000` versus target `0.1333`, absolute gap `0.0333` above the `0.03` tolerance. Rows for seeds 42 and 44 are marked `failed` in `matched_coverage_pilot.csv`.
- The fixed accepted-set smoke found an empty common served intersection for seed 42 and persisted `status = empty_intersection`; this is a readiness finding for the report/ledger, not a crash.

## Verification

- `PYTHONPATH=src pytest tests/test_phase05_pilot.py -q` -> 13 passed.
- `PYTHONPATH=src pytest tests/test_runner.py tests/test_metrics.py tests/test_variants.py -q` -> 77 passed.
- `PYTHONPATH=src python -m experiments.phase05_coverage_smoke` -> wrote `matched_coverage_pilot.csv` and `fixed_accepted_set_smoke.json`.

## User Setup Required

None - no external service configuration required.

## Next Phase Readiness

Ready for `05-03` gate reporting. The report and bug ledger must record the matched-coverage tolerance blocker before Phase 6 can proceed.

---
*Phase: 05-pilot-experiments*
*Completed: 2026-06-15*
