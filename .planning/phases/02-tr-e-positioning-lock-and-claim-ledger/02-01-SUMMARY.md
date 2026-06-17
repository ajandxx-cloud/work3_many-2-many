---
phase: 02-tr-e-positioning-lock-and-claim-ledger
plan: 02-01
subsystem: claim-governance
tags: [tr-e, positioning, evidence-boundary, claim-control]

requires:
  - phase: 01-evidence-foundation-and-milestone-setup
    provides: milestone plan, repository/evidence audit, manuscript action plan
provides:
  - TR-E positioning lock with allowed framing, prohibited framing, core contribution, journal-fit rationale, evidence-role boundaries, safe sentences, downstream routing, and readiness-label boundary
affects: [phase-03-manuscript-repositioning, phase-04-numerical-provenance, phase-05-readiness-closeout]

tech-stack:
  added: []
  patterns: [planning governance artifact, evidence-role boundary table, downstream routing table]

key-files:
  created:
    - .planning/milestones/tr_e_claim_ready/02_TR_E_POSITIONING_LOCK.md
  modified: []

key-decisions:
  - "The manuscript is locked as operational service-design evidence for TR-E, not policy validation or optimization-method supremacy."
  - "The strongest allowed mechanism label is passenger-response-aware simulation framework."
  - "Diagnostic matched-coverage, fixed-accepted-set, Gamma/Pareto, and MILP evidence require explicit diagnostic qualifiers."
  - "TR-E submission-ready is reserved for Phase 5 after hard readiness gates pass."

patterns-established:
  - "Positioning lock pattern: allowed wording, prohibited wording, downstream owner."
  - "Evidence role boundary pattern: role label, Phase 3 use, prohibited use."
  - "Routing pattern: Phase 3 wording, Phase 4 numerical provenance, Phase 5 readiness, future/v2 gaps."

requirements-completed: [CLAI-01, CLAI-04]

duration: 4 min
completed: 2026-06-17
---

# Phase 02 Plan 01: Write TR-E Positioning Lock And Journal-Fit Rationale Summary

**TR-E positioning lock with conditional logistics/operations framing, diagnostic evidence boundaries, and Phase 5-only readiness labeling**

## Performance

- **Duration:** 4 min
- **Started:** 2026-06-17T10:09:35Z
- **Completed:** 2026-06-17T10:14:12Z
- **Tasks:** 2
- **Files modified:** 1

## Accomplishments

- Created `.planning/milestones/tr_e_claim_ready/02_TR_E_POSITIONING_LOCK.md`.
- Locked the allowed TR-E contribution as operational service-design evidence with the required passenger-response-aware simulation framework label.
- Explicitly prohibited policy-first framing, universal dominance, real-world Beijing validation, endogenous Gamma/Pareto control, co-optimization wording, and exact dynamic benchmark or ALNS near-optimality claims.
- Added evidence-role boundaries for primary behavioral evidence, diagnostics, robustness/sensitivity, equity/type heterogeneity, algorithm diagnostics, and limitations.
- Added Phase 3 safe sentences, downstream routing rules, and the Phase 5-only `TR-E submission-ready` boundary.

## Task Commits

Each task was committed atomically:

1. **Task 1: Create the allowed and prohibited TR-E framing lock** - `d54e1c8` (docs)
2. **Task 2: Add evidence-role boundaries, safe sentences, and routing rules** - `a7ac651` (docs)

**Plan metadata:** committed with this summary.

## Files Created/Modified

- `.planning/milestones/tr_e_claim_ready/02_TR_E_POSITIONING_LOCK.md` - TR-E positioning, prohibited framing, core contribution, evidence-role boundaries, safe sentences, routing, and readiness-label lock.

## Decisions Made

- The manuscript must be framed as `operational service-design evidence`, not policy validation, a deployable decision tool, or optimization-method supremacy.
- `passenger-response-aware simulation framework` is the strongest allowed mechanism label.
- Matched coverage, fixed accepted set, MILP, and Gamma/Pareto material require exact diagnostic qualifiers before downstream prose may use them.
- Phase 3 owns non-numeric wording; Phase 4 owns final numerical provenance; Phase 5 owns package/readiness verification; future/v2 owns real Beijing data, endogenous Gamma behavior, and full exact dynamic benchmark gaps.

## Deviations from Plan

None - plan executed exactly as written.

**Total deviations:** 0 auto-fixed.
**Impact on plan:** No scope expansion; manuscript, results, source, experiments, analysis, package docs, and dependency files were not edited.

## Issues Encountered

None.

## Known Stubs

| File | Line | Reason |
|------|------|--------|
| `.planning/milestones/tr_e_claim_ready/02_TR_E_POSITIONING_LOCK.md` | 72 | The word "placeholders" is an intentional Phase 4 gating instruction for future verified numerical text, not a missing implementation or data stub. |

## Threat Flags

None - this plan created a planning governance artifact only and introduced no new network endpoint, auth path, file-access behavior, schema change, or runtime trust boundary beyond the plan's documented wording-to-planning trust boundary.

## Verification

Passed:

- `Test-Path .planning\milestones\tr_e_claim_ready\02_TR_E_POSITIONING_LOCK.md`
- `rg -n "Allowed TR-E Framing|Prohibited Framing|Core Contribution Lock|Journal-Fit Rationale|Evidence Role Boundaries|Safe Sentences Phase 3 May Use|Downstream Routing|Readiness Label Boundary" .planning\milestones\tr_e_claim_ready\02_TR_E_POSITIONING_LOCK.md`
- `rg -n "operational service-design evidence|passenger-response-aware simulation framework|post-hoc welfare or sensitivity accounting|simplified ex-post diagnostic over fixed accepted sets" .planning\milestones\tr_e_claim_ready\02_TR_E_POSITIONING_LOCK.md`
- `rg -n "18\.3%|29\.1%|35\.0%|0\.1216" .planning\milestones\tr_e_claim_ready\02_TR_E_POSITIONING_LOCK.md` returned no matches.
- `git diff --name-only -- manuscript results src experiments analysis README.md CLAUDE.md pyproject.toml` returned no paths.

## Self-Check: PASSED

- Created file exists: `.planning/milestones/tr_e_claim_ready/02_TR_E_POSITIONING_LOCK.md`.
- Task commit exists: `d54e1c8`.
- Task commit exists: `a7ac651`.
- Required sections, required phrases, diagnostic qualifier phrases, downstream routing, and readiness boundary were verified with `rg`.

## User Setup Required

None - no external service configuration required.

## Next Phase Readiness

Ready for Plan 02-02 to build the occurrence-level claim ledger against the positioning lock and formal Phase 6 evidence boundaries.

---
*Phase: 02-tr-e-positioning-lock-and-claim-ledger*
*Completed: 2026-06-17*
