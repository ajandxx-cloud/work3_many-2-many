---
phase: 01-literature-and-novelty-audit
plan: 01-01
subsystem: docs
tags: [literature-audit, novelty-positioning, claims, tr-e, drt]
requires:
  - phase: 00-repository-and-manuscript-audit
    provides: manuscript claim audit, repository audit, current experiment map
provides:
  - citation-by-claim matrix for meeting-point, choice, dynamic DRT, and ALNS positioning
  - allowed, risky, forbidden, and unresolved novelty wording contract
  - revised conditional research questions for later evidence phases
  - Phase 1 updates to the claim and risk register
affects: [phase-02-experiment-contract, phase-08-claim-gate, phase-09-manuscript-restructure]
tech-stack:
  added: []
  patterns: [citation-by-claim matrix, conservative novelty wording gate, downstream evidence ownership]
key-files:
  created:
    - .planning/phases/01-literature-and-novelty-audit/01_LITERATURE_AUDIT.md
    - .planning/phases/01-literature-and-novelty-audit/01_NOVELTY_POSITIONING.md
    - .planning/phases/01-literature-and-novelty-audit/01_REVISED_RESEARCH_QUESTIONS.md
  modified:
    - .planning/CLAIMS_AND_RISKS.md
    - .planning/REQUIREMENTS.md
    - .planning/ROADMAP.md
    - .planning/STATE.md
key-decisions:
  - "Do not preserve broad first/only novelty language for bidirectional meeting points."
  - "Use TR-E-level rigor as the planning bar while leaving final venue choice to later manuscript strategy."
  - "Center the contribution on an integrated choice-aware dynamic service-design simulation framework."
patterns-established:
  - "Novelty claims are classified as allowed, risky, forbidden, or unresolved before manuscript editing."
  - "Residual literature and bibliography issues are assigned to downstream phase owners."
requirements-completed: [POS-01, POS-02, POS-03]
duration: 13 min
completed: 2026-06-15
---

# Phase 01 Plan 01: Literature and Novelty Audit Summary

**Citation-backed novelty positioning contract for bidirectional meeting-point DRT under conservative TR-E evidence standards**

## Performance

- **Duration:** 13 min
- **Started:** 2026-06-15T02:19:00Z
- **Completed:** 2026-06-15T02:32:34Z
- **Tasks:** 4
- **Files modified:** 7

## Accomplishments

- Built a citation-by-claim matrix covering Cortenbach et al. (2024), Fielbaum et al. (2021), Wu et al. (2025), Alonso-Mora-style dynamic assignment, current manuscript references, and supporting DARP/DRT/ALNS background.
- Reclassified novelty language so unsupported "first", "only", and pickup-side-only claims are forbidden or unresolved.
- Established the conservative contribution center: an integrated choice-aware dynamic service-design simulation framework.
- Revised research questions so later phases test conditional evidence rather than universal superiority.
- Updated `.planning/CLAIMS_AND_RISKS.md` and marked POS-01, POS-02, and POS-03 complete for planning with residual citation cleanup assigned downstream.

## Task Commits

Each task was committed atomically:

1. **Task 01: Build literature corpus and citation-by-claim matrix** - `1dba2c8`
2. **Task 02: Define novelty positioning contract** - `7aec699`
3. **Task 03: Revise research questions and risk register** - `26d4d29`

**Plan metadata:** committed after this summary with STATE, ROADMAP, and REQUIREMENTS updates.

## Files Created/Modified

- `.planning/phases/01-literature-and-novelty-audit/01_LITERATURE_AUDIT.md` - Literature corpus, source notes, citation-by-claim matrix, blockers, and POS-01 coverage.
- `.planning/phases/01-literature-and-novelty-audit/01_NOVELTY_POSITIONING.md` - Allowed/risky/forbidden/unresolved wording and TR-E vs TR-A positioning recommendation.
- `.planning/phases/01-literature-and-novelty-audit/01_REVISED_RESEARCH_QUESTIONS.md` - Five conditional research questions mapped to later evidence phases.
- `.planning/CLAIMS_AND_RISKS.md` - Phase 1 claim/risk section with approved, forbidden, unresolved, and venue-positioning entries.
- `.planning/REQUIREMENTS.md` - POS-01, POS-02, and POS-03 marked complete for planning.
- `.planning/ROADMAP.md` - Phase 1 plan progress synchronized after summary creation.
- `.planning/STATE.md` - Phase execution state advanced to ready for verification.

## Decisions Made

1. Broad "first bidirectional meeting-point DRT" language is not approved.
2. The current manuscript's "existing work assigns meeting points only on the pickup side" claim is forbidden unless later full-text review overturns the audit.
3. Fielbaum et al. (2021) directly narrows any dropoff-walking novelty claim.
4. Cortenbach et al. (2024) and Wu et al. (2025) local bibliography metadata should be corrected during manuscript restructuring.
5. TR-E-level rigor is the planning bar; policy framing remains secondary until external-validity evidence improves.

## Deviations from Plan

None - plan executed within the documented boundary. The only extra action was external metadata verification for required literature targets, which the plan explicitly required where local sources could not verify scope.

**Total deviations:** 0 auto-fixed.
**Impact on plan:** No scope creep. No experiment scripts, result files, or manuscript section files were edited.

## Issues Encountered

- Git history contained older `01-01` commits from a deleted previous phase directory. This was a stale history collision, not current Phase 1 work, so execution continued after path inspection.
- The checkout already had unrelated dirty changes before this plan, including result-file and historical-directory changes. This plan did not modify or stage those files.
- Review-note raw filename from Phase 1 context was not readable under the expected path. Phase 0 extracted the needed risks, so the blocker was recorded for Phase 10 provenance cleanup.
- Local bibliography metadata for Cortenbach et al. (2024) and Wu et al. (2025) appears inconsistent with external metadata; this was recorded as a downstream manuscript cleanup risk.

## Verification

- Required artifacts exist: passed.
- `01_LITERATURE_AUDIT.md` contains the required matrix columns and the strings `Cortenbach`, `Fielbaum`, `Wu`, and `Alonso-Mora`: passed.
- `01_NOVELTY_POSITIONING.md` contains allowed/risky/forbidden/unresolved wording classes and a TR-E vs TR-A recommendation: passed.
- `.planning/CLAIMS_AND_RISKS.md` contains `Phase 1 Literature and Novelty Audit`: passed.
- POS-01, POS-02, and POS-03 are complete for planning, with residual citation risks explicit: passed.
- No files under `results/` or `manuscript/sections/` were intentionally modified by this plan. Pre-existing dirty changes in those paths remain outside this plan's staged commits.

## User Setup Required

None - no external service configuration required.

## Next Phase Readiness

Phase 2 can now define experiment contracts and metric standards without relying on unsafe novelty claims. Phase 8 should treat this summary as a claim-gate input, and Phase 9 should correct the bibliography metadata before manuscript rewriting.

## Self-Check: PASSED

All plan artifacts were created, acceptance criteria were checked, and the phase boundary was preserved.

---
*Phase: 01-literature-and-novelty-audit*
*Completed: 2026-06-15*
