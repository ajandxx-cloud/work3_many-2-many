---
phase: 03-passenger-choice-model-rebuild
plan: 03-03
subsystem: experiments
tags: [actual-offer-choice, status-schema, utility-logs, runner-output]
requires:
  - phase: 03-01
    provides: choice contract and calibration table
  - phase: 03-02
    provides: core actual-offer choice evaluator
provides:
  - behavioral variant integration
  - durable request status fields
  - joinable utility_components.csv output
  - choice sensitivity hooks
  - no-proxy regression coverage
affects: [experiments, variants, metrics, runner]
tech-stack:
  added: []
  patterns: [actual-offer acceptance sequence, status-derived metrics, two-layer output]
key-files:
  modified:
    - experiments/variants.py
    - experiments/metrics.py
    - experiments/runner.py
    - experiments/config.py
    - tests/test_variants.py
    - tests/test_metrics.py
    - tests/test_runner.py
    - .planning/phases/03-passenger-choice-model-rebuild/03_CHOICE_MODEL_CONTRACT.md
key-decisions:
  - "Behavioral variants now evaluate a feasible offer before passenger acceptance."
  - "DoorToDoor and SingleSidedPickup use the shared response model with exact door-side radii."
  - "Utility components are written to utility_components.csv with run/seed/scenario/method/request join keys."
  - "The legacy nearest-meeting-point MNL proxy is quarantined and covered by a regression test."
patterns-established:
  - "PassengerRecord.status is the source of truth; accepted is derived from served status for compatibility."
  - "Feasibility rejections keep missing utility fields instead of fabricated proxy values."
requirements-completed: [CHO-01, CHO-02, CHO-03, CHO-04]
duration: 32 min
completed: 2026-06-15
---

# Phase 03 Plan 03: Variant Integration, Status Schema, and Utility Logging Summary

**Actual feasible offers now drive behavioral acceptance, with status-aware metrics and joinable utility logs.**

## Performance

- **Duration:** 32 min
- **Completed:** 2026-06-15
- **Tasks:** 5
- **Files modified:** 8

## Accomplishments

- Replaced live behavioral acceptance in `DoorToDoor`, `SingleSidedPickup`, `FullModel`, and `AblationNoRollingHorizon` with the shared actual-offer choice sequence.
- Added request statuses, detailed reasons, acceptance probability, and random draw fields to passenger records.
- Added served share, behavioral acceptance rate, choice rejection rate, and feasibility rejection rate metrics.
- Added `utility_components.csv` as the chosen two-layer utility artifact with join keys.
- Added choice configuration hooks for service ASC, outside option, seed, and type shares.
- Added tests for no-proxy regression, rejected-offer routing exclusion, stable type assignment, sensitivity direction, status separation, and utility artifact schema.

## Task Commits

1. **Tasks 1-5: Actual-offer variant integration, status metrics, runner logs, and tests** - `054377f` (feat)

## Files Created/Modified

- `experiments/variants.py` - Added shared actual-offer sequence and integrated behavioral variants.
- `experiments/metrics.py` - Added durable status fields and status-derived aggregate metrics.
- `experiments/runner.py` - Added utility log collection and `utility_components.csv` output.
- `experiments/config.py` - Added documented choice parameter defaults.
- `tests/test_variants.py` - Added behavioral integration and no-proxy regression tests.
- `tests/test_metrics.py` - Added status accounting tests.
- `tests/test_runner.py` - Added bounded runner smoke tests and utility artifact checks.
- `03_CHOICE_MODEL_CONTRACT.md` - Documented the implemented utility artifact name/schema.

## Decisions Made

- Kept `_mnl_filter_requests()` only as a quarantined legacy helper so regression tests can prove Phase 3 paths do not call it.
- Used zero door-side radii for DoorToDoor and SingleSidedPickup constrained sides to prevent cost optimization from choosing non-door meeting points.
- Kept runner smoke tests small and monkeypatched Beijing scale to avoid turning unit tests into full experiment runs.

## Deviations from Plan

- The runner test was narrowed to a bounded smoke command because the previous Beijing fixture used the full imported scale and exceeded practical unit-test runtime.

## Issues Encountered

- SingleSidedPickup initially allowed non-door dropoffs through the shared candidate list; setting `rho_d=0.0` fixed the constrained dropoff semantics.
- A one-request ASC sensitivity test hit an infeasible synthetic request; the final test uses the first actually offered row from the shared small scenario.

## Verification

- `PYTHONPATH=src pytest tests/test_choice.py tests/test_metrics.py tests/test_variants.py tests/test_runner.py -q` - passed, 77 tests.
- `rg "_mnl_filter_requests|utility_components.csv|chosen output artifact" experiments/variants.py tests/test_variants.py .planning/phases/03-passenger-choice-model-rebuild/03_CHOICE_MODEL_CONTRACT.md` - confirmed proxy helper is quarantined and output schema is documented.

## User Setup Required

None.

## Next Phase Readiness

Ready for Phase 4 baseline and algorithm implementation checks. Phase 4 can consume status-aware rows and utility-component logs without rerunning Phase 3 design work.

---
*Phase: 03-passenger-choice-model-rebuild*
*Completed: 2026-06-15*
