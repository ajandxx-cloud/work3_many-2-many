# Phase 6 Plan 06-04 Summary: Robustness, Sensitivity, and Equity Diagnostics

## 1. Purpose

Execute reduced formal robustness diagnostics after the 06-02 main behavioral matrix and 06-03 coverage-confounding controls.

## 2. Why Robustness Diagnostics Are Needed After 06-02 And 06-03

06-02 established the main behavioral matrix under default choice parameters. 06-03 showed that FullModel efficiency advantages survive matched coverage and are mixed under fixed accepted-set vkm/original. 06-04 tests whether the remaining evidence boundary is sensitive to utility assumptions, walking-radius and meeting-point-density settings, fleet-demand stress, and passenger-type outcomes.

## 3. Commands Run

- `python -m experiments.phase06_robustness --package all --results-root results/formal/phase06/robustness --write-summary`
- `python -m experiments.phase06_robustness --package algorithm_diagnostics --results-root results/formal/phase06/robustness`

## 4. Git Commit Before Run

`d1a157b`

## 5. Packages Executed

utility_sensitivity, mp_density_walking_radius, fleet_demand_stress, equity_type_outcomes, algorithm_diagnostics

## 6. Seed List And Pairing

Seeds: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]. Seeds are paired across methods and settings.

## 7. Scale List

Scales: [100, 200, 300]. The design is a reduced formal diagnostic, not main headline evidence.

## 8. Method List

Methods: ['DoorToDoor_Choice_CommonRouting', 'BidirectionalMP_Choice_RH_ALNS']. Single-sided variants were not included in this reduced runtime-bounded diagnostic.

## 9. Parameter Grids

- Utility sensitivity: `results\formal\phase06\robustness\utility_sensitivity\sensitivity_grid.json`
- Walking radius / MP density: `results\formal\phase06\robustness\mp_density_walking_radius\density_radius_grid.json`
- Fleet-demand stress: `results\formal\phase06\robustness\fleet_demand_stress\stress_grid.json`

## 10. Expected Row Counts

- algorithm_diagnostics: expected=8, actual=8, completed=8, failed=0, timeout=0, blocked=0
- equity_type_outcomes: expected=180, actual=180, completed=180, failed=0, timeout=0, blocked=0
- fleet_demand_stress: expected=60, actual=60, completed=60, failed=0, timeout=0, blocked=0
- mp_density_walking_radius: expected=180, actual=180, completed=180, failed=0, timeout=0, blocked=0
- utility_sensitivity: expected=420, actual=420, completed=420, failed=0, timeout=0, blocked=0

## 11. Actual Row Counts

- algorithm_diagnostics: actual=8, expected=8, completed=8, failed=0, timeout=0, blocked=0
- equity_type_outcomes: actual=180, expected=180, completed=180, failed=0, timeout=0, blocked=0
- fleet_demand_stress: actual=60, expected=60, completed=60, failed=0, timeout=0, blocked=0
- mp_density_walking_radius: actual=180, expected=180, completed=180, failed=0, timeout=0, blocked=0
- utility_sensitivity: actual=420, expected=420, completed=420, failed=0, timeout=0, blocked=0

## 12. Completed / Failed / Timeout / Blocked Row Counts

- algorithm_diagnostics: expected=8, actual=8, completed=8, failed=0, timeout=0, blocked=0
- equity_type_outcomes: expected=180, actual=180, completed=180, failed=0, timeout=0, blocked=0
- fleet_demand_stress: expected=60, actual=60, completed=60, failed=0, timeout=0, blocked=0
- mp_density_walking_radius: expected=180, actual=180, completed=180, failed=0, timeout=0, blocked=0
- utility_sensitivity: expected=420, actual=420, completed=420, failed=0, timeout=0, blocked=0

## 13. Durable Failure Summary

Failure rows, if any, were appended to `.planning/phases/06-formal-synthetic-experiments/06_FAILURE_RERUN_LEDGER.csv`. Structural validation errors: none.

## 14. Schema Validation

schema_drift: False

## 15. Denominator Validation

{
  "algorithm_diagnostics": {
    "status": "not_applicable_algorithm_diagnostic"
  },
  "equity_type_outcomes": {
    "rejection_partition": "passed",
    "served_share": "passed",
    "type_level_acceptance_rate": "passed"
  },
  "fleet_demand_stress": {
    "behavioral_acceptance_rate": "passed",
    "rejection_partition": "passed",
    "served_share": "passed",
    "vkm_per_original_request": "passed",
    "vkm_per_served_trip": "passed"
  },
  "mp_density_walking_radius": {
    "behavioral_acceptance_rate": "passed",
    "rejection_partition": "passed",
    "served_share": "passed",
    "vkm_per_original_request": "passed",
    "vkm_per_served_trip": "passed"
  },
  "utility_sensitivity": {
    "behavioral_acceptance_rate": "passed",
    "rejection_partition": "passed",
    "served_share": "passed",
    "vkm_per_original_request": "passed",
    "vkm_per_served_trip": "passed"
  }
}

## 16. Utility Sensitivity Summary

{
  "vkm_per_served": "yes",
  "vkm_per_original": "yes",
  "served_diff_by_setting": [
    {
      "parameter_setting_id": "baseline_default",
      "mean": -5.20211841391595,
      "min": -16.82296886106752,
      "max": -2.4608677965702928
    },
    {
      "parameter_setting_id": "ivt_disutility_high",
      "mean": -6.019263699775453,
      "min": -14.893786912254978,
      "max": -2.1274580682783792
    },
    {
      "parameter_setting_id": "outside_option_high",
      "mean": -6.24348071272174,
      "min": -14.893786912254978,
      "max": 9.663158544332124
    },
    {
      "parameter_setting_id": "service_asc_low",
      "mean": -6.24348071272174,
      "min": -14.893786912254978,
      "max": 9.663158544332124
    },
    {
      "parameter_setting_id": "wait_disutility_high",
      "mean": -5.630864268554894,
      "min": -16.82296886106752,
      "max": -2.9899459572947933
    },
    {
      "parameter_setting_id": "walk_disutility_high",
      "mean": -5.19963328070192,
      "min": -16.82296886106752,
      "max": -2.4608677965702928
    },
    {
      "parameter_setting_id": "walk_sensitive_majority",
      "mean": -4.62991853573838,
      "min": -8.744117633699204,
      "max": 1.202401059127073
    }
  ],
  "original_diff_by_setting": [
    {
      "parameter_setting_id": "baseline_default",
      "mean": -1.5533386850022153,
      "min": -3.0204735041523167,
      "max": 0.026644172827989587
    },
    {
      "parameter_setting_id": "ivt_disutility_high",
      "mean": -1.4526127916891698,
      "min": -3.1187119484002865,
      "max": 0.30821404487960924
    },
    {
      "parameter_setting_id": "outside_option_high",
      "mean": -0.876603662301351,
      "min": -1.687713242400206,
      "max": 0.0966315854433212
    },
    {
      "parameter_setting_id": "service_asc_low",
      "mean": -0.876603662301351,
      "min": -1.687713242400206,
      "max": 0.0966315854433212
    },
    {
      "parameter_setting_id": "wait_disutility_high",
      "mean": -1.5118762171686038,
      "min": -3.463887743434313,
      "max": 0.026644172827989587
    },
    {
      "parameter_setting_id": "walk_disutility_high",
      "mean": -1.5551307255128166,
      "min": -3.0204735041523167,
      "max": 0.026644172827989587
    },
    {
      "parameter_setting_id": "walk_sensitive_majority",
      "mean": -1.7590642047089695,
      "min": -3.3555577442140407,
      "max": -0.3025415103592639
    }
  ]
}

## 17. Walking Radius / Meeting-Point Density Summary

{
  "vkm_per_served": "yes",
  "vkm_per_original": "yes",
  "served_diff_by_setting": [
    {
      "parameter_setting_id": "default_radius_default_density",
      "mean": -5.20211841391595,
      "min": -16.82296886106752,
      "max": -2.4608677965702928
    },
    {
      "parameter_setting_id": "high_radius_dense_density",
      "mean": -5.266913954185283,
      "min": -23.19915899786195,
      "max": -1.8067376312396561
    },
    {
      "parameter_setting_id": "low_radius_sparse_density",
      "mean": -15.706705524772218,
      "min": -36.31035500493399,
      "max": -12.869880290069776
    }
  ],
  "original_diff_by_setting": [
    {
      "parameter_setting_id": "default_radius_default_density",
      "mean": -1.5533386850022153,
      "min": -3.0204735041523167,
      "max": 0.026644172827989587
    },
    {
      "parameter_setting_id": "high_radius_dense_density",
      "mean": -1.1452054413551742,
      "min": -3.0069031086922804,
      "max": 0.5546801704457026
    },
    {
      "parameter_setting_id": "low_radius_sparse_density",
      "mean": -3.0750399611748973,
      "min": -4.556323060545425,
      "max": -0.3631035500493398
    }
  ]
}

## 18. Fleet-Demand Stress Summary

{
  "vkm_per_served": "yes",
  "vkm_per_original": "yes",
  "served_diff_by_setting": [
    {
      "parameter_setting_id": "stress_base",
      "mean": -5.145021675700479,
      "min": -7.348746560636543,
      "max": -2.6073724206490763
    },
    {
      "parameter_setting_id": "stress_high_demand",
      "mean": -3.8057050163322743,
      "min": -6.158829077708553,
      "max": -1.3102978508885315
    },
    {
      "parameter_setting_id": "stress_low_demand",
      "mean": -6.047219334353781,
      "min": -9.113551153529011,
      "max": -3.793577819257127
    }
  ],
  "original_diff_by_setting": [
    {
      "parameter_setting_id": "stress_base",
      "mean": -1.4364164149257899,
      "min": -1.9529190054296364,
      "max": -0.8271396564385092
    },
    {
      "parameter_setting_id": "stress_high_demand",
      "mean": -1.546303547658377,
      "min": -2.2541067235227636,
      "max": -0.9881816668078285
    },
    {
      "parameter_setting_id": "stress_low_demand",
      "mean": -1.8416418714185088,
      "min": -2.9077947566123017,
      "max": -0.7692915640287834
    }
  ]
}

## 19. Equity / Type-Level Summary

Equity validation: True. Type-level outcomes and individual burden distribution were generated. Passenger types remain simulation-range constructs.

## 20. Whether FullModel Advantage Is Robust, Conditional, Mixed, Or Unsupported

conditional. The diagnostic evidence supports a conditional efficiency interpretation, not an unconditional final manuscript claim.

## 21. Phase 8 Claim Strength Supported

Supports at most moderate/conditional robustness screening for efficiency. Equity remains exploratory until Phase 8 grades claim evidence.

## 22. Whether 06-04 Passed Or Blocked

passed

## 23. Exact Blockers If Blocked

None

## 24. Whether Phase 6 Can Proceed To 06-05

Phase 6 can proceed to 06-05; do not enter 06-05 automatically.
