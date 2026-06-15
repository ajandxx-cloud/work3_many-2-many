# Phase 6 Pattern Map

**Phase:** 06 - Formal Synthetic Experiments
**Date:** 2026-06-15

## Purpose

Map Phase 6 plan files to nearby implementation patterns so execution can extend the existing experiment stack instead of inventing a parallel workflow.

## Candidate Files and Analogs

| Target | Role | Closest analog | Pattern to reuse |
|---|---|---|---|
| `experiments/phase06_formal.py` | Formal main matrix orchestration, seed/config manifests, validation CLI | `experiments/phase05_pilot.py`, `experiments/runner.py` | Filter exact behavioral-main variants, call `run_all_experiments`, pass isolated `results_dir`, expose module CLI |
| `experiments/formal_validation.py` | Persisted formal artifact validator | `experiments/pilot_validation.py`, `tests/test_phase05_pilot.py` | Required columns, range checks, status closure, utility joinability, expected matrix completeness |
| `experiments/phase06_supplementary.py` | Supplementary package orchestration and gate rows | `experiments/phase05_coverage_smoke.py`, `experiments/endogenous_matched_coverage.py`, `experiments/milp_gap.py`, `analysis/sensitivity.py`, `analysis/equity.py` | Durable rows with package ID, status, detailed reason, evidence family, diagnostic role, and output path |
| `experiments/formal_statistics.py` | Paired differences, paired bootstrap CIs, table generation | `experiments/metrics.py`, `.planning/phases/02-experimental-contract-and-metric-standardization/02_STATISTICAL_PLAN.md` | Status-aware metric selection, seed/scale pairing keys, transparent CI output tables |
| `tests/test_phase06_formal.py` | Focused Phase 6 tests | `tests/test_phase05_pilot.py`, `tests/test_runner.py`, `tests/test_metrics.py`, `tests/test_variants.py` | Temporary result dirs, monkeypatched small matrices, exact schema/closure assertions |
| `.planning/phases/06-formal-synthetic-experiments/06_FORMAL_SYNTHETIC_RESULTS.md` | Evidence report and gate summary | `.planning/phases/05-pilot-experiments/05_PILOT_RESULTS.md`, `04_BASELINE_VALIDATION.md` | Purpose, manifest, gates, failures/reruns, limitations, no unsupported claims |
| `results/formal/phase06/` | Isolated formal output root | `results/pilot/phase05/` | Keep raw, processed, utility, gate, table, and plot artifacts out of legacy `results/*.csv` names |

## Existing Behaviors to Preserve

- `experiments/runner.py` persists failed and timeout rows.
- `utility_components.csv` is joinable by `run_id`, `seed`, `scenario`, `method`, and `request_id`.
- Main behavioral identity is determined by `method_metadata`, not class name.
- Phase 5 validation checks persisted outputs, not just in-memory objects.
- `milp_gap.py` records `no_gurobi`, `timeout`, `infeasible`, and incomparable rows instead of hiding them.
- Pilot artifacts and formal artifacts must remain in separate directories.

## Data Flow

1. `phase06_formal.py` writes seed/config manifests and runs only the four behavioral-main methods.
2. `formal_validation.py` validates matrix closure, status, schema, utility joinability, and quartet metrics.
3. `phase06_supplementary.py` writes independent supplementary package outputs and gate rows.
4. `formal_statistics.py` reads persisted rows and produces paired differences, paired bootstrap CIs, main tables, and supplementary summaries.
5. `06_FORMAL_SYNTHETIC_RESULTS.md` links all raw, processed, config, failure, rerun, table, CI, plot, and gate artifacts.

## Landmines

- Do not run all `ALL_VARIANTS` entries for the main behavioral table.
- Do not allow scale `20` into formal main evidence.
- Do not let `FullModel` paper-facing labels pass without a label/implementation check.
- Do not overwrite legacy `results/synthetic_results.csv` with formal rows.
- Do not drop failed, timeout, no-Gurobi, infeasible, or empty-intersection rows.
- Do not treat fixed accepted-set diagnostics as behavioral acceptance evidence.
- Do not use the old `vkm_per_trip` label in new formal outputs.
- Do not upgrade to 30 seeds unless every optional paired cell completes.
