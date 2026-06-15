---
phase: 04-baseline-and-algorithm-implementation-check
plan: 04-03
subsystem: algorithms
tags: [alns, greedy, diagnostics, feasibility]
requires:
  - phase: 04-01
    provides: method metadata and behavioral variant mapping
  - phase: 04-02
    provides: runner schema and durable result rows
provides:
  - GreedyInsertionBaseline diagnostic variant
  - optional RollingHorizon diagnostic traces
  - ALNS multi-budget smoke helper
  - algorithm validation report
affects: [phase-05-pilot-runs, phase-06-formal-experiments]
tech-stack:
  added: []
  patterns: [collect_diagnostics flag, algorithm_diagnostic evidence family]
key-files:
  created:
    - experiments/algorithm_diagnostics.py
    - .planning/phases/04-baseline-and-algorithm-implementation-check/04_ALGORITHM_VALIDATION.md
  modified:
    - src/drt/alns.py
    - experiments/variants.py
    - tests/test_alns.py
    - tests/test_insertion.py
    - tests/test_variants.py
key-decisions:
  - "Kept ALNS trace collection opt-in through collect_diagnostics to avoid changing default solver behavior."
  - "Labeled multi-budget diagnostics as algorithm smoke evidence only, not formal runtime-quality evidence."
patterns-established:
  - "Algorithm diagnostic rows include evidence_family and diagnostic_role fields."
  - "RollingHorizon trace entries include objective, runtime, accepted/unassigned counts, and operator names."
requirements-completed: [ALG-01, ALG-02, ALG-03]
duration: 50 min
completed: 2026-06-15
---

# Phase 04 Plan 03: Greedy, No-Rolling-Horizon, and ALNS Diagnostics Summary

**Algorithm diagnostics now expose greedy, no-rolling-horizon, ALNS trace, and multi-budget smoke evidence without mixing into behavioral claims**

## Performance

- **Duration:** 50 min
- **Started:** 2026-06-15T11:00:00Z
- **Completed:** 2026-06-15T11:50:00Z
- **Tasks:** 5
- **Files modified:** 7

## Accomplishments

- Added `GreedyInsertionBaseline` as a named algorithm diagnostic variant.
- Added optional ALNS trace collection and operator/improvement counters to `RollingHorizon`.
- Added `experiments.algorithm_diagnostics.run_alns_budget_smoke()` for `[5, 20, 50]` iteration smoke rows.
- Added route-commitment tests for tagged stops, completed IDs, pickup times, and walking-radius failure.
- Created `04_ALGORITHM_VALIDATION.md` with diagnostic boundaries and commands.

## Task Commits

1. **Tasks 1-5: algorithm diagnostics and ALNS traces** - `2fbe94f` (feat)

## Files Created/Modified

- `src/drt/alns.py` - Adds opt-in diagnostic trace collection and operator statistics.
- `experiments/variants.py` - Adds and registers `GreedyInsertionBaseline`.
- `experiments/algorithm_diagnostics.py` - Adds small ALNS multi-budget smoke callable and CLI.
- `tests/test_alns.py` - Adds trace, route-commitment, pruning, and diagnostic smoke tests.
- `tests/test_insertion.py` - Adds walking-radius failure coverage.
- `tests/test_variants.py` - Adds greedy diagnostic runner-schema coverage.
- `.planning/phases/04-baseline-and-algorithm-implementation-check/04_ALGORITHM_VALIDATION.md` - Documents D-12 through D-16 and ALG-01 through ALG-03.

## Decisions Made

- Used `collect_diagnostics=False` by default so trace collection is observational and opt-in.
- Kept the multi-budget helper in a separate module to avoid writing formal evidence outputs during local validation.

## Deviations from Plan

None - plan executed exactly as written.

## Issues Encountered

None.

## Verification

```bash
PYTHONPATH=src pytest tests/test_feasibility.py tests/test_insertion.py tests/test_alns.py tests/test_variants.py -q
PYTHONPATH=src python -m experiments.algorithm_diagnostics
PYTHONPATH=src pytest tests/test_runner.py -q
```

Results:

- Algorithm/variant focused suite: 42 passed.
- Diagnostic CLI emitted 5, 20, and 50 budget rows with objective/runtime/operator/accepted/unassigned fields.
- Runner smoke suite: 14 passed.

## User Setup Required

None - no external service configuration required.

## Next Phase Readiness

Algorithm diagnostics are ready for MILP/exact diagnostic scope validation in `04-04`.

---
*Phase: 04-baseline-and-algorithm-implementation-check*
*Completed: 2026-06-15*

