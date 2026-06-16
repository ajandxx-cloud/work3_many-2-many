# Phase 10 Result Manifest

**Status:** Blocked: prerequisites missing
**Purpose:** Inventory result, diagnostic, display, and manuscript-build artifacts by evidence role before final claim verification.

## Prerequisite Gate

Phase 10 must fail closed until the formal evidence report and claim-gate artifacts below exist. Missing prerequisites use the exact status `Blocked: prerequisites missing`.

| prerequisite_path | status | implication |
|---|---|---|
| `.planning/phases/06-formal-synthetic-experiments/06_FORMAL_SYNTHETIC_RESULTS.md` | Blocked: prerequisites missing | Formal synthetic evidence report is absent, so main results cannot be certified as final evidence. |
| `.planning/phases/08-evidence-synthesis-and-claim-gate/08_CLAIM_EVIDENCE_MATRIX.md` | Blocked: prerequisites missing | Claim-to-evidence mapping is absent, so artifact claim links remain `pending Phase 8`. |
| `.planning/phases/08-evidence-synthesis-and-claim-gate/08_SUPPORTED_CLAIMS.md` | Blocked: prerequisites missing | Supported final claims are not approved. |
| `.planning/phases/08-evidence-synthesis-and-claim-gate/08_UNSUPPORTED_OR_EXPLORATORY_CLAIMS.md` | Blocked: prerequisites missing | Unsupported or exploratory claims are not classified for final manuscript use. |

## Manifest Schema

Rows in the layered manifest use one artifact per row and the following stable columns so the table can later be exported to JSON or CSV.

| path | role | evidence_family | status | source_command | inputs | outputs | code_revision | claim_link | notes/blockers |
|---|---|---|---|---|---|---|---|---|---|
| Example path | Example role | Example evidence family | Example status | Example command | Example inputs | Example outputs | Example revision | Example claim link | Example notes/blockers |

## Evidence Families

| evidence_family | allowed role | final-claim rule |
|---|---|---|
| `formal_main_evidence` | final evidence candidate | Requires complete Phase 6 report and Phase 8 claim support before use in headline claims. |
| `critical_robustness` | robustness evidence candidate | May qualify final claims only after Phase 8 support; otherwise `pending Phase 8`. |
| `supplementary_diagnostic` | diagnostic | Mechanism or appendix support only unless Phase 8 explicitly promotes a bounded claim. |
| `legacy_diagnostic` | legacy or provenance | Not final evidence; use only to explain historical outputs or audit provenance. |
| `pilot_readiness` | readiness or provenance | Not final evidence; pilot outputs cannot support headline claims. |
| `manuscript_display` | display asset | Reproducible display artifact; empirical status depends on underlying evidence and Phase 8 support. |
| `manuscript_build` | build artifact | Reproducibility and packaging support, not empirical evidence by itself. |

## Layered Artifact Manifest

All rows use the schema from `Manifest Schema`. `claim_link` stays `pending Phase 8` until the Phase 8 claim-gate trio exists. No pilot, legacy, or diagnostic artifact below supports headline claims in its current state.

### Formal Main Evidence

| path | role | evidence_family | status | source_command | inputs | outputs | code_revision | claim_link | notes/blockers |
|---|---|---|---|---|---|---|---|---|---|
| `.planning/phases/06-formal-synthetic-experiments/06_FORMAL_SYNTHETIC_RESULTS.md` | final evidence prerequisite | `formal_main_evidence` | Blocked: prerequisites missing | Phase 6 formal execution, not run in Phase 10 | Formal paired-seed configs and raw rows | Formal synthetic evidence report | pending task 10-01-03 revision capture | pending Phase 8 | Missing; main formal evidence cannot be certified. |
| `results/formal/phase06/` | final evidence output root | `formal_main_evidence` | Blocked: prerequisites missing | Phase 6 formal runners, not run in Phase 10 | Predeclared Phase 6 seeds, scales, methods, configs | Raw rows, processed tables, failure ledger, plots | pending task 10-01-03 revision capture | pending Phase 8 | Expected formal output root is not present in this workspace. |

### Critical Robustness

| path | role | evidence_family | status | source_command | inputs | outputs | code_revision | claim_link | notes/blockers |
|---|---|---|---|---|---|---|---|---|---|
| `results/matched_coverage.csv` | robustness diagnostic | `critical_robustness` | Pending | `python -m experiments.matched_coverage` | Synthetic result rows and coverage target design | Matched-coverage CSV | pending task 10-01-03 revision capture | pending Phase 8 | Needs Phase 6/8 support before any main-text robustness claim. |
| `results/endogenous_matched_coverage.csv` | robustness diagnostic | `critical_robustness` | Pending | `python -m experiments.endogenous_matched_coverage` | Synthetic result rows and endogenous cap design | Endogenous matched-coverage CSV | pending task 10-01-03 revision capture | pending Phase 8 | Needs Phase 6/8 support and design confirmation. |
| `results/sensitivity_walk.csv` | robustness diagnostic | `critical_robustness` | Pending | `python -m analysis.sensitivity` | Scenario and walking tolerance grid | Walking-sensitivity CSV | pending task 10-01-03 revision capture | pending Phase 8 | Boundary-condition evidence only until claim-gated. |
| `results/sensitivity_fleet.csv` | robustness diagnostic | `critical_robustness` | Pending | `python -m analysis.sensitivity` | Scenario and fleet-size grid | Fleet-sensitivity CSV | pending task 10-01-03 revision capture | pending Phase 8 | Boundary-condition evidence only until claim-gated. |
| `results/equity_table.csv` | robustness diagnostic | `critical_robustness` | Pending | `python -m analysis.equity` | Current result CSVs and passenger-type fields | Equity summary table | pending task 10-01-03 revision capture | pending Phase 8 | Type-level trade-off evidence remains bounded and pending. |

### Supplementary Diagnostics

| path | role | evidence_family | status | source_command | inputs | outputs | code_revision | claim_link | notes/blockers |
|---|---|---|---|---|---|---|---|---|---|
| `results/milp_gap.json` | algorithm diagnostic | `supplementary_diagnostic` | Pending | `python -m experiments.milp_gap` | Small fixed accepted-set diagnostic instances | MILP gap JSON | pending task 10-01-03 revision capture | pending Phase 8 | Solver-dependent diagnostic; not service-design evidence by itself. |
| `results/milp_benchmark.json` | algorithm diagnostic | `supplementary_diagnostic` | Pending | MILP benchmark writer | Static benchmark scenario | MILP benchmark JSON | pending task 10-01-03 revision capture | pending Phase 8 | Scope remains static diagnostic, not online stochastic benchmark. |
| `results/pareto_gamma_sweep.csv` | welfare-accounting diagnostic | `supplementary_diagnostic` | Not final evidence | `python -m experiments.pareto_sweep` | Current FullModel outputs and gamma grid | Gamma sweep CSV | pending task 10-01-03 revision capture | pending Phase 8 | Gamma is post-hoc unless implementation changes; do not call this a Pareto frontier. |
| `results/weight_sensitivity.json` | diagnostic robustness | `supplementary_diagnostic` | Not final evidence | `python -m experiments.weight_sensitivity` | Weight grid and synthetic scenario | Weight sensitivity JSON | pending task 10-01-03 revision capture | pending Phase 8 | Known formula concern; requires review before any manuscript use. |
| `results/policy_recommendations.md` | managerial diagnostic | `supplementary_diagnostic` | Not final evidence | `python -m analysis.policy` | Current result CSVs | Policy recommendation markdown | pending task 10-01-03 revision capture | pending Phase 8 | Must be rewritten as bounded insights, not universal prescriptions. |

### Pilot Readiness

All rows in this group use `pilot_readiness` and the `readiness` or `provenance` role. They are not final evidence and cannot support headline claims.

| path | role | evidence_family | status | source_command | inputs | outputs | code_revision | claim_link | notes/blockers |
|---|---|---|---|---|---|---|---|---|---|
| `results/pilot/phase05/synthetic_results.csv` | readiness | `pilot_readiness` | Passed for readiness | `python -m experiments.phase05_pilot` | Seeds 42, 43, 44 at scale 20 | Pilot behavioral raw rows | pending task 10-01-03 revision capture | pending Phase 8 | Readiness-only; no method-superiority claim. |
| `results/pilot/phase05/metrics_table.csv` | readiness | `pilot_readiness` | Passed for readiness | `python -m experiments.phase05_pilot` | Pilot raw rows | Pilot aggregate metrics | pending task 10-01-03 revision capture | pending Phase 8 | Readiness-only aggregate checks. |
| `results/pilot/phase05/utility_components.csv` | readiness | `pilot_readiness` | Passed for readiness | `python -m experiments.phase05_pilot` | Pilot utility logging | Utility component rows | pending task 10-01-03 revision capture | pending Phase 8 | Joinability evidence for pilot only. |
| `results/pilot/phase05/matched_coverage_pilot.csv` | readiness diagnostic | `pilot_readiness` | Passed for readiness | `python -m experiments.phase05_coverage_smoke` | Pilot matched-coverage targets | Pilot matched-coverage CSV | pending task 10-01-03 revision capture | pending Phase 8 | Readiness diagnostic with per-seed integer target repair. |
| `results/pilot/phase05/fixed_accepted_set_smoke.json` | readiness diagnostic | `pilot_readiness` | Passed for readiness | Phase 5 fixed accepted-set smoke | Seed 42 candidate-serviceable retained set | Fixed accepted-set smoke JSON | pending task 10-01-03 revision capture | pending Phase 8 | Uses `common_candidate_serviceable` fallback; not formal construction evidence. |
| `results/pilot/phase05/plots/status_counts.png` | readiness display | `pilot_readiness` | Passed for readiness | Phase 5 pilot plotting | Pilot status rows | Status-count plot | pending task 10-01-03 revision capture | pending Phase 8 | Diagnostic display only. |
| `results/pilot/phase05/plots/failure_timeout_counts.png` | readiness display | `pilot_readiness` | Passed for readiness | Phase 5 pilot plotting | Pilot failure/timeout rows | Failure/timeout plot | pending task 10-01-03 revision capture | pending Phase 8 | Diagnostic display only. |
| `results/pilot/phase05/plots/matched_coverage_gaps.png` | readiness display | `pilot_readiness` | Passed for readiness | Phase 5 pilot plotting | Pilot matched-coverage gaps | Matched-coverage gap plot | pending task 10-01-03 revision capture | pending Phase 8 | Diagnostic display only. |

### Legacy Provenance

| path | role | evidence_family | status | source_command | inputs | outputs | code_revision | claim_link | notes/blockers |
|---|---|---|---|---|---|---|---|---|---|
| `results/synthetic_results.csv` | legacy provenance | `legacy_diagnostic` | Not final evidence | `python run_experiments.py` or `python -m experiments.runner` | Legacy synthetic scenarios and variants | Synthetic result CSV | pending task 10-01-03 revision capture | pending Phase 8 | Legacy/provisional rows; replace with Phase 6 formal matrix before final claims. |
| `results/metrics_table.csv` | legacy provenance | `legacy_diagnostic` | Not final evidence | `python run_experiments.py` or `python -m experiments.runner` | Legacy raw rows | Metrics table CSV | pending task 10-01-03 revision capture | pending Phase 8 | Legacy metrics table; must not drive final main table. |
| `results/beijing_results.csv` | synthetic-boundary provenance | `legacy_diagnostic` | Not final evidence | `python run_experiments.py` or `python -m experiments.runner` | Beijing-inspired synthetic scenario | Beijing-inspired result CSV | pending task 10-01-03 revision capture | pending Phase 8 | Synthetic boundary/case stress test only. |
| `results/experiment_log.txt` | provenance | `legacy_diagnostic` | Not final evidence | Historical experiment run logging | Experiment run commands and outputs | Text log | pending task 10-01-03 revision capture | pending Phase 8 | Useful for provenance review, not final evidence. |
| `results/targeted_run_log.txt` | provenance | `legacy_diagnostic` | Not final evidence | Historical targeted run logging | Targeted commands and outputs | Text log | pending task 10-01-03 revision capture | pending Phase 8 | Useful for provenance review, not final evidence. |
| `results/runner_output.txt` | provenance | `legacy_diagnostic` | Not final evidence | Historical runner output capture | Runner stdout/stderr | Text output | pending task 10-01-03 revision capture | pending Phase 8 | Empty in current workspace; not evidence. |

### Manuscript Displays

| path | role | evidence_family | status | source_command | inputs | outputs | code_revision | claim_link | notes/blockers |
|---|---|---|---|---|---|---|---|---|---|
| `manuscript/figures/scripts/fig01_system_overview.py` | figure script | `manuscript_display` | Pending | `python manuscript/figures/scripts/fig01_system_overview.py` | Script-local schematic inputs | Figure 1 PDF/PNG | pending task 10-01-03 revision capture | pending Phase 8 | Conceptual/display asset; caption must state evidence role. |
| `manuscript/figures/scripts/fig02_three_layer.py` | figure script | `manuscript_display` | Pending | `python manuscript/figures/scripts/fig02_three_layer.py` | Script-local schematic inputs | Figure 2 PDF/PNG | pending task 10-01-03 revision capture | pending Phase 8 | Conceptual/display asset; caption must state evidence role. |
| `manuscript/figures/scripts/fig03_algorithm.py` | figure script | `manuscript_display` | Pending | `python manuscript/figures/scripts/fig03_algorithm.py` | Script-local schematic inputs | Figure 3 PDF/PNG | pending task 10-01-03 revision capture | pending Phase 8 | Algorithm display, not empirical evidence. |
| `manuscript/figures/scripts/fig04_baseline_comparison.py` | figure script | `manuscript_display` | Pending | `python manuscript/figures/scripts/fig04_baseline_comparison.py` | Legacy or future Phase 6 result data | Figure 4 PDF/PNG | pending task 10-01-03 revision capture | pending Phase 8 | Must be regenerated from Phase 6/8-supported data before final use. |
| `manuscript/figures/scripts/fig05_sensitivity.py` | figure script | `manuscript_display` | Pending | `python manuscript/figures/scripts/fig05_sensitivity.py` | Sensitivity result files | Figure 5 PDF/PNG | pending task 10-01-03 revision capture | pending Phase 8 | Bounded robustness display only if Phase 8 supports it. |
| `manuscript/figures/scripts/fig06_policy_map.py` | figure script | `manuscript_display` | Pending | `python manuscript/figures/scripts/fig06_policy_map.py` | Policy-map inputs | Figure 6 PDF/PNG | pending task 10-01-03 revision capture | pending Phase 8 | Prescriptive deployment-map framing must be replaced or bounded. |
| `manuscript/figures/scripts/fig07_pareto.py` | figure script | `manuscript_display` | Pending | `python manuscript/figures/scripts/fig07_pareto.py` | Gamma sweep CSV | Figure 7 PDF/PNG | pending task 10-01-03 revision capture | pending Phase 8 | Retitle as gamma sensitivity unless model behavior changes and Phase 8 supports. |
| `manuscript/figures/fig01_system_overview.pdf` | generated figure | `manuscript_display` | Pending | Figure 1 script | Figure script | PDF output | pending task 10-01-03 revision capture | pending Phase 8 | Display asset. |
| `manuscript/figures/fig01_system_overview.png` | generated figure | `manuscript_display` | Pending | Figure 1 script | Figure script | PNG output | pending task 10-01-03 revision capture | pending Phase 8 | Display asset. |
| `manuscript/figures/fig02_three_layer.pdf` | generated figure | `manuscript_display` | Pending | Figure 2 script | Figure script | PDF output | pending task 10-01-03 revision capture | pending Phase 8 | Display asset. |
| `manuscript/figures/fig02_three_layer.png` | generated figure | `manuscript_display` | Pending | Figure 2 script | Figure script | PNG output | pending task 10-01-03 revision capture | pending Phase 8 | Display asset. |
| `manuscript/figures/fig03_algorithm.pdf` | generated figure | `manuscript_display` | Pending | Figure 3 script | Figure script | PDF output | pending task 10-01-03 revision capture | pending Phase 8 | Display asset. |
| `manuscript/figures/fig03_algorithm.png` | generated figure | `manuscript_display` | Pending | Figure 3 script | Figure script | PNG output | pending task 10-01-03 revision capture | pending Phase 8 | Display asset. |
| `manuscript/figures/fig04_baseline_comparison.pdf` | generated figure | `manuscript_display` | Pending | Figure 4 script | Figure script and result data | PDF output | pending task 10-01-03 revision capture | pending Phase 8 | Legacy comparison display pending replacement. |
| `manuscript/figures/fig04_baseline_comparison.png` | generated figure | `manuscript_display` | Pending | Figure 4 script | Figure script and result data | PNG output | pending task 10-01-03 revision capture | pending Phase 8 | Legacy comparison display pending replacement. |
| `manuscript/figures/fig05_sensitivity.pdf` | generated figure | `manuscript_display` | Pending | Figure 5 script | Figure script and sensitivity data | PDF output | pending task 10-01-03 revision capture | pending Phase 8 | Bounded robustness display pending support. |
| `manuscript/figures/fig05_sensitivity.png` | generated figure | `manuscript_display` | Pending | Figure 5 script | Figure script and sensitivity data | PNG output | pending task 10-01-03 revision capture | pending Phase 8 | Bounded robustness display pending support. |
| `manuscript/figures/fig06_policy_map.pdf` | generated figure | `manuscript_display` | Pending | Figure 6 script | Figure script and policy data | PDF output | pending task 10-01-03 revision capture | pending Phase 8 | Prescriptive policy-map framing pending replacement. |
| `manuscript/figures/fig06_policy_map.png` | generated figure | `manuscript_display` | Pending | Figure 6 script | Figure script and policy data | PNG output | pending task 10-01-03 revision capture | pending Phase 8 | Prescriptive policy-map framing pending replacement. |
| `manuscript/figures/fig07_pareto.pdf` | generated figure | `manuscript_display` | Pending | Figure 7 script | Figure script and gamma sweep data | PDF output | pending task 10-01-03 revision capture | pending Phase 8 | Gamma sensitivity display pending correction/support. |
| `manuscript/figures/fig07_pareto.png` | generated figure | `manuscript_display` | Pending | Figure 7 script | Figure script and gamma sweep data | PNG output | pending task 10-01-03 revision capture | pending Phase 8 | Gamma sensitivity display pending correction/support. |

### Manuscript Build

| path | role | evidence_family | status | source_command | inputs | outputs | code_revision | claim_link | notes/blockers |
|---|---|---|---|---|---|---|---|---|---|
| `manuscript/main.tex` | manuscript build entry | `manuscript_build` | Pending | `latexmk -pdf manuscript/main.tex` or equivalent local LaTeX command | Manuscript sections, bibliography, figures | `manuscript/main.pdf` | pending task 10-01-03 revision capture | pending Phase 8 | Build reproducibility must be documented before final package. |
| `manuscript/main.pdf` | compiled manuscript output | `manuscript_build` | Pending | LaTeX build command | `manuscript/main.tex` and dependencies | PDF manuscript | pending task 10-01-03 revision capture | pending Phase 8 | Output exists but final claims remain blocked by Phase 8. |

## Revision and Dependency Provenance

The current code revision and dependency commands are required manifest data. A reviewer or coauthor should capture the exact command outputs alongside any regenerated final result package.

| field | required command | current Phase 10 note |
|---|---|---|
| Code revision | `git rev-parse HEAD` | Current captured HEAD before this provenance update: `0ac1b6c45fcfedc064e416217447739e975c7596`. Re-run after final Phase 10 commits before packaging. |
| Working-tree state | `git status --short` | Required because the workspace is currently dirty, with many tracked deletions from old paths, untracked current `README.md`/`archive/`/`docs/`/`manuscript/` trees, modified generated outputs, and Phase 10 planning-state edits. |
| Dependency snapshot | `python -m pip freeze` | Required output for reviewer package; save to a timestamped dependency snapshot before final reproduction. |
| Editable install | `python -m pip install -e .` | Required setup command from `README.md` and `pyproject.toml`; current declared core dependencies are `gurobipy` and `numpy`. |
| Test command | `$env:PYTHONPATH='src'; pytest tests -q` | PowerShell equivalent of the reproducibility smoke command. The codebase concern map notes that bare `pytest` may collect archived ad hoc tests, so the active-suite command should be recorded explicitly. |

Environment notes to preserve with the final package:

- `pyproject.toml` requires Python `>=3.10`.
- `gurobipy` is solver/license dependent; MILP diagnostics must record solver status and no-Gurobi behavior.
- Runtime imports used by experiments and figures include packages not declared in core dependencies, notably `pandas` and `matplotlib`; the dependency snapshot must therefore be captured from the actual reproduction environment.
- Generated result files and manuscript display outputs should be tied to the exact post-Phase-10 commit hash, not just to the current dirty working tree.

## Recommended Improvements

These improve reproducibility but are not hard blockers for creating the blocked/pending Phase 10 manifest while Phase 6 and Phase 8 prerequisites are absent.

- Add checksums for final CSV, JSON, Markdown, PDF, PNG, and LaTeX build outputs; non-blocking until the final evidence package exists.
- Export a dependency snapshot file from `python -m pip freeze`; non-blocking for the current blocked manifest, required before reviewer release.
- Record hardware/runtime notes for formal reruns, including CPU, memory, OS, Python version, solver availability, and approximate wall time.
- Export this manifest to a machine-readable JSON or CSV companion once the Phase 6 formal outputs and Phase 8 claim-gate artifacts exist.
- Reconcile the version-control reorganization in a separate maintenance commit so `git status --short` becomes small enough for clean archival.
