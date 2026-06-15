---
phase: "02-experimental-contract-and-metric-standardization"
plan: "02-03"
subsystem: docs
tags: [statistical-plan, paired-seeds, downstream-tasks, phase-closure]
requires:
  - phase: "02-experimental-contract-and-metric-standardization"
    provides: "experiment contract, taxonomy, metric definitions, coverage controls"
provides:
  - "standalone statistical plan"
  - "Phase 4/5 code-change task list"
  - "Phase 2 artifact traceability closure"
affects: [phase-04-baseline-validation, phase-05-pilot-experiments, phase-06-formal-experiments]
tech-stack:
  added: []
  patterns: [paired-seed statistics, pilot/formal evidence separation, downstream implementation checklist]
key-files:
  created:
    - ".planning/phases/02-experimental-contract-and-metric-standardization/02_STATISTICAL_PLAN.md"
    - ".planning/phases/02-experimental-contract-and-metric-standardization/02_PHASE45_CODE_TASKS.md"
  modified: []
key-decisions:
  - "Formal comparisons should use paired seeds and paired differences where possible."
  - "Phase 2 does not lock the final formal-experiment sample size; Phase 5 pilots inform the final count."
  - "Phase 4/5 implementation tasks are explicit, but Phase 2 does not edit code."
requirements-completed: [EXP-01, EXP-02, EXP-03, EXP-04, MET-01, MET-02, MET-03]
duration: "4 min"
completed: 2026-06-15
---

# Phase 02 Plan 03: Statistical Plan and Downstream Task List Summary

**Paired-seed statistical contract plus Phase 4/5 implementation handoff**

## Performance

- **Duration:** 4 min
- **Tasks:** 3
- **Files created:** 2
- **Commits:** `822fd33`, `f6ac47b`

## Accomplishments

- Created `02_STATISTICAL_PLAN.md` with paired experimental design, paired difference metrics, confidence interval rules, pilot/formal evidence separation, and reporting templates.
- Created `02_PHASE45_CODE_TASKS.md` with downstream Phase 4/5 tasks for variants, shared response hooks, row-level request status, metrics/CSV outputs, matched-coverage cap, fixed accepted-set diagnostics, provenance/failure rows, gamma/welfare semantics, and ALNS/MILP diagnostics.
- Ran phase-wide traceability checks for all required Phase 2 artifacts, EXP/MET requirement IDs, and D-01 through D-23 decision IDs.

## Task Commits

1. **Task 01: Create statistical plan** - `822fd33`
2. **Task 02: Create downstream code task list** - `f6ac47b`
3. **Task 03: Close Phase 2 planning/execution traceability** - completed by artifact checks in this summary

## Deviations from Plan

None - plan executed exactly as written.

**Total deviations:** 0 auto-fixed.
**Impact on plan:** No scope changes.

## Verification

- Required Phase 2 files exist: `02_EXPERIMENT_CONTRACT.md`, `02_BASELINE_TAXONOMY.md`, `02_METRICS_DEFINITIONS.md`, `02_COVERAGE_CONFOUNDING_PLAN.md`, `02_STATISTICAL_PLAN.md`, and `02_PHASE45_CODE_TASKS.md`: passed.
- EXP-01, EXP-02, EXP-03, EXP-04, MET-01, MET-02, and MET-03 appear in the Phase 2 outputs: passed.
- D-01 through D-23 appear in Phase 2 outputs: passed.
- `02_STATISTICAL_PLAN.md` contains paired seeds, paired differences, confidence intervals, and pilot/formal separation: passed.
- `02_PHASE45_CODE_TASKS.md` routes implementation work to Phase 4/5 and states Phase 2 does not implement code changes: passed.
- No intentional edits were made under `results/`, `experiments/`, `src/`, or `manuscript/sections/`. Pre-existing dirty/generated files in those paths remain unrelated.

## Issues Encountered

- A parallel commit attempt collided with Git's transient `index.lock`; the statistical-plan commit succeeded and the downstream-task commit was retried serially after the lock cleared.
- `gsd-sdk query state.advance-plan` could not parse the current STATE body format during Plan 02-01 closeout. `state.update-progress` and `roadmap.update-plan-progress` were used instead and completed successfully.

## Next Phase Readiness

Phase 2 outputs are ready for phase-level verification. Phase 3 can rebuild the passenger-choice model using the shared-response constraints, and Phase 4 can implement the task list without guessing the experiment contract.

## Self-Check: PASSED

Plan outputs exist, acceptance criteria passed, traceability checks passed, and Phase 2 scope was preserved.

