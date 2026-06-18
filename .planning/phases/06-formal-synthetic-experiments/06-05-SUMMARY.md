# Phase 6 Plan 06-05 Summary: Formal Synthetic Experiment Closeout

## 1. Current Phase And Plan

Phase 6 Plan 06-05: formal synthetic experiment closeout and Phase 6 verification.

## 2. Commands Run

- `$env:PYTHONPATH='src'; python -m experiments.formal_statistics --closeout --results-dir results/formal/phase06`
- `$env:PYTHONPATH='src'; python -m experiments.formal_statistics --validate --results-dir results/formal/phase06`
- `$env:PYTHONPATH='src'; pytest tests/test_phase06_formal.py tests/test_runner.py tests/test_metrics.py tests/test_variants.py tests/test_phase06_coverage_controls.py tests/test_phase06_robustness.py -q`

## 3. Git Commit Before Run

`398403f`

## 4. Artifacts Read

- `.planning/STATE.md`
- `.planning/REQUIREMENTS.md`
- `.planning/ROADMAP.md`
- `.planning/CLAIMS_AND_RISKS.md`
- Phase 6 summaries 06-02, 06-03, 06-04
- Phase 6 failure ledger
- Main, coverage-control, and robustness validation reports
- All available formal raw and processed result CSV files under `results/formal/phase06/`

## 5. Artifacts Generated

- `06_FORMAL_SYNTHETIC_RESULTS.md`
- `06_FORMAL_RESULT_MANIFEST.md`
- `06_STATISTICAL_SUMMARY.md`
- `06_EVIDENCE_BOUNDARY.md`
- `06-05-SUMMARY.md`
- `06-VERIFICATION.md`
- `results\formal\phase06\phase06_result_manifest.json`
- `results\formal\phase06\phase06_verification_report.json`
- `results\formal\phase06\tables\main_behavioral_table.csv`
- `results\formal\phase06\tables\paired_differences.csv`
- `results\formal\phase06\tables\paired_bootstrap_ci.csv`
- `results\formal\phase06\tables\matched_coverage_paired_differences.csv`
- `results\formal\phase06\tables\fixed_accepted_set_paired_differences.csv`
- `results\formal\phase06\tables\robustness_setting_summary.csv`
- `results\formal\phase06\tables\equity_type_summary.csv`
- `results\formal\phase06\tables\supplementary_summary.csv`
- `results\formal\phase06\tables\critical_conflicts.csv`
- `results\formal\phase06\tables\final_synthesis_validation.json`
- `results\formal\phase06\plots\phase06_main_efficiency_coverage.png`
- `results\formal\phase06\plots\phase06_failure_ledger_status.png`
- `results\formal\phase06\plots\plot_metadata.json`

## 6. All Package Row Counts

| package | rows | completed | failed | timeout | blocked |
| --- | --- | --- | --- | --- | --- |
| 06-02_main_behavioral | 320 | 320 | 0 | 0 | 0 |
| 06-03_matched_coverage | 320 | 305 | 15 | 0 | 0 |
| 06-03_fixed_accepted_set | 320 | 320 | 0 | 0 | 0 |
| 06-04_utility_sensitivity | 420 | 420 | 0 | 0 | 0 |
| 06-04_mp_density_walking_radius | 180 | 180 | 0 | 0 | 0 |
| 06-04_fleet_demand_stress | 60 | 60 | 0 | 0 | 0 |
| 06-04_equity_type_outcomes | 180 | 180 | 0 | 0 | 0 |
| 06-04_algorithm_diagnostics | 8 | 8 | 0 | 0 | 0 |

## 7. All Validator Statuses

| package | validator |
| --- | --- |
| 06-02_main_behavioral | true |
| 06-03_matched_coverage | true |
| 06-03_fixed_accepted_set | true |
| 06-04_utility_sensitivity | true |
| 06-04_mp_density_walking_radius | true |
| 06-04_fleet_demand_stress | true |
| 06-04_equity_type_outcomes | true |
| 06-04_algorithm_diagnostics | true |

## 8. Schema Drift Summary

| package | schema_drift |
| --- | --- |
| 06-02_main_behavioral | false |
| 06-03_matched_coverage | false |
| 06-03_fixed_accepted_set | false |
| 06-04_utility_sensitivity | false |
| 06-04_mp_density_walking_radius | false |
| 06-04_fleet_demand_stress | false |
| 06-04_equity_type_outcomes | false |
| 06-04_algorithm_diagnostics | false |

## 9. Denominator Check Summary

| package | denominator |
| --- | --- |
| 06-02_main_behavioral | passed |
| 06-03_matched_coverage | passed |
| 06-03_fixed_accepted_set | passed |
| 06-04_utility_sensitivity | passed |
| 06-04_mp_density_walking_radius | passed |
| 06-04_fleet_demand_stress | passed |
| 06-04_equity_type_outcomes | passed |
| 06-04_algorithm_diagnostics | passed |

## 10. Durable Failure Ledger Summary

The ledger records 15 durable rows. All are known matched-coverage rows and are included in verification.

## 11. Whether All Phase 6 Formal Packages Are Reproducible

Yes. Raw rows, processed rows or diagnostic payloads, config manifests, seed/run manifests, validation reports, and result manifests are recorded for each formal package.

## 12. Whether EXP-05 Is Satisfied

True

## 13. Whether Phase 6 Passed Or Blocked

passed

## 14. If Passed, Next Allowed Step

Phase 7 ready. Do not enter Phase 7 automatically.

## 15. If Blocked, Exact Blockers And Rerun Requirements

None
