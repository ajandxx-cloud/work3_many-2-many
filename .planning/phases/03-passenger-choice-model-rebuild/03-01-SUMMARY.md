---
phase: 03-passenger-choice-model-rebuild
plan: 03-01
subsystem: docs
tags: [choice-model, calibration, sensitivity, passenger-response]
requires:
  - phase: 02-experimental-contract-and-metric-standardization
    provides: shared passenger-response and metric/status contracts
provides:
  - passenger choice model contract
  - parameter calibration and sensitivity design
  - status and utility logging documentation
affects: [choice-model, experiments, metrics, runner, phase-4-baselines, phase-5-pilots]
tech-stack:
  added: []
  patterns: [actual-offer choice contract, low-baseline-high sensitivity grid, two-layer utility logging]
key-files:
  created:
    - .planning/phases/03-passenger-choice-model-rebuild/03_CHOICE_MODEL_CONTRACT.md
    - .planning/phases/03-passenger-choice-model-rebuild/03_PARAMETER_CALIBRATION.md
  modified: []
key-decisions:
  - "Choice must be evaluated only after an actual feasible service offer exists."
  - "Main evidence uses a unified service ASC; design-specific ASCs are sensitivity-only."
  - "Current coefficients are inherited or simulation-range inputs, not real-data calibration."
patterns-established:
  - "Choice docs distinguish behavioral rejection from feasibility rejection before metrics aggregate rows."
  - "Calibration docs require source tags and evidence status for every parameter value."
requirements-completed: [CHO-01, CHO-02, CHO-03]
duration: 11 min
completed: 2026-06-15
---

# Phase 03 Plan 01: Choice Contract and Calibration Summary

**Actual-offer passenger choice contract with explicit ASC, outside option, type shares, sensitivity ranges, and utility logging obligations**

## Performance

- **Duration:** 11 min
- **Started:** 2026-06-15T14:34:20+08:00
- **Completed:** 2026-06-15T14:45:46+08:00
- **Tasks:** 2
- **Files modified:** 2

## Accomplishments

- Created `03_CHOICE_MODEL_CONTRACT.md` defining actual feasible-offer timing, single-offer semantics, terminal statuses, utility specification, deterministic type assignment, and two-layer utility logging.
- Created `03_PARAMETER_CALIBRATION.md` defining baseline, low, and high values for walk, wait, IVT, fare, service ASC, outside option, and type shares.
- Labeled current coefficient values as inherited or simulation-range inputs so later manuscript text cannot imply real-data calibration.

## Task Commits

Each task was committed atomically:

1. **Task 1: Create the passenger choice model contract** - `614b6e1` (docs)
2. **Task 2: Create the parameter calibration and sensitivity document** - `71fec38` (docs)

## Files Created/Modified

- `.planning/phases/03-passenger-choice-model-rebuild/03_CHOICE_MODEL_CONTRACT.md` - Defines the Phase 3 passenger-choice behavioral contract.
- `.planning/phases/03-passenger-choice-model-rebuild/03_PARAMETER_CALIBRATION.md` - Defines coefficient/source labels and sensitivity grid.

## Decisions Made

- Kept the main service ASC unified and made design-specific ASC sensitivity-only to avoid tuning a service design into success.
- Treated all current coefficient values as inherited or simulation-range inputs because no local artifact establishes real stated/revealed preference calibration.
- Required feasibility-rejected rows to avoid fabricated proxy utility values.

## Deviations from Plan

None - plan executed exactly as written.

## Issues Encountered

None.

## User Setup Required

None - no external service configuration required.

## Next Phase Readiness

Ready for `03-02`: the core code plan can implement the explicit choice parameters, outside option, seeded type assignment, and utility-component objects against these docs.

---
*Phase: 03-passenger-choice-model-rebuild*
*Completed: 2026-06-15*

