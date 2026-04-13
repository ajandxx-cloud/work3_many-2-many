---
phase: 10-metric-audit-coverage-comparison
plan: "01"
subsystem: metrics + paper
tags: [metrics, latex, audit, vkm, correctness]
dependency_graph:
  requires: []
  provides: [vkm_per_trip helper, corrected Table 1, corrected Section 5.2, abstract placeholder]
  affects: [experiments/metrics.py, paper/sections/experiments.tex, paper/sections/abstract.tex]
tech_stack:
  added: []
  patterns: [append-only function addition, LaTeX table column extension]
key_files:
  created: []
  modified:
    - experiments/metrics.py
    - paper/sections/experiments.tex
    - paper/sections/abstract.tex
decisions:
  - "Use n_requests * acceptance_rate as denominator for vkm/trip (accepted trip count, not acceptance fraction)"
  - "Abstract efficiency sentence replaced with MATCHED_* placeholders pending Plan 02 matched-coverage experiment"
  - "Footnote added to Section 5.2 reconciling old 3022/4268 values as dimensionally incorrect"
metrics:
  duration: ~10 min
  completed: 2026-04-13
  tasks_completed: 2
  files_modified: 3
---

# Phase 10 Plan 01: Metric Audit and vkm/trip Correction Summary

Dimensionally correct vkm_per_trip helper added to metrics.py; all three inconsistent efficiency numbers in the paper reconciled to use the single denominator vkm / (n_requests * acceptance_rate).

## Tasks Completed

| Task | Name | Commit | Files |
|------|------|--------|-------|
| 1 | Add vkm_per_trip helper to metrics.py | 8e8140e | experiments/metrics.py |
| 2 | Audit and correct all vkm/trip numbers | 8887956 | paper/sections/experiments.tex, paper/sections/abstract.tex |

## Decisions Made

1. Correct denominator is `n_requests * acceptance_rate` (= accepted trip count), not the acceptance rate fraction alone. The percentage improvement (29.2%) is unchanged because the n=200 factor cancels.
2. Abstract efficiency sentence replaced with `[MATCHED_FM]`/`[MATCHED_DTD]`/`[MATCHED_PCT]` placeholders — Plan 02 will fill these after the matched-coverage experiment.
3. Old values 3022/4268 documented in a footnote as dimensionally incorrect (km per fraction, not km per trip).

## Deviations from Plan

None — plan executed exactly as written.

## Known Stubs

- `[MATCHED_FM]`, `[MATCHED_DTD]`, `[MATCHED_PCT]` in abstract.tex are intentional placeholders to be resolved by Plan 02 (matched-coverage experiment).

## Verification Results

All five plan verification checks passed:
1. `vkm_per_trip(628.5, 200, 0.208)` = 15.108 (~15.11) ✓
2. `vkm/trip` column header present in experiments.tex ✓
3. `200 \times 0.208` corrected formula present in Section 5.2 ✓
4. `2383.85` and `3662.33` absent from abstract.tex ✓
5. `METRIC AUDIT` reconciliation comment block present in experiments.tex ✓

## Self-Check: PASSED
