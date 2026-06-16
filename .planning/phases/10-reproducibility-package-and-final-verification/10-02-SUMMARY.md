---
phase: 10-reproducibility-package-and-final-verification
plan: 10-02
subsystem: reproducibility
tags: [reproduction-guide, artifact-index, manuscript-build, claim-gate]

requires:
  - phase: 10-01
    provides: Structured artifact manifest and prerequisite gate used as the guide's source.
  - phase: 06-formal-synthetic-experiments
    provides: Formal synthetic evidence report and final result artifacts; currently missing and recorded as blocked.
  - phase: 08-evidence-synthesis-and-claim-gate
    provides: Claim-evidence matrix and supported/unsupported claim lists; currently missing and recorded as blocked.
provides:
  - Reviewer-facing reproduction guide with environment setup and command taxonomy.
  - Reproduction entry-point table grouped by evidence role.
  - Manuscript build chain, table/figure provenance, and human-readable final artifact index.
affects: [phase-10, reproducibility-package, manuscript-build, final-artifact-index]

tech-stack:
  added: []
  patterns: [blocked reproduction status, evidence-role command taxonomy, human-readable artifact index]

key-files:
  created:
    - .planning/phases/10-reproducibility-package-and-final-verification/10_REPRODUCIBILITY.md
    - .planning/phases/10-reproducibility-package-and-final-verification/10-02-SUMMARY.md
  modified: []

key-decisions:
  - "Kept the guide status as `Blocked: prerequisites missing` until Phase 6 and Phase 8 artifacts exist."
  - "Separated final evidence, critical robustness, supplementary diagnostics, legacy diagnostics, pilot readiness, manuscript figures, and manuscript build commands."
  - "Classified pilot and legacy outputs as non-final evidence while preserving them as reproducibility/provenance assets."
  - "Recorded manuscript figure scripts and generated outputs as reproducibility artifacts that require Phase 8 support before supporting final claims."

patterns-established:
  - "Reviewer commands are listed with purpose, evidence_role, command, inputs, outputs, status, and blocker columns."
  - "The human-readable artifact index lives in `10_REPRODUCIBILITY.md`; the structured manifest remains `10_RESULT_MANIFEST.md`."

requirements-addressed: [REP-01, REP-02]
requirements-completed: []

duration: 6 min
completed: 2026-06-16
---

# Phase 10 Plan 10-02: Reviewer Reproduction Guide and Artifact Index Summary

**Blocked reviewer reproduction guide with environment setup, evidence-role entry points, manuscript build provenance, and final artifact index**

## Performance

- **Duration:** 6 min
- **Started:** 2026-06-16T03:51:36Z
- **Completed:** 2026-06-16T03:57:32Z
- **Tasks:** 3
- **Files modified:** 2

## Accomplishments

- Created `10_REPRODUCIBILITY.md` with `Reproduction Status`, `Environment Setup`, `Command Taxonomy`, and `Prerequisite Blockers`.
- Added required setup/provenance commands: `python -m pip install -e .`, `python -m pip freeze`, `git rev-parse HEAD`, and `$env:PYTHONPATH='src'; pytest tests -q`.
- Documented reviewer-facing reproduction entry points for formal Phase 6 evidence, Phase 8 claim gate, root result regeneration, matched-coverage diagnostics, sensitivity/equity analysis, MILP diagnostics, pilot artifacts, figure scripts, and manuscript build.
- Added manuscript build, table/figure provenance, and final artifact index sections while preserving the fail-closed Phase 8 blocker.

## Task Commits

Each task was committed atomically:

1. **Task 10-02-01: Create reproduction status, setup, and command taxonomy** - `dc71ca5` (docs)
2. **Task 10-02-02: Document reviewer-facing reproduction entry points** - `8ec000b` (docs)
3. **Task 10-02-03: Document manuscript build, table/figure chain, and final artifact index** - `7e83f3e` (docs)

**Plan metadata:** this summary commit.

## Files Created/Modified

- `10_REPRODUCIBILITY.md` - Reviewer-facing reproduction guide and final artifact index.
- `10-02-SUMMARY.md` - This execution summary.

## Decisions Made

- Formal Phase 6 and Phase 8 reproduction rows remain blocked with `Blocked: prerequisites missing`.
- Current root result commands are legacy diagnostic/provenance commands, not final evidence.
- Matched coverage, sensitivity, equity, and MILP commands are diagnostic or robustness artifacts pending Phase 8 support.
- Manuscript figures and generated outputs are reproducibility artifacts, but they cannot support final claims until Phase 8 approves the linked claims.

## Deviations from Plan

None - plan executed exactly as written.

## Issues Encountered

- The repository remains heavily dirty from pre-existing reorganization and generated-file churn. Plan commits staged only Phase 10 reproduction guide and summary files.
- Phase 6 and Phase 8 hard blockers remain absent, so the guide intentionally records a blocked/pending package rather than a final reproducibility release.

## Verification

- `Test-Path '.planning/phases/10-reproducibility-package-and-final-verification/10_REPRODUCIBILITY.md'` -> passed.
- `Select-String ... 'Reproduction Status','Reproduction Entry Points','Manuscript Build Chain','Final Artifact Index'` -> passed.
- `Select-String ... 'Blocked: prerequisites missing','Not final evidence','pending Phase 8'` -> passed.
- `Select-String ... 'Manuscript Build Chain','Table and Figure Provenance','Final Artifact Index','manuscript/main.tex','fig07_pareto.py','generated manuscript outputs'` -> passed.

## User Setup Required

None - no external service configuration required.

## Next Phase Readiness

Plan `10-03` can create the final verification artifact by checking the manifest and reproduction guide against the missing Phase 6/8 prerequisites. It must keep the phase fail-closed until those prerequisite artifacts exist.

---
*Phase: 10-reproducibility-package-and-final-verification*
*Completed: 2026-06-16*
