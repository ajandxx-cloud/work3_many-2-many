# Phase 02 Statistical Plan

**Phase:** 02 - Experimental Contract and Metric Standardization
**Status:** standalone statistical contract

## Purpose

This plan defines how later pilot and formal experiments summarize uncertainty and compare methods. It specifies paired seeds, paired differences, confidence intervals, and reporting rules without locking the final formal-experiment sample size in Phase 2.

## Paired Experimental Design

Formal synthetic experiments in Phase 6 should use paired seeds wherever possible:

- Same seed.
- Same request stream.
- Same fleet size.
- Same meeting-point set.
- Same demand realization.
- Same scenario profile.

The pairing unit is the scenario-seed configuration. Every method row should be traceable to the same pairing key so later tables can compare within-seed differences.

The final formal-experiment sample size is not locked in Phase 2. Phase 5 pilot runtime, failure rows, and variance estimates should inform the final feasible seed count before Phase 6 starts.

## Paired Difference Metrics

For each paired method comparison, compute paired differences using a declared reference method:

- `delta_served_share`
- `delta_behavioral_acceptance_rate`
- `delta_choice_rejection_rate`
- `delta_feasibility_rejection_rate`
- `delta_total_vkm`
- `delta_vkm_per_served_trip`
- `delta_vkm_per_original_request`
- `delta_average_wait_time_min`
- `delta_average_walk_distance_m`
- `delta_average_ivt_min`

Report whether each difference is defined for all pairs. Missing, failed, timeout, or infeasible rows must remain visible and must not be silently dropped.

## Confidence Intervals

For each paired-difference metric:

1. Compute the mean paired difference.
2. Compute a 95% confidence interval over paired differences.
3. Use a transparent method such as paired t-interval or bootstrap interval; name the method in the table note.
4. If normality is implausible or seed count is small, prefer bootstrap intervals and report the number of bootstrap resamples.
5. If the number of valid pairs is too low, report the metric as exploratory and explain why.

Minimum CI outputs:

- served share differences
- `vkm_per_served_trip` differences
- `vkm_per_original_request` differences
- wait, walk, and IVT differences
- choice and feasibility rejection differences

## Multiple Experiment Families

| Family | Statistical comparison | Interpretation |
|---|---|---|
| Unconstrained behavioral | Paired differences across shared seed/scenario keys | Full service-design tradeoff under natural coverage and response. |
| Matched coverage | Paired differences near target served-share cap | Efficiency comparison near equal coverage. |
| Fixed accepted-set diagnostic | Paired differences on common request intersection | Routing/service-design diagnostic only. |
| Deterministic diagnostics | Descriptive paired or scoped exact comparisons | Mechanism and implementation insight only. |

## Pilot vs Formal Evidence

Pilot evidence:

- Phase 5 only.
- Used for smoke tests, runtime estimates, schema validation, and bug detection.
- Must not support headline manuscript claims.

Formal evidence:

- Phase 6.
- Uses paired seed design, saved configs, raw rows, failure rows, and confidence intervals.
- Supports Phase 8 claim grading only after verification passes.

## Reporting Templates

Main behavioral table minimum columns:

| method | n_pairs | served_share_mean | served_share_ci | total_vkm_mean | vkm_per_served_trip_mean | vkm_per_served_trip_ci | vkm_per_original_request_mean | choice_rejection_rate_mean | feasibility_rejection_rate_mean |
|---|---:|---:|---|---:|---:|---|---:|---:|---:|

Paired-difference table minimum columns:

| comparison | metric | n_valid_pairs | mean_difference | ci_low | ci_high | method | interpretation |
|---|---|---:|---:|---:|---:|---|---|

Failure/provenance table minimum columns:

| method | scenario | seed | status | error_message | runtime_seconds | config_id | code_revision |
|---|---|---:|---|---|---:|---|---|

## Interpretation Rules

- Do not report an efficiency difference without served-share and rejection-rate context.
- Do not treat fixed accepted-set results as passenger behavioral evidence.
- Do not convert pilot/tuning results into formal evidence.
- Do not hide failed, timeout, or infeasible rows.
- If matched coverage changes natural served share, state that it is a control design rather than the real behavioral outcome.

## Requirements Coverage

| Requirement | Coverage |
|---|---|
| EXP-01 | Statistical comparisons are grouped by service design, response assumptions, routing, and diagnostic family. |
| EXP-02 | Behavioral comparisons use shared response assumptions and paired seed keys. |
| EXP-03 | Deterministic diagnostics are interpreted separately. |
| EXP-04 | Matched coverage and fixed accepted-set families receive separate statistical treatment. |
| MET-01 | Metrics use explicit formulas and confidence intervals over paired differences. |
| MET-02 | Acceptance, served share, choice rejection, and feasibility rejection are distinct paired metrics. |
| MET-03 | Reporting templates include total vehicle-km, vehicle-km per served trip, vehicle-km per original request, and served share together. |

## Decision Trace

- D-19: This is a standalone appendix-style Phase 2 output.
- D-21: Later code and manuscript tables can cite this file directly.
- D-22: Paired seeds, paired differences, confidence intervals, and concrete computation methods are specified without locking final sample size.

