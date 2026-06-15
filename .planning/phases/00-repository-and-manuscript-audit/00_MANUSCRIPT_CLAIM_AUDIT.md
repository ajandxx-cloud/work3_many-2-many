# 00 Manuscript Claim Audit

**Phase:** 0 - Repository and Manuscript Audit
**Date:** 2026-06-15
**Status:** complete with caveats

## Purpose

Classify current manuscript claims against the existing evidence chain before any new experiments are run. This is not the final Phase 8 claim gate; it is the starting risk register for the rebuild.

## Headline Claim Table

| Claim | Current Location | Current Evidence | Audit Classification | Required Fix |
|-------|------------------|------------------|----------------------|--------------|
| Existing work assigns meeting points only on the pickup side and ignores passenger heterogeneity | `abstract.tex`, likely intro/literature | Literature narrative in manuscript | Unsupported / high risk | Phase 1 literature audit must verify Cortenbach et al. (2024), Fielbaum et al. (2021), Wu et al. (2025), and related choice-based DRT |
| The paper proposes a many-to-many DRT framework with bidirectional pickup/dropoff meeting points and simulated passenger response | Abstract and model sections | Code and model prose exist | Supported as framework description | Keep, but do not overclaim novelty |
| FullModel improves vkm/trip by 29.1% vs DoorToDoor | `abstract.tex`, `experiments.tex` Table 7 | Values match `results/metrics_table.csv`, but that file aggregates all synthetic scales while the manuscript says 200 requests / 15 vehicles | Exploratory / coverage-confounded / provenance mismatch | Re-evaluate under consistent passenger-response and matched-coverage designs; fix caption and aggregation |
| FullModel served share is 18.3% vs DoorToDoor 61.0% | `abstract.tex`, `experiments.tex` | Manuscript table and current result summaries | Supported as current-run description | Must be reported alongside vkm/trip; undermines unconditional efficiency claim |
| Matched-coverage diagnostic suggests efficiency persists | `abstract.tex`, `experiments.tex` | `results/matched_coverage.csv` and `experiments/matched_coverage.py` | Exploratory / method mismatch | Current script applies post-hoc random rejection, while manuscript describes endogenous cap and rerouting; rebuild as formal design |
| FullModel equity Gini is 0.1216 and time-sensitive passengers are disadvantaged | `abstract.tex`, `experiments.tex` | `results/equity_table.csv` and type-level analysis | Exploratory | Rebuild after calibrated/sensitivity-tested passenger types; add individual-level distributions |
| Rolling horizon reoptimization is essential because no-rolling-horizon increases wait and detour | `experiments.tex` | AblationNoRollingHorizon comparison | Plausible but weak | Formal rolling-horizon sensitivity across intervals/horizons and consistent response assumptions |
| Beijing-inspired scenario supports Chinese city policy implications | `experiments.tex`, `policy.tex`, abstract | Synthetic grid only | Overstated | Rewrite as simulation-based insight unless real/semi-real case data are added |
| Gamma sweep is a coverage-efficiency Pareto frontier | Figure/table discussion | `experiments/pareto_sweep.py`; gamma is post-hoc only; CSV confirms served share and vkm/served trip do not change by gamma | Contradicted by implementation | Delete Pareto framing or implement endogenous gamma in routing/offer objective |
| MILP validates ALNS quality | Algorithm/experiment discussion | `experiments/milp_gap.py`; large gaps | Unsupported | Reframe current MILP as limited diagnostic or implement a stronger exact model and validation matrix |
| Weight sensitivity supports robust efficiency gains | `experiments.tex` Table 13 | `results/weight_sensitivity.json` | Ambiguous / formula mismatch | JSON vkm/trip values appear to use `vehicle_km / acceptance_rate`, not accepted trip count; table provenance must be rebuilt |

## Section-Level Claim Scan

| Section | Strong Claim Found | Evidence Trace | Phase 0 Classification |
|---------|--------------------|----------------|------------------------|
| `manuscript/sections/abstract.tex` | Existing work assigns meeting points only on pickup side and ignores passenger heterogeneity | Manuscript literature narrative only; review note flags Cortenbach/Fielbaum/Wu risk | Unsupported until Phase 1 literature audit |
| `manuscript/sections/abstract.tex` | 29.1% vkm/trip improvement under unconstrained comparison | `results/metrics_table.csv` aggregate means | Reproducible as current diagnostic, but exploratory and coverage-confounded |
| `manuscript/sections/abstract.tex` | Matched-coverage diagnostic suggests persistence of efficiency advantage | `results/endogenous_matched_coverage.csv` supports 11.1 vs 17.1; `results/matched_coverage.csv` is a different post-hoc method | Exploratory; method provenance must be named precisely |
| `manuscript/sections/intro.tex` | First or novel integrated contribution | Literature table and references, not independently checked in Phase 0 | Plausible only under narrow integrated-framework wording; novelty wording must wait for Phase 1 |
| `manuscript/sections/experiments.tex` | MILP vs ALNS gap is only a minimal sanity check | `results/milp_gap.json`; `experiments/milp_gap.py` | Supported as a limitation; unsupported as validation of heuristic quality |
| `manuscript/sections/experiments.tex` | Beijing-inspired case has similar qualitative pattern | `results/beijing_results.csv` | Supported as synthetic simulation only |
| `manuscript/sections/experiments.tex` | Gamma is post-hoc and does not affect routing or acceptance | `results/pareto_gamma_sweep.csv`; `experiments/pareto_sweep.py`; `experiments/config.py` | Supported; figure title/frontier language remains risky |
| `manuscript/sections/experiments.tex` | Weight sensitivity shows robust efficiency advantage | `results/weight_sensitivity.json` | Ambiguous; current manuscript table scale does not directly match JSON |
| `manuscript/sections/policy.tex` | Regulatory bodies should require disaggregated acceptance reporting | `results/equity_table.csv`; simulation-only passenger types | Overstated; should become a monitoring suggestion unless real deployment evidence is added |
| `manuscript/sections/policy.tex` | 1000 m and 15 vehicles per 100 requests as deployment guidance | `results/sensitivity_walk.csv`; `results/sensitivity_fleet.csv` | Supported only as scenario-specific simulation thresholds |
| `manuscript/sections/conclusion.tex` | Efficiency gains and equity implications for Chinese low-density urban areas | Aggregate synthetic and Beijing-inspired synthetic outputs | Exploratory; final wording must be conditional and simulation-based |

## Review-Note Risks Incorporated

The review note `docs/工作3讨论-6.14.md` identifies ten major risks:

1. Novelty overclaim around DARP meeting points and bidirectional pickup/dropoff locations.
2. Passenger choice model lacks empirical calibration and may mechanically depress acceptance.
3. Main efficiency claim is coverage-confounded.
4. Baseline variants mix all-feasible acceptance and binary-logit response.
5. ALNS solution-quality validation is insufficient and gaps are large.
6. MILP formulation is not described as a complete route-sequencing model.
7. Experiments use too few seeds for stable TR-E-level claims.
8. Beijing-inspired synthetic grid is not real-data evidence.
9. Gamma/Pareto analysis is post-hoc and should not be called a frontier.
10. Equity analysis is promising but currently overinterpreted from artificial type parameters.

## Claim Gate

| Claim Category | Current Status |
|----------------|----------------|
| Framework existence | Can remain with careful wording |
| Novelty | Must be re-audited before any strong statement |
| Efficiency superiority | Must be downgraded until fair comparisons are rebuilt |
| Passenger response findings | Must be conditional on simulation parameters |
| ALNS quality | Must be downgraded to heuristic simulation unless validated |
| Policy implications | Must be conditional and simulation-based |
| Equity findings | Exploratory until calibration/sensitivity and richer metrics exist |
| Current result provenance | Mapped enough for planning; inconsistent enough that no headline table should be treated as final |

## Required Manuscript Language Changes Later

Do not implement manuscript rewrites during Phase 0, but preserve these required changes for Phase 8/9:

- Replace "existing work assigns meeting points only on the pickup side" with a qualified literature-backed statement.
- Replace "FullModel is superior" style language with comparison-condition-specific claims.
- Report served share, vkm/request, and vkm/served trip together.
- Distinguish behavioral acceptance, feasibility rejection, choice rejection, inserted share, and served share.
- Describe Beijing results as synthetic unless real/semi-real data are introduced.
- Describe gamma results as post-hoc welfare sensitivity unless gamma enters the objective/choice logic.
- Position ALNS as a scalable heuristic unless exact/benchmark evidence improves.

## Phase 0 Gate Decision

**Status:** pass with caveats for audit completion; fail for final manuscript claims.

Phase 0 has classified the current claim surface sufficiently for the rebuild to proceed. No final manuscript claim should be treated as strong until Phase 6 formal results and Phase 8 claim gate are complete.
