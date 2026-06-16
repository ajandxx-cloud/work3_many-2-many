---
status: passed
phase: 10-reproducibility-package-and-final-verification
verified: 2026-06-16
requirements_checked: [REP-01, REP-02]
score: "25/25 checks passed"
---

# Phase 10 Verification Report

## Verdict

Status: `passed`

Phase 10 final reproducibility verification passed after rerunning the required active pytest suite, Phase 6 synthesis validation, schema drift check, denominator/failure-ledger review, claim-gate consistency review, and Phase 9 refresh boundary review.

## Checks

| # | Check | Result | Evidence |
|---|---|---|---|
| 1 | Phase 6 formal results exist | passed | `06_FORMAL_SYNTHETIC_RESULTS.md`; `results/formal/phase06/`. |
| 2 | Phase 7 case boundary exists | passed | `07_DATA_AUDIT.md`; `07_CASE_CLAIM_BOUNDARY.md`; `07-VERIFICATION.md`. |
| 3 | Phase 8 claim gate exists | passed | `08_CLAIM_EVIDENCE_MATRIX.md`; `08_SUPPORTED_CLAIMS.md`; `08_UNSUPPORTED_OR_EXPLORATORY_CLAIMS.md`; `08-VERIFICATION.md`. |
| 4 | Phase 9 refreshed manuscript plan exists | passed | All required Phase 9 refresh artifacts present. |
| 5 | Phase 6 verification passed | passed | `phase06_verification_report.json` -> `passed: true`; `06-VERIFICATION.md`. |
| 6 | Phase 7 verification passed | passed | `07-VERIFICATION.md` -> `Status: passed`. |
| 7 | Phase 8 verification passed | passed | `08-VERIFICATION.md` -> `Status: passed`. |
| 8 | Phase 9 verification passed | passed | `09-VERIFICATION.md` -> `status: passed`. |
| 9 | `10_RESULT_MANIFEST.md` complete | passed | Planning, Phase 6/7/8/9, validation, and commit-reference sections updated. |
| 10 | `10_REPRODUCIBILITY.md` complete | passed | Root, revision, environment, PYTHONPATH, dependencies, commands, limitations, failure policy, dirty-state policy, and reviewer artifact set recorded. |
| 11 | `10_FINAL_VERIFICATION.md` complete | passed | Phase, requirement, evidence, claim, reproducibility, and git/worktree gates recorded. |
| 12 | Tests passed | passed | Required command -> 100 passed in 5.55s. |
| 13 | Schema drift false | passed | `gsd-sdk query verify.schema-drift 10` -> `drift_detected: false`. |
| 14 | Denominator checks passed | passed | Phase 6 verification report records denominator checks passed. |
| 15 | All supported claims map to evidence | passed | Phase 8 supported-claims and matrix artifacts. |
| 16 | All forbidden claims excluded | passed | Phase 8 unsupported file and Phase 9 claim-gate audit. |
| 17 | No real-Beijing validation claim | passed | Phase 7/8/9 artifacts require Beijing-inspired synthetic wording only. |
| 18 | No unconditional superiority claim | passed | Phase 8 and Phase 9 require lower vkm intensity with served-share/rejection context. |
| 19 | No first/only overclaim | passed | Phase 1/8/9 forbid broad first/only language. |
| 20 | No deployment-ready claim | passed | Phase 8/9 require real/semi-real validation before deployment guidance. |
| 21 | No hidden failed rows | passed | 15 matched-coverage failed rows recorded durably. |
| 22 | Result artifacts traceable | passed | Raw -> processed/tables/plots -> Phase 6 reports -> Phase 8 claims -> Phase 9 plans -> Phase 10 manifest. |
| 23 | REP-01 can be marked complete | passed | Commands, dependencies, configs, seeds, code revisions, and manifests recorded. |
| 24 | REP-02 can be marked complete | passed | Main Phase 6 tables/plots regenerate from saved artifacts; manuscript implementation remains a later phase. |
| 25 | Phase 10 status | passed | All required checks passed. |

## Commands Run

```powershell
$env:PYTHONPATH='src;.'; python -m experiments.formal_statistics --validate --results-dir results/formal/phase06
gsd-sdk query verify.schema-drift 10
$env:PYTHONPATH='src;.'; pytest tests/test_phase06_formal.py tests/test_runner.py tests/test_metrics.py tests/test_variants.py tests/test_phase06_coverage_controls.py tests/test_phase06_robustness.py -q
git diff --check
```

Results:

- Phase 6 synthesis validation: passed.
- Schema drift: false.
- Required pytest suite: 100 passed in 5.55s.
- `git diff --check`: passed after trailing-whitespace cleanup.

## Requirement Accounting

| requirement | status | evidence |
|---|---|---|
| REP-01 | complete | `10_RESULT_MANIFEST.md`; `10_REPRODUCIBILITY.md`; Phase 6 manifests and seed/config/run records. |
| REP-02 | complete | Phase 6 formal tables and plots regenerate from saved artifacts through `experiments.formal_statistics`; Phase 9 specifies final manuscript table/figure implementation boundaries. |

## Closeout

Phase 10 passed and the milestone evidence-chain rebuild is complete. No unsupported final manuscript claims were added, and manuscript `.tex`正文 was not edited in this phase. Broader unrelated worktree dirtiness remains untouched and documented.
