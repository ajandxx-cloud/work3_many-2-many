# TR-E Claim-Ready Milestone Verification

## Scope

- Milestone: Work 3 TR-E Claim-Ready Manuscript Package
- Phase: 05 verification and readiness closeout
- Completed: 2026-06-19T13:31:09+08:00
- Requirements covered: VERI-02, VERI-03, VERI-04, VERI-05, VERI-06
- Canonical formal evidence boundary: `results/formal/phase06/`

This report verifies the core manuscript submission package. The hard gates are
the formal validation commands, active pytest command, manuscript compilation,
claim ledger coverage, table and figure provenance, and prohibited wording scan.
Package-facing files such as `README.md`, `CLAUDE.md`,
`manuscript/cover_letter.tex`, and `manuscript/response_to_reviewers.tex` are
not hard gates unless they are included in the submitted package.

## Readiness Classification

**TR-E submission-ready**

All hard readiness gates passed or have documented non-impacting warnings. No
claim, evidence, ledger, prohibited wording, or manuscript compilation blocker
remains for the verified core package.

## Command Log

| Gate | Command | Status | Evidence source |
|------|---------|--------|-----------------|
| VERI-02 formal synthesis validation | `$env:PYTHONPATH='src'; python -m experiments.formal_statistics --validate --results-dir results/formal/phase06` | passed | `.planning/phases/05-verification-and-readiness-closeout/05-01-SUMMARY.md` |
| VERI-02 main behavioral validation | `$env:PYTHONPATH='src'; python -m experiments.phase06_formal --validate --results-dir results/formal/phase06/main_behavioral` | passed | `.planning/phases/05-verification-and-readiness-closeout/05-01-SUMMARY.md` |
| VERI-02 coverage-control validation | `$env:PYTHONPATH='src'; python -m experiments.phase06_coverage_controls --validate --package all` | passed | `.planning/phases/05-verification-and-readiness-closeout/05-01-SUMMARY.md` |
| VERI-02 robustness validation | `$env:PYTHONPATH='src'; python -m experiments.phase06_robustness --validate --package all` | passed | `.planning/phases/05-verification-and-readiness-closeout/05-01-SUMMARY.md` |
| VERI-03 targeted pytest | `$env:PYTHONPATH='src'; pytest tests/ analysis/test_sensitivity.py` | passed | `.planning/phases/05-verification-and-readiness-closeout/05-01-SUMMARY.md` |
| VERI-04 manuscript compile | `pdflatex main`; `bibtex main`; `pdflatex main`; `pdflatex main` from `manuscript/` | passed | `.planning/phases/05-verification-and-readiness-closeout/05-02-SUMMARY.md` |
| VERI-05 final scans and report | active manuscript scan, ledger schema scan, provenance scan, readiness-label scan | passed | this report and `05-03-SUMMARY.md` |

## Validation Results

Formal Phase 6 validation passed. The synthesis validator reported
`passed: true`, no missing required files, paired confidence-interval outputs
present, and supplementary gates present. Main behavioral validation reported
320 main rows, 0 failed rows, 0 timeout rows, no schema drift, and denominator
checks passed.

Coverage-control validation passed. The matched-coverage package retains 15
durable failed rows, but they are diagnostic-only rows and do not support the
primary behavioral claim. Fixed accepted-set validation passed.

Robustness validation passed for utility sensitivity, meeting-point/walking
radius settings, fleet stress, equity/type outcomes, and algorithm diagnostics,
with no schema drift.

## Targeted Pytest Results

The active readiness command passed:

`$env:PYTHONPATH='src'; pytest tests/ analysis/test_sensitivity.py`

Result: `199 passed, 1 skipped in 201.09s (0:03:21)`.

The single skip is acceptable as optional Gurobi/MILP diagnostic coverage. It
does not alter the simplified ex-post MILP diagnostic boundary in the
manuscript.

## Manuscript Compilation Results

The required sequence from `manuscript/` passed:

1. `pdflatex main`
2. `bibtex main`
3. `pdflatex main`
4. `pdflatex main`

The final PDF is `manuscript/main.pdf`, 47 pages, 785,207 bytes. Log scans found
no fatal LaTeX errors, undefined control sequences, undefined citations,
undefined references, missing bibliography database, missing bibliography entry,
or missing file blocker.

Non-impacting compile warnings are listed below.

## Claim Ledger Coverage

Claim ledger coverage is **100% for active numerical manuscript claims**. The
ledger contains the mandatory provenance columns:

- `source_path`
- `script_path`
- `generation_command`
- `metric_formula`
- `numerator`
- `denominator`
- `evidence_role`
- `allowed_sentence`
- `prohibited_sentence`

Historical blocker rows remain in
`.planning/milestones/tr_e_claim_ready/03_CLAIM_LEDGER.md` for audit
traceability. They are not active manuscript blockers because Phase 4 queue rows
record that active text was either verified, de-numericized, or retained only
with diagnostic and provenance boundaries. Active manuscript scans found no old
headline values or unresolved placeholders.

## Table And Figure Provenance

Formal table and figure evidence traces to `results/formal/phase06/`.

Primary manuscript assets:

- `manuscript/tables/phase06_main_behavioral_table.tex`
- `manuscript/figures/fig04_phase06_main_efficiency_coverage.png`

Canonical formal sources:

- `results/formal/phase06/tables/main_behavioral_table.csv`
- `results/formal/phase06/tables/paired_differences.csv`
- `results/formal/phase06/tables/paired_bootstrap_ci.csv`
- `results/formal/phase06/plots/phase06_main_efficiency_coverage.png`
- `results/formal/phase06/plots/plot_metadata.json`

Diagnostic and robustness sources remain labeled as diagnostic, robustness,
equity/type, or algorithm-diagnostic evidence, not primary headline evidence.

## Prohibited Wording Scan

The active manuscript and table scan passed over:

- `manuscript/main.tex`
- `manuscript/sections`
- `manuscript/tables`

The scan found no old Phase 4 values, unresolved Phase 4 placeholders,
non-canonical result paths for formal claims, unsupported significance wording,
real-world validation overclaims, Gamma control overclaims, near-optimality
overclaims, or full exact dynamic benchmark overclaims.

The readiness-label scan also passed for active manuscript files. No readiness
label appears outside this final verification report.

## Blockers

None for the verified core submission package.

## Non-Impacting Warnings

- Matched coverage includes 15 durable failed rows, documented as diagnostic and
  not used as primary behavioral evidence.
- The active pytest command has 1 optional Gurobi/MILP diagnostic skip.
- The LaTeX log contains non-blocking layout warnings: 16 overfull boxes, 7
  underfull boxes, 3 float-size warnings, 8 float-placement warnings, and 4
  hyperref PDF-string warnings.
- MiKTeX printed local update notices during compilation; these do not affect
  manuscript content or PDF generation.
- Package-facing files outside the verified core package should be reviewed
  before being included in any external submission bundle.

## Materials Checklist

Core materials verified:

- [x] `manuscript/main.tex`
- [x] `manuscript/sections/*.tex`
- [x] `manuscript/references.bib`
- [x] `manuscript/main.pdf`
- [x] `manuscript/tables/phase06_main_behavioral_table.tex`
- [x] `manuscript/figures/fig04_phase06_main_efficiency_coverage.png`
- [x] `results/formal/phase06/`
- [x] `.planning/milestones/tr_e_claim_ready/03_CLAIM_LEDGER.md`
- [x] `.planning/milestones/tr_e_claim_ready/06_PHASE4_PROVENANCE_CHECK.md`
- [x] `.planning/phases/05-verification-and-readiness-closeout/05-01-SUMMARY.md`
- [x] `.planning/phases/05-verification-and-readiness-closeout/05-02-SUMMARY.md`
- [x] `.planning/phases/05-verification-and-readiness-closeout/05-03-SUMMARY.md`

Optional package-facing materials not treated as hard gates:

- [ ] `README.md`
- [ ] `CLAUDE.md`
- [ ] `manuscript/cover_letter.tex`
- [ ] `manuscript/response_to_reviewers.tex`
- [ ] legacy figure scripts not used for the formal Phase 6 manuscript figure

## Requirement Closure

- VERI-02: complete.
- VERI-03: complete.
- VERI-04: complete.
- VERI-05: complete.
- VERI-06: complete.

