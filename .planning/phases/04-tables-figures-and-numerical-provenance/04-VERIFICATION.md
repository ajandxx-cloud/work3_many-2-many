---
phase: 04-tables-figures-and-numerical-provenance
status: passed
verified_at: 2026-06-18T11:30:00+08:00
verifier: codex-inline
requirements: [TFIG-01, TFIG-02, TFIG-03, TFIG-04, TFIG-05, TFIG-06]
---

# Phase 4 Verification

## Result

Phase 4 passed verification.

All three Phase 4 plans have summaries, all Phase 4 requirements are marked
complete, formal Phase 6 synthesis validation passes, manuscript table and
figure assets trace to `results/formal/phase06/`, and active manuscript/table
sources are clean of old values, placeholders, non-canonical formal-claim paths,
unsupported significance wording, and prohibited overclaim wording.

## Plan Summary Gate

Command:

`gsd-sdk query phase-plan-index 04`

Result:

- `04-01` summary present.
- `04-02` summary present.
- `04-03` summary present.
- `incomplete: []`.

## Requirement Gate

Phase 4 requirements are complete:

- `TFIG-01`: manuscript-ready tables generated/refreshed from formal Phase 6 processed outputs.
- `TFIG-02`: manuscript-ready figures generated/refreshed from validated formal Phase 6 processed outputs.
- `TFIG-03`: old 3-seed table usage replaced or removed from the main paper.
- `TFIG-04`: old values checked and either replaced, removed, or confined to formal table/figure provenance.
- `TFIG-05`: denominators verified and labeled for required metrics.
- `TFIG-06`: weight sensitivity verified against shared metric columns and validators.

## Verification Commands

| Command | Status | Notes |
|---------|--------|-------|
| `gsd-sdk query phase-plan-index 04` | passed | All three plans have summaries; no incomplete plans. |
| `gsd-sdk query verify.schema-drift "04"` | passed | `drift_detected: false`, `blocking: false`. |
| `$env:PYTHONPATH='src'; python -m experiments.formal_statistics --validate --results-dir results/formal/phase06` | passed | `passed: true`, no missing required synthesis files. |
| `$env:PYTHONPATH='src'; python -m experiments.phase06_formal --validate --results-dir results/formal/phase06/main_behavioral` | passed in plan 04-03 | Main behavioral row counts and denominator checks passed. |
| `$env:PYTHONPATH='src'; python -m experiments.phase06_coverage_controls --validate --package all` | passed in plan 04-03 | Matched coverage and fixed accepted-set validators passed; 15 matched-coverage durable failed rows remain documented diagnostic limitations. |
| `$env:PYTHONPATH='src'; python -m experiments.phase06_robustness --validate --package all` | passed in plan 04-03 | Robustness, equity/type, and algorithm diagnostics passed with no schema drift. |
| Active manuscript/table unsafe scan | passed | No old values, Phase 4 placeholders, root legacy formal paths, p-value/significance wording, or prohibited overclaim wording found. |
| Phase 4 requirement pending scan | passed | No pending `TFIG-*` requirement rows remain. |

## Manuscript Artifact Gate

Verified active manuscript artifacts:

- `manuscript/tables/phase06_main_behavioral_table.tex`
- `manuscript/figures/fig04_phase06_main_efficiency_coverage.png`
- `manuscript/sections/experiments.tex`
- `manuscript/main.pdf`

Plan 04-02 compiled `manuscript/main.tex` with `pdflatex` and produced
`manuscript/main.pdf`. The compile had non-blocking layout warnings, including
overfull/underfull boxes and float-placement warnings. Phase 5 owns the final
submission compilation sequence and package polish.

## Provenance Gate

The final Phase 4 provenance check is:

`.planning/milestones/tr_e_claim_ready/06_PHASE4_PROVENANCE_CHECK.md`

It records:

- denominator formulas for `served_share`, `vkm_per_original_request`,
  `vkm_per_served_trip`, `behavioral_acceptance_rate`,
  `choice_rejection_rate`, and `feasibility_rejection_rate`;
- formal table, figure, validation, coverage-control, robustness, equity, and
  algorithm diagnostic source paths;
- weight sensitivity denominator verification;
- Gamma post-hoc-only boundary;
- diagnostic role decisions for matched coverage, fixed accepted sets,
  equity/type outcomes, Beijing-inspired evidence, and MILP diagnostics;
- remaining Phase 5 package risks.

## Non-Blocking Known Issues

- Matched coverage has 15 durable failed FullModel rows. They are documented
  and remain diagnostic, not primary behavioral evidence.
- Package-facing README, CLAUDE, cover letter, response file, and legacy figure
  scripts still require Phase 5 consistency review.
- Final readiness classification is not granted by Phase 4. Phase 5 owns final
  tests, full manuscript compilation, package scans, and readiness reporting.

## Decision

Phase 4 is verified and ready for Phase 5.
