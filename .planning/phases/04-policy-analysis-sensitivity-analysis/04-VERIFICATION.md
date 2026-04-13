---
phase: 04-policy-analysis-sensitivity-analysis
verified: 2026-04-11T00:00:00Z
status: passed
score: 5/5 must-haves verified
overrides_applied: 0
---

# Phase 4: Policy Analysis & Sensitivity Analysis Verification Report

**Phase Goal:** The TR Part A policy contribution is complete — sensitivity sweeps across walking tolerance and fleet size are done, equity analysis across passenger types is documented, and concrete policy recommendations for Chinese city DRT deployment are written.
**Verified:** 2026-04-11
**Status:** PASSED
**Re-verification:** No — initial verification

## Goal Achievement

### Observable Truths

| # | Truth | Status | Evidence |
|---|-------|--------|----------|
| 1 | Sensitivity analysis across walking tolerance thresholds shows how system performance changes as tolerance changes | VERIFIED | sensitivity_walk.csv: 14 rows, rho in [200,300,400,500,700,1000], FullModel + DoorToDoor variants, all 4 metrics populated |
| 2 | Fleet size sensitivity analysis produces a service quality vs. fleet size tradeoff curve | VERIFIED | sensitivity_fleet.csv: 12 rows (6 fleet sizes × 2 variants), n_vehicles in [5,10,15,20,25,30] |
| 3 | Equity analysis compares service quality across passenger types and identifies systematic disadvantage | VERIFIED | equity_table.csv: 3 rows (price_sensitive, time_sensitive, walk_sensitive), Gini=0.1216, time_sensitive lowest at 14.4% |
| 4 | At least three concrete, actionable policy recommendations for Chinese city DRT operators are written | VERIFIED | policy_recommendations.md: exactly 5 recommendations, each with Evidence + Policy implication sections and numeric values from CSVs |
| 5 | City tier comparison distinguishes when to use bidirectional vs other modes by density | VERIFIED | density_tier column in sensitivity_walk.csv with values low/standard/high; Recommendation 4 covers three-tier deployment framework |

**Score:** 5/5 truths verified

### Required Artifacts

| Artifact | Expected | Status | Details |
|----------|----------|--------|---------|
| `analysis/sensitivity.py` | sweep_walking_tolerance() and sweep_fleet_size() | VERIFIED | 156 lines, both functions defined, imports experiments.scenarios and experiments.variants |
| `results/sensitivity_walk.csv` | >= 14 rows with rho, variant, density_tier, 4 metrics | VERIFIED | 14 rows: 12 standard (6 rho × 2 variants) + 2 density tier rows (FullModel at rho=500 for low/high) |
| `results/sensitivity_fleet.csv` | 12 rows with n_vehicles, variant, 3 metrics | VERIFIED | 12 rows: 6 fleet sizes × 2 variants, columns n_vehicles/variant/acceptance_rate/vehicle_km/avg_wait |
| `analysis/equity.py` | run_equity_analysis() function | VERIFIED | 113 lines, function defined, imports PassengerRecord and FullModel |
| `results/equity_table.csv` | 3 rows with per-type metrics and Gini | VERIFIED | 3 rows, columns passenger_type/acceptance_rate/avg_wait/avg_walk/avg_ivt/gini_acceptance, Gini consistent at 0.1216 |
| `analysis/policy.py` | generate_policy_recommendations() function | VERIFIED | 361 lines, function defined, reads all 4 CSVs via DictReader |
| `results/policy_recommendations.md` | 5 "## Recommendation" headings | VERIFIED | Exactly 5 headings, 899 words, all sections have Evidence + Policy implication with numeric values |

### Key Link Verification

| From | To | Via | Status | Details |
|------|----|-----|--------|---------|
| analysis/sensitivity.py | experiments/scenarios.generate_synthetic | direct import | WIRED | `from experiments.scenarios import generate_synthetic` confirmed |
| analysis/sensitivity.py | experiments/variants.FullModel / DoorToDoor | direct import | WIRED | `from experiments.variants import DoorToDoor, FullModel` confirmed |
| analysis/equity.py | experiments/metrics.PassengerRecord | direct import | WIRED | PassengerRecord and FullModel imports confirmed |
| analysis/policy.py | results/sensitivity_walk.csv | csv.DictReader | WIRED | `sensitivity_walk.csv` string present in policy.py |
| analysis/policy.py | results/sensitivity_fleet.csv | csv.DictReader | WIRED | `sensitivity_fleet.csv` string present in policy.py |
| analysis/policy.py | results/equity_table.csv | csv.DictReader | WIRED | `equity_table.csv` string present in policy.py |
| analysis/policy.py | results/metrics_table.csv | csv.DictReader | WIRED | `metrics_table.csv` string present in policy.py |

### Data-Flow Trace (Level 4)

| Artifact | Data Variable | Source | Produces Real Data | Status |
|----------|---------------|--------|--------------------|--------|
| sensitivity_walk.csv | acceptance_rate, vehicle_km, avg_walk, avg_wait | FullModel/DoorToDoor simulation runs with seed=42 | Yes — non-zero values at rho>=700 (FullModel 0.015 at 700m, 0.09 at 1000m); DoorToDoor 0.58 flat | FLOWING |
| sensitivity_fleet.csv | acceptance_rate, vehicle_km, avg_wait | FullModel/DoorToDoor simulation runs | Yes — values vary with fleet size (0.165 at n=5 to 0.24 at n=30) | FLOWING |
| equity_table.csv | acceptance_rate, avg_wait, avg_walk, avg_ivt, gini_acceptance | FullModel runs across seeds [42,43,44] | Yes — distinct values per type, Gini=0.1216 | FLOWING |
| policy_recommendations.md | All numeric claims | CSV rows via DictReader in policy.py | Yes — values match CSV data (rho_threshold=1000m, Gini=0.122, time-sensitive 14.4%) | FLOWING |

### Behavioral Spot-Checks

| Behavior | Command | Result | Status |
|----------|---------|--------|--------|
| sensitivity_walk.csv has >= 14 rows | pandas read + len check | 14 rows | PASS |
| sensitivity_fleet.csv has exactly 12 rows | pandas read + len check | 12 rows | PASS |
| equity_table.csv has exactly 3 rows | pandas read + len check | 3 rows | PASS |
| policy_recommendations.md has exactly 5 recommendations | content.count('## Recommendation') | 5 | PASS |
| density_tier column present with low/standard/high | set check on unique values | {'low','standard','high'} | PASS |
| Each recommendation has Evidence + Policy implication + numbers | regex check | All 5 pass | PASS |

### Requirements Coverage

| Requirement | Source Plan | Description | Status | Evidence |
|-------------|------------|-------------|--------|----------|
| POLICY-01 | (excluded) | Demand density × bidirectional benefit sensitivity | DEFERRED | Explicitly excluded per user decision in 04-CONTEXT.md; city tier proxy via density_tier column partially addresses intent |
| POLICY-02 | 04-01-PLAN.md | Walking tolerance sensitivity | SATISFIED | sensitivity_walk.csv: 6 rho values × 2 variants = 12 standard rows |
| POLICY-03 | 04-01-PLAN.md | Fleet size sensitivity | SATISFIED | sensitivity_fleet.csv: 6 fleet sizes × 2 variants = 12 rows |
| POLICY-04 | 04-02-PLAN.md | Equity analysis across passenger types | SATISFIED | equity_table.csv: 3 types, Gini=0.1216, time_sensitive most disadvantaged |
| POLICY-05 | 04-03-PLAN.md | Policy recommendations document | SATISFIED | policy_recommendations.md: 5 structured recommendations, 899 words |
| POLICY-06 | 04-01-PLAN.md | City tier comparison | SATISFIED | density_tier column in sensitivity_walk.csv with low/standard/high rows |

### Anti-Patterns Found

| File | Line | Pattern | Severity | Impact |
|------|------|---------|----------|--------|
| analysis/policy.py | 170, 175 | `return None` in get_vkm() helper | Info | Not a stub — helper handles missing CSV rows; fallback to known Phase 3 values at L182-184 |

No blockers or warnings found. The `return None` instances are in a data-extraction helper with proper fallback logic, not in rendering or user-visible output paths.

### Human Verification Required

None. All must-haves are verifiable programmatically from file contents and CSV data.

### Gaps Summary

No gaps. All five roadmap success criteria are met:

1. Walking tolerance sensitivity — sensitivity_walk.csv with 6 rho values and both variants
2. Fleet size sensitivity — sensitivity_fleet.csv with 6 fleet sizes and both variants
3. Equity analysis — equity_table.csv with 3 passenger types, Gini coefficient, per-type metrics
4. Policy recommendations — 5 structured recommendations with evidence and policy implications
5. City tier comparison — density_tier column with low/standard/high in sensitivity_walk.csv

POLICY-01 (demand density sensitivity) was explicitly excluded by user decision documented in 04-CONTEXT.md. The city tier proxy in POLICY-06 partially covers the intent.

---

_Verified: 2026-04-11_
_Verifier: Claude (gsd-verifier)_
