---
phase: 03-passenger-choice-model-rebuild
plan: 03-02
subsystem: choice
tags: [binary-logit, offer-attributes, utility-components, passenger-types]
requires:
  - phase: 03-01
    provides: choice contract and calibration table
provides:
  - actual-offer choice API
  - stable binary logit evaluation
  - deterministic passenger type assignment
  - utility-component log rows
affects: [experiments, variants, metrics, runner]
tech-stack:
  added: []
  patterns: [dataclass choice contract, stable hash seeding, flattened utility log rows]
key-files:
  created:
    - tests/test_choice.py
  modified:
    - src/drt/choice.py
    - src/drt/types.py
    - src/drt/__init__.py
key-decisions:
  - "Preserved the legacy accept_probability import while adding actual-offer helpers."
  - "Used stable SHA-256 based request seeding instead of Python process hash randomization."
  - "Represented feasibility rejection as a no-offer evaluation with no fabricated utility fields."
patterns-established:
  - "OfferAttributes carries all utility-relevant fields for one actual feasible offer."
  - "ChoiceEvaluation.as_log_row flattens offer and utility components only when an offer exists."
requirements-completed: [CHO-01, CHO-02, CHO-03, CHO-04]
duration: 13 min
completed: 2026-06-15
---

# Phase 03 Plan 02: Core Choice Evaluator Summary

**Actual-offer choice primitives with explicit service ASC, outside option, seeded passenger types, and utility-component rows**

## Performance

- **Duration:** 13 min
- **Started:** 2026-06-15T14:45:46+08:00
- **Completed:** 2026-06-15T14:58:40+08:00
- **Tasks:** 4
- **Files modified:** 4

## Accomplishments

- Added `OfferAttributes`, `ChoiceParameters`, `UtilityComponents`, and `ChoiceEvaluation` dataclasses.
- Added stable single-offer evaluation helpers with explicit `service_asc` and `outside_option_constant`.
- Added deterministic request-level passenger type assignment using stable SHA-256 seeding.
- Added focused tests for ASC, outside option, attribute disutility, extreme utilities, log row fields, deterministic type assignment, invalid shares, non-uniform shares, and feasibility-rejected no-offer rows.

## Task Commits

Each task was committed atomically by outcome:

1. **Tasks 1-3: Choice parameters, actual-offer utility, and seeded type assignment** - `acbd2d0` (feat)
2. **Task 4: Backfill core choice tests** - `3dea76c` (test)

## Files Created/Modified

- `src/drt/types.py` - Added offer, parameter, component, and evaluation dataclasses.
- `src/drt/choice.py` - Added stable binary logit, actual-offer evaluation, feasibility-rejected no-offer rows, and type assignment.
- `src/drt/__init__.py` - Re-exported the new choice API while preserving existing exports.
- `tests/test_choice.py` - Added focused Phase 3 choice tests.

## Decisions Made

- Kept compatibility for `accept_probability` rather than replacing the legacy Bundle API in this plan.
- Used `None` utility fields for feasibility rejections so no proxy nearest-meeting-point utility can leak into logs.
- Kept the new choice helpers independent of experiment variants so Wave 3 can integrate them without circular dependencies.

## Deviations from Plan

None - plan executed exactly as written.

## Issues Encountered

None.

## Verification

- `PYTHONPATH=src pytest tests/test_choice.py -q` - passed, 11 tests.
- `PYTHONPATH=src python -c "from drt.choice import accept_probability; print(accept_probability.__name__)"` - passed.
- `rg "service_asc|outside_option_constant|UtilityComponents|OfferAttributes|ChoiceEvaluation|assign_passenger_type|nearest|min\\(|meeting_points" src/drt/choice.py tests/test_choice.py` - confirmed required fields/helpers and no nearest-meeting-point search in `src/drt/choice.py`.

## User Setup Required

None - no external service configuration required.

## Next Phase Readiness

Ready for `03-03`: experiment variants can consume the actual-offer evaluator, add row-level statuses, and write utility-component logs.

---
*Phase: 03-passenger-choice-model-rebuild*
*Completed: 2026-06-15*

