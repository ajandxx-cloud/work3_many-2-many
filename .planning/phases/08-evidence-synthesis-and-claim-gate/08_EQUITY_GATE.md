# Phase 8 MET-04 Equity Gate

**Phase:** 08 - Evidence Synthesis and Claim Gate
**Date:** 2026-06-16
**Status:** passed as metrics produced and bounded

## Evidence Read

- `results/formal/phase06/robustness/equity_type_outcomes/type_level_outcomes.csv`
- `results/formal/phase06/robustness/equity_type_outcomes/individual_burden_distribution.csv`
- `results/formal/phase06/robustness/equity_type_outcomes/equity_summary.json`
- `results/formal/phase06/robustness/equity_type_outcomes/validation_report.json`
- `.planning/phases/06-formal-synthetic-experiments/06_FORMAL_SYNTHETIC_RESULTS.md`
- `.planning/phases/06-formal-synthetic-experiments/06_FORMAL_RESULT_MANIFEST.md`

## Gate Findings

| question | finding | status |
|---|---|---|
| type-level outcomes exist? | Yes. `type_level_outcomes.csv` has 180 rows. | passed |
| individual-level burden distributions exist? | Yes. `individual_burden_distribution.csv` has 12,000 rows. | passed |
| passenger type parameters empirical or simulation ranges? | Simulation-range constructs, per `equity_summary.json` and Phase 6 boundary. | bounded |
| validation report exists and passes? | Yes. Equity package validator passed with schema_drift=false and denominator_validation=passed. | passed |
| equity evidence can support what? | Reporting modeled type-level outcomes and individual burden distributions as diagnostics. | supported |
| equity evidence cannot support what? | Strong equity improvement, demographic equity, regulatory mandates, or real-world distributional conclusions. | forbidden |
| MET-04 status | Complete as "metrics produced and bounded." | complete |
| equity claim grade | Exploratory. | exploratory |

## Allowed Equity Wording

- "Equity diagnostics report modeled passenger-type outcomes and individual
  burden distributions."
- "These diagnostics are bounded by simulation-range passenger types and should
  not be interpreted as empirical demographic equity evidence."
- "Future real or semi-real validation should calibrate passenger types and
  burden measures with observed or surveyed users."

## Forbidden Equity Wording

- "Equity benefits are strongly established."
- "The system improves equity."
- "Time-sensitive passengers are empirically disadvantaged in real Chinese DRT
  operations."
- "Regulators should require a specific reporting rule based on these results."

## MET-04 Decision

MET-04 is complete because both required metric layers exist:

- type-level outcomes: 180 rows
- individual-level burden distributions: 12,000 rows

The completion is bounded. It satisfies metric production and documentation, not
strong equity inference. The supported claim grade for C-EQ-01 is exploratory.

