# Phase 10 Result Manifest

**Status:** passed
**Updated:** 2026-06-16
**Scope:** Final reproducibility-package manifest for the evidence-chain rebuild after Phase 6 formal evidence, Phase 7 bounded case closure, Phase 8 claim gate, and Phase 9 claim-gated manuscript refresh.

## Manifest Schema

Each row uses the required Phase 10 fields:

| artifact path | artifact role | source phase | evidence role | status | required for Phase 10 pass | notes |
|---|---|---|---|---|---|---|

Status values are `present`, `missing`, `stale`, or `blocked`. No required row is missing, stale, or blocked as of this verification.

## Planning Files

| artifact path | artifact role | source phase | evidence role | status | required for Phase 10 pass | notes |
|---|---|---|---|---|---|---|
| `.planning/PROJECT.md` | project contract and current validated scope | Planning | verification | present | yes | Updated to include Phase 10 completion boundary. |
| `.planning/REQUIREMENTS.md` | requirement status and traceability | Planning | verification | present | yes | REP-01 and REP-02 marked complete only after this Phase 10 pass. |
| `.planning/ROADMAP.md` | phase roadmap and outputs | Planning | verification | present | yes | Phase 10 marked complete. |
| `.planning/STATE.md` | active phase state | Planning | verification | present | yes | Current phase is 10 with passed status. |
| `.planning/CLAIMS_AND_RISKS.md` | risk and claim policy source | Planning | verification | present | yes | Preserves synthetic-data, novelty, and overclaim risks. |

## Phase 6 Formal Evidence

| artifact path | artifact role | source phase | evidence role | status | required for Phase 10 pass | notes |
|---|---|---|---|---|---|---|
| `.planning/phases/06-formal-synthetic-experiments/06_FORMAL_SYNTHETIC_RESULTS.md` | formal evidence synthesis report | 06 | main | present | yes | Formal synthetic evidence only; Phase 8 owns claim grading. |
| `.planning/phases/06-formal-synthetic-experiments/06_FORMAL_RESULT_MANIFEST.md` | human-readable formal result manifest | 06 | verification | present | yes | Lists formal packages and validation status. |
| `.planning/phases/06-formal-synthetic-experiments/06_STATISTICAL_SUMMARY.md` | main statistics and paired summaries | 06 | main | present | yes | Includes bootstrap CIs; paired hypothesis tests are not implemented. |
| `.planning/phases/06-formal-synthetic-experiments/06_EVIDENCE_BOUNDARY.md` | evidence-boundary contract | 06 | verification | present | yes | Separates main, control, diagnostic, exploratory, and forbidden claims. |
| `.planning/phases/06-formal-synthetic-experiments/06-05-SUMMARY.md` | closeout summary | 06 | verification | present | yes | Records 06-05 closeout and package counts. |
| `.planning/phases/06-formal-synthetic-experiments/06-VERIFICATION.md` | Phase 6 fail-closed verification | 06 | verification | present | yes | Phase 6 passed; EXP-05 satisfied. |
| `results/formal/phase06/phase06_result_manifest.json` | machine-readable result manifest | 06 | verification | present | yes | Eight formal packages listed; smoke excluded. |
| `results/formal/phase06/phase06_verification_report.json` | machine-readable verification report | 06 | verification | present | yes | Passed, schema drift false, denominator checks passed, 15 durable failed rows recorded. |
| `results/formal/phase06/main_behavioral/raw_results.csv` | main behavioral raw rows | 06 | main | present | yes | 320 rows, 20 paired seeds x 4 scales x 4 methods. |
| `results/formal/phase06/main_behavioral/processed_results.csv` | main behavioral processed summary | 06 | main | present | yes | Processed package output. |
| `results/formal/phase06/main_behavioral/metrics_table.csv` | main behavioral aggregate metrics | 06 | main | present | yes | Regeneration input for main evidence displays. |
| `results/formal/phase06/main_behavioral/synthetic_results.csv` | copied main behavioral raw export | 06 | main | present | yes | Legacy-compatible formal output copy. |
| `results/formal/phase06/main_behavioral/utility_components.csv` | utility component rows | 06 | diagnostic | present | yes | Utility joinability evidence. |
| `results/formal/phase06/main_behavioral/utility_logs.csv` | utility logs | 06 | diagnostic | present | yes | 88,000 linkable rows per Phase 6 state. |
| `results/formal/phase06/main_behavioral/config_manifest.json` | main behavioral config manifest | 06 | verification | present | yes | Config provenance. |
| `results/formal/phase06/main_behavioral/seed_manifest.json` | main behavioral seed manifest | 06 | verification | present | yes | Seed provenance. |
| `results/formal/phase06/main_behavioral/run_manifest.json` | main behavioral run manifest | 06 | verification | present | yes | Run provenance. |
| `results/formal/phase06/main_behavioral/validation_report.json` | main behavioral validator output | 06 | verification | present | yes | Validator passed. |
| `results/formal/phase06/coverage_controls/matched_coverage/raw_results.csv` | matched-coverage raw rows | 06 | control | present | yes | 320 durable rows, 305 completed and 15 failed FullModel rows. |
| `results/formal/phase06/coverage_controls/matched_coverage/processed_results.csv` | matched-coverage processed rows | 06 | control | present | yes | Control summary input. |
| `results/formal/phase06/coverage_controls/matched_coverage/config_manifest.json` | matched-coverage config manifest | 06 | verification | present | yes | Control provenance. |
| `results/formal/phase06/coverage_controls/matched_coverage/seed_manifest.json` | matched-coverage seed manifest | 06 | verification | present | yes | Control seed provenance. |
| `results/formal/phase06/coverage_controls/matched_coverage/validation_report.json` | matched-coverage validator output | 06 | verification | present | yes | Validator passed; denominator checks passed. |
| `results/formal/phase06/coverage_controls/fixed_accepted_set/raw_results.csv` | fixed accepted-set raw rows | 06 | diagnostic | present | yes | 320 completed rows; diagnostic only. |
| `results/formal/phase06/coverage_controls/fixed_accepted_set/processed_results.csv` | fixed accepted-set processed rows | 06 | diagnostic | present | yes | Diagnostic summary input. |
| `results/formal/phase06/coverage_controls/fixed_accepted_set/retained_set_manifest.json` | fixed accepted-set retained set manifest | 06 | diagnostic | present | yes | Documents common accepted-set construction. |
| `results/formal/phase06/coverage_controls/fixed_accepted_set/config_manifest.json` | fixed accepted-set config manifest | 06 | verification | present | yes | Diagnostic provenance. |
| `results/formal/phase06/coverage_controls/fixed_accepted_set/seed_manifest.json` | fixed accepted-set seed manifest | 06 | verification | present | yes | Diagnostic seed provenance. |
| `results/formal/phase06/coverage_controls/fixed_accepted_set/validation_report.json` | fixed accepted-set validator output | 06 | verification | present | yes | Validator passed; diagnostic only. |
| `results/formal/phase06/robustness/utility_sensitivity/raw_results.csv` | utility-sensitivity raw rows | 06 | diagnostic | present | yes | 420 completed diagnostic rows. |
| `results/formal/phase06/robustness/utility_sensitivity/processed_results.csv` | utility-sensitivity processed rows | 06 | diagnostic | present | yes | Reduced robustness diagnostic. |
| `results/formal/phase06/robustness/utility_sensitivity/sensitivity_grid.json` | utility grid | 06 | diagnostic | present | yes | Records simulation-range settings. |
| `results/formal/phase06/robustness/utility_sensitivity/utility_logs.csv` | utility-sensitivity utility logs | 06 | diagnostic | present | yes | Diagnostic utility provenance. |
| `results/formal/phase06/robustness/utility_sensitivity/config_manifest.json` | utility-sensitivity config manifest | 06 | verification | present | yes | Diagnostic config provenance. |
| `results/formal/phase06/robustness/utility_sensitivity/validation_report.json` | utility-sensitivity validator output | 06 | verification | present | yes | Validator passed. |
| `results/formal/phase06/robustness/mp_density_walking_radius/raw_results.csv` | MP-density/walking-radius raw rows | 06 | diagnostic | present | yes | 180 completed diagnostic rows. |
| `results/formal/phase06/robustness/mp_density_walking_radius/processed_results.csv` | MP-density/walking-radius processed rows | 06 | diagnostic | present | yes | Diagnostic summary input. |
| `results/formal/phase06/robustness/mp_density_walking_radius/density_radius_grid.json` | density/radius grid | 06 | diagnostic | present | yes | Synthetic grid only. |
| `results/formal/phase06/robustness/mp_density_walking_radius/config_manifest.json` | density/radius config manifest | 06 | verification | present | yes | Diagnostic config provenance. |
| `results/formal/phase06/robustness/mp_density_walking_radius/validation_report.json` | density/radius validator output | 06 | verification | present | yes | Validator passed. |
| `results/formal/phase06/robustness/fleet_demand_stress/raw_results.csv` | fleet-demand stress raw rows | 06 | diagnostic | present | yes | 60 completed diagnostic rows. |
| `results/formal/phase06/robustness/fleet_demand_stress/processed_results.csv` | fleet-demand stress processed rows | 06 | diagnostic | present | yes | Diagnostic summary input. |
| `results/formal/phase06/robustness/fleet_demand_stress/stress_grid.json` | fleet-demand stress grid | 06 | diagnostic | present | yes | Synthetic stress settings. |
| `results/formal/phase06/robustness/fleet_demand_stress/config_manifest.json` | fleet-demand config manifest | 06 | verification | present | yes | Diagnostic config provenance. |
| `results/formal/phase06/robustness/fleet_demand_stress/validation_report.json` | fleet-demand validator output | 06 | verification | present | yes | Validator passed. |
| `results/formal/phase06/robustness/equity_type_outcomes/type_level_outcomes.csv` | equity type-level rows | 06 | exploratory | present | yes | 180 completed rows; simulation-range type constructs. |
| `results/formal/phase06/robustness/equity_type_outcomes/individual_burden_distribution.csv` | individual burden rows | 06 | exploratory | present | yes | 12,000 individual burden rows. |
| `results/formal/phase06/robustness/equity_type_outcomes/equity_summary.json` | equity summary | 06 | exploratory | present | yes | Exploratory only. |
| `results/formal/phase06/robustness/equity_type_outcomes/config_manifest.json` | equity config manifest | 06 | verification | present | yes | Exploratory package provenance. |
| `results/formal/phase06/robustness/equity_type_outcomes/validation_report.json` | equity validator output | 06 | verification | present | yes | Validator passed. |
| `results/formal/phase06/robustness/algorithm_diagnostics/rolling_horizon_diagnostics.csv` | rolling-horizon diagnostics | 06 | diagnostic | present | yes | Algorithm diagnostic only. |
| `results/formal/phase06/robustness/algorithm_diagnostics/alns_budget_diagnostics.json` | ALNS budget diagnostics | 06 | diagnostic | present | yes | Heuristic diagnostic evidence only. |
| `results/formal/phase06/robustness/algorithm_diagnostics/milp_gap_diagnostics.json` | MILP static diagnostic | 06 | diagnostic | present | yes | Static/scope-limited diagnostic. |
| `results/formal/phase06/robustness/algorithm_diagnostics/config_manifest.json` | algorithm diagnostic config manifest | 06 | verification | present | yes | Diagnostic config provenance. |
| `results/formal/phase06/robustness/algorithm_diagnostics/validation_report.json` | algorithm diagnostic validator output | 06 | verification | present | yes | Validator passed; denominator checks not applicable to algorithm diagnostic. |
| `results/formal/phase06/robustness/run_manifest.json` | robustness run manifest | 06 | verification | present | yes | Shared robustness package run manifest. |
| `results/formal/phase06/robustness/validation_report.json` | robustness aggregate validator output | 06 | verification | present | yes | Validator passed. |
| `results/formal/phase06/robustness/supplementary_gate_results.csv` | supplementary gate output | 06 | verification | present | yes | Robustness gate summary. |
| `results/formal/phase06/tables/main_behavioral_table.csv` | regenerated main behavioral table | 06 | main | present | yes | Reviewer/coauthor main table source. |
| `results/formal/phase06/tables/paired_differences.csv` | paired differences | 06 | main | present | yes | Main paired difference source. |
| `results/formal/phase06/tables/paired_bootstrap_ci.csv` | paired bootstrap CIs | 06 | main | present | yes | 150 CI rows; no paired hypothesis tests. |
| `results/formal/phase06/tables/matched_coverage_paired_differences.csv` | matched-coverage paired differences | 06 | control | present | yes | Includes valid-pair accounting. |
| `results/formal/phase06/tables/fixed_accepted_set_paired_differences.csv` | fixed accepted-set paired differences | 06 | diagnostic | present | yes | Diagnostic only. |
| `results/formal/phase06/tables/robustness_setting_summary.csv` | robustness setting summary | 06 | diagnostic | present | yes | Reduced diagnostic summary. |
| `results/formal/phase06/tables/equity_type_summary.csv` | equity type summary | 06 | exploratory | present | yes | Exploratory summary. |
| `results/formal/phase06/tables/supplementary_summary.csv` | supplementary package summary | 06 | verification | present | yes | Gate/package summary. |
| `results/formal/phase06/tables/critical_conflicts.csv` | critical conflicts table | 06 | verification | present | yes | Empty critical conflicts after closeout. |
| `results/formal/phase06/tables/final_synthesis_validation.json` | closeout validation JSON | 06 | verification | present | yes | `passed: true`; no missing required files. |
| `results/formal/phase06/plots/phase06_main_efficiency_coverage.png` | main evidence plot | 06 | main | present | yes | Regenerated display artifact. |
| `results/formal/phase06/plots/phase06_failure_ledger_status.png` | failure ledger status plot | 06 | verification | present | yes | Makes durable failures visible. |
| `results/formal/phase06/plots/plot_metadata.json` | plot metadata | 06 | verification | present | yes | Plot provenance. |

## Phase 7 Case-Study Boundary

| artifact path | artifact role | source phase | evidence role | status | required for Phase 10 pass | notes |
|---|---|---|---|---|---|---|
| `.planning/phases/07-semi-real-or-beijing-inspired-case-study/07_DATA_AUDIT.md` | data availability audit | 07 | illustrative | present | yes | Finds no real/semi-real case data. |
| `.planning/phases/07-semi-real-or-beijing-inspired-case-study/07_CASE_STUDY_RESULTS.md` | bounded case result note | 07 | illustrative | present | yes | No new real/semi-real case experiment was run. |
| `.planning/phases/07-semi-real-or-beijing-inspired-case-study/07_CASE_CLAIM_BOUNDARY.md` | case claim boundary | 07 | verification | present | yes | Beijing-inspired synthetic only. |
| `.planning/phases/07-semi-real-or-beijing-inspired-case-study/07-VERIFICATION.md` | Phase 7 verification | 07 | verification | present | yes | Phase 7 passed. |
| `results/beijing_results.csv` | legacy Beijing-labeled rows | legacy | illustrative | present | no | Not formal validated evidence; may only support provenance/illustrative boundary discussion. |

## Phase 8 Claim Gate

| artifact path | artifact role | source phase | evidence role | status | required for Phase 10 pass | notes |
|---|---|---|---|---|---|---|
| `.planning/phases/08-evidence-synthesis-and-claim-gate/08_CLAIM_INVENTORY.md` | claim inventory | 08 | verification | present | yes | 20 inventoried claim units. |
| `.planning/phases/08-evidence-synthesis-and-claim-gate/08_CLAIM_EVIDENCE_MATRIX.md` | claim-to-evidence matrix | 08 | verification | present | yes | Grades claims strong/moderate/exploratory/unsupported. |
| `.planning/phases/08-evidence-synthesis-and-claim-gate/08_SUPPORTED_CLAIMS.md` | allowed claim list | 08 | verification | present | yes | Source of allowed manuscript claim units. |
| `.planning/phases/08-evidence-synthesis-and-claim-gate/08_UNSUPPORTED_OR_EXPLORATORY_CLAIMS.md` | forbidden/downgraded claims | 08 | verification | present | yes | Blocks overclaims and unsupported wording. |
| `.planning/phases/08-evidence-synthesis-and-claim-gate/08_REVISED_ABSTRACT_BULLETS.md` | revised abstract bullets | 08 | verification | present | yes | Claim-gated abstract-unit planning. |
| `.planning/phases/08-evidence-synthesis-and-claim-gate/08_REVISED_CONCLUSION_BULLETS.md` | revised conclusion bullets | 08 | verification | present | yes | Claim-gated conclusion planning. |
| `.planning/phases/08-evidence-synthesis-and-claim-gate/08_EQUITY_GATE.md` | equity gate | 08 | exploratory | present | yes | Equity remains bounded/exploratory. |
| `.planning/phases/08-evidence-synthesis-and-claim-gate/08-VERIFICATION.md` | Phase 8 verification | 08 | verification | present | yes | Phase 8 passed; CLM-01/02/03 and MET-04 complete. |

## Phase 9 Refreshed Manuscript Planning

| artifact path | artifact role | source phase | evidence role | status | required for Phase 10 pass | notes |
|---|---|---|---|---|---|---|
| `.planning/phases/09-manuscript-restructure-for-tr-part-e/09_CLAIM_GATE_AUDIT.md` | Phase 8-to-Phase 9 audit | 09 | verification | present | yes | Confirms unsupported wording excluded. |
| `.planning/phases/09-manuscript-restructure-for-tr-part-e/09_TR_E_MANUSCRIPT_STRUCTURE.md` | claim-gated manuscript structure | 09 | verification | present | yes | Planning artifact only; no `.tex` rewrite in Phase 10. |
| `.planning/phases/09-manuscript-restructure-for-tr-part-e/09_REVISED_ABSTRACT.md` | revised abstract plan | 09 | verification | present | yes | Obeys Phase 8 allowed wording. |
| `.planning/phases/09-manuscript-restructure-for-tr-part-e/09_REVISED_INTRODUCTION_PLAN.md` | revised introduction plan | 09 | verification | present | yes | Avoids first/only overclaim. |
| `.planning/phases/09-manuscript-restructure-for-tr-part-e/09_EXPERIMENT_SECTION_PLAN.md` | evidence-family experiment-section plan | 09 | verification | present | yes | Separates main/control/diagnostic/exploratory/illustrative evidence. |
| `.planning/phases/09-manuscript-restructure-for-tr-part-e/09_TABLE_FIGURE_PLAN.md` | table/figure plan | 09 | verification | present | yes | Requires served share/rejection context and evidence family captions. |
| `.planning/phases/09-manuscript-restructure-for-tr-part-e/09_MANAGERIAL_INSIGHT_AND_LIMITATION_PLAN.md` | managerial/limitation plan | 09 | verification | present | yes | Simulation-based, limitation-first. |
| `.planning/phases/09-manuscript-restructure-for-tr-part-e/09-REFRESH-SUMMARY.md` | Phase 9 refresh summary | 09 | verification | present | yes | Phase 9 refresh closeout. |
| `.planning/phases/09-manuscript-restructure-for-tr-part-e/09-VERIFICATION.md` | Phase 9 verification | 09 | verification | present | yes | Phase 9 refresh passed. |

## Test And Validation Artifacts

| artifact path | artifact role | source phase | evidence role | status | required for Phase 10 pass | notes |
|---|---|---|---|---|---|---|
| Active pytest command | final regression command | 10 | verification | present | yes | `$env:PYTHONPATH='src;.'; pytest tests/test_phase06_formal.py tests/test_runner.py tests/test_metrics.py tests/test_variants.py tests/test_phase06_coverage_controls.py tests/test_phase06_robustness.py -q` -> 100 passed in 5.55s. |
| Schema drift check | final schema drift command | 10 | verification | present | yes | `gsd-sdk query verify.schema-drift 10` -> `drift_detected: false`, `blocking: false`. |
| Phase 6 synthesis validation | formal synthesis validation command | 10 | verification | present | yes | `$env:PYTHONPATH='src;.'; python -m experiments.formal_statistics --validate --results-dir results/formal/phase06` -> passed with no missing files. |
| Denominator check status | denominator integrity | 06/10 | verification | present | yes | Phase 6 verification report records denominator checks passed across main, coverage, and non-algorithm robustness packages. |
| Failure ledger status | durable failure ledger | 06/10 | verification | present | yes | 15 matched-coverage failed rows recorded; no silent missing rows. |
| Durable failure row summary | failure-row policy evidence | 06/10 | verification | present | yes | Failed rows are explicit durable artifacts, not hidden omissions. |
| Commit `98f0cb8` | Phase 6 main matrix commit | 06 | verification | present | yes | `feat(06-02): run formal main behavioral matrix`. |
| Commit `d1a157b` | Phase 6 coverage-control commit | 06 | verification | present | yes | `feat(06-03): run formal coverage-confounding controls`. |
| Commit `8e6c618` | Phase 6 robustness commit | 06 | verification | present | yes | `feat(06-04): run formal robustness diagnostics`. |
| Commit `3037cc2` | Phase 6 closeout commit | 06 | verification | present | yes | `docs(06-05): synthesize formal synthetic evidence`. |
| Commit `83309a9` | Phase 7 commit | 07 | verification | present | yes | `docs(07): close case study with synthetic-data limitations`. |
| Commit `8236ca1` | Phase 8 commit | 08 | verification | present | yes | `docs(08): gate claims against formal evidence`. |
| Commit `9b03eb0` | Phase 9 commit | 09 | verification | present | yes | `docs(09): refresh manuscript structure after claim gate`. |
| This commit | Phase 10 final reproducibility verification commit | 10 | verification | present | yes | `docs(10): pass final reproducibility verification`; exact hash is available from `git log -1 --oneline`. |

## Final Manifest Status

All required Phase 10 manifest rows are present. Main evidence, control evidence, diagnostic evidence, exploratory evidence, illustrative case evidence, and verification artifacts are separated. No pilot, legacy, diagnostic, exploratory, or illustrative artifact is promoted to a headline claim role.
