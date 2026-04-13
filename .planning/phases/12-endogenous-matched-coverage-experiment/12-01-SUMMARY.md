---
phase: 12-endogenous-matched-coverage-experiment
plan: "01"
subsystem: experiments
tags: [DoorToDoorCapped, endogenous-comparison, matched-coverage, vkm-per-trip]
dependency_graph:
  requires: []
  provides: [DoorToDoorCapped-class, endogenous-matched-coverage-csv]
  affects: [paper/sections/experiments.tex]
tech_stack:
  added: []
  patterns: [BaseVariant-subclass, greedy_insertion-with-cap, experiment-runner-mirror]
key_files:
  created:
    - experiments/endogenous_matched_coverage.py
    - results/endogenous_matched_coverage.csv
  modified:
    - experiments/variants.py
decisions:
  - "DoorToDoorCapped uses >= cap check (not >) to prevent off-by-one (T-12-01)"
  - "cap_share computed dynamically at runtime from FullModel mean served_share"
  - "Tolerance check warns but does not raise — CSV always written"
metrics:
  completed_date: "2026-04-13"
  tasks_completed: 2
  tasks_total: 2
  files_created: 2
  files_modified: 1
---

# Phase 12 Plan 01: DoorToDoorCapped Implementation and Endogenous Experiment Summary

DoorToDoorCapped variant implemented with endogenous acceptance cap; experiment run for seeds 42/43/44 at n=200/15 vehicles; FullModel 11.11 vkm/trip vs DoorToDoorCapped 17.09 vkm/trip (35.0% improvement at matched ~23% served share).

## Experiment Results

| Metric | FullModel | DoorToDoorCapped |
|--------|-----------|-----------------|
| Mean vkm/trip | 11.11 | 17.09 |
| Mean served_share | 0.2283 | 0.2300 |
| Improvement | — | 35.0% |
| Tolerance check (±3pp) | — | PASSED (diff=0.0017) |

### Per-seed breakdown

| Variant | Seed | served_share | vkm_per_trip |
|---------|------|-------------|-------------|
| FullModel | 42 | 0.2400 | 9.9522 |
| FullModel | 43 | 0.2350 | 11.1586 |
| FullModel | 44 | 0.2100 | 12.2172 |
| DoorToDoorCapped | 42 | 0.2300 | 15.85 |
| DoorToDoorCapped | 43 | 0.2300 | 18.54 |
| DoorToDoorCapped | 44 | 0.2300 | 16.89 |

## Tasks Completed

| Task | Name | Commit | Files |
|------|------|--------|-------|
| 1 | Add DoorToDoorCapped to variants.py | 339329f | experiments/variants.py |
| 2 | Write endogenous_matched_coverage.py and run experiment | e5119ce | experiments/endogenous_matched_coverage.py, results/endogenous_matched_coverage.csv |

## Deviations from Plan

None — plan executed exactly as written.

## Known Stubs

None. All data is wired from actual simulation runs.

## Threat Flags

None. No new network endpoints, auth paths, or trust boundaries introduced.

## Self-Check: PASSED

- experiments/variants.py: modified, DoorToDoorCapped class present
- experiments/endogenous_matched_coverage.py: created
- results/endogenous_matched_coverage.csv: created, 6 rows
- Commit 339329f: exists (Task 1)
- Commit e5119ce: exists (Task 2)
- Tolerance check: PASSED (|0.2300 - 0.2283| = 0.0017 <= 0.03)
