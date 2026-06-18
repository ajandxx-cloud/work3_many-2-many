# Phase 6 Verification

This verification is strict and fail-closed. EXP-05 can be marked complete only if every check below passes.

| check | passed | evidence |
| --- | --- | --- |
| 06-02_exists_and_passed | true | results\formal\phase06\main_behavioral\validation_report.json |
| 06-03_exists_and_passed | true | matched and fixed validation reports passed |
| 06-04_exists_and_passed | true | results\formal\phase06\robustness\validation_report.json |
| main_behavioral_has_20_paired_seeds | true | unique seeds=20 |
| main_expected_seed_scale_method_rows_exist | true | missing=0 extra=0 |
| coverage_controls_have_durable_rows | true | matched_missing=0 fixed_missing=0 |
| robustness_packages_have_complete_or_durable_rows | true | algorithm_diagnostics: expected=8 actual=8 passed=True; equity_type_outcomes: expected=180 actual=180 passed=True; fleet_demand_stress: expected=60 actual=60 passed=True; mp_density_walking_radius: expected=180 actual=180 passed=True; utility_sensitivity: expected=420 actual=420 passed=True |
| no_silent_missing_rows | true | all expected grids have completed or durable status rows |
| schema_drift_false_across_packages | true | schema_drift false in main, coverage, and robustness validation reports |
| denominator_checks_passed | true | all non-algorithm denominator checks passed |
| failure_ledger_records_known_failed_rows | true | known_failed_rows=15 missing_from_ledger=0 |
| raw_to_processed_reproducibility_documented | true | config manifests exist for all listed formal packages |
| pilot_smoke_not_used_as_formal_evidence | true | manifest excludes smoke package |
| no_final_manuscript_claims_written | true | .planning\phases\06-formal-synthetic-experiments\06_FORMAL_SYNTHETIC_RESULTS.md |
| exp05_complete_only_if_all_checks_pass | true | EXP-05 may be marked complete only because all verification checks pass |

## Result

- Phase 6 passed: True
- EXP-05 satisfied: True
- Next allowed step: Phase 7 ready
