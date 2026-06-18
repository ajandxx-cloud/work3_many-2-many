---
phase: 04-tables-figures-and-numerical-provenance
plan: 04-03
subsystem: publication-provenance
tags: [phase6, provenance, denominators, gamma, robustness]

requires:
  - phase: 04-tables-figures-and-numerical-provenance
    provides: manuscript-ready formal Phase 6 table and figure assets
provides:
  - Phase 4 denominator, formula, Gamma, diagnostic-role, and source-provenance report
  - Final claim-ledger queue row closing TFIG-05 and TFIG-06
  - Validator-backed handoff notes for Phase 5 readiness closeout
affects: [phase-05-readiness, claim-ledger, manuscript-verification]

tech-stack:
  added: []
  patterns: [formal Phase 6 provenance reporting, denominator-first numerical claim audit]

key-files:
  created:
    - .planning/milestones/tr_e_claim_ready/06_PHASE4_PROVENANCE_CHECK.md
  modified:
    - .planning/milestones/tr_e_claim_ready/03_CLAIM_LEDGER.md
    - .planning/REQUIREMENTS.md
    - .planning/STATE.md

key-decisions:
  - "Weight sensitivity remains valid because robustness summaries use the same vkm_per_served_trip, vkm_per_original_request, and served_share metric columns validated by formal validators."
  - "Gamma remains post-hoc accounting only; active manuscript sources do not promote it into routing, offer-generation, acceptance, policy-control, or Pareto-control semantics."
  - "Matched coverage, fixed accepted set, equity/type, Beijing-inspired, and MILP evidence remain diagnostic, exploratory, robustness, or limitation material rather than headline primary evidence."

patterns-established:
  - "Phase-level provenance reports cite exact commands, source paths, denominator formulas, diagnostic roles, and remaining downstream package risks."
  - "Validation commands that mutate formal run-manifest metadata must not be committed unless a formal rerun actually occurred."

requirements-completed: [TFIG-05, TFIG-06]

duration: 7min
completed: 2026-06-18
---

# Phase 04 Plan 04-03 Summary: Provenance Verification

**Validator-backed denominator and source-provenance audit for Phase 4 numerical claims**

## Performance

- **Duration:** 7 min
- **Started:** 2026-06-18T11:20:00+08:00
- **Completed:** 2026-06-18T11:27:00+08:00
- **Tasks:** 3
- **Files modified:** 4

## Accomplishments

- Created `.planning/milestones/tr_e_claim_ready/06_PHASE4_PROVENANCE_CHECK.md` documenting denominator formulas, validation commands, source paths, Gamma boundaries, diagnostic roles, and Phase 5 risks.
- Added `Q-04-03-01` to the active claim-ledger queue, closing `TFIG-05` and `TFIG-06` with explicit source/script/command/formula/numerator/denominator fields.
- Verified formal statistics, main behavioral outputs, coverage controls, robustness/equity/algorithm diagnostics, and active manuscript unsafe-content scans.

## Task Commits

1. **Task 1-3: Phase 4 provenance report and ledger closure** - `df35a72` (`feat(04-03): record phase 4 provenance checks`)

**Plan metadata:** pending in this summary commit.

## Files Created/Modified

- `.planning/milestones/tr_e_claim_ready/06_PHASE4_PROVENANCE_CHECK.md` - Records Phase 4 denominator, formula, Gamma, diagnostic-role, and source-provenance checks.
- `.planning/milestones/tr_e_claim_ready/03_CLAIM_LEDGER.md` - Adds `Q-04-03-01` for denominator and weight-sensitivity closure.
- `.planning/REQUIREMENTS.md` - Marks `TFIG-05` and `TFIG-06` complete.
- `.planning/STATE.md` - Advances Phase 4 to ready for verification.

## Verification

- `$env:PYTHONPATH='src'; python -m experiments.formal_statistics --validate --results-dir results/formal/phase06` - passed.
- `$env:PYTHONPATH='src'; python -m experiments.phase06_formal --validate --results-dir results/formal/phase06/main_behavioral` - passed, with all main denominator checks passed.
- `$env:PYTHONPATH='src'; python -m experiments.phase06_coverage_controls --validate --package all` - passed; matched coverage keeps 15 durable failed rows as a diagnostic limitation.
- `$env:PYTHONPATH='src'; python -m experiments.phase06_robustness --validate --package all` - passed, including utility sensitivity, meeting-point density, fleet stress, equity/type, and algorithm diagnostics.
- Report existence/content checks passed for `TFIG-05`, `TFIG-06`, required metric names, weight sensitivity, Gamma, and source provenance.
- Active manuscript/table unsafe scan passed for old values, Phase 4 placeholders, non-canonical root result paths, unsupported significance wording, and prohibited wording.

## Decisions Made

- Denominator formulas are accepted as validated: `served_share = n_served / n_requests`, `vkm_per_original_request = vehicle_km / n_requests`, `vkm_per_served_trip = vehicle_km / n_served`, rejection rates use `n_requests`, and `behavioral_acceptance_rate = 1.0 - choice_rejection_rate`.
- Weight sensitivity is not acceptance-denominator inflated because `robustness_setting_summary.csv` is built from the shared formal metric columns and the robustness validator repeats denominator checks.
- Gamma numerical detail remains post-hoc/supplementary or diagnostic only; the active manuscript contains only non-numeric post-hoc boundary wording.

## Deviations from Plan

### Auto-fixed Issues

**1. Validation command mutated formal run-manifest metadata**
- **Found during:** Task 1 validation.
- **Issue:** Running the main behavioral validator rewrote `finished_at_utc` and `git_commit_before_run` in `results/formal/phase06/main_behavioral/formal_run_manifest.json` and `run_manifest.json`, making validation metadata look like a fresh formal run.
- **Fix:** Restored those generated manifests to their pre-validation state and excluded them from the plan commit.
- **Files modified:** none in the final diff.
- **Verification:** `git status --short` showed only the intended provenance report and ledger/state/requirements files afterward.
- **Committed in:** not committed; restoration kept evidence-run provenance intact.

**Total deviations:** 1 auto-fixed provenance safeguard.
**Impact on plan:** No scope expansion. The fix prevented accidental evidence provenance drift.

## Issues Encountered

- Matched coverage still has 15 durable failed FullModel rows, but validators classify the package as passed with those failures documented. This remains a diagnostic limitation, not a primary evidence blocker.
- Phase 5 still owns package-facing consistency cleanup for README, CLAUDE, cover letter, response files, and legacy figure scripts.

## User Setup Required

None.

## Next Phase Readiness

Phase 4 is ready for phase-level verification. Phase 5 can cite the Phase 4 provenance check when running final validation, targeted tests, manuscript compilation, package scans, and readiness classification.

---
*Phase: 04-tables-figures-and-numerical-provenance*
*Completed: 2026-06-18*
