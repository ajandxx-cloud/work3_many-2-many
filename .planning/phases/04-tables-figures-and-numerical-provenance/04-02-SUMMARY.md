---
phase: 04-tables-figures-and-numerical-provenance
plan: 02
subsystem: manuscript-provenance
tags: [claim-ledger, manuscript, formal-phase06, table-first, latex]

requires:
  - phase: 04-01
    provides: formal Phase 6 manuscript table and figure assets
provides:
  - Ledger-controlled numerical occurrence queue
  - Formal table and figure integration in experiments
  - Clean non-numeric front and back manuscript sections
affects: [phase-04, phase-05, manuscript, claim-ledger]

tech-stack:
  added: []
  patterns:
    - experiments prose points to one generated table and one generated figure
    - front/back sections remain non-numeric while concrete values live in generated artifacts

key-files:
  created:
    - .planning/phases/04-tables-figures-and-numerical-provenance/04-02-SUMMARY.md
  modified:
    - .planning/milestones/tr_e_claim_ready/03_CLAIM_LEDGER.md
    - manuscript/sections/abstract.tex
    - manuscript/sections/experiments.tex
    - manuscript/sections/policy.tex
    - manuscript/sections/conclusion.tex
    - manuscript/tables/phase06_main_behavioral_table.tex
    - experiments/formal_statistics.py
    - manuscript/main.pdf

key-decisions:
  - "Final values remain in the generated formal table/figure rather than abstract, introduction, implications, or conclusion prose."
  - "The ledger records Phase 4 queue outcomes while preserving historical blocker rows for audit traceability."
  - "Negated prohibited wording such as universal was replaced with non-triggering conditional language."

patterns-established:
  - "Ledger queue outcomes are recorded in a separate Phase 4 section instead of deleting historical rows."
  - "Manuscript result integration is table-first and denominator-aware."

requirements-completed: [TFIG-04]

duration: 5 min
completed: 2026-06-18
---

# Phase 04 Plan 02: Reconcile Numerical Claims and Inject Verified Manuscript Values Summary

**The active manuscript now presents formal Phase 6 values through one generated table and one generated figure, with prose kept conditional and non-overclaiming.**

## Performance

- **Duration:** 5 min
- **Started:** 2026-06-18T03:14:00Z
- **Completed:** 2026-06-18T03:19:19Z
- **Tasks:** 3
- **Files modified:** 12

## Accomplishments

- Added a Phase 4 active numerical occurrence queue to `03_CLAIM_LEDGER.md`.
- Integrated `manuscript/tables/phase06_main_behavioral_table.tex` into the experiments section.
- Integrated `manuscript/figures/fig04_phase06_main_efficiency_coverage.png` into the experiments section.
- Kept abstract, introduction, managerial/operational implications, and conclusion non-numeric.
- Removed broad prohibited-word scan hits by replacing negated `universal` language with conditional wording.
- Recompiled `manuscript/main.tex` successfully with `pdflatex` after the table and figure integration.

## Task Commits

1. **Task 1-3: Reconcile ledger, integrate formal table/figure, and clean front/back sections** - `85348f9` (feat)

## Files Created/Modified

- `.planning/milestones/tr_e_claim_ready/03_CLAIM_LEDGER.md` - Adds Phase 4 active numerical occurrence queue outcomes.
- `manuscript/sections/experiments.tex` - Adds formal table/figure references, includes the generated table, and inserts the formal main figure.
- `manuscript/sections/abstract.tex` - Replaces negated prohibited wording with conditional wording.
- `manuscript/sections/policy.tex` - Replaces negated prohibited wording with conditional wording.
- `manuscript/sections/conclusion.tex` - Replaces negated prohibited wording with conditional wording.
- `experiments/formal_statistics.py` - Tightens generated LaTeX table formatting and notes.
- `manuscript/tables/phase06_main_behavioral_table.tex` - Regenerated with escaped LaTeX paths and resized tabular.
- `manuscript/main.pdf` - Recompiled manuscript PDF.

## Decisions Made

- Active manuscript prose does not repeat old headline numbers; historical blocker rows remain in the ledger.
- Diagnostic numerical families remain qualitative/deferred in active prose instead of becoming main-text headline values.
- Formal table/figure captions and notes carry concise provenance, while detailed formulas and source paths remain in the ledger.

## Deviations from Plan

### Auto-fixed Issues

**1. [Rule 3 - Blocking] Generated LaTeX paths contained raw underscores**
- **Found during:** Task 2 (Integrate the main formal table and figure into experiments)
- **Issue:** Raw file paths in table notes and figure caption could break or clutter LaTeX output.
- **Fix:** Escaped paths in generated table notes and shortened the figure caption to reference formal closeout provenance.
- **Files modified:** `experiments/formal_statistics.py`, `manuscript/sections/experiments.tex`, `manuscript/tables/phase06_main_behavioral_table.tex`
- **Verification:** `pdflatex -interaction=nonstopmode main.tex` completed successfully.
- **Committed in:** `85348f9`

**2. [Rule 3 - Blocking] Broad prohibited-word scan caught negated universal wording**
- **Found during:** Task 3 (Clean front/back sections)
- **Issue:** Negated uses of `universal` in abstract, implications, and conclusion tripped the plan-level scan.
- **Fix:** Replaced with `unconditional` phrasing while preserving the conditional claim posture.
- **Files modified:** `manuscript/sections/abstract.tex`, `manuscript/sections/policy.tex`, `manuscript/sections/conclusion.tex`
- **Verification:** Broad unsafe-manuscript scan passed.
- **Committed in:** `85348f9`

---

**Total deviations:** 2 auto-fixed blocking manuscript-integration issues.
**Impact on plan:** Both fixes improve compile safety and wording-gate cleanliness without changing formal evidence values.

## Issues Encountered

- `pdflatex` reports existing layout warnings, including overfull boxes and float-size warnings in pre-existing sections. The compile exits successfully and writes `main.pdf`; these warnings are non-blocking for this plan.
- MiKTeX reports an update notice. This is environmental and not manuscript-critical.

## Verification

- Old-number scan over active manuscript returned no hits.
- Experiments table/figure reference scan passed.
- Broad unsafe wording scan over `manuscript/main.tex` and `manuscript/sections` passed.
- Front/back sections contain no old numbers, Phase 4 placeholders, significance language, or numeric table/figure references.
- Ledger mandatory provenance-field scan passed and records Phase 4 queue outcomes.
- `pdflatex -interaction=nonstopmode main.tex` completed successfully after two passes.

## User Setup Required

None - no external service configuration required.

## Next Phase Readiness

Ready for `04-03`: active manuscript values and table/figure references are now ledger-controlled, and provenance verification can focus on denominators, formulas, source paths, Gamma/sensitivity boundaries, and validation hooks.

---
*Phase: 04-tables-figures-and-numerical-provenance*
*Completed: 2026-06-18*
