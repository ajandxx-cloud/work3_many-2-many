---
phase: 03-numerical-experiments
type: context
created: "2026-04-11"
---

# Phase 3 Context: Numerical Experiments

## Scenario Decisions

| Parameter | Value | Rationale |
|-----------|-------|-----------|
| Synthetic area | 20km × 20km grid | Covers range of suburban densities |
| Synthetic meeting points | 100 points on 10×10 grid | Uniform coverage |
| Semi-realistic area | 15km × 15km suburban Beijing | Low-density district, matches TR Part A policy framing |
| Beijing meeting points | 80 points at ~500m spacing | Realistic bus-stop-like density |
| Beijing demand pattern | Morning peak 7–9am commute | Highest-stress scenario for DRT |
| Random seed | RANDOM_SEED = 42 | Reproducibility |
| Request scales | [100, 200, 300, 500] | Covers small to large-scale |
| Vehicle counts | [10, 15, 20, 30] (matched to scale) | Realistic fleet ratios |
| Seeds per scale | 3 (42, 43, 44) | Mean ± std reporting |
| Walking radius ρ | 500m (pickup and dropoff) | rho_P = rho_D = 500m |
| Candidate top-k | k_top = 3 | Per Phase 2 design |
| Rolling horizon window | H = 30 min | Per Phase 2 design |
| Time step | delta = 5 min | Per Phase 2 design |
| MNL alpha weights | [1, 1, 1, 1, 5] | Price weight 5× per Work 1/2 calibration |

## Variant Decisions

All 4 model variants and 2 ablations are included for full comparison:

| ID | Variant | Description |
|----|---------|-------------|
| V1 | DoorToDoor | No meeting points; direct DARP insertion baseline |
| V2 | SingleSidedPickup | Flexible pickup MP, door-to-door dropoff |
| V3 | BidirectionalNoChoice | Bidirectional MPs, deterministic accept (no MNL) |
| V4 | FullModel | Bidirectional MPs + MNL choice + rolling horizon (main contribution) |
| A1 | AblationNoRollingHorizon | FullModel without periodic re-optimization (myopic only) |
| A2 | AblationNoChoice | FullModel with all requests accepted (P_rb = 1, no MNL) |

All variants share the same scenario generator and metrics module for fair comparison.

## Performance Metrics (EXP-09)

All 9 metrics computed for every variant × scenario × seed:

| # | Metric | Field name | Notes |
|---|--------|------------|-------|
| 1 | Acceptance rate | acceptance_rate | Fraction of requests served |
| 2 | Vehicle-km | vehicle_km | Total fleet distance |
| 3 | Avg waiting time | avg_wait | From request time to pickup |
| 4 | 95th-pct waiting time | p95_wait | Tail service quality |
| 5 | Avg walking distance | avg_walk | Weighted avg of pickup + dropoff walk |
| 6 | Avg in-vehicle time | avg_ivt | Door-to-door IVT proxy |
| 7 | Detour ratio | detour_ratio | IVT / direct travel time |
| 8 | Fairness index | fairness_index | Gini coefficient across passenger types |
| 9 | CPU time | cpu_time | Seconds per scenario run |

## Key Design Principles

- All variants use the same `Scenario` dataclass (requests, vehicles, meeting points)
- All variants implement `run(scenario) -> SimulationResult` interface
- `compute_metrics(SimulationResult) -> MetricsResult` is called identically for all variants
- Results aggregated as mean ± std across 3 seeds per scale
- Beijing scenario uses scale=200 only (semi-realistic, not full sweep)

## Phase 2 Dependencies

The following Phase 2 modules are imported by experiment variants:

- `src.drt.types` — Request, Vehicle, MeetingPoint, Bundle, PassengerType
- `src.drt.candidate` — generate_candidates()
- `src.drt.feasibility` — check_feasibility()
- `src.drt.insertion` — evaluate_insertion(), InsertionResult
- `src.drt.choice` — choice_probability()
- `src.drt.alns` — RollingHorizon, greedy_insertion
