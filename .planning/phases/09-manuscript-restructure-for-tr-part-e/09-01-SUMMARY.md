---
phase: 09-manuscript-restructure-for-tr-part-e
plan: 09-01
subsystem: manuscript-architecture
tags: [manuscript, tr-e, claim-gate, evidence-family, documentation]

requires:
  - phase: 01-literature-and-novelty-audit
    provides: novelty and venue-positioning guardrails
  - phase: 02-experimental-contract-and-metric-standardization
    provides: evidence-family and metric-denominator rules
  - phase: 06-formal-synthetic-experiments
    provides: formal-evidence design boundaries
provides:
  - TR-E evidence-chain manuscript architecture
  - old-to-new manuscript section map
  - Phase 8 claim placeholder policy
  - evidence-family placement and direct LaTeX edit boundaries
affects: [phase-09, manuscript, phase-10-reproducibility, claim-gate]

tech-stack:
  added: []
  patterns: [claim-gated manuscript planning, evidence-family placement table]

key-files:
  created:
    - .planning/phases/09-manuscript-restructure-for-tr-part-e/09_TR_E_MANUSCRIPT_STRUCTURE.md
  modified: []

key-decisions:
  - "Use evidence-chain reconstruction as the source-of-truth manuscript story."
  - "Keep final claim wording blocked on the three Phase 8 claim-gate artifacts."
  - "Place behavioral main comparisons, supplementary controls, deterministic diagnostics, and algorithm diagnostics in separate manuscript roles."
  - "Prevent direct LaTeX edits from introducing unsupported final claims."

patterns-established:
  - "Phase 9 manuscript artifacts use placeholders until Phase 8 supported claims exist."
  - "Manuscript restructuring maps current LaTeX files to TR-E evidence-chain sections before direct edits."

requirements-completed: [MS-01, MS-02]

duration: 14min
completed: 2026-06-16
---

# Phase 09 Plan 01: TR-E Manuscript Architecture and Claim-Gate Map Summary

**TR-E evidence-chain architecture with Phase 8 claim blockers, manuscript section mapping, and evidence-family placement rules**

## Performance

- **Duration:** 14 min
- **Started:** 2026-06-16T02:40:00Z
- **Completed:** 2026-06-16T02:54:00Z
- **Tasks:** 3
- **Files modified:** 1

## Accomplishments

- Created the source-of-truth Phase 9 manuscript architecture artifact.
- Mapped every current `manuscript/sections/*.tex` file to a target TR-E section role.
- Recorded the missing Phase 8 claim-gate artifacts as blocking inputs for final wording.
- Defined evidence-family placement rules and direct LaTeX edit boundaries.

## Task Commits

Each task was committed atomically:

1. **Task 09-01-01: Audit current section order and build the old-to-new manuscript map** - `ea20157` (docs)
2. **Task 09-01-02: Record Phase 8 claim-gate blockers and placeholder policy** - `69ce553` (docs)
3. **Task 09-01-03: Define evidence-family placement and direct-edit boundaries** - `ba1e894` (docs)

**Plan metadata:** pending in this commit.

## Files Created/Modified

- `.planning/phases/09-manuscript-restructure-for-tr-part-e/09_TR_E_MANUSCRIPT_STRUCTURE.md` - Defines the TR-E architecture, old-to-new section map, Phase 8 blockers, placeholder policy, evidence-family placement, and direct LaTeX edit boundary.

## Decisions Made

- Use the nine-section TR-E evidence-chain architecture from Phase 9 context.
- Treat absent Phase 8 artifacts as blockers for final abstract, introduction, captions, conclusion, and managerial insight wording.
- Keep deterministic and algorithm diagnostics out of headline behavioral claims.
- Require later direct LaTeX edits to cite Phase 8 supported claims or remain placeholders.

## Deviations from Plan

None - plan executed exactly as written.

**Total deviations:** 0 auto-fixed.
**Impact on plan:** No scope changes.

## Issues Encountered

- Safe-resume search found old `09-01` commits from a previous phase-numbering scheme. Inspection showed those commits touched `.planning/phases/09-paper-section-updates/` and `paper/`, not the current Phase 9 output, so this was treated as a phase-number reuse false positive.

## Verification

- `Test-Path '.planning/phases/09-manuscript-restructure-for-tr-part-e/09_TR_E_MANUSCRIPT_STRUCTURE.md'` returned true.
- `Select-String` found `Phase 8 Blocking Inputs`, `Claim Placeholder Policy`, `Evidence Family Placement Rules`, and `Direct LaTeX Edit Boundary`.
- `git diff --name-only -- 'manuscript/sections/*.tex'` returned no direct manuscript section edits.

## User Setup Required

None - no external service configuration required.

## Next Phase Readiness

Wave 1 can continue with the abstract/highlights planning artifact. Wave 2 can use this structure artifact as the vocabulary source for the introduction and experiment-section plans.

## Self-Check: PASSED

---
*Phase: 09-manuscript-restructure-for-tr-part-e*
*Completed: 2026-06-16*
