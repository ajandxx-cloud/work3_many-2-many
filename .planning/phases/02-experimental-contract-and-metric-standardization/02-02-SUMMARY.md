---
phase: "02-experimental-contract-and-metric-standardization"
plan: "02-02"
subsystem: docs
tags: [metrics, denominators, coverage-confounding, matched-coverage, fixed-accepted-set]
requires:
  - phase: "02-experimental-contract-and-metric-standardization"
    provides: "research and pattern map"
provides:
  - "standalone metric dictionary"
  - "row-level status vocabulary"
  - "coverage-confounding control plan"
affects: [phase-04-baseline-validation, phase-05-pilot-experiments, phase-06-formal-experiments, phase-08-claim-gate]
tech-stack:
  added: []
  patterns: [metric denominator contract, row-status vocabulary, matched-coverage control, fixed accepted-set diagnostic]
key-files:
  created:
    - ".planning/phases/02-experimental-contract-and-metric-standardization/02_METRICS_DEFINITIONS.md"
    - ".planning/phases/02-experimental-contract-and-metric-standardization/02_COVERAGE_CONFOUNDING_PLAN.md"
  modified: []
key-decisions:
  - "`vkm_per_trip` is forbidden for new formal evidence."
  - "Main behavioral tables must report served share, rejection mechanisms, total vehicle-km, vkm per served trip, and vkm per original request together."
  - "Matched coverage is core supplementary evidence and fixed accepted-set diagnostics do not replace behavioral evidence."
requirements-completed: [EXP-04, MET-01, MET-02, MET-03]
duration: "4 min"
completed: 2026-06-15
---

# Phase 02 Plan 02: Metric Definitions and Coverage Controls Summary

**Standalone metric and coverage-control contracts for denominator-safe formal experiments**

## Performance

- **Duration:** 4 min
- **Tasks:** 2
- **Files created:** 2
- **Commits:** `7e51afa`, `d2ce5a7`

## Accomplishments

- Created `02_METRICS_DEFINITIONS.md` with row-level status vocabulary and a metric dictionary covering formulas, numerators, denominators, units, valid ranges, interpretations, experiment families, and forbidden uses.
- Defined `served_share`, `behavioral_acceptance_rate`, `choice_rejection_rate`, `feasibility_rejection_rate`, `deterministic_inserted_share`, `total_vkm`, `vkm_per_served_trip`, and `vkm_per_original_request` as distinct quantities.
- Created `02_COVERAGE_CONFOUNDING_PLAN.md` defining unconstrained behavioral comparison, matched-coverage comparison using a target `served_share` cap, and fixed accepted-set routing diagnostics using the intersection of commonly serviceable/accepted requests.

## Task Commits

1. **Task 01: Create metric definitions** - `7e51afa`
2. **Task 02: Create coverage-confounding control plan** - `d2ce5a7`

## Deviations from Plan

None - plan executed exactly as written.

**Total deviations:** 0 auto-fixed.
**Impact on plan:** No scope changes.

## Verification

- `02_METRICS_DEFINITIONS.md` contains required metric dictionary, row statuses, formulas, forbidden metric language, MET-01/MET-02/MET-03, and D-09 through D-13 plus D-21: passed.
- `02_COVERAGE_CONFOUNDING_PLAN.md` contains required design headings, target served-share cap, intersection accepted-set rule, EXP-04, and D-14 through D-18: passed.
- No intentional edits were made under `results/`, `experiments/`, `src/`, or `manuscript/sections/`. Pre-existing dirty files in those paths remain unrelated.

## Issues Encountered

None.

## Next Phase Readiness

Ready for Plan `02-03`: statistical plan, Phase 4/5 code task list, and Phase 2 closure.

## Self-Check: PASSED

Plan outputs exist, acceptance criteria passed, and Phase 2 scope was preserved.

