# Repository And Evidence Audit

## Purpose

This audit locks the canonical manuscript and evidence boundary for the TR-E
claim-ready milestone. It is a source map and risk taxonomy, not a manuscript
rewrite and not a numerical-claim replacement document.

## Canonical Manuscript Sources

| Manuscript area | Path | Phase use |
|-----------------|------|-----------|
| Master document and journal metadata | `manuscript/main.tex` | Phase 3 updates TR-E metadata and includes; Phase 5 compiles. |
| Abstract | `manuscript/sections/abstract.tex` | Phase 3 rewrites non-numeric framing; Phase 4 injects verified final numbers. |
| Introduction and contributions | `manuscript/sections/intro.tex` | Phase 3 repositions contribution claims; Phase 4 injects verified final numbers. |
| Literature review | `manuscript/sections/literature.tex` | Phase 3 strengthens logistics/operations and DRT/DARP positioning. |
| Model | `manuscript/sections/model.tex` | Phase 3 clarifies offer, choice, Gamma, and scenario semantics. |
| Algorithm | `manuscript/sections/algorithm.tex` | Phase 3 clarifies rolling horizon, ALNS, and MILP diagnostic scope. |
| Experiments | `manuscript/sections/experiments.tex` | Phase 3 separates evidence roles; Phase 4 verifies tables, figures, and numbers. |
| Implications | `manuscript/sections/policy.tex` | Phase 3 reframes as managerial/operational implications. |
| Conclusion | `manuscript/sections/conclusion.tex` | Phase 3 states conditional contribution; Phase 4 injects verified final numbers. |
| Bibliography | `manuscript/references.bib` | Phase 3/4 update only if needed for TR-E positioning or evidence support. |

Supporting submission files `manuscript/cover_letter.tex` and
`manuscript/response_to_reviewers.tex` are not main manuscript evidence. They
are package-consistency targets only if the final submission package includes
them.

## Formal Phase 6 Evidence Roles

The canonical evidence root is `results/formal/phase06/`.

The manifest source is `results/formal/phase06/phase06_result_manifest.json`.
Important manifest status:

- `formal_smoke_excluded: true`
- generated at `2026-06-16T09:53:00.529202+00:00`
- git commit recorded as `8e6c618`

| Evidence role | Source paths | Validation source | Allowed use | Prohibited use |
|---------------|--------------|-------------------|-------------|----------------|
| Primary behavioral evidence | `results/formal/phase06/main_behavioral/raw_results.csv`, `results/formal/phase06/main_behavioral/processed_results.csv`, `results/formal/phase06/main_behavioral/metrics_table.csv`, `results/formal/phase06/tables/main_behavioral_table.csv`, `results/formal/phase06/tables/paired_differences.csv`, `results/formal/phase06/tables/paired_bootstrap_ci.csv` | `results/formal/phase06/main_behavioral/validation_report.json` | Main conditional efficiency, coverage, acceptance, rejection, and denominator claims after Phase 4 provenance checks. | Universal dominance, equal-coverage dominance, or final numerical claims before Phase 4. |
| Matched-coverage diagnostic | `results/formal/phase06/coverage_controls/matched_coverage/raw_results.csv`, `results/formal/phase06/coverage_controls/matched_coverage/processed_results.csv`, `results/formal/phase06/tables/matched_coverage_paired_differences.csv` | `results/formal/phase06/coverage_controls/matched_coverage/validation_report.json` | Diagnostic explanation of coverage confounding and sensitivity to served-share matching. | Main headline estimate or proof of equal-service efficiency. |
| Fixed-accepted-set diagnostic | `results/formal/phase06/coverage_controls/fixed_accepted_set/raw_results.csv`, `results/formal/phase06/coverage_controls/fixed_accepted_set/processed_results.csv`, `results/formal/phase06/tables/fixed_accepted_set_paired_differences.csv` | `results/formal/phase06/coverage_controls/fixed_accepted_set/validation_report.json` | Diagnostic decomposition over fixed accepted sets. | Complete online behavioral benchmark or dynamic routing optimum. |
| Robustness/sensitivity evidence | `results/formal/phase06/robustness/utility_sensitivity/`, `results/formal/phase06/robustness/mp_density_walking_radius/`, `results/formal/phase06/robustness/fleet_demand_stress/`, `results/formal/phase06/tables/robustness_setting_summary.csv`, `results/formal/phase06/tables/supplementary_summary.csv` | `results/formal/phase06/robustness/validation_report.json` | Conditional robustness and service-design boundary statements. | Unbounded generalization beyond tested synthetic service-design conditions. |
| Equity/type heterogeneity evidence | `results/formal/phase06/robustness/equity_type_outcomes/type_level_outcomes.csv`, `results/formal/phase06/robustness/equity_type_outcomes/individual_burden_distribution.csv`, `results/formal/phase06/robustness/equity_type_outcomes/equity_summary.json`, `results/formal/phase06/tables/equity_type_summary.csv` | `results/formal/phase06/robustness/equity_type_outcomes/validation_report.json` | Limited passenger-type heterogeneity and monitoring implications. | Real population equity conclusions or welfare dominance. |
| Algorithm/MILP diagnostic evidence | `results/formal/phase06/robustness/algorithm_diagnostics/rolling_horizon_diagnostics.csv`, `results/formal/phase06/robustness/algorithm_diagnostics/alns_budget_diagnostics.json`, `results/formal/phase06/robustness/algorithm_diagnostics/milp_gap_diagnostics.json` | `results/formal/phase06/robustness/algorithm_diagnostics/validation_report.json` | Ex-post simplified diagnostics, limitations, and algorithm-scope explanation. | ALNS near-optimality proof or full exact dynamic routing benchmark. |
| Excluded smoke package | `results/formal/phase06/smoke/` | `results/formal/phase06/smoke/validation_report.json` | Smoke/package sanity reference only when explicitly labeled non-canonical. | Any formal manuscript claim. |

## Validation Status Snapshot

Top-level verification source:
`results/formal/phase06/phase06_verification_report.json`.

Recorded status:

- main behavioral validation passed
- coverage controls validation passed with durable known failures recorded
- robustness validation passed
- main behavioral package has 20 paired seeds
- expected seed/scale/method rows are present
- denominator checks passed
- failure ledger records 15 known failed matched-coverage rows
- raw-to-processed provenance is documented
- pilot smoke is not used as formal evidence

Main behavioral validator source:
`results/formal/phase06/main_behavioral/validation_report.json`.

Recorded status:

- `passed: true`
- `schema_drift: false`
- row counts include 320 main behavioral rows, 320 synthetic results rows,
  4 metrics-table rows, and 88,000 utility component rows
- denominator checks passed for served share, vkm per served trip, vkm per
  original request, behavioral acceptance rate, rejection partition, and total
  vehicle-km alias

Final synthesis validation source:
`results/formal/phase06/tables/final_synthesis_validation.json`.

Recorded status:

- `passed: true`
- main matrix passed
- paired confidence interval table present
- supplementary gates present
- no required synthesis files missing

## Generation And Validation Scripts

| Script | Role |
|--------|------|
| `experiments/phase06_formal.py` | Formal main behavioral runner, manifests, aliases, and validation. |
| `experiments/formal_validation.py` | Main formal output validation helpers and denominator checks. |
| `experiments/formal_statistics.py` | Formal tables, plots, manifests, verification reports, synthesis validation, and markdown reports. |
| `experiments/phase06_coverage_controls.py` | Matched-coverage and fixed-accepted-set controls and validators. |
| `experiments/phase06_robustness.py` | Utility, density/radius, fleet stress, equity/type, and algorithm diagnostics packages. |
| `manuscript/figures/scripts/fig04_baseline_comparison.py` | Baseline comparison figure script; Phase 4 must verify formal input paths before relying on output. |
| `manuscript/figures/scripts/fig05_sensitivity.py` | Sensitivity figure script; Phase 4 must verify formal input paths before relying on output. |
| `manuscript/figures/scripts/fig06_policy_map.py` | Implication/decision-map figure script; Phase 3/4 must reframe policy language and verify inputs. |
| `manuscript/figures/scripts/fig07_pareto.py` | Pareto/Gamma figure script; Phase 4 must label Gamma as post-hoc only. |

Known validation commands for later gates:

- `$env:PYTHONPATH='src'; python -m experiments.formal_statistics --validate --results-dir results/formal/phase06`
- `$env:PYTHONPATH='src'; python -m experiments.phase06_formal --validate --results-dir results/formal/phase06/main_behavioral`
- `$env:PYTHONPATH='src'; python -m experiments.phase06_coverage_controls --validate --package all`
- `$env:PYTHONPATH='src'; python -m experiments.phase06_robustness --validate --package all`
- `$env:PYTHONPATH='src'; pytest tests`

## Non-Canonical Or Excluded Sources

| Source family | Paths/examples | Default status | Allowed handling |
|---------------|----------------|----------------|------------------|
| Smoke package | `results/formal/phase06/smoke/` | Excluded from formal evidence. | Mention only as non-canonical smoke/package sanity output. |
| Pilot outputs | `results/pilot/phase05/` | Non-canonical for formal claims. | Historical/pilot context only. |
| Root legacy outputs | `results/synthetic_results.csv`, `results/beijing_results.csv`, `results/metrics_table.csv`, `results/equity_table.csv`, `results/policy_recommendations.md`, `results/milp_gap.json` | Non-canonical by default. | Later audit can label historical or diagnostic; do not use as formal claims. |
| Archive outputs | `archive/` | Historical/superseded. | Do not cite as current evidence without explicit audit. |
| Ad hoc tests/logs | `archive/adhoc_tests/`, `archive/output_logs/`, root smoke output text files | Non-canonical. | Repro/debug context only. |
| Discussion/proposal notes | `docs/` | Human context, not formal evidence. | Use for risk discovery, not manuscript evidence. |

## Risk Appendix

| Risk | Impact class | Tracking notes |
|------|--------------|----------------|
| Part A framing in `README.md`, `CLAUDE.md`, `manuscript/main.tex`, `manuscript/references.bib`, cover/response letters, and figure-script comments | manuscript/package consistency risk | Route to Phase 3 for TR-E repositioning and Phase 5 package consistency checks. |
| Policy-first language in abstract, introduction, experiments, policy section, model, conclusion, and generated `results/policy_recommendations.md` | manuscript/package consistency risk | Reframe as managerial and operational implications; avoid policy-overreach. |
| Old values `18.3%`, `29.1%`, `35.0%`, and `0.1216` in manuscript text and legacy outputs | claim-critical blocker until Phase 4 | Track as high-priority values; do not replace or retain until Phase 4 verifies formal provenance. |
| Beijing wording could imply real-world validation | claim-critical blocker | Use Beijing-inspired or semi-realistic synthetic grid unless future public-data ingestion exists. |
| Universal dominance wording could imply FullModel dominates DoorToDoor or all baselines | claim-critical blocker | Use conditional operational wording with coverage and passenger-response trade-offs. |
| Gamma/Pareto language could imply endogenous behavior | claim-critical blocker | Gamma is post-hoc welfare accounting only unless future model work changes behavior. |
| MILP/ALNS language could imply exact dynamic benchmark or ALNS near-optimality | claim-critical blocker | MILP is a simplified ex-post routing diagnostic for fixed accepted sets. |
| Bare root `pytest` fails by collecting archived ad hoc tests | verification risk | Known green targeted command is `$env:PYTHONPATH='src'; pytest tests`. |
| `pandas` and `matplotlib` are used but not declared in `pyproject.toml` | reproducibility hardening / verification risk | Document affected workflows; defer metadata edits unless verification blocks. |
| Route-stop bookkeeping and completed-trip metric precision | claim-impact conditional risk | If later claims use walk, IVT, detour, fairness, or completed-trip precision, verify or downgrade. |
| README old known issues conflict with current repository state | manuscript/package consistency risk | Route to Phase 3 or Phase 5 package polish, not Phase 1. |
| Real Beijing public-data ingestion | future model/evidence | Defer to v2. |
| Endogenous Gamma behavior | future model/evidence | Defer to v2. |
| Full dynamic exact benchmark | future model/evidence | Defer to v2. |

## Deferred Items

The following are explicitly outside this milestone unless later evidence or
verification gates make them claim-critical:

- real Beijing public-data ingestion
- endogenous Gamma behavior in routing, offer construction, or choice
- a full dynamic exact benchmark
- broad import normalization
- root pytest configuration hardening
- dependency metadata cleanup
- route-stop refactoring
- lockfile or constraints-file creation

