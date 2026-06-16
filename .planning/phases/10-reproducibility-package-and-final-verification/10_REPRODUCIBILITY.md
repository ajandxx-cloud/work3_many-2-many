# Phase 10 Reproducibility Guide

**Status:** Blocked: prerequisites missing
**Structured source:** `10_RESULT_MANIFEST.md`

## Reproduction Status

Phase 10 is `Blocked: prerequisites missing` until the formal Phase 6 evidence report and the Phase 8 claim-gate artifacts exist. This guide is still created as a blocked/pending artifact so reviewers, coauthors, and future agents can see exactly what is reproducible now and what must wait.

Current blocker summary:

- Phase 6 formal synthetic evidence report is missing.
- Phase 8 claim-evidence matrix is missing.
- Phase 8 supported-claims list is missing.
- Phase 8 unsupported/exploratory-claims list is missing.

## Environment Setup

Run these commands from the repository root unless a later row says otherwise.

| purpose | command | notes |
|---|---|---|
| Editable install | `python -m pip install -e .` | Installs the local `drt` package declared in `pyproject.toml`. |
| Dependency snapshot | `python -m pip freeze` | Save the output with the final package; `pandas` and `matplotlib` may be present even though core metadata lists only `gurobipy` and `numpy`. |
| Code revision | `git rev-parse HEAD` | Capture after final Phase 10 commits and after any repository-maintenance commit. |
| Working-tree state | `git status --short` | Required because current version-control state is heavily drifted. |
| Active test suite | `$env:PYTHONPATH='src'; pytest tests -q` | PowerShell command for the active test suite; bare `pytest` may collect archived ad hoc tests. |

## Command Taxonomy

Command groups:

- `final evidence`: Phase 6 formal main evidence and Phase 8-supported final tables/figures.
- `critical robustness`: matched-coverage, fixed accepted-set, sensitivity, and equity checks that can qualify claims only after Phase 8.
- `supplementary diagnostic`: MILP, ALNS, gamma, weight, and other mechanism diagnostics.
- `legacy diagnostic`: current root result regeneration or historical outputs that are provenance only.
- `pilot readiness`: Phase 5 pilot artifacts and smoke checks; not final evidence.
- `manuscript figures`: figure-generation scripts and generated figure files.
- `manuscript build`: LaTeX build inputs and compiled PDF outputs.

## Prerequisite Blockers

The hard blockers are defined in `10_RESULT_MANIFEST.md` under `Prerequisite Gate`. They are repeated here for reviewer-facing clarity:

| prerequisite | status |
|---|---|
| `.planning/phases/06-formal-synthetic-experiments/06_FORMAL_SYNTHETIC_RESULTS.md` | Blocked: prerequisites missing |
| `.planning/phases/08-evidence-synthesis-and-claim-gate/08_CLAIM_EVIDENCE_MATRIX.md` | Blocked: prerequisites missing |
| `.planning/phases/08-evidence-synthesis-and-claim-gate/08_SUPPORTED_CLAIMS.md` | Blocked: prerequisites missing |
| `.planning/phases/08-evidence-synthesis-and-claim-gate/08_UNSUPPORTED_OR_EXPLORATORY_CLAIMS.md` | Blocked: prerequisites missing |

## Reproduction Entry Points

Reviewer-facing commands are grouped by evidence role. Commands that regenerate current outputs do not upgrade those outputs to final evidence; Phase 6 formal completion and Phase 8 claim support are still required.

| purpose | evidence_role | command | inputs | outputs | status | blocker |
|---|---|---|---|---|---|---|
| Formal Phase 6 main evidence | final evidence | `python -m experiments.phase06_formal` or the final Phase 6 runner once implemented | Predeclared Phase 6 seeds, scales, method set, configs, and failure/rerun ledger | `results/formal/phase06/` and `06_FORMAL_SYNTHETIC_RESULTS.md` | Blocked | Blocked: prerequisites missing |
| Phase 8 claim gate | final evidence | `$gsd-execute-phase 8` after Phase 8 plans exist | Formal Phase 6 report, result manifest, manuscript claim inventory | `08_CLAIM_EVIDENCE_MATRIX.md`, `08_SUPPORTED_CLAIMS.md`, `08_UNSUPPORTED_OR_EXPLORATORY_CLAIMS.md` | Blocked | Blocked: prerequisites missing |
| Legacy root result regeneration | legacy diagnostic / provenance | `python run_experiments.py` | Current runner, variants, synthetic/Beijing scenario generators, existing config constants | `results/synthetic_results.csv`, `results/beijing_results.csv`, `results/metrics_table.csv`, `results/utility_components.csv` | Not final evidence | pending Phase 8; legacy outputs must be replaced by formal Phase 6 evidence before headline claims |
| Importable full runner | legacy diagnostic / provenance | `python -m experiments.runner` | Same as root runner | Same root result CSVs | Not final evidence | pending Phase 8; runner timeout and dependency concerns remain documented |
| Matched coverage diagnostic | critical robustness | `python -m experiments.matched_coverage` | Synthetic scenario seeds, FullModel baseline, DoorToDoor post-hoc rejection calibration | `results/matched_coverage.csv` | Pending | pending Phase 8; post-hoc control is diagnostic unless formalized |
| Endogenous matched coverage diagnostic | critical robustness | `python -m experiments.endogenous_matched_coverage` | FullModel target share and DoorToDoorCapped served-share cap | `results/endogenous_matched_coverage.csv` | Pending | pending Phase 8 and formal design confirmation |
| Sensitivity diagnostics | critical robustness | `python -m analysis.sensitivity` | Current scenario generator, FullModel, DoorToDoor, walking and fleet grids | `results/sensitivity_walk.csv`, `results/sensitivity_fleet.csv` | Pending | pending Phase 8; bounded robustness only |
| Equity diagnostic | critical robustness | `python -m analysis.equity` | FullModel synthetic runs and passenger-type records | `results/equity_table.csv` | Pending | pending Phase 8; type-level trade-off only |
| MILP/static-snapshot diagnostic | supplementary diagnostic | `python -m experiments.milp_gap` | Small fixed accepted-set instances, optional Gurobi solver | `results/milp_gap.json` | Not final evidence | solver/license dependent; algorithm diagnostic only |
| Phase 5 pilot readiness package | pilot readiness | `python -m experiments.phase05_pilot` and `python -m experiments.phase05_coverage_smoke` | Seeds 42/43/44 at scale 20, pilot validation harness | `results/pilot/phase05/*` | Not final evidence | readiness/provenance only; not formal claim support |
| Manuscript figure scripts | manuscript figures | `python manuscript/figures/scripts/<script>.py` from the supported working directory | Current result files and script-local inputs | `manuscript/figures/*.pdf`, `manuscript/figures/*.png` | Pending | generated displays require Phase 8 support before supporting final claims |
| Manuscript build | manuscript build | `latexmk -pdf manuscript/main.tex` or locally supported `pdflatex`/`bibtex` sequence | `manuscript/main.tex`, `manuscript/sections/`, `manuscript/references.bib`, figures | `manuscript/main.pdf` | Pending | final claims remain blocked by Phase 8 |

## Manuscript Build Chain

The manuscript build surface is present, but final numerical, table, figure, and claim wording remain blocked by Phase 8 support.

| build input/output | path | reproduction command or role | status |
|---|---|---|---|
| Master LaTeX entry | `manuscript/main.tex` | `latexmk -pdf manuscript/main.tex` if `latexmk` is locally supported; otherwise use the local sequence `pdflatex main`, `bibtex main`, `pdflatex main`, `pdflatex main` from inside `manuscript/` | Pending |
| Compiled manuscript | `manuscript/main.pdf` | Output of the LaTeX build chain | Pending |
| Section sources | `manuscript/sections/` | Inputs included by `manuscript/main.tex` | Pending Phase 8 claim support |
| Bibliography | `manuscript/references.bib` | Input to `bibtex main` | Pending bibliography cleanup/final build |
| Figure outputs | `manuscript/figures/` | Generated by scripts under `manuscript/figures/scripts/` | Generated figure/table outputs require Phase 8 support before supporting final claims |

## Table and Figure Provenance

Generated figure/table outputs require Phase 8 support before supporting final claims. Several current scripts encode legacy displays and must be regenerated from Phase 6/8-supported data before final manuscript use.

| script_path | expected_outputs | evidence_role | Phase 8 note |
|---|---|---|---|
| `manuscript/figures/scripts/fig01_system_overview.py` | `manuscript/figures/fig01_system_overview.pdf`, `manuscript/figures/fig01_system_overview.png` | manuscript figure / conceptual display | Caption must identify the evidence role. |
| `manuscript/figures/scripts/fig02_three_layer.py` | `manuscript/figures/fig02_three_layer.pdf`, `manuscript/figures/fig02_three_layer.png` | manuscript figure / conceptual display | Caption must identify the evidence role. |
| `manuscript/figures/scripts/fig03_algorithm.py` | `manuscript/figures/fig03_algorithm.pdf`, `manuscript/figures/fig03_algorithm.png` | manuscript figure / algorithm display | Algorithm display only unless Phase 8 approves a bounded claim. |
| `manuscript/figures/scripts/fig04_baseline_comparison.py` | `manuscript/figures/fig04_baseline_comparison.pdf`, `manuscript/figures/fig04_baseline_comparison.png` | manuscript figure / legacy comparison display | Must be regenerated from Phase 6 formal data and Phase 8-supported claims. |
| `manuscript/figures/scripts/fig05_sensitivity.py` | `manuscript/figures/fig05_sensitivity.pdf`, `manuscript/figures/fig05_sensitivity.png` | manuscript figure / robustness display | Use only as bounded robustness after Phase 8 support. |
| `manuscript/figures/scripts/fig06_policy_map.py` | `manuscript/figures/fig06_policy_map.pdf`, `manuscript/figures/fig06_policy_map.png` | manuscript figure / managerial display | Prescriptive deployment-map framing must be removed or bounded. |
| `manuscript/figures/scripts/fig07_pareto.py` | `manuscript/figures/fig07_pareto.pdf`, `manuscript/figures/fig07_pareto.png` | manuscript figure / gamma diagnostic display | Retitle as gamma sensitivity unless implementation and Phase 8 support a Pareto claim. |

## Final Artifact Index

This human-readable index mirrors the structured manifest in `10_RESULT_MANIFEST.md`. The manifest remains the structured table suitable for later JSON/CSV conversion.

### source-of-truth planning artifacts

- `.planning/PROJECT.md`
- `.planning/REQUIREMENTS.md`
- `.planning/ROADMAP.md`
- `.planning/STATE.md`
- `.planning/phases/10-reproducibility-package-and-final-verification/10-CONTEXT.md`
- `.planning/phases/09-manuscript-restructure-for-tr-part-e/09_TR_E_MANUSCRIPT_STRUCTURE.md`
- `.planning/phases/09-manuscript-restructure-for-tr-part-e/09_TABLE_FIGURE_PLAN.md`

### structured manifests

- `.planning/phases/10-reproducibility-package-and-final-verification/10_RESULT_MANIFEST.md`
- `.planning/phases/10-reproducibility-package-and-final-verification/10_REPRODUCIBILITY.md`
- `.planning/phases/10-reproducibility-package-and-final-verification/10_FINAL_VERIFICATION.md` (planned by Phase 10 plan 10-03)

### result artifacts

- `results/synthetic_results.csv`
- `results/metrics_table.csv`
- `results/beijing_results.csv`
- `results/matched_coverage.csv`
- `results/endogenous_matched_coverage.csv`
- `results/equity_table.csv`
- `results/milp_gap.json`
- `results/milp_benchmark.json`
- `results/pareto_gamma_sweep.csv`
- `results/weight_sensitivity.json`
- `results/policy_recommendations.md`
- `results/pilot/phase05/`

### manuscript source

- `manuscript/main.tex`
- `manuscript/sections/`
- `manuscript/references.bib`
- `manuscript/cover_letter.tex`
- `manuscript/response_to_reviewers.tex`

### figure scripts

- `manuscript/figures/scripts/fig01_system_overview.py`
- `manuscript/figures/scripts/fig02_three_layer.py`
- `manuscript/figures/scripts/fig03_algorithm.py`
- `manuscript/figures/scripts/fig04_baseline_comparison.py`
- `manuscript/figures/scripts/fig05_sensitivity.py`
- `manuscript/figures/scripts/fig06_policy_map.py`
- `manuscript/figures/scripts/fig07_pareto.py`

### generated manuscript outputs

- `manuscript/main.pdf`
- `manuscript/figures/*.pdf`
- `manuscript/figures/*.png`

Generated manuscript outputs are reproducibility artifacts. They require Phase 8 support before supporting final claims.
