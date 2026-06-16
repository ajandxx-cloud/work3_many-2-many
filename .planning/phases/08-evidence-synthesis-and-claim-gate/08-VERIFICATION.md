# Phase 8 Verification

**Phase:** 08 - Evidence Synthesis and Claim Gate
**Date:** 2026-06-16
**Status:** passed
**Next allowed step:** Phase 9 refresh ready
**Do not enter:** Phase 10 until Phase 9 refresh and reproducibility rerun are complete

## Fail-Closed Checks

| check | result | evidence |
|---|---|---|
| 08_CLAIM_INVENTORY.md exists | passed | `08_CLAIM_INVENTORY.md` |
| 08_CLAIM_EVIDENCE_MATRIX.md exists | passed | `08_CLAIM_EVIDENCE_MATRIX.md` |
| 08_SUPPORTED_CLAIMS.md exists | passed | `08_SUPPORTED_CLAIMS.md` |
| 08_UNSUPPORTED_OR_EXPLORATORY_CLAIMS.md exists | passed | `08_UNSUPPORTED_OR_EXPLORATORY_CLAIMS.md` |
| 08_REVISED_ABSTRACT_BULLETS.md exists | passed | `08_REVISED_ABSTRACT_BULLETS.md` |
| 08_REVISED_CONCLUSION_BULLETS.md exists | passed | `08_REVISED_CONCLUSION_BULLETS.md` |
| 08_EQUITY_GATE.md exists | passed | `08_EQUITY_GATE.md` |
| every supported claim has evidence source | passed | supported-claims tables include `evidence source` column |
| every supported claim has claim grade | passed | supported-claims tables include `evidence grade` column |
| every supported claim has allowed wording | passed | supported-claims tables include `final allowed wording` column |
| every unsupported claim has action | passed | unsupported-claims table includes `manuscript action` column |
| CLM-01 is satisfied | passed | every supported claim links to formal evidence, diagnostic evidence, or limitation evidence |
| CLM-02 is satisfied | passed | matrix grades: 4 strong, 4 moderate, 7 exploratory, 5 unsupported |
| CLM-03 is satisfied | passed | unsupported file assigns delete/rewrite/move/limitations actions |
| MET-04 is satisfied or explicitly blocked | passed | MET-04 complete as metrics produced and bounded |
| Phase 7 synthetic-data limitation is respected | passed | C-CASE-01 and C-LIM-01 keep Beijing material synthetic/illustrative only |
| no final manuscript prose is written | passed | only claim units, bullets, matrices, and verification artifacts were created |
| Phase 9 is not entered | passed | Phase 9 is marked refresh ready only; no manuscript or Phase 9 refresh artifacts were edited |
| Phase 10 is not entered | passed | REP-01/REP-02 remain pending; Phase 10 final verification not rerun |
| no unsupported broad first/only or real-Beijing claim remains in supported allowed wording | passed | such statements appear only as forbidden wording or unsupported actions |

## Evidence Boundary Checks

| boundary | result |
|---|---|
| 06-02 main behavioral matrix treated as main formal evidence | passed |
| 06-03 matched coverage treated as main/control evidence with 15 durable failed rows | passed |
| 06-03 fixed accepted-set treated as routing diagnostic only | passed |
| 06-04 utility sensitivity, walking radius / MP density, and fleet-demand stress treated as robustness diagnostics | passed |
| 06-04 equity treated as exploratory because passenger types are simulation-range constructs | passed |
| 06-04 algorithm diagnostics treated as diagnostic evidence only | passed |
| Phase 7 Beijing-inspired scenario treated as illustrative/limitation-level evidence only | passed |
| legacy `results/beijing_results.csv` not used as formal validated case evidence | passed |

## Requirement Effects

| requirement | status after Phase 8 | evidence |
|---|---|---|
| CLM-01 | complete | `08_CLAIM_EVIDENCE_MATRIX.md`; `08_SUPPORTED_CLAIMS.md` |
| CLM-02 | complete | grade counts in `08_CLAIM_EVIDENCE_MATRIX.md` |
| CLM-03 | complete | `08_UNSUPPORTED_OR_EXPLORATORY_CLAIMS.md` |
| MET-04 | complete as metrics produced and bounded | `08_EQUITY_GATE.md` |
| REP-01 | unchanged, pending | Phase 10 |
| REP-02 | unchanged, pending | Phase 10 |

## Claim Counts

| grade | count |
|---|---:|
| strong | 4 |
| moderate | 4 |
| exploratory | 7 |
| unsupported | 5 |
| total inventoried | 20 |

## Strongest Allowed Main Claim

FullModel/BidirectionalMP shows lower vehicle-km intensity in formal synthetic
paired experiments, but the claim must be paired with the lower served-share
and rejection/coverage context. It is not an unconditional superiority claim.

## Strongest Forbidden Overclaim

FullModel is unconditionally superior and validates real-city deployment.

## Commands Run

```powershell
$env:PYTHONPATH='src;.'; pytest tests/test_phase06_formal.py tests/test_runner.py tests/test_metrics.py tests/test_variants.py tests/test_phase06_coverage_controls.py tests/test_phase06_robustness.py -q
```

Result: passed, `100 passed in 5.66s`.

## Phase 8 Decision

Phase 8 passed.

The next allowed step is Phase 9 refresh. Phase 9 must read the Phase 8 claim
gate artifacts before revising abstract, introduction, experiment text,
captions, limitations, managerial insights, or conclusion. Phase 10 must not be
treated as final until the Phase 9 refresh and final reproducibility checks are
rerun.

