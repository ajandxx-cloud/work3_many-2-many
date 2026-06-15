---
phase: "02-experimental-contract-and-metric-standardization"
plan: "02-01"
subsystem: docs
tags: [experiment-contract, baseline-taxonomy, fair-comparison, evidence-chain]
requires:
  - phase: "01-literature-and-novelty-audit"
    provides: "conservative contribution framing and research questions"
provides:
  - "main experiment evidence-family contract"
  - "four-axis baseline taxonomy"
  - "paper-facing method label mapping"
affects: [phase-03-choice-model, phase-04-baseline-validation, phase-06-formal-experiments, phase-08-claim-gate]
tech-stack:
  added: []
  patterns: [evidence-family contract, four-axis taxonomy, diagnostic-role separation]
key-files:
  created:
    - ".planning/phases/02-experimental-contract-and-metric-standardization/02_EXPERIMENT_CONTRACT.md"
    - ".planning/phases/02-experimental-contract-and-metric-standardization/02_BASELINE_TAXONOMY.md"
  modified: []
key-decisions:
  - "Behavioral service-design evidence must use shared passenger-response assumptions."
  - "Deterministic no-choice/all-feasible variants are diagnostics, not main behavioral evidence."
  - "Paper-facing contracts use `BidirectionalMP + Choice + RollingHorizon/ALNS` instead of `FullModel`."
requirements-completed: [EXP-01, EXP-02, EXP-03]
duration: "3 min"
completed: 2026-06-15
---

# Phase 02 Plan 01: Experiment Contract and Baseline Taxonomy Summary

**Experiment-family and baseline-taxonomy contract for fair bidirectional meeting-point DRT comparisons**

## Performance

- **Duration:** 3 min
- **Tasks:** 2
- **Files created:** 2
- **Commits:** `8150dfd`, `376a88b`

## Accomplishments

- Created `02_EXPERIMENT_CONTRACT.md` defining behavioral main comparison, core supplementary controls, deterministic diagnostics, algorithm diagnostics, claim boundaries, and downstream phase ownership.
- Created `02_BASELINE_TAXONOMY.md` mapping conceptual methods across service design, passenger response, routing algorithm, and diagnostic role.
- Marked `SingleSidedDropoff` as a required missing downstream baseline.
- Replaced paper-facing `FullModel` wording with `BidirectionalMP + Choice + RollingHorizon/ALNS` while preserving the implementation mapping.

## Task Commits

1. **Task 01: Create experiment contract** - `8150dfd`
2. **Task 02: Create baseline taxonomy** - `376a88b`

## Deviations from Plan

None - plan executed exactly as written.

**Total deviations:** 0 auto-fixed.
**Impact on plan:** No scope changes.

## Verification

- `02_EXPERIMENT_CONTRACT.md` contains required evidence-family, behavioral/deterministic separation, claim-boundary, requirement, and decision-trace strings: passed.
- `02_BASELINE_TAXONOMY.md` contains the four-axis taxonomy, `SingleSidedDropoff`, `BidirectionalMP + Choice + RollingHorizon/ALNS`, and D-05 through D-08: passed.
- No intentional edits were made under `results/`, `experiments/`, `src/`, or `manuscript/sections/`. Pre-existing dirty files in those paths remain unrelated.

## Issues Encountered

None.

## Next Phase Readiness

Ready for Plan `02-02`: standalone metric definitions and coverage-confounding controls.

## Self-Check: PASSED

Plan outputs exist, acceptance criteria passed, and Phase 2 scope was preserved.

