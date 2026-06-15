# 00 Repository Audit

**Phase:** 0 - Repository and Manuscript Audit
**Date:** 2026-06-15
**Status:** complete with caveats

## Purpose

Map the current repository before any new experiment work. This audit identifies code modules, experiment scripts, result artifacts, manuscript sources, reproducibility risks, and immediate blockers for the TR-E-level experimental rebuild.

## Repository Snapshot

The repository is a brownfield Python research project with these active surfaces:

- Core DRT package: `src/drt/`
- Experiment runners and focused experiment scripts: `experiments/`
- Post-hoc analysis scripts: `analysis/`
- Current result artifacts: `results/`
- Manuscript source and figures: `manuscript/`
- Human-written notes and review context: `docs/`
- Historical outputs and ad hoc tests: `archive/`
- GSD codebase map: `.planning/codebase/`

## Core Code Map

| Area | Files | Current Role | Phase 0 Assessment |
|------|-------|--------------|--------------------|
| Domain types | `src/drt/types.py` | Defines requests, vehicles, meeting points, bundles, routes, passenger types | Existing data contract; route stop typing is fragile |
| Candidate generation | `src/drt/candidate.py` | Filters meeting points by walking radius and top-k proximity | Relevant to meeting-point density and walking-radius experiments |
| Passenger choice | `src/drt/choice.py`, `experiments/variants.py` | Binary-logit acceptance helpers and pre-routing MNL filtering | Requires rebuild: current acceptance appears based on nearest MP proxy before actual offer/routing |
| Feasibility | `src/drt/feasibility.py` | Capacity, time-window, ride-time, route-duration checks | Needs explicit audit against full DARP constraints and rolling-horizon committed stops |
| Insertion | `src/drt/insertion.py` | Best insertion over vehicles, candidates, and positions | Core search primitive; likely combinatorial bottleneck |
| ALNS / rolling horizon | `src/drt/alns.py` | ALNS state, destroy/repair operators, rolling horizon simulation | Needs convergence, runtime-quality, and correctness validation |
| MILP diagnostic | `src/drt/milp.py`, `experiments/milp_gap.py` | Small exact/static diagnostic using Gurobi | Scope appears simplified; should be framed as diagnostic unless full sequencing model is implemented |

## Experiment Script Map

| Script | Role | Rebuild Relevance |
|--------|------|-------------------|
| `run_experiments.py` | Root launcher for experiment suite and summary checks | Current default entry point, but formal rebuild needs provenance and config manifests |
| `experiments/runner.py` | Runs variants across scales/seeds, writes synthetic/Beijing/result CSVs | Needs failure rows with status/error fields and reliable timeout isolation |
| `experiments/config.py` | Central experiment constants | Needs pilot/formal profile separation and parameter preregistration |
| `experiments/scenarios.py` | Synthetic and Beijing-inspired scenario generation | Needs train/tuning/final split and clear synthetic labeling |
| `experiments/variants.py` | DoorToDoor, DoorToDoorCapped, SingleSidedPickup, BidirectionalNoChoice, FullModel, AblationNoRollingHorizon, AblationNoChoice | Needs new baseline taxonomy and consistent passenger response |
| `experiments/metrics.py` | Aggregate metric computation | Needs denominator contract and additional rejection/coverage metrics |
| `experiments/matched_coverage.py` | Matched-coverage diagnostic | Should become a primary design, not an exploratory aside |
| `experiments/endogenous_matched_coverage.py` | Endogenous coverage-matching experiment | Candidate for formal coverage-confounding controls |
| `experiments/pareto_sweep.py` | Gamma welfare sweep | Currently post-hoc welfare scoring; not a real Pareto frontier |
| `experiments/weight_sensitivity.py` | Objective weight sensitivity | Needs formula audit and shared metric helper use |
| `experiments/milp_gap.py` | MILP-vs-ALNS diagnostic | Needs expanded validation and honest diagnostic framing |

## Result Artifact Map

| Artifact | Current Meaning | Caution |
|----------|-----------------|---------|
| `results/synthetic_results.csv` | Raw synthetic variant rows | Uses current variant assumptions; not final evidence |
| `results/beijing_results.csv` | Beijing-inspired synthetic rows | Must not be called real Beijing evidence |
| `results/metrics_table.csv` | Aggregated means/stds | Aggregation alone does not resolve coverage confounding |
| `results/matched_coverage.csv` | Matched-coverage diagnostic | Should be upgraded to formal design with paired seeds |
| `results/endogenous_matched_coverage.csv` | Endogenous coverage diagnostic | Needs method contract and reproducibility manifest |
| `results/pareto_gamma_sweep.csv` | Gamma welfare sweep | Gamma does not affect routing/acceptance in current implementation |
| `results/equity_table.csv` | Type-level equity outputs | Type parameters are simulation assumptions, not calibrated population evidence |
| `results/milp_gap.json` | MILP/ALNS comparison | Current gap is large; MILP scope likely simplified |
| `results/weight_sensitivity.json` | Weight sensitivity outputs | Needs metric formula audit |
| `results/policy_recommendations.md` | Policy prose from analysis | Needs strict downgrade to simulation-based insights |

## Manuscript and Documentation Map

| Artifact | Role | Audit Note |
|----------|------|------------|
| `manuscript/main.tex` | Master LaTeX manuscript | Current target journal says Part A |
| `manuscript/sections/abstract.tex` | Abstract with headline claims | Contains 29.1% improvement, served-share contrast, equity Gini, policy implications |
| `manuscript/sections/experiments.tex` | Main experimental evidence | Exposes current baseline/coverage/gamma limitations |
| `manuscript/sections/policy.tex` | Policy implications | Must be conditional and simulation-based |
| `manuscript/references.bib` | Bibliography | Needs fact-check of Cortenbach, Fielbaum, Wu, Psaraftis, and choice-based routing literature |
| `docs/工作3讨论-6.14.md` | Review report | Key Phase 0 risk source; file has mojibake/encoding damage |
| `README.md` | Project overview and known issues | Notes git and planning drift; target journal conflicts with rebuild prompt |

## Existing Codebase Concerns To Carry Forward

- Mixed import roots: experiment code imports `src.drt.*` while package/tests use `drt.*`.
- Runtime dependencies `pandas` and `matplotlib` are used but not declared in `pyproject.toml`.
- Route stops are untyped tuples with inconsistent 2-tuple and 4-tuple forms.
- `src/drt/alns.py` mixes state, operators, rolling horizon, and benchmark behavior.
- Bare `pytest` can collect archived ad hoc tests and fail.
- Runner timeout may not bound wall time because thread executor shutdown waits for the worker.
- `FullModel(gamma=...)` does not affect acceptance, routing, or offer generation.
- `compute_metrics()` declares `social_welfare` but does not populate it.
- `analysis/policy.py` may use hardcoded fallback values silently.
- Experiment outputs lack complete provenance.

## Newly Verified Phase 0 Concerns

- `experiments/runner.py` writes `metrics_table.csv` by grouping all synthetic scales by variant. The manuscript's main table values match this all-scale aggregation, despite the table caption describing a 200-request, 15-vehicle scenario.
- `experiments/matched_coverage.py` documents a post-hoc random-rejection approach where DoorToDoor routing remains unchanged. The manuscript text describes an endogenous cap with continued route optimization, so the script and prose do not match.
- `experiments/endogenous_matched_coverage.py` and `results/endogenous_matched_coverage.csv` do provide an endogenous capped diagnostic close to the manuscript's 11.1 vs 17.1 vkm/trip table, but the mean served share is about 23%, not exactly the main-table 18.3% headline.
- `experiments/pareto_sweep.py` passes gamma into `FullModel(gamma=...)`, but `FullModel` stores `_gamma` without using it in acceptance or routing. The output confirms served share and vkm/served trip are invariant across gamma.
- `analysis/equity.py` computes type-level acceptance across 3 seeds with fixed artificial passenger-type assignment. This reproduces the current Gini but should not support calibrated population-equity claims.
- `results/weight_sensitivity.json` stores vkm/trip on a different scale than the manuscript table, suggesting a formula or post-processing mismatch.
- `manuscript/figures/scripts/fig04_baseline_comparison.py` reads `results/metrics_table.csv`, but its annotation text says `-34.9% vkm/acceptance vs D2D`, which does not match the manuscript's 29.1% vkm/trip claim.
- `manuscript/figures/scripts/fig06_policy_map.py` is hard-coded from threshold logic rather than generated from a result artifact.
- `manuscript/figures/scripts/fig07_pareto.py` still titles the plot as a Pareto frontier even though the underlying CSV is invariant in served share and vkm/trip across gamma.

## Phase 0-Relevant Blockers For Later Work

| Blocker | Evidence | Routed To |
|---------|----------|-----------|
| Target journal conflict | `README.md` and manuscript cover letter say Transportation Research Part A; rebuild roadmap targets TR-E or comparable evidence quality | Phase 1 |
| Novelty overclaim risk | `abstract.tex`, `intro.tex`, `literature.tex`, and review note flag prior bidirectional walking/meeting-point work | Phase 1 |
| Baseline taxonomy conflates service design, passenger response, and routing algorithm | `experiments/variants.py`; current `DoorToDoor`, `BidirectionalNoChoice`, `FullModel`, and ablations use different response/optimization assumptions | Phase 2 |
| Metric denominator ambiguity | `results/metrics_table.csv`, `results/weight_sensitivity.json`, and manuscript tables use inconsistent vkm/trip derivations | Phase 2 |
| Choice model calibration gap | `src/drt/choice.py`, `experiments/variants.py`, and manuscript VOT section show manually selected beta parameters | Phase 3 |
| ALNS/MILP validation gap | `results/milp_gap.json` and `.planning/codebase/CONCERNS.md` show large gaps and limited exact scope | Phase 4 |
| Formal reproducibility gap | Current CSV/JSON outputs lack config ID, command, code revision, dependency versions, status/error rows, and enough paired seeds | Phase 5/6 |
| Synthetic policy external validity | `results/beijing_results.csv`, `results/policy_recommendations.md`, and `fig06_policy_map.py` are synthetic/illustrative | Phase 7/9 |

## Phase 0 Gate Decision

**Status:** pass with caveats.

The repository is sufficiently mapped to start the rebuild, and the highest-risk result provenance issues are visible. Phase 0 does not certify current results as final evidence; it certifies that the risks and artifact sources are explicit enough to plan Phase 1 and Phase 2.

## Next Actions

- Start Phase 1 literature and novelty audit before preserving any first/only contribution language.
- Start Phase 2 experiment contract before regenerating formal results.
- Preserve current result files as exploratory baseline artifacts, but do not use them as final manuscript evidence.
