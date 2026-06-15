# 00 Current Experiment Map

**Phase:** 0 - Repository and Manuscript Audit
**Date:** 2026-06-15
**Status:** complete with caveats

## Purpose

Map current experiment families, variants, parameters, metrics, and outputs so the rebuild can replace or formalize them without losing provenance.

## Current Variant Registry

`experiments/variants.py` currently registers:

| Variant | Current Implementation | Current Interpretation Problem |
|---------|------------------------|--------------------------------|
| `DoorToDoor` | Direct origin/destination synthetic meeting points, greedy insertion | No binary-logit passenger response; served share reflects feasibility/insertion |
| `DoorToDoorCapped` | Door-to-door with endogenous cap share | Useful for matched-coverage diagnostics but needs formal contract |
| `SingleSidedPickup` | Flexible pickup MP, destination dropoff | No binary-logit response; missing single-sided dropoff counterpart |
| `BidirectionalNoChoice` | Bidirectional MPs, deterministic all-feasible insertion | Diagnostic, not behavioral comparison |
| `FullModel` | Bidirectional MPs, pre-routing MNL filtering, rolling horizon | Choice is simulated before actual route offer; gamma unused |
| `AblationNoRollingHorizon` | MNL filtering plus static greedy insertion | Behavioral diagnostic but not same dynamic setting |
| `AblationNoChoice` | Rolling horizon without MNL rejection | Diagnostic inserted share, not behavioral acceptance |

## Required Future Taxonomy

The rebuild brief requires explicit definitions for:

- `DoorToDoor`
- `SingleSidedPickup`
- `SingleSidedDropoff`
- `BidirectionalMeetingPoint`
- `BidirectionalNoRollingHorizon`
- `GreedyInsertionBaseline`
- `ALNSFullModel`
- `ExactOrMILPDiagnostic`

The current code lacks a clearly symmetric `SingleSidedDropoff` and conflates some algorithmic diagnostics with behavioral service-design variants.

## Current Experiment Families

| Family | Current Files | Current Role | Rebuild Decision |
|--------|---------------|--------------|------------------|
| Baseline comparison | `experiments/runner.py`, `results/metrics_table.csv`, manuscript Table 7 | Primary reported comparison | Must be rebuilt with fair choice-based and deterministic families |
| Beijing-inspired scenario | `experiments/scenarios.py`, `results/beijing_results.csv` | Synthetic external-validity probe | Keep synthetic label; optional real/semi-real phase later |
| Matched coverage | `experiments/matched_coverage.py`, `experiments/endogenous_matched_coverage.py`, `results/matched_coverage.csv` | Exploratory diagnostic | Promote to formal comparison design |
| Walking/fleet sensitivity | `analysis/sensitivity.py`, `results/sensitivity_walk.csv`, `results/sensitivity_fleet.csv` | Parameter sensitivity | Expand to formal utility and scenario sensitivity |
| Weight sensitivity | `experiments/weight_sensitivity.py`, `results/weight_sensitivity.json` | Objective-weight diagnostic | Audit formula and integrate with formal experiments |
| Gamma welfare sweep | `experiments/pareto_sweep.py`, `results/pareto_gamma_sweep.csv` | Post-hoc welfare scoring | Do not call Pareto frontier unless gamma affects decisions |
| Equity analysis | `analysis/equity.py`, `results/equity_table.csv` | Passenger-type metrics | Rebuild with calibrated/sensitivity-tested types and individual distributions |
| MILP gap | `experiments/milp_gap.py`, `results/milp_gap.json`, `results/milp_benchmark.json` | Small fixed-set diagnostic | Expand and reframe according to exact model scope |

## Current Metric Surface

`experiments/metrics.py` computes:

- `acceptance_rate`
- `vehicle_km`
- `avg_wait`
- `p95_wait`
- `avg_walk`
- `avg_ivt`
- `detour_ratio`
- `fairness_index`
- `cpu_time`
- `social_welfare` field defaults to 0.0 and is not populated by `compute_metrics()`

The rebuild requires at minimum:

- `served_share`
- `behavioral_acceptance_rate`
- `feasibility_rejection_rate`
- `choice_rejection_rate`
- `total_vkm`
- `vkm_per_served_trip`
- `vkm_per_request`
- `average_wait_time_min`
- `p95_wait_time_min`
- `average_walk_distance_m`
- `p95_walk_distance_m`
- `average_ivt_min`
- `detour_ratio`
- `average_fare`
- `operator_cost`
- `revenue` if fare is modeled
- `profit` only if cost/revenue are defined
- `social_welfare` only if utility and rejection penalty are explicit
- `type_level_acceptance_rate`
- `type_level_wait_time`
- `type_level_walk_distance`
- `equity_gini_acceptance`
- `equity_gini_generalized_cost`

## Current Formality Gaps

- Seeds currently visible in manuscript are 42, 43, 44; formal TR-E-level claims require at least 20 paired seeds.
- Current output rows do not include `status`, `failed`, `timeout`, or `infeasible` categories with error messages and traceback paths.
- Current CSVs do not record config ID, code revision, dependency versions, command, or hardware/runtime metadata.
- Current baselines do not use a common passenger-response model in the primary behavioral comparison.
- Current deterministic comparison is mixed into headline interpretation rather than isolated as diagnostic evidence.
- Current accepted-set routing comparison is not formalized as a primary experiment family.
- Current ALNS convergence and operator diagnostics are not saved as formal artifacts.

## Result-To-Manuscript Trace Seeds

Initial mapping from manuscript claims:

| Manuscript Artifact | Likely Source | Status |
|---------------------|---------------|--------|
| Table 7 main baseline comparison | `results/metrics_table.csv` and `results/synthetic_results.csv` | Partially verified; values match `metrics_table.csv`, but that file aggregates all synthetic scales rather than only 200 requests |
| Matched-coverage table | `results/matched_coverage.csv` and manuscript text | Partially verified; CSV uses post-hoc random rejection and gives much higher DoorToDoor matched vkm/trip than manuscript table text |
| Beijing-inspired table | `results/beijing_results.csv` | Partially verified; 21 rows = 3 seeds x 7 variants |
| Sensitivity figure/table | `results/sensitivity_walk.csv`, `results/sensitivity_fleet.csv`, figure scripts | Needs formula/unit verification |
| Gamma welfare table/figure | `results/pareto_gamma_sweep.csv`, `manuscript/figures/scripts/fig07_pareto.py` | Post-hoc diagnostic only |
| Equity Gini/type rates | `results/equity_table.csv`, `analysis/equity.py` | Exploratory until choice calibration rebuilt |
| MILP gap table | `results/milp_gap.json`, `experiments/milp_gap.py` | Diagnostic scope only |

## Row-Level Result Provenance

| Manuscript Result / Artifact | Source Checked | Audit Result | Gate For Later Phases |
|------------------------------|----------------|--------------|-----------------------|
| Main baseline table: DoorToDoor served share 0.610, vehicle-km 2603.7; FullModel served share 0.183, vehicle-km 552.0 | `results/metrics_table.csv`; generated by `experiments/runner.py` grouping `synthetic_results.csv` by `variant` | Verified as current aggregate values, but not the captioned single 200-request scenario | Phase 2 must define table denominator and scenario scope; Phase 6 must regenerate formal table with paired seeds |
| Main baseline table: 15.1 vs 21.3 vkm/trip and 29.1% improvement | Derived from `vehicle_km_mean / (200 * acceptance_rate_mean)` using `results/metrics_table.csv` means | Numerically reproducible from current aggregate means, but coverage-confounded because served shares differ sharply | Keep only as current-run diagnostic until matched-coverage and fixed accepted-set designs are formalized |
| Scale-200 synthetic check | `results/synthetic_results.csv` filtered to `scale=200` | Means differ from `metrics_table.csv`: DoorToDoor vkm 1870.55, FullModel vkm 383.413, vkm/trip about 15.17 vs 10.36 | Confirms caption mismatch; no final manuscript table should use current values without explicit aggregation statement |
| Matched-coverage table: FullModel 11.1 vs DoorToDoor(capped) 17.1 vkm/trip | `results/endogenous_matched_coverage.csv`; `experiments/endogenous_matched_coverage.py` | Verified as the closest source for the manuscript's endogenous capped wording; mean served shares are 0.2283 and 0.2300, not 18.3% | Treat as exploratory diagnostic; Phase 2 must decide target share and cap mechanics before formal reuse |
| Older matched-coverage claim using post-hoc random rejection | `results/matched_coverage.csv`; `experiments/matched_coverage.py` | Verified as a separate post-hoc diagnostic: FullModel 10.8952 vs DoorToDoor_matched 42.3219 vkm/trip at about 0.22 served share | Do not describe this as endogenous rerouting |
| Beijing-inspired table | `results/beijing_results.csv` | Verified: 21 rows = 3 seeds x 7 variants. Table values match means, including FullModel served share 0.313, vehicle-km 261.7, vkm/trip 4.2 | Keep explicitly synthetic; no real-city policy claim without Phase 7 data |
| Walking-radius sensitivity | `results/sensitivity_walk.csv`; `manuscript/figures/scripts/fig05_sensitivity.py` | Verified current rows include FullModel zero acceptance at rho 200, 300, 400, 500 and 9.0% at rho 1000 | Treat threshold as calibration-dependent; Phase 3 must rebuild passenger utility before final claim |
| Fleet-size sensitivity | `results/sensitivity_fleet.csv`; `manuscript/figures/scripts/fig05_sensitivity.py` | Verified current FullModel acceptance rises from 0.165 at 5 vehicles to 0.240 at 30 vehicles | Exploratory; Phase 6 needs paired formal sweep |
| Equity table | `results/equity_table.csv`; `analysis/equity.py` | Verified type rates and Gini: price-sensitive 0.2537, time-sensitive 0.1443, walk-sensitive 0.2020, Gini 0.121608 | Exploratory until passenger-type calibration and individual-level equity metrics are rebuilt |
| Gamma / welfare sweep table | `results/pareto_gamma_sweep.csv`; `experiments/pareto_sweep.py`; `manuscript/figures/scripts/fig07_pareto.py` | Verified served share and vkm/trip are invariant by gamma; only welfare changes | Must not be called a Pareto frontier unless gamma enters routing, offer, or acceptance decisions |
| Weight sensitivity table | `results/weight_sensitivity.json`; `experiments/weight_sensitivity.py` | Current JSON stores vkm/acceptance-rate scale values around 1600-3200, while manuscript reports 10-15 vkm/trip | Mark manuscript table provenance ambiguous; rebuild from shared metric helper |
| MILP gap table | `results/milp_gap.json`; `experiments/milp_gap.py` | Verified gaps: n=20 mean about 169.6%, n=30 mean about 98.8%, accepted sets only 2-7 requests | Use only as limited exact-routing diagnostic; not ALNS validation |
| Policy map figure | `manuscript/figures/scripts/fig06_policy_map.py`; `results/policy_recommendations.md` | Figure is hard-coded from derived policy thresholds, not generated directly from experiment rows | Treat as illustrative manuscript graphic, not independent evidence |
| Baseline comparison figure | `manuscript/figures/scripts/fig04_baseline_comparison.py` | Reads `results/metrics_table.csv`; script annotation says `-34.9% vkm/acceptance vs D2D`, inconsistent with manuscript 29.1% vkm/trip text | Figure script needs correction or removal during manuscript rebuild |

## Verified Current Result Facts

- `results/synthetic_results.csv` has 84 rows, consistent with 4 synthetic scales x 3 seeds x 7 variants.
- `results/beijing_results.csv` has 21 rows, consistent with 3 seeds x 7 variants.
- `results/metrics_table.csv` groups `synthetic_results.csv` by `variant` across all scales, not by the manuscript caption's "200 requests, 15 vehicles" condition.
- Manuscript Table 7 values such as DoorToDoor vehicle-km 2603.7, FullModel vehicle-km 552.0, DoorToDoor served share 0.610, and FullModel served share 0.183 match `results/metrics_table.csv`.
- When filtering `synthetic_results.csv` to scale 200 only, the means differ materially: DoorToDoor vkm is 1870.55 and FullModel vkm is 383.413, with vkm/served trip approximately 15.17 vs 10.36.
- `results/matched_coverage.csv` contains 6 rows: FullModel for seeds 42, 43, 44 and `DoorToDoor_matched` for the same seeds. The script uses post-hoc random rejection after DoorToDoor routing, not endogenous rerouting. This contradicts the manuscript wording that describes an endogenous acceptance cap and continued ALNS rerouting.
- `results/pareto_gamma_sweep.csv` shows served share and vkm/served trip identical across gamma values within each seed; only social welfare changes. This confirms gamma is post-hoc welfare accounting.
- `results/equity_table.csv` matches the manuscript's type-level acceptance rates and Gini value: price-sensitive 0.2537, time-sensitive 0.1443, walk-sensitive 0.2020, Gini 0.121608.
- `results/milp_gap.json` contains n=20 and n=30 diagnostics over seeds 42, 43, 44, with gaps ranging from 44.7% to 234.3% and very small accepted sets (2 to 7 passengers).
- `results/weight_sensitivity.json` stores `*_vkm_per_trip` values around 1600-3200 because the script computes `vehicle_km / acceptance_rate`, not `vehicle_km / accepted trip count`. The manuscript table reports values around 10-15, so either a separate transformation was applied or the manuscript table is not directly reproducible from that JSON as written.

## Provenance Risks Raised By Verification

1. **Main table caption mismatch:** The table claims a 200-request, 15-vehicle scenario, but the matching CSV aggregates all synthetic scales.
2. **Matched-coverage method mismatch:** The script says post-hoc random rejection with unchanged DoorToDoor routing, while the manuscript describes an endogenous cap with continued rerouting.
3. **Weight sensitivity formula mismatch:** JSON values and manuscript table values use different vkm/trip scales.
4. **Gamma/Pareto semantics confirmed:** Gamma does not affect routing or acceptance.
5. **AblationNoChoice instability:** At scale 200, current `synthetic_results.csv` shows zero accepted/inserted rows for AblationNoChoice, while the all-scale aggregate in `metrics_table.csv` reports a nonzero mean due to other scales.

## Phase 0 Gate Decision

**Status:** pass with caveats.

The existing experiment surface is mapped well enough to plan Phase 1 and Phase 2 without guessing. Current results are not approved as final paper evidence. The audit found multiple provenance and interpretation risks that must be fixed before final claims:

1. Main table values are reproducible from current aggregate files, but the aggregation does not match the captioned single scenario.
2. Coverage confounding remains central because FullModel and DoorToDoor serve very different request shares.
3. The manuscript's matched-coverage text matches `endogenous_matched_coverage.csv` better than `matched_coverage.csv`, but both are exploratory.
4. Figure 7 and the gamma sweep are post-hoc welfare diagnostics, not a behavioral frontier.
5. Figure 6 and current policy recommendations are illustrative, synthetic, and partly hard-coded.
6. Weight sensitivity table provenance is ambiguous and must be rebuilt.

## No-New-Experiment Confirmation

No new experiment commands were run while creating this map.
