---
phase: 09-manuscript-restructure-for-tr-part-e
plan: 09-05
subsystem: manuscript-displays-and-insights
tags: [tables, figures, captions, limitations, managerial-insights]

requires:
  - phase: 02-experimental-contract-and-metric-standardization
    provides: metric and statistical display contracts
  - phase: 06-formal-synthetic-experiments
    provides: formal result placeholders and figure/data dependencies
  - phase: 09-manuscript-restructure-for-tr-part-e
    provides: experiment-section evidence-family allocation
provides:
  - current display inventory and target roles
  - main table and figure contracts
  - caption and vocabulary checklist
  - limitations-first managerial insight template
affects: [phase-09, manuscript-experiments, manuscript-policy, manuscript-conclusion, manuscript-figures]

tech-stack:
  added: []
  patterns: [display role inventory, caption guardrail checklist, managerial insight rewrite table]

key-files:
  created:
    - .planning/phases/09-manuscript-restructure-for-tr-part-e/09_TABLE_FIGURE_PLAN.md
  modified: []

key-decisions:
  - "Replace legacy main results and baseline-comparison displays with Phase 6/8-supported formal displays."
  - "Move detailed matched-coverage, fixed accepted-set, algorithm, gamma, weight-sensitivity, and case-stress-test displays to appendix/supplement unless Phase 8 promotes limited summaries."
  - "Require main figures to come from reproducible scripts/data rather than AI-created artwork."
  - "Rename the old policy section to `Managerial Insights and Boundary Conditions`."
  - "Convert R1-R5 from recommendations into condition/insight/boundary/limitation/support-status rows."

patterns-established:
  - "Every current experiment/policy display has a target role before manuscript rewriting begins."
  - "Captions carry metric, evidence-family, and Phase 8 support checks."
  - "Managerial insights begin with limitations and conditions, not universal prescriptions."

requirements-completed: [MS-01, MS-02]

duration: 11min
completed: 2026-06-16
---

# Phase 09 Plan 05: Tables, Figures, Limitations, and Managerial Insights Plan Summary

**Display inventory, table/figure contracts, caption guardrails, and
limitations-first managerial insight template**

## Performance

- **Duration:** 11 min
- **Started:** 2026-06-16T02:50:00Z
- **Completed:** 2026-06-16T03:01:00Z
- **Tasks:** 3
- **Files modified:** 1

## Accomplishments

- Created `09_TABLE_FIGURE_PLAN.md`.
- Inventoried all current experiment and policy display labels and assigned
  each a target role.
- Defined target main-text displays and appendix/supplement display families.
- Added main table, main figure, and caption/vocabulary contracts.
- Added limitations-first boundaries for synthetic scenario evidence,
  choice-parameter calibration, missing case evidence, algorithm diagnostics,
  Phase 8 claim gating, and external validity.
- Converted R1-R5 recommendations into a conditional managerial-insight table.

## Task Commits

Each task was committed atomically:

1. **Task 09-05-01: Inventory current and target tables/figures** - `f11f749` (docs)
2. **Task 09-05-02: Define table, figure, and caption contracts** - `d4bb76c` (docs)
3. **Task 09-05-03: Convert policy recommendations into limitations-first managerial insights** - `b9354f1` (docs)

**Plan metadata:** pending in this commit.

## Files Created/Modified

- `.planning/phases/09-manuscript-restructure-for-tr-part-e/09_TABLE_FIGURE_PLAN.md` - Inventories displays, assigns target roles, defines main table/figure contracts, adds caption vocabulary checks, and provides the managerial-insight rewrite template.

## Decisions Made

- Treat `fig:policy-map` as remove/replace because the current display is too
  prescriptive for the evidence gate.
- Keep `tab:vot-mapping` as appendix/supplement calibration material rather than
  main policy evidence.
- Require unsupported Phase 8 claims to be removed, downgraded, or moved to
  limitations/future work.

## Deviations from Plan

None - plan executed exactly as written.

**Total deviations:** 0 auto-fixed.  
**Impact on plan:** No scope changes.

## Issues Encountered

- The current figure scripts include legacy titles, labels, or numeric
  annotations. The plan records this as a regeneration requirement but does not
  edit scripts during Phase 9.
- The current conclusion still contains legacy numerical claims; the plan
  explicitly requires conclusion alignment with Phase 8-gated limitations.

## Verification

- `Test-Path '.planning/phases/09-manuscript-restructure-for-tr-part-e/09_TABLE_FIGURE_PLAN.md'` returned true.
- `Select-String` found the required current labels, including `tab:main-results`, `tab:matched-coverage`, `tab:result-provenance`, `tab:beijing-results`, `tab:pareto`, `tab:weight-sensitivity`, `fig:baseline-comparison`, `fig:sensitivity`, `fig:pareto`, and `fig:policy-map`.
- `Select-String` found `Main Table Contract`, required metrics/columns, `Main Figure Contract`, `AI-created artwork`, `Caption and Vocabulary Checklist`, and `Pareto frontier`.
- `Select-String` found `Limitations Before Insights`, all required boundary conditions, `Managerial Insight Rewrite Template`, R1-R5, and `downgraded`.
- Search for legacy unplaceholdered effect-size phrases returned no matches.

## User Setup Required

None - no external service configuration required.

## Next Phase Readiness

Phase 9 now has all five manuscript-restructuring artifacts needed for review,
verification, and later manuscript drafting.

## Self-Check: PASSED

---
*Phase: 09-manuscript-restructure-for-tr-part-e*
*Completed: 2026-06-16*
