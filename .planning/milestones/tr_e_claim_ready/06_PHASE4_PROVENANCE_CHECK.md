# Phase 4 Provenance Check

## Status

- Phase: 04 tables, figures, and numerical provenance
- Plan: 04-03
- Completed: 2026-06-18T11:23:44+08:00
- Base commit checked: `23c998f`
- Requirements covered: `TFIG-05`, `TFIG-06`
- Result: passed

This report records the denominator, formula, weight sensitivity, Gamma, and
source provenance checks used to close Phase 4 before Phase 5 readiness work.

## Commands Run

| Command | Status | Evidence |
|---------|--------|----------|
| `$env:PYTHONPATH='src'; python -m experiments.formal_statistics --validate --results-dir results/formal/phase06` | passed | Synthesis validation reported `passed: true`, no missing files, paired CI present, supplementary gates present. |
| `$env:PYTHONPATH='src'; python -m experiments.phase06_formal --validate --results-dir results/formal/phase06/main_behavioral` | passed | Main behavioral validation reported 320 main rows, 0 failed rows, 0 timeout rows, `schema_drift: false`, and all denominator checks passed. |
| `$env:PYTHONPATH='src'; python -m experiments.phase06_coverage_controls --validate --package all` | passed | Matched coverage and fixed accepted-set packages passed structural validation. Matched coverage carries 15 durable failed rows as a documented diagnostic limitation. |
| `$env:PYTHONPATH='src'; python -m experiments.phase06_robustness --validate --package all` | passed | Utility sensitivity, meeting-point density/walking radius, fleet stress, equity/type outcomes, and algorithm diagnostics passed with no schema drift. |
| `rg -n "served_share|vkm_per_served_trip|vkm_per_original_request|choice_rejection_rate|feasibility_rejection_rate|behavioral_acceptance_rate" experiments/metrics.py experiments/formal_validation.py experiments/formal_statistics.py .planning/milestones/tr_e_claim_ready/03_CLAIM_LEDGER.md` | passed | Found the shared metric definitions, formal denominator validator, formal statistics table/summary use, and claim-ledger formula reference. |
| `rg -n "weight|gamma|Gamma|supplementary|vkm_per_served_trip|served_share|diagnostic|equity|milp|MILP" experiments/formal_statistics.py experiments/phase06_robustness.py results/formal/phase06/tables` | passed | Confirmed robustness and diagnostic summaries use formal roles and the paired-difference metric columns. |
| Active manuscript unsafe scan for old values, placeholders, non-canonical result paths, unsupported significance language, and prohibited wording | passed | No hits in `manuscript/main.tex`, `manuscript/sections`, or `manuscript/tables`. Intentional formal source-path comments remain in the generated table. |

## Formal Source Paths

Primary behavioral table and figure values trace to:

- `results/formal/phase06/tables/main_behavioral_table.csv`
- `results/formal/phase06/tables/paired_differences.csv`
- `results/formal/phase06/tables/paired_bootstrap_ci.csv`
- `results/formal/phase06/plots/phase06_main_efficiency_coverage.png`
- `results/formal/phase06/plots/plot_metadata.json`
- `manuscript/tables/phase06_main_behavioral_table.tex`
- `manuscript/figures/fig04_phase06_main_efficiency_coverage.png`

Diagnostic and robustness checks trace to:

- `results/formal/phase06/tables/matched_coverage_paired_differences.csv`
- `results/formal/phase06/tables/fixed_accepted_set_paired_differences.csv`
- `results/formal/phase06/tables/robustness_setting_summary.csv`
- `results/formal/phase06/tables/equity_type_summary.csv`
- `results/formal/phase06/tables/supplementary_summary.csv`
- `results/formal/phase06/coverage_controls/matched_coverage/validation_report.json`
- `results/formal/phase06/coverage_controls/fixed_accepted_set/validation_report.json`
- `results/formal/phase06/robustness/validation_report.json`
- `results/formal/phase06/robustness/equity_type_outcomes/validation_report.json`
- `results/formal/phase06/robustness/algorithm_diagnostics/validation_report.json`

## Denominator Decisions

These formulas are verified in `experiments/metrics.py` and
`experiments/formal_validation.py` and are repeated in the claim ledger.

| Metric | Formula | Numerator | Denominator | Phase 4 decision |
|--------|---------|-----------|-------------|------------------|
| `served_share` | `served_share = n_served / n_requests` | `n_served` | `n_requests` | Use for coverage and served-share claims. |
| `vkm_per_original_request` | `vkm_per_original_request = vehicle_km / n_requests` | `vehicle_km` | `n_requests` | Use to keep coverage loss visible in routing-intensity interpretation. |
| `vkm_per_served_trip` | `vkm_per_served_trip = vehicle_km / n_served` | `vehicle_km` | `n_served` | Use for routing intensity among realized served trips. |
| `behavioral_acceptance_rate` | `behavioral_acceptance_rate = 1.0 - choice_rejection_rate` | `1.0 - choice_rejection_rate` | not applicable | Treat as a choice-model acceptance rate, not as served share. |
| `choice_rejection_rate` | `choice_rejection_rate = choice_rejected / n_requests` | `choice_rejected` | `n_requests` | Use original requests as denominator. |
| `feasibility_rejection_rate` | `feasibility_rejection_rate = feasibility_rejected / n_requests` | `feasibility_rejected` | `n_requests` | Use original requests as denominator. |
| `rejection_partition` | `served_share + choice_rejection_rate + feasibility_rejection_rate = 1.0` | partition components | all original requests | Validated for completed formal rows. |

Main behavioral validation reports `served_share`, `vkm_per_original_request`,
`vkm_per_served_trip`, `behavioral_acceptance_rate`, `rejection_partition`, and
`total_vehicle_km_alias` as passed. Coverage-control and robustness validators
repeat the relevant denominator checks for their packages.

## Weight Sensitivity Check

`TFIG-06` is satisfied. Weight and utility sensitivity values in
`results/formal/phase06/tables/robustness_setting_summary.csv` are generated by
`experiments/formal_statistics.py::write_robustness_setting_summary()`, which
calls `paired_difference_frame()` over the formal raw result columns:

- `vkm_per_served_trip`
- `vkm_per_original_request`
- `served_share`

Those columns are produced by the same metric contract validated in
`experiments/formal_validation.py` and `experiments/phase06_robustness.py`.
The robustness validator reports denominator checks passed for
`utility_sensitivity`, `mp_density_walking_radius`, and `fleet_demand_stress`.
Therefore the weight sensitivity evidence is not inflated by an
acceptance-rate-only denominator.

## Gamma Boundary

Gamma remains post-hoc welfare or sensitivity accounting only. Active manuscript
sources say Gamma does not alter routing, offer generation, or acceptance. The
source scan found legacy Gamma/Pareto wording in historical scripts and planning
ledger rows, but the active manuscript/table unsafe scan found no `Gamma
controls`, `results/pareto_gamma_sweep.csv`, or unsupported Pareto-control
wording in active manuscript sources.

Allowed Phase 4 use: non-numeric post-hoc accounting boundary.

Prohibited Phase 4 use: Gamma as a routing, offer-generation, acceptance,
policy-control, endogenous Pareto, or headline evidence variable.

## Diagnostic Role Decisions

These decisions cover context decisions `D-03`, `D-10`, `D-11`, `D-12`,
`D-13`, `D-14`, `D-15`, `D-16`, `D-17`, and `D-18`.

| Evidence family | Phase 4 decision |
|-----------------|------------------|
| Bootstrap intervals | Allowed only in generated table/table notes as descriptive paired bootstrap intervals. No p-value or statistically significant wording is introduced. |
| Matched coverage | Diagnostic coverage-confounding control. Validation passed, but 15 durable failed rows remain documented and values are not promoted into headline text. |
| Fixed accepted set | Diagnostic fixed accepted-set routing decomposition. It is not a complete dynamic behavioral benchmark. |
| Equity/type outcomes | Limited simulated passenger-type monitoring evidence. No real population equity conclusion or Gini headline value is active in the manuscript. |
| Gamma | Post-hoc welfare or sensitivity accounting only. No active main-text numerical Gamma detail. |
| Beijing-inspired evidence | Synthetic robustness setting only. No real-world Beijing validation claim is active. |
| MILP and algorithm diagnostics | Method-scope and limitation evidence only. No near-optimality or full exact dynamic benchmark claim is active. |
| Legacy result paths | Root legacy CSV paths are absent from active manuscript sources and manuscript table assets. |

## Source Provenance Scan

The final active manuscript scan checked `manuscript/main.tex`,
`manuscript/sections`, and `manuscript/tables` for:

- old values: `18.3`, `29.1`, `35.0`, `0.1216`
- Phase 4 placeholders: `[PHASE4_VERIFIED`
- non-canonical formal-claim paths: `results/synthetic_results.csv`,
  `results/beijing_results.csv`, `results/metrics_table.csv`,
  `results/pareto_gamma_sweep.csv`
- unsupported significance language: `statistically significant`, `p-value`
- prohibited claim wording: `real-world Beijing validation`, `Gamma controls`,
  `near-optimal`, `full exact dynamic benchmark`

Result: passed. Formal `results/formal/phase06/` path references remain only as
intentional provenance notes in `manuscript/tables/phase06_main_behavioral_table.tex`
and as the experiments-section formal package path.

## Non-Impacting Failures And Warnings

- Matched coverage has 15 durable failed FullModel rows. They are documented in
  the matched-coverage validator and the durable failure ledger. They do not
  affect primary behavioral table/figure claims because matched coverage remains
  diagnostic.
- Phase 4 manuscript compilation from Plan 04-02 passed, with non-blocking
  overfull/underfull box and float-placement warnings. Phase 5 owns final
  package polish.
- Package-facing files such as README, CLAUDE, cover letter, response template,
  and legacy figure-script comments still require Phase 5 consistency review.
- Legacy figure scripts that read root result paths remain package-facing risk
  unless excluded or rewritten from formal Phase 6 sources in Phase 5.

## Phase 5 Risks

Phase 5 should still verify:

- final manuscript compilation sequence and bibliography state;
- targeted pytest checks or documented non-impacting failures;
- package-facing wording in README, CLAUDE, cover letter, response file, and
  figure scripts;
- final readiness label gating;
- whether any diagnostic appendix/supplement material is included or excluded.

Phase 4 does not authorize `TR-E submission-ready`; it closes the table,
figure, denominator, and source provenance gate for Phase 5.
