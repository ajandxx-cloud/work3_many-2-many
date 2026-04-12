---
phase: 04-policy-analysis-sensitivity-analysis
plan: "02"
subsystem: analysis
tags: [equity, passenger-type, gini, acceptance-rate, policy]
dependency_graph:
  requires: [experiments/variants.FullModel, experiments/scenarios.generate_synthetic, experiments/metrics.PassengerRecord]
  provides: [analysis/equity.run_equity_analysis, results/equity_table.csv]
  affects: [plan-04-03]
tech_stack:
  added: []
  patterns: [per-type metric aggregation, Gini coefficient, CSV output]
key_files:
  created:
    - analysis/__init__.py
    - analysis/equity.py
    - results/equity_table.csv
  modified: []
decisions:
  - "Used seeds [42, 43, 44] from experiments.config.SEEDS (plan specifies these; prompt mentioned [42, 123, 456] but plan frontmatter and config both use [42, 43, 44])"
  - "Gini computed with inline _gini_three() using sorted-array formula as specified in plan"
  - "avg_walk = pickup_walk + dropoff_walk for accepted records only"
metrics:
  duration: "~60s"
  completed: "2026-04-11"
  tasks_completed: 1
  files_created: 3
---

# Phase 4 Plan 02: Equity Analysis Across Passenger Types Summary

Per-type equity metrics (acceptance rate, wait, walk, IVT) computed across 3 seeds using FullModel on synthetic(200,15), with Gini coefficient of acceptance rates written to equity_table.csv.

## Results

| passenger_type  | acceptance_rate | avg_wait (s) | avg_walk (m) | avg_ivt (s) | gini_acceptance |
|-----------------|-----------------|--------------|--------------|-------------|-----------------|
| price_sensitive | 0.2537          | 425.97       | 27.73        | 914.52      | 0.1216          |
| time_sensitive  | 0.1443          | 603.18       | 117.35       | 1109.60     | 0.1216          |
| walk_sensitive  | 0.2020          | 432.98       | 159.94       | 1073.49     | 0.1216          |

Key finding: time_sensitive passengers have the lowest acceptance rate (14.4%), indicating they are most disadvantaged by bidirectional meeting point assignment. price_sensitive passengers have the highest acceptance rate (25.4%). Gini = 0.1216 quantifies moderate cross-type inequity.

## Commits

| Task | Name | Commit | Files |
|------|------|--------|-------|
| 1 | Equity analysis module | 37824de | analysis/equity.py, analysis/__init__.py, results/equity_table.csv |

## Deviations from Plan

None — plan executed exactly as written.

## Self-Check: PASSED

- analysis/equity.py: FOUND
- results/equity_table.csv: FOUND (3 rows, all columns present, gini_acceptance consistent)
- Commit 37824de: FOUND
