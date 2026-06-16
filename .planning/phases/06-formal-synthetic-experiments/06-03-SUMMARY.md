# Phase 6 Plan 06-03 Summary: Coverage-Confounding Formal Controls

## 1. Task Purpose

Run formal coverage-confounding controls after the 06-02 main behavioral matrix to test whether the observed FullModel vehicle-km advantage survives comparable served-count and fixed accepted-set comparisons.

## 2. Why This Control Is Necessary

The 06-02 main behavioral matrix completed, but FullModel also had lower served share than DoorToDoor and the single-sided baselines. That means lower vehicle-km and lower vkm denominators can be coverage-confounded. 06-03 therefore isolates matched coverage and fixed accepted-set routing before any final manuscript claim is allowed.

## 3. Commands Run

- `python -m experiments.phase06_coverage_controls --package all --results-root results/formal/phase06/coverage_controls`
- `python -m experiments.phase06_coverage_controls --validate --package all --results-root results/formal/phase06/coverage_controls --write-summary`

## 4. Git Commit Before Run

`98f0cb8`

## 5. Seed List

[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

## 6. Scale List

[100, 200, 300, 500]

## 7. Method List

['BidirectionalMP_Choice_RH_ALNS', 'DoorToDoor_Choice_CommonRouting', 'SingleSidedDropoff_Choice_CommonRouting', 'SingleSidedPickup_Choice_CommonRouting']

## 8. Matched-Coverage Construction Rule

For each seed x scale cell, the target served count is the minimum completed 06-02 served count across all four comparison methods. Each method is rerun on the same formal synthetic demand realization with a deterministic served-count cap. Rows record the attainable count, matched target, actual served count, served share, coverage gap, total vehicle-km, vkm/served, and vkm/original.

## 9. Fixed Accepted-Set Construction Rule

For each seed x scale cell, retained requests are selected by common served intersection first, common actual-offer serviceable intersection second, and the Phase 5 `common_candidate_serviceable` fallback only when both strict intersections are empty. The same retained set is routed for every method under diagnostic-only deterministic routing.

## 10. Fallback Rule And Fallback Count

Fallback rule: use `common_candidate_serviceable` only when `common_served` and `common_actual_offer_serviceable` are empty. Fallback seed x scale cells: 0.

## 11. Expected Rows

- Matched coverage: 320
- Fixed accepted set: 320

## 12. Actual Rows

- Matched coverage: 320
- Fixed accepted set: 320

## 13. Completed / Failed / Timeout / Blocked Row Counts

- Matched coverage: completed=305, failed=15, timeout=0, blocked=0
- Fixed accepted set: completed=320, failed=0, timeout=0, blocked=0

## 14. Method x Seed x Scale Completeness

- Matched coverage validator row count: {'actual_rows': 320, 'blocked_rows': 0, 'completed_rows': 305, 'expected_rows': 320, 'failed_rows': 15, 'processed_rows': 4, 'timeout_rows': 0}
- Fixed accepted-set validator row count: {'actual_rows': 320, 'blocked_rows': 0, 'completed_rows': 320, 'expected_rows': 320, 'failed_rows': 0, 'fallback_rows': 0, 'processed_rows': 4, 'timeout_rows': 0}

## 15. Schema Validation

- Matched coverage schema_drift: False
- Fixed accepted set schema_drift: False

## 16. Denominator Validation

- Matched coverage: {'coverage_gap': 'passed', 'coverage_tolerance': 'passed', 'served_share': 'passed', 'vkm_per_original_request': 'passed', 'vkm_per_served_trip': 'passed'}
- Fixed accepted set: {'deterministic_inserted_share': 'passed', 'unserved_accepted_count': 'passed', 'vkm_per_original_request': 'passed', 'vkm_per_served_request': 'passed'}

## 17. Matched Target Served Count Summary

{
  "matched_target_served_count": {
    "mean": 44.3875,
    "min": 0.0,
    "max": 109.0
  }
}

## 18. Actual Served Count Summary

{
  "actual_served_count": {
    "mean": 44.171875,
    "min": 0.0,
    "max": 109.0
  }
}

## 19. Coverage Gap Summary

{
  "coverage_gap_abs": {
    "mean": 0.215625,
    "min": 0.0,
    "max": 9.0
  }
}

## 20. Vehicle-Km Summary

Matched coverage:

{
  "total_vehicle_km": {
    "mean": 545.158141314768,
    "min": 0.0,
    "max": 1307.5615757640364
  },
  "vkm_per_served_trip": {
    "mean": 13.132816942519735,
    "min": 0.0,
    "max": 36.36001404284988
  },
  "vkm_per_original_request": {
    "mean": 1.9802868340947382,
    "min": 0.0,
    "max": 4.378440647092241
  }
}

Fixed accepted set:

{
  "total_vehicle_km": {
    "mean": 284.9575362516169,
    "min": 11.048452818700095,
    "max": 854.3501627061079
  },
  "vkm_per_served_request": {
    "mean": 14.317128165810402,
    "min": 5.707106636123141,
    "max": 36.36001404284988
  },
  "vkm_per_original_request": {
    "mean": 0.9500603244013337,
    "min": 0.1104845281870009,
    "max": 1.903635313895449
  }
}

## 21. Paired Differences Versus Baselines

Matched coverage vkm/served:

| metric | baseline | mean_full_minus_baseline | min_full_minus_baseline | max_full_minus_baseline | full_better_share |
| --- | --- | --- | --- | --- | --- |
| vkm_per_served_trip | DoorToDoor_Choice_CommonRouting | -4.61684 | -14.8938 | 0 | 0.8 |
| vkm_per_served_trip | SingleSidedPickup_Choice_CommonRouting | -3.99848 | -14.3585 | 0.0501465 | 0.7875 |
| vkm_per_served_trip | SingleSidedDropoff_Choice_CommonRouting | -4.10731 | -14.9434 | 0 | 0.8 |

Matched coverage vkm/original:

| metric | baseline | mean_full_minus_baseline | min_full_minus_baseline | max_full_minus_baseline | full_better_share |
| --- | --- | --- | --- | --- | --- |
| vkm_per_original_request | DoorToDoor_Choice_CommonRouting | -0.68084 | -1.80404 | 0 | 0.8 |
| vkm_per_original_request | SingleSidedPickup_Choice_CommonRouting | -0.580799 | -1.32749 | 0.00902636 | 0.7875 |
| vkm_per_original_request | SingleSidedDropoff_Choice_CommonRouting | -0.604853 | -2.17037 | 0 | 0.8 |

Fixed accepted set vkm/served:

| metric | baseline | mean_full_minus_baseline | min_full_minus_baseline | max_full_minus_baseline | full_better_share |
| --- | --- | --- | --- | --- | --- |
| vkm_per_served_request | DoorToDoor_Choice_CommonRouting | -5.23247 | -19.178 | 4.48566 | 0.975 |
| vkm_per_served_request | SingleSidedPickup_Choice_CommonRouting | -3.79588 | -19.8149 | 6.10372 | 0.95 |
| vkm_per_served_request | SingleSidedDropoff_Choice_CommonRouting | -3.83108 | -19.8149 | 4.37088 | 0.9625 |

Fixed accepted set vkm/original:

| metric | baseline | mean_full_minus_baseline | min_full_minus_baseline | max_full_minus_baseline | full_better_share |
| --- | --- | --- | --- | --- | --- |
| vkm_per_original_request | DoorToDoor_Choice_CommonRouting | 0.0523446 | -0.659468 | 0.864787 | 0.525 |
| vkm_per_original_request | SingleSidedPickup_Choice_CommonRouting | 0.126704 | -0.442666 | 1.04467 | 0.35 |
| vkm_per_original_request | SingleSidedDropoff_Choice_CommonRouting | 0.115084 | -0.381313 | 1.02679 | 0.35 |

## 22. Whether FullModel Advantage Persists Under Matched Coverage

vkm_per_served: yes; vkm_per_original: yes

## 23. Whether FullModel Advantage Persists Under Fixed Accepted Set

vkm_per_served: yes; vkm_per_original: no_or_mixed

## 24. Whether 06-03 Passed Or Blocked

passed

## 25. Exact Blockers If Blocked

Matched coverage errors: []

Fixed accepted-set errors: []

## 26. Whether Phase 6 Can Proceed To 06-04

Phase 6 Plan 06-04 ready. Do not enter 06-04 automatically.
