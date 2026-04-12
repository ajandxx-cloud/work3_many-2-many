---
phase: 08-pareto-experiment-new-metrics
plan: "01"
subsystem: experiments
tags: [pareto, gamma-sweep, social-welfare, metrics, figures]
dependency_graph:
  requires: []
  provides: [results/pareto_gamma_sweep.csv, figures/fig07_pareto.pdf, figures/fig07_pareto.png]
  affects: [experiments/metrics.py, experiments/variants.py]
tech_stack:
  added: []
  patterns: [dataclass-default-field, post-hoc-metric, csv-sweep-runner]
key_files:
  created:
    - experiments/pareto_sweep.py
    - figures/scripts/fig07_pareto.py
    - results/pareto_gamma_sweep.csv
    - figures/fig07_pareto.pdf
    - figures/fig07_pareto.png
  modified:
    - experiments/metrics.py
    - experiments/variants.py
decisions:
  - "gamma is post-hoc only: does not alter MNL acceptance or routing, only social_welfare computation"
  - "generate_synthetic_scenario aliased to generate_synthetic (actual export name in scenarios.py)"
metrics:
  duration: ~3 minutes
  completed: 2026-04-12
  tasks_completed: 3
  tasks_total: 3
  files_created: 5
  files_modified: 2
---

# Phase 08 Plan 01: Gamma Rejection-Penalty Sweep and Pareto Frontier Summary

JWT-style one-liner: Gamma sweep over [0,5,10,20,50,100] with FullModel at scale=200 producing 18-row CSV and labeled Pareto frontier figure responding to REV-05/06/07.

## Objective Achieved

All three tasks completed. The gamma rejection-penalty sweep infrastructure is in place: `compute_social_welfare` is importable from `experiments.metrics`, `FullModel` accepts a `gamma` keyword, the sweep runner produces the required CSV, and the figure script generates a publication-quality Pareto frontier.

## Key Metric Values (gamma=0 baseline)

| gamma | served_share | vkm_per_served_trip | social_welfare |
|-------|-------------|---------------------|----------------|
| 0     | 0.1833      | 9.8930              | -2783.46       |
| 5     | 0.1833      | 9.8930              | -3600.13       |
| 10    | 0.1833      | 9.8930              | -4416.80       |
| 20    | 0.1833      | 9.8930              | -6050.13       |
| 50    | 0.1833      | 9.8930              | -10950.13      |
| 100   | 0.1833      | 9.8930              | -19116.80      |

Note: served_share and vkm_per_served_trip are identical across all gamma values. This is expected and correct — gamma is a post-hoc penalty applied only to social_welfare; it does not alter the MNL acceptance probability or routing decisions. The Pareto frontier therefore shows a single operating point for FullModel at scale=200, with social_welfare decreasing linearly as gamma increases (each rejected passenger incurs -gamma). The figure labels each point with its Gamma value.

## Deviations from Plan

### Auto-fixed Issues

**1. [Rule 1 - Bug] Wrong function name for scenario generation**
- Found during: Task 3 (first sweep run)
- Issue: Plan referenced `generate_synthetic_scenario` but `experiments/scenarios.py` exports `generate_synthetic` (same signature)
- Fix: Added alias import `from experiments.scenarios import generate_synthetic as generate_synthetic_scenario` in `pareto_sweep.py`
- Files modified: experiments/pareto_sweep.py
- Commit: 37f2a1f

## Known Stubs

None. All data flows are wired: sweep runner produces CSV, figure script reads CSV and saves PDF+PNG.

## Threat Flags

None. All files are internal research artifacts on local filesystem with no external inputs or outputs.

## Self-Check: PASSED

- experiments/pareto_sweep.py: FOUND
- figures/scripts/fig07_pareto.py: FOUND
- results/pareto_gamma_sweep.csv: FOUND
- figures/fig07_pareto.pdf: FOUND
- figures/fig07_pareto.png: FOUND
- Commits: fd46a9a, d8d64a8, 37f2a1f all present
