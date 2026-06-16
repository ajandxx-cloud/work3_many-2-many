# Phase 10 Reproducibility Guide

**Status:** passed
**Updated:** 2026-06-16
**Repository root:** `C:\Users\39583\Desktop\4_Publication\3.工作3`

This guide records how a reviewer or coauthor can trace and regenerate the Phase 6 formal synthetic evidence package and the Phase 8/9 claim-gated planning artifacts used for manuscript writing. It does not approve any claim beyond the Phase 8 allowed wording.

## Code Revision And Commit References

Current pre-Phase-10-update HEAD during verification: `9b03eb0aee756a5f1141ddad10205b4cce6f0ce6` (`9b03eb0`, `docs(09): refresh manuscript structure after claim gate`).

Relevant prior commits:

| Phase | Commit | Message |
|---|---|---|
| 06-02 | `98f0cb8` | `feat(06-02): run formal main behavioral matrix` |
| 06-03 | `d1a157b` | `feat(06-03): run formal coverage-confounding controls` |
| 06-04 | `8e6c618` | `feat(06-04): run formal robustness diagnostics` |
| 06-05 | `3037cc2` | `docs(06-05): synthesize formal synthetic evidence` |
| 07 | `83309a9` | `docs(07): close case study with synthetic-data limitations` |
| 08 | `8236ca1` | `docs(08): gate claims against formal evidence` |
| 09 | `9b03eb0` | `docs(09): refresh manuscript structure after claim gate` |
| 10 | this commit | `docs(10): pass final reproducibility verification`; exact hash from `git log -1 --oneline` |

## Python Environment Assumptions

- Python: verified with Python 3.12.4.
- Project metadata: `pyproject.toml` requires Python `>=3.10`.
- Core dependencies declared in `pyproject.toml`: `gurobipy`, `numpy`.
- Dev/test dependency: `pytest` via `.[dev]`.
- Experiment and display scripts also rely on runtime packages present in the working environment, including `pandas` and `matplotlib`.
- `gurobipy` is solver/license dependent; MILP outputs are diagnostic and must record solver availability/status.

## Setup And PYTHONPATH

Run from the repository root:

```powershell
python -m pip install -e .
python -m pip install -e ".[dev]"
$env:PYTHONPATH='src;.'
```

For reviewer packaging, capture:

```powershell
git rev-parse HEAD
git status --short
python --version
python -m pip freeze
```

## Active Tests

Required Phase 10 command:

```powershell
$env:PYTHONPATH='src;.'; pytest tests/test_phase06_formal.py tests/test_runner.py tests/test_metrics.py tests/test_variants.py tests/test_phase06_coverage_controls.py tests/test_phase06_robustness.py -q
```

Phase 10 verification result: `100 passed in 5.55s`.

## Regenerating Phase 6 Main Behavioral Matrix

The persisted formal main matrix is already present under `results/formal/phase06/main_behavioral/`. To rerun the full formal package from code, use the Phase 6 runner with the predeclared seed/scale configuration:

```powershell
$env:PYTHONPATH='src;.'; python -m experiments.phase06_formal --results-dir results/formal/phase06/main_behavioral
```

Expected artifacts:

- `results/formal/phase06/main_behavioral/raw_results.csv`
- `results/formal/phase06/main_behavioral/processed_results.csv`
- `results/formal/phase06/main_behavioral/metrics_table.csv`
- `results/formal/phase06/main_behavioral/utility_components.csv`
- `results/formal/phase06/main_behavioral/utility_logs.csv`
- config, seed, run, and validation manifests in the same directory

## Regenerating Phase 6 Coverage Controls

```powershell
$env:PYTHONPATH='src;.'; python -m experiments.phase06_coverage_controls --package all
$env:PYTHONPATH='src;.'; python -m experiments.phase06_coverage_controls --validate --package all
```

Expected artifacts:

- `results/formal/phase06/coverage_controls/matched_coverage/raw_results.csv`
- `results/formal/phase06/coverage_controls/matched_coverage/processed_results.csv`
- `results/formal/phase06/coverage_controls/matched_coverage/validation_report.json`
- `results/formal/phase06/coverage_controls/fixed_accepted_set/raw_results.csv`
- `results/formal/phase06/coverage_controls/fixed_accepted_set/processed_results.csv`
- `results/formal/phase06/coverage_controls/fixed_accepted_set/retained_set_manifest.json`
- `results/formal/phase06/coverage_controls/fixed_accepted_set/validation_report.json`

Matched coverage intentionally carries 15 durable failed FullModel rows. These are not hidden missing rows.

## Regenerating Phase 6 Robustness Diagnostics

```powershell
$env:PYTHONPATH='src;.'; python -m experiments.phase06_robustness --package all
$env:PYTHONPATH='src;.'; python -m experiments.phase06_robustness --validate --package all
```

Expected robustness families:

- utility sensitivity
- walking-radius / meeting-point-density
- fleet-demand stress
- equity type outcomes and individual burden distribution
- algorithm diagnostics

The fixed accepted-set and algorithm diagnostics are diagnostic only. Equity evidence is bounded/exploratory because passenger types are simulation-range constructs.

## Regenerating Phase 6 Closeout Statistics And Manifests

```powershell
$env:PYTHONPATH='src;.'; python -m experiments.formal_statistics --closeout --results-dir results/formal/phase06
$env:PYTHONPATH='src;.'; python -m experiments.formal_statistics --validate --results-dir results/formal/phase06
```

Expected closeout artifacts:

- `.planning/phases/06-formal-synthetic-experiments/06_FORMAL_SYNTHETIC_RESULTS.md`
- `.planning/phases/06-formal-synthetic-experiments/06_FORMAL_RESULT_MANIFEST.md`
- `.planning/phases/06-formal-synthetic-experiments/06_STATISTICAL_SUMMARY.md`
- `.planning/phases/06-formal-synthetic-experiments/06_EVIDENCE_BOUNDARY.md`
- `.planning/phases/06-formal-synthetic-experiments/06-VERIFICATION.md`
- `results/formal/phase06/phase06_result_manifest.json`
- `results/formal/phase06/phase06_verification_report.json`
- generated tables and plots under `results/formal/phase06/tables/` and `results/formal/phase06/plots/`

Phase 10 validation result for the closeout validator: `passed: true`, `missing_required_files: []`, `phase8_blocked_by_conflicts: false`.

## Phase 7 Bounded Synthetic Case Closure

Phase 7 is reproduced by reading and preserving:

- `.planning/phases/07-semi-real-or-beijing-inspired-case-study/07_DATA_AUDIT.md`
- `.planning/phases/07-semi-real-or-beijing-inspired-case-study/07_CASE_STUDY_RESULTS.md`
- `.planning/phases/07-semi-real-or-beijing-inspired-case-study/07_CASE_CLAIM_BOUNDARY.md`
- `.planning/phases/07-semi-real-or-beijing-inspired-case-study/07-VERIFICATION.md`

No new Phase 7 real/semi-real experiment is available. The Beijing-labeled material is a Beijing-inspired synthetic scenario only. `results/beijing_results.csv` is legacy/illustrative provenance, not formal validated evidence.

## Phase 8 Claim Gate Regeneration Process

Phase 8 is a planning artifact generated from Phase 6 formal evidence, Phase 7 boundary files, and the manuscript claim inventory. To regenerate:

```powershell
# Use the GSD phase workflow if rerunning planning artifacts:
# $gsd-execute-phase 8
```

If rerunning manually, read Phase 6/7 artifacts first and recreate:

- `08_CLAIM_INVENTORY.md`
- `08_CLAIM_EVIDENCE_MATRIX.md`
- `08_SUPPORTED_CLAIMS.md`
- `08_UNSUPPORTED_OR_EXPLORATORY_CLAIMS.md`
- `08_REVISED_ABSTRACT_BULLETS.md`
- `08_REVISED_CONCLUSION_BULLETS.md`
- `08_EQUITY_GATE.md`
- `08-VERIFICATION.md`

The claim gate must preserve the strongest allowed result: lower vehicle-km intensity under tested formal synthetic paired conditions, paired with lower served share and rejection/coverage context. It must forbid unconditional superiority, real-Beijing validation, broad first/only novelty, deployment readiness, and universal policy prescriptions.

## Phase 9 Refreshed Planning Regeneration Process

Phase 9 refresh consumes Phase 8 and produces claim-gated manuscript planning artifacts. To regenerate:

```powershell
# Use the GSD phase workflow if rerunning planning artifacts:
# $gsd-execute-phase 9
```

Manual regeneration must recreate:

- `09_CLAIM_GATE_AUDIT.md`
- `09_TR_E_MANUSCRIPT_STRUCTURE.md`
- `09_REVISED_ABSTRACT.md`
- `09_REVISED_INTRODUCTION_PLAN.md`
- `09_EXPERIMENT_SECTION_PLAN.md`
- `09_TABLE_FIGURE_PLAN.md`
- `09_MANAGERIAL_INSIGHT_AND_LIMITATION_PLAN.md`
- `09-REFRESH-SUMMARY.md`
- `09-VERIFICATION.md`

Phase 9 planning artifacts are not manuscript `.tex` edits.

## Known Limitations

- Current evidence is synthetic only and limits external validity.
- Phase 7 did not find real/semi-real OD, road-network, transit-stop/POI, request-time, passenger-preference, or fleet data.
- Equity evidence is bounded/exploratory.
- Fixed accepted-set evidence is diagnostic only.
- Bootstrap CIs exist, but paired hypothesis tests are not implemented.
- ALNS remains heuristic evidence supported by diagnostics, not optimality proof.
- MILP checks are static/scope-limited diagnostics and solver/license dependent.
- Utility parameters are simulation ranges, not empirical calibration.
- Legacy root result files are provenance only unless explicitly regenerated into the Phase 6 formal package.

## Non-Reproducible Or Illustrative-Only Legacy Artifacts

- `results/beijing_results.csv`: Beijing-inspired synthetic legacy rows, not formal case validation.
- `results/synthetic_results.csv` and `results/metrics_table.csv`: legacy/provisional root outputs.
- `results/pareto_gamma_sweep.csv`: post-hoc gamma sensitivity, not a Pareto frontier.
- `results/weight_sensitivity.json`: legacy diagnostic provenance unless rebuilt.
- `results/policy_recommendations.md`: must be rewritten as bounded managerial insight before manuscript use.
- Current manuscript figure outputs under `manuscript/figures/` are display artifacts. Figure scripts are reproducible, but final claim-bearing figure captions must follow Phase 8/9 boundaries.

## Failure-Row Policy

Failed, timeout, infeasible, and blocked runs must remain durable rows with status, error message, runtime, config ID, seed, method, and scenario where applicable. The 15 matched-coverage failed rows are a documented limitation, not an omission.

## Worktree Dirtiness Policy

The broader worktree contains unrelated pre-existing deletions, generated bytecode changes, modified legacy result files, and untracked `README.md`/`archive/`/`docs/`/`manuscript/` trees. Phase 10 does not clean, revert, reorganize, or stage those unrelated paths. Reproducibility reporting records this dirtiness so reviewers do not confuse it with Phase 10 artifacts.

## Exact Reviewer/Coauthor Artifact Set

Minimum package:

- `.planning/PROJECT.md`
- `.planning/REQUIREMENTS.md`
- `.planning/ROADMAP.md`
- `.planning/STATE.md`
- `.planning/CLAIMS_AND_RISKS.md`
- all Phase 6 files listed in `10_RESULT_MANIFEST.md`
- all Phase 7 boundary files listed in `10_RESULT_MANIFEST.md`
- all Phase 8 claim-gate files listed in `10_RESULT_MANIFEST.md`
- all Phase 9 refreshed planning files listed in `10_RESULT_MANIFEST.md`
- `results/formal/phase06/` including raw, processed, table, plot, config, seed, run, validation, manifest, and failure-ledger artifacts
- this Phase 10 reproducibility guide, result manifest, final verification report, and verification report

Optional package:

- `manuscript/` source and figure scripts for later manuscript writing
- dependency snapshot from `python -m pip freeze`
- final post-Phase-10 `git status --short`
