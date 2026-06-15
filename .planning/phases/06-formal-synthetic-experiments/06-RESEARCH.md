# Phase 6 Research: Formal Synthetic Experiments

## RESEARCH COMPLETE

**Phase:** 06 - Formal Synthetic Experiments
**Requirement:** EXP-05
**Date:** 2026-06-15

## Research Question

What does Phase 6 need to know to plan formal paired synthetic experiments that can support later claim gating without mixing pilot evidence, diagnostic rows, or coverage-confounded results into the manuscript evidence base?

## Key Findings

### Main Evidence Boundary

The formal main evidence should use exactly the four behavioral-main service designs already exposed through Phase 4 metadata:

- `DoorToDoor_Choice_CommonRouting`
- `SingleSidedPickup_Choice_CommonRouting`
- `SingleSidedDropoff_Choice_CommonRouting`
- `BidirectionalMP_Choice_RH_ALNS`

The implementation class names are provenance only. Paper-facing outputs must use `method_label`, `service_design`, `choice_model`, `reoptimization`, `routing_solver`, `evidence_family`, and `diagnostic_role` from `experiments/variants.py`.

The main matrix should be:

- Scenario family: synthetic
- Scales: `100`, `200`, `300`, `500` from `experiments/config.py`
- Minimum seeds: 20 paired seeds
- Optional extension: seeds 21-30 only if all 10 extra paired seeds complete under the same rules
- Main row count: `4 methods x 4 scales x 20 seeds = 320` completed behavioral-main rows

Phase 5 scale `20` remains readiness-only and must not appear in formal main evidence.

### Existing Run Surface

`experiments/runner.py` is the closest reusable execution surface. It already writes:

- `synthetic_results.csv`
- `beijing_results.csv`
- `metrics_table.csv`
- `utility_components.csv`

It also persists status, reason, runtime, error message, config ID, seed, scenario, artifact directory, and code revision. This is the right base for formal raw rows, but Phase 6 should not run the whole `ALL_VARIANTS` registry for the main matrix. A Phase 6 wrapper should filter to the four behavioral-main method labels and write under an isolated formal result directory such as `results/formal/phase06/main/`.

### Runner and Label Risk

The code currently labels `FullModel` as `BidirectionalMP_Choice_RH_ALNS` with `reoptimization = "rolling_horizon"` and `routing_solver = "alns"`, but the current `FullModel._solve()` implementation delegates to the shared actual-offer sequential insertion path. Phase 6 planning must include a pre-run validation step that either:

- confirms the implementation matches the label before using it for headline evidence, or
- records the mismatch as a blocking evidence-label issue and corrects metadata or implementation before formal runs.

This is critical because a table labelled rolling-horizon/ALNS cannot be generated from a non-rolling sequential implementation without creating a false evidence claim.

### Failure, Timeout, and Rerun Rules

Phase 6 must preserve every failed or timeout run as a durable raw row. If a bug is fixed, the rerun must use the same `seed x scale x method` cell. Replacement seeds are not allowed.

The main evidence gate passes only when all four behavioral methods over `100/200/300/500 x 20` paired seeds have terminal `status = completed` rows and zero unresolved `failed` or `timeout` rows. Optional seeds 21-30 upgrade the evidence base only if all extra paired cells complete under the same predeclared rules.

### Critical Supplementary Controls

Matched coverage and fixed accepted-set controls are critical for interpreting headline behavioral claims.

Matched coverage should use per-seed integer target counts from the Phase 5 repair pattern:

- record original `BidirectionalMP` served count/share;
- record uncapped control serviceable count/share;
- set target count to the attainable predeclared target;
- record any target adjustment explicitly;
- block the package when achieved share exceeds tolerance or when target construction is invalid.

Fixed accepted-set diagnostics must preserve the construction rule and retained request count. The pilot `common_candidate_serviceable` fallback is allowed only as an explicitly diagnostic fallback. It cannot be presented as behavioral acceptance evidence. If strict served/serviceable intersections remain empty in formal runs, the package should produce a critical conflict that Phase 8 must handle.

### Broader Supplementary Packages

The roadmap also requires utility sensitivity, meeting-point density, fleet/demand, rolling-horizon, equity, and algorithm validation packages. These should be independent packages with their own manifests, outputs, gate status, and reporting role.

Important package boundaries:

- Utility sensitivity should vary declared choice parameters one at a time and keep baseline values recoverable.
- Meeting-point density and walking-radius sweeps should report both efficiency and passenger burden.
- Fleet/demand stress tests should avoid universal policy wording and report synthetic-scenario limits.
- Rolling-horizon diagnostics must first resolve the `FullModel` label/implementation risk.
- Equity analysis should report type-level outcomes and make clear that passenger types are simulation-range constructs.
- ALNS/MILP diagnostics must keep no-Gurobi, timeout, infeasible, and incomparable rows durable and non-blocking unless the diagnostic is needed for a specific claim.

### Statistical Reporting

Formal tables should prioritize paired differences by seed and scale. The primary uncertainty summary should be paired bootstrap 95% confidence intervals, with paired t or Wilcoxon diagnostics optional for appendix material.

Main tables must always include the efficiency-and-coverage quartet:

- `total_vehicle_km`
- `vkm_per_served_trip`
- `vkm_per_original_request`
- `served_share`

Tables must also preserve choice and feasibility rejection rates. A vehicle-km result without served-share and rejection context is not acceptable for Phase 8 claim gating.

### Output Architecture

Recommended output layout:

- `results/formal/phase06/main/` for main behavioral matrix artifacts
- `results/formal/phase06/supplementary/` for independent package artifacts
- `results/formal/phase06/tables/` for processed tables and CI outputs
- `.planning/phases/06-formal-synthetic-experiments/06_FORMAL_SYNTHETIC_RESULTS.md` for the evidence report
- `.planning/phases/06-formal-synthetic-experiments/06_FAILURE_RERUN_LEDGER.csv` for durable failure/rerun tracking

The formal report should link raw rows, processed rows, configs, seed manifests, utility logs, failure rows, package gate results, table outputs, and plots.

## Implementation Risks

| Risk | Impact | Mitigation |
|---|---|---|
| `FullModel` label does not match implementation | Headline method label can overclaim ALNS/rolling-horizon evidence | Add a blocking pre-run label/implementation validation gate |
| Main matrix includes diagnostics | Behavioral evidence becomes contaminated | Filter by exact method labels and `evidence_family == behavioral_main` |
| Failed rows are overwritten by reruns | Formal completeness cannot be audited | Maintain raw failure rows and a rerun ledger keyed by `seed x scale x method` |
| Optional seeds 21-30 partially complete | Evidence base becomes ambiguous | Treat optional extension as 30 seeds only when all extra paired cells complete |
| Matched-coverage target is unattainable | Control comparison can create biased rows | Persist target basis/adjustment and block critical conflicts |
| Fixed accepted set is empty | Routing diagnostic may be uninformative | Report retained set construction and mark critical if claim interpretation depends on it |
| Existing sensitivity scripts use old denominators or labels | Supplementary tables can be inconsistent | Route through formal metric helpers and explicit formal table schemas |
| MILP solver unavailable | Algorithm diagnostics can fail environment-dependently | Persist `no_gurobi` rows with `comparable_gap = false` |

## Recommended Plan Shape

1. Build the Phase 6 formal experiment harness, manifests, validators, and tests.
2. Run and close the 20-seed main behavioral matrix, with optional 30-seed extension only if fully complete.
3. Implement and run critical controls: matched coverage, fixed accepted set, and utility sensitivity.
4. Implement and run broader robustness and algorithm diagnostics: density/walking, fleet/demand, rolling horizon, equity, ALNS/MILP.
5. Generate paired bootstrap CIs, main/supplementary tables, plots, failure ledger, and `06_FORMAL_SYNTHETIC_RESULTS.md`.

## Validation Architecture

Use existing pytest infrastructure plus persisted artifact validation.

Quick command:

`$env:PYTHONPATH='src'; pytest tests/test_phase06_formal.py tests/test_runner.py tests/test_metrics.py tests/test_variants.py -q`

Formal smoke command:

`$env:PYTHONPATH='src'; python -m experiments.phase06_formal --family main --scales 100 --seeds 1 --results-dir results/formal/phase06/smoke`

Formal validation command:

`$env:PYTHONPATH='src'; python -m experiments.phase06_formal --validate --results-dir results/formal/phase06/main`

Validation must sample persisted artifacts:

- `formal_seed_manifest.json`
- `formal_config_manifest.json`
- `synthetic_results.csv`
- `utility_components.csv`
- `main_matrix_validation.json`
- `supplementary_gate_results.csv`
- `paired_differences.csv`
- `paired_bootstrap_ci.csv`
- `06_FAILURE_RERUN_LEDGER.csv`
- `06_FORMAL_SYNTHETIC_RESULTS.md`

## Planning Inputs

Downstream plans must read:

- `.planning/phases/06-formal-synthetic-experiments/06-CONTEXT.md`
- `.planning/phases/02-experimental-contract-and-metric-standardization/02_EXPERIMENT_CONTRACT.md`
- `.planning/phases/02-experimental-contract-and-metric-standardization/02_BASELINE_TAXONOMY.md`
- `.planning/phases/02-experimental-contract-and-metric-standardization/02_METRICS_DEFINITIONS.md`
- `.planning/phases/02-experimental-contract-and-metric-standardization/02_COVERAGE_CONFOUNDING_PLAN.md`
- `.planning/phases/02-experimental-contract-and-metric-standardization/02_STATISTICAL_PLAN.md`
- `.planning/phases/03-passenger-choice-model-rebuild/03_CHOICE_MODEL_CONTRACT.md`
- `.planning/phases/04-baseline-and-algorithm-implementation-check/VARIANT_MAPPING.md`
- `.planning/phases/04-baseline-and-algorithm-implementation-check/04_BASELINE_VALIDATION.md`
- `.planning/phases/04-baseline-and-algorithm-implementation-check/04_ALGORITHM_VALIDATION.md`
- `.planning/phases/05-pilot-experiments/05_PILOT_RESULTS.md`
- `.planning/phases/05-pilot-experiments/05_BUG_LEDGER.csv`
- `experiments/config.py`
- `experiments/runner.py`
- `experiments/variants.py`
- `experiments/metrics.py`
- `experiments/phase05_pilot.py`
- `experiments/pilot_validation.py`
- `experiments/phase05_coverage_smoke.py`
- `experiments/endogenous_matched_coverage.py`
- `experiments/milp_gap.py`
- `experiments/algorithm_diagnostics.py`
- `analysis/equity.py`
- `analysis/sensitivity.py`
- `tests/test_phase05_pilot.py`
- `tests/test_runner.py`
- `tests/test_metrics.py`
- `tests/test_variants.py`
