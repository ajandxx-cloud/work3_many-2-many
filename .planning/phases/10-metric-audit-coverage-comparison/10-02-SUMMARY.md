---
phase: 10-metric-audit-coverage-comparison
plan: 02
subsystem: experiments/paper
tags: [matched-coverage, vkm-per-trip, efficiency, latex]
dependency_graph:
  requires: [10-01]
  provides: [matched_coverage_experiment, results/matched_coverage.csv, tab:matched-coverage]
  affects: [paper/sections/experiments.tex, paper/sections/abstract.tex]
tech_stack:
  added: []
  patterns: [post-hoc-rejection-calibration, closed-form-rejection-fraction]
key_files:
  created:
    - experiments/matched_coverage.py
    - results/matched_coverage.csv
  modified:
    - paper/sections/experiments.tex
    - paper/sections/abstract.tex
decisions:
  - Post-hoc random rejection preserves DoorToDoor routing (conservative lower bound on efficiency advantage)
  - rejection_fraction = 1 - target/dtd_share (exact closed form, no binary search)
  - RNG seed = scenario_seed + 1000 per Threat T-10-03 mitigation
metrics:
  duration: ~8 min
  completed: 2026-04-13
  tasks_completed: 2
  files_changed: 4
---

# Phase 10 Plan 02: Matched-Coverage Experiment and Paper Update Summary

Implemented and ran a matched-coverage experiment comparing FullModel vs. DoorToDoor at equal served share (~23.5%), producing `results/matched_coverage.csv` (6 rows: 3 seeds × 2 variants). At equal coverage, FullModel achieves 10.9 vkm/trip vs. 42.3 for DoorToDoor (74.3% improvement). Section 5.2 now uses this as the primary efficiency claim with `tab:matched-coverage`, and `abstract.tex` [MATCHED_*] placeholders are replaced with concrete numbers.

## Key Results

| Variant | Served share (mean) | vkm/trip (mean) | Rejection fraction |
|---------|--------------------|-----------------|--------------------|
| FullModel | 23.5% | 10.9 | --- |
| DoorToDoor_matched | 22.2% | 42.3 | 0.61 |

Improvement at equal coverage: **74.3%**
Unconstrained reference (retained in paper): 15.1 vs. 21.3 vkm/trip (29.2%)

## Deviations from Plan

None — plan executed exactly as written. Import name confirmed as `generate_synthetic` (not `generate_synthetic_scenario`); the plan's interfaces block noted this correctly.

## Known Stubs

None. All CSV values are computed from live simulation runs; paper numbers are transcribed directly from experiment output.

## Threat Flags

None. No new network endpoints, auth paths, or schema changes introduced.

## Self-Check

- [x] `experiments/matched_coverage.py` exists and is importable
- [x] `results/matched_coverage.csv` exists with 6 rows, columns: variant, seed, served_share, vkm_per_trip, rejection_penalty
- [x] `paper/sections/experiments.tex` contains `tab:matched-coverage` and matched-coverage narrative
- [x] `paper/sections/abstract.tex` contains no `[MATCHED_*]` placeholders
- [x] Commits: 8070ca7 (experiment script), eddac0f (CSV + paper)

## Self-Check: PASSED
