---
phase: 09-manuscript-restructure-for-tr-part-e
plan: 09-04
subsystem: manuscript-experiments
tags: [experiment-section, evidence-families, metrics, robustness, synthetic-boundary]

requires:
  - phase: 02-experimental-contract-and-metric-standardization
    provides: metric dictionary, paired-comparison protocol, baseline taxonomy, and coverage-control semantics
  - phase: 06-formal-synthetic-experiments
    provides: formal result placeholders and claim-gate dependencies
  - phase: 09-manuscript-restructure-for-tr-part-e
    provides: TR-E architecture for manuscript ordering
provides:
  - experiment-section evidence-family architecture
  - formal main-evidence table contract
  - metric denominator language rules
  - robustness, equity, diagnostic, and synthetic-case boundaries
affects: [phase-09, manuscript-experiments, manuscript-policy, manuscript-results]

tech-stack:
  added: []
  patterns: [evidence-family allocation table, claim-gated metric table contract]

key-files:
  created:
    - .planning/phases/09-manuscript-restructure-for-tr-part-e/09_EXPERIMENT_SECTION_PLAN.md
  modified: []

key-decisions:
  - "Order the experiment section as design, metrics protocol, formal main evidence, robustness, equity, diagnostics, then synthetic case boundary."
  - "Restrict the formal main-evidence table to four approved behavioral methods."
  - "Forbid ambiguous `vkm_per_trip` language and require coverage/rejection context for every efficiency statement."
  - "Treat matched coverage and fixed accepted-set controls as main-text robustness summaries with details in appendix or supplement."
  - "Treat equity as a trade-off summary, not a universal policy claim."
  - "Require current Beijing language to use `Beijing-inspired synthetic scenario`."

patterns-established:
  - "Experiment displays are assigned by evidence family before numerical values are finalized."
  - "Diagnostic evidence must remain subordinate to formal behavioral evidence unless Phase 8 explicitly promotes a limited summary."

requirements-completed: [MS-01, MS-02]

duration: 10min
completed: 2026-06-16
---

# Phase 09 Plan 04: Experiment Section and Evidence-Family Plan Summary

**Experiment-section architecture with formal evidence, robustness, diagnostic,
equity, and synthetic-boundary rules**

## Performance

- **Duration:** 10 min
- **Started:** 2026-06-16T02:39:00Z
- **Completed:** 2026-06-16T02:49:00Z
- **Tasks:** 3
- **Files modified:** 1

## Accomplishments

- Created `09_EXPERIMENT_SECTION_PLAN.md`.
- Defined the target experiment-section order from design through synthetic-case
  boundaries.
- Specified the formal main-evidence table contract and approved behavioral
  method labels.
- Added denominator rules that forbid ambiguous `vkm_per_trip` language.
- Allocated matched coverage, fixed accepted-set controls, equity, algorithm
  diagnostics, gamma, and weight sensitivity to appropriate manuscript roles.
- Required the exact phrase `Beijing-inspired synthetic scenario` for current
  Beijing-related material.

## Task Commits

Each task was committed atomically:

1. **Task 09-04-01: Define experiment section architecture and evidence-family order** - `7b9029c` (docs)
2. **Task 09-04-02: Specify formal main-evidence table and metric-denominator rules** - `a1aa1f0` (docs)
3. **Task 09-04-03: Define robustness, equity, diagnostic, and synthetic-case boundaries** - `da61348` (docs)

**Plan metadata:** pending in this commit.

## Files Created/Modified

- `.planning/phases/09-manuscript-restructure-for-tr-part-e/09_EXPERIMENT_SECTION_PLAN.md` - Defines current experiment-section risks, target architecture, evidence-family order, formal table contract, metric language rules, robustness/diagnostic allocation, and synthetic case boundary.

## Decisions Made

- Keep final numerical results blocked until Phase 6 formal artifacts and Phase
  8 claim-gate artifacts are available.
- Use `total_vehicle_km` as the paper-facing column while allowing raw outputs
  to map from `total_vkm`.
- Keep ALNS, greedy, no-rolling-horizon, no-choice, MILP, gamma, and
  weight-sensitivity evidence diagnostic unless Phase 8 promotes a limited
  summary.

## Deviations from Plan

None - plan executed exactly as written.

**Total deviations:** 0 auto-fixed.  
**Impact on plan:** No scope changes.

## Issues Encountered

- The verification command for method labels required literal matching because
  PowerShell treats `+` as a regex operator. The file contains all exact
  approved labels.

## Verification

- `Test-Path '.planning/phases/09-manuscript-restructure-for-tr-part-e/09_EXPERIMENT_SECTION_PLAN.md'` returned true.
- `Select-String` found `Target Experiment Section Architecture`, `Formal Main Evidence`, `Robustness Controls`, and `Phase 8`.
- Literal `Select-String` found all four approved method labels.
- `Select-String` found `total_vehicle_km`, `vkm_per_served_trip`, `vkm_per_original_request`, `served_share`, and `vkm_per_trip is forbidden`.
- `Select-String` found `Robustness and Diagnostic Allocation`, `fixed accepted-set`, `Beijing-inspired synthetic scenario`, and `trade-off summary`.
- Search for legacy unplaceholdered effect-size phrases returned no matches.

## User Setup Required

None - no external service configuration required.

## Next Phase Readiness

The table/figure plan can use this artifact to assign each table, figure, and
policy display to a formal, robustness, diagnostic, appendix, supplement, or
limitations role.

## Self-Check: PASSED

---
*Phase: 09-manuscript-restructure-for-tr-part-e*
*Completed: 2026-06-16*
