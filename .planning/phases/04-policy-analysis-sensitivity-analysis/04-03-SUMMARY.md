---
phase: 04-policy-analysis-sensitivity-analysis
plan: "03"
subsystem: policy-output
tags: [policy, recommendations, drt, equity, sensitivity]
dependency_graph:
  requires: [04-01, 04-02]
  provides: [results/policy_recommendations.md]
  affects: [05-paper-writing]
tech_stack:
  added: []
  patterns: [csv.DictReader, f-string template generation]
key_files:
  created:
    - analysis/policy.py
    - results/policy_recommendations.md
  modified: []
decisions:
  - "Use rho with largest FullModel acceptance gap as threshold when no 5pp superiority exists (FullModel never exceeds DoorToDoor in this dataset due to high walking penalties)"
  - "Report vkm at rho_threshold rather than rho=500 to avoid misleading 0.0 km figure"
  - "Extend Recommendation 3 evidence paragraph to include absolute IVT and wait numbers from equity_table.csv"
metrics:
  duration_minutes: 25
  completed_date: "2026-04-12T13:24:17Z"
  tasks_completed: 1
  tasks_total: 1
  files_created: 2
  files_modified: 0
requirements:
  - POLICY-05
---

# Phase 04 Plan 03: Policy Recommendations Generator Summary

**One-liner:** Five evidence-backed DRT policy recommendations generated from sensitivity, fleet, equity, and ablation CSVs, ready for direct incorporation into Phase 5 paper writing.

## What Was Built

`analysis/policy.py` reads all four Phase 4 result CSVs and writes `results/policy_recommendations.md` with five structured policy recommendations for TR Part A. The module exposes a single public function `generate_policy_recommendations()` callable both as a script (`python -m analysis.policy`) and as an import.

The output document (899 words) covers:

1. Walking radius threshold at 1000 m — where bidirectional DRT first achieves non-trivial acceptance rates under MNL utility
2. Minimum fleet ratio of 15 vehicles per 100 requests — derived from fleet sensitivity peak acceptance
3. Time-sensitive passenger equity — Gini = 0.122, lowest acceptance 14.4% vs 25.4% for price-sensitive
4. Three-tier city density deployment framework — bidirectional / single-sided / door-to-door matched to demand density
5. Rolling horizon re-optimization — 16.6% vehicle-km increase when disabled (AblationNoRollingHorizon ablation)

## Commits

| Task | Commit | Files |
|------|--------|-------|
| Task 1: Policy recommendation generator | 38ffc71 | analysis/policy.py, results/policy_recommendations.md |

## Deviations from Plan

### Auto-fixed Issues

**1. [Rule 1 - Bug] Fixed misleading vkm reference in Recommendation 1**
- **Found during:** Task 1 verification
- **Issue:** Plan template referenced "rho=500 m" for vehicle-km comparison, but at rho=500 the FullModel has 0 accepted trips (0.0 vkm), making the number meaningless
- **Fix:** Changed extraction logic to read vkm at `rho_threshold` (1000 m), where trips actually occur; updated doc template to match
- **Files modified:** analysis/policy.py

**2. [Rule 2 - Missing context] FullModel never exceeds DoorToDoor acceptance in walk sensitivity data**
- **Found during:** Task 1 data extraction
- **Issue:** Plan assumed FullModel would exceed DoorToDoor by >=5pp at some rho; actual data shows DoorToDoor = 58% flat while FullModel peaks at 9% at rho=1000 m (heavy MNL walking penalty)
- **Fix:** Fell back to plan-specified fallback: "use rho with largest gap." Reframed Recommendation 1 as "minimum viable threshold" rather than "superiority threshold," which is more accurate and equally policy-relevant
- **Files modified:** analysis/policy.py, results/policy_recommendations.md

## Known Stubs

None. All numeric values in `policy_recommendations.md` are extracted directly from CSV rows — no placeholders or hardcoded values (except the Phase 3 vkm fallback, which is unused since `metrics_table.csv` contains the actual FullModel and AblationNoRollingHorizon rows).

## Threat Flags

None. Output is a text document with no network endpoints or trust boundaries introduced.

## Self-Check: PASSED

- `analysis/policy.py` exists: FOUND
- `results/policy_recommendations.md` exists: FOUND
- Commit 38ffc71 exists: FOUND
- Recommendation count = 5: PASSED
- Word count >= 800 (actual: 899): PASSED
- Each recommendation contains numeric values: PASSED
