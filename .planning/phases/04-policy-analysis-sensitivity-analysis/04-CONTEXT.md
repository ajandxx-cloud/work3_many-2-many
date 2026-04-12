---
phase: 04-policy-analysis-sensitivity-analysis
type: context
created: "2026-04-11"
---

# Phase 4 Context: Policy Analysis & Sensitivity Analysis

## User Decisions

### Sensitivity Parameters Selected
- Walking tolerance: ρ^P = ρ^D varied across [200, 300, 400, 500, 700, 1000] meters
- Fleet size: n_vehicles varied across [5, 10, 15, 20, 25, 30] with n_requests=200 fixed
- Demand density: NOT selected — POLICY-01 is skipped per user decision

### Policy Output Format
- Structured document with 5 numbered policy recommendations
- Each recommendation: title + evidence (numbers from results) + policy implication
- Saved as results/policy_recommendations.md

## Key Phase 3 Result to Reference

FullModel vehicle efficiency: 2383.85 vkm vs DoorToDoor 3662.33 vkm = **-34.9% vehicle-km reduction**

This is the headline result that anchors all policy recommendations.

## Passenger Types (from experiments/variants.py)

Three types defined in src/drt/types.py:
- `price_sensitive` (PRICE_SENSITIVE): high weight on price/cost
- `time_sensitive` (TIME_SENSITIVE): high weight on wait + IVT
- `walk_sensitive` (WALK_SENSITIVE): high weight on walking distance

## Experiment Infrastructure (Phase 3, reused in Phase 4)

- `experiments/scenarios.py`: `generate_synthetic(n_requests, n_vehicles, seed)` → Scenario
- `experiments/variants.py`: `FullModel`, `DoorToDoor` classes with `.run(scenario)` → SimulationResult
- `experiments/metrics.py`: `compute_metrics(result)` → MetricsResult (9 metrics)
- `experiments/config.py`: SEEDS = [42, 43, 44], RHO_P = RHO_D = 1500.0 (baseline)

## City Tier Proxy (POLICY-06)

No real multi-city data available. Use synthetic scenario density as proxy:
- Low density: `generate_synthetic(100, 10, 42)` — 100 requests in 20km×20km
- High density: `generate_synthetic(400, 20, 42)` — 400 requests in 20km×20km
- Add `density_tier` column to sensitivity outputs

## Scope Boundary

POLICY-01 (demand density × bidirectional benefit) is explicitly excluded.
All other requirements (POLICY-02 through POLICY-06) are in scope.
