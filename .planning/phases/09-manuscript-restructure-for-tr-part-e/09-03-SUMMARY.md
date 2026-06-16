---
phase: 09-manuscript-restructure-for-tr-part-e
plan: 09-03
subsystem: manuscript-introduction
tags: [introduction, literature-positioning, research-questions, claim-gate]

requires:
  - phase: 01-literature-and-novelty-audit
    provides: novelty positioning and revised research questions
  - phase: 09-manuscript-restructure-for-tr-part-e
    provides: TR-E architecture and abstract/front-matter framing
provides:
  - evidence-gap-first introduction flow
  - three approved research questions
  - contribution order
  - literature positioning rewrite rules
affects: [phase-09, manuscript-introduction, manuscript-literature]

tech-stack:
  added: []
  patterns: [evidence-gap-first introduction outline, novelty-risk rewrite table]

key-files:
  created:
    - .planning/phases/09-manuscript-restructure-for-tr-part-e/09_REVISED_INTRODUCTION_PLAN.md
  modified: []

key-decisions:
  - "Open the introduction with evidence confounding: passenger response, coverage, baseline inconsistency, and diagnostic/result mixing."
  - "Use exactly three manuscript research questions for Phase 9 framing."
  - "Order contributions as evidence discipline, model/framework, experimental findings, managerial implications."
  - "Treat unresolved literature items as blockers rather than safe novelty claims."

patterns-established:
  - "Numbered research questions are isolated in their own section for easy transfer to manuscript prose."
  - "Literature positioning uses allowed replacement language with required source and Phase 8 dependency columns."

requirements-completed: [MS-01]

duration: 12min
completed: 2026-06-16
---

# Phase 09 Plan 03: Introduction and Literature Positioning Plan Summary

**Evidence-gap-first introduction plan with three claim-gated research questions and literature rewrite rules**

## Performance

- **Duration:** 12 min
- **Started:** 2026-06-16T03:04:00Z
- **Completed:** 2026-06-16T03:16:00Z
- **Tasks:** 3
- **Files modified:** 1

## Accomplishments

- Created `09_REVISED_INTRODUCTION_PLAN.md`.
- Planned an introduction that opens with passenger response, coverage,
  baseline inconsistency, and diagnostic/result mixing.
- Added exactly three approved research questions and locked the contribution
  order.
- Added literature positioning rewrite rules to prevent broad first/only and
  pickup-side-only overclaims.

## Task Commits

Each task was committed atomically:

1. **Task 09-03-01: Create the revised introduction flow and paragraph-level outline** - `cdcd53f` (docs)
2. **Task 09-03-02: Add approved research questions and contribution ordering** - `59d427a` (docs)
3. **Task 09-03-03: Define literature positioning rewrite rules** - `5a2fa73` (docs)

**Plan metadata:** pending in this commit.

## Files Created/Modified

- `.planning/phases/09-manuscript-restructure-for-tr-part-e/09_REVISED_INTRODUCTION_PLAN.md` - Defines current introduction risks, revised flow, paragraph outline, research questions, contribution order, and literature positioning rewrite rules.

## Decisions Made

- Keep algorithm diagnostics as methodological support, not a standalone research question.
- Use broader integrated-framework positioning unless exact citation and Phase 8 evidence support a narrower claim.
- Mark unresolved Cortenbach/DARPmp/ridepooling overlap as a blocker for precise novelty wording.

## Deviations from Plan

None - plan executed exactly as written.

**Total deviations:** 0 auto-fixed.
**Impact on plan:** No scope changes.

## Issues Encountered

- Safe-resume search found old `09-03` commits from a previous phase-numbering scheme. No current Phase 9 introduction artifact or summary existed, so this was treated as a phase-number reuse false positive.

## Verification

- `Test-Path '.planning/phases/09-manuscript-restructure-for-tr-part-e/09_REVISED_INTRODUCTION_PLAN.md'` returned true.
- `Select-String` found `Research Questions`, `Contribution Order`, and `Literature Positioning Rewrite Rules`.
- A line-based check found exactly three numbered research-question lines ending in question marks.
- Search for unsupported final effect-size phrases returned no matches.

## User Setup Required

None - no external service configuration required.

## Next Phase Readiness

The experiment-section and table/figure plans can reuse this evidence-gap-first introduction vocabulary and literature guardrails.

## Self-Check: PASSED

---
*Phase: 09-manuscript-restructure-for-tr-part-e*
*Completed: 2026-06-16*
