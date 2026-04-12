---
phase: 09-paper-section-updates
plan: 01
subsystem: paper-sections
tags: [milp, alns, optimality-gap, algorithm, experiments, rev-09, rev-10]
dependency_graph:
  requires: []
  provides: [algorithm.tex-milp-clarification, experiments.tex-table3, milp_gap.py]
  affects: [paper/sections/algorithm.tex, paper/sections/experiments.tex, experiments/milp_gap.py]
tech_stack:
  added: []
  patterns: [deferred-import-for-optional-dependency, graceful-fallback-no-gurobi]
key_files:
  created:
    - experiments/milp_gap.py
  modified:
    - paper/sections/algorithm.tex
    - paper/sections/experiments.tex
decisions:
  - "Use actual variants.py API (FullModel().run(scenario)) rather than non-existent run_variant() helper"
  - "Report MILP objective_value / alpha_op as milp_vkm proxy since MILP optimizes weighted cost not raw vkm"
  - "Leave [FILL] placeholders in Table 3 with TODO comment — Gurobi not available in current environment"
metrics:
  duration: 526s
  completed_date: "2026-04-12"
  tasks_completed: 2
  files_changed: 3
---

# Phase 9 Plan 01: MILP Ex-Post Benchmark Clarification and Optimality Gap Table Summary

**One-liner:** Added explicit ex-post benchmark framing to algorithm.tex (REV-09) and created milp_gap.py + Table 3 in experiments.tex (REV-10), with graceful Gurobi fallback.

## Tasks Completed

| Task | Name | Commit | Files |
|------|------|--------|-------|
| 1 | Clarify MILP ex-post benchmark in algorithm.tex | 10c4f02 | paper/sections/algorithm.tex |
| 2 | Write milp_gap.py and add Table 3 to experiments.tex | 04dd554 | experiments/milp_gap.py, paper/sections/experiments.tex |

## Verification Results

All four plan checks passed:
1. `grep "ex-post" algorithm.tex` — 2 hits (lines 48, 62)
2. `grep "tab:milp-gap" experiments.tex` — 1 hit (line 106, `\label{tab:milp-gap}`)
3. `python -c "from experiments.milp_gap import run_gap_experiment; print('ok')"` — prints "ok"
4. `grep "subsec:milp-gap" experiments.tex` — 1 hit (line 92)

## Deviations from Plan

### Auto-fixed Issues

**1. [Rule 1 - Bug] Adapted script to actual API — no run_variant() function exists**
- **Found during:** Task 2
- **Issue:** Plan template used `run_variant("FullModel", requests, vehicles, meeting_points)` and `alns_metrics["vkm"]` / `alns_metrics["accepted_ids"]` — none of these exist in the codebase. `runner.py` has no `run_variant` function; variants are called via `FullModel().run(scenario)` returning `SimulationResult`.
- **Fix:** Used `FullModel().run(scenario)` directly; extracted `total_vehicle_km` for ALNS vkm; extracted accepted IDs from `[r.request_id for r in sim_result.records if r.accepted]`.
- **Files modified:** experiments/milp_gap.py
- **Commit:** 04dd554

**2. [Rule 2 - Missing critical functionality] Added path setup for script execution**
- **Found during:** Task 2
- **Issue:** Script needs to be runnable as `python experiments/milp_gap.py` from repo root; without sys.path setup the `from drt.milp import DRTModel` deferred import would fail.
- **Fix:** Added `_REPO_ROOT` detection and `sys.path.insert(0, _REPO_ROOT)` at module top.
- **Files modified:** experiments/milp_gap.py
- **Commit:** 04dd554

## Known Stubs

- Table 3 in experiments.tex has `[FILL]` placeholders for ALNS vkm, MILP vkm, gap%, and solve time values. These require running `experiments/milp_gap.py` with a valid Gurobi license. A `% TODO` comment is present in the LaTeX source. This is intentional per the plan's explicit fallback instruction.

## Threat Surface Scan

No new network endpoints, auth paths, file access patterns, or schema changes introduced. `milp_gap.py` writes to `results/milp_gap.json` (local research artifact, no PII — T-09-02 accepted per threat model).

## Self-Check: PASSED

- `paper/sections/algorithm.tex` — FOUND, contains "ex-post benchmark"
- `experiments/milp_gap.py` — FOUND, importable without Gurobi
- `paper/sections/experiments.tex` — FOUND, contains `\label{tab:milp-gap}`
- Commits 10c4f02 and 04dd554 — FOUND in git log
