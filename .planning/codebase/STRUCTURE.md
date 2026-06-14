# Codebase Structure

**Analysis Date:** 2026-06-14

## Directory Layout

```text
3.工作3/
├── README.md                         # Project overview, run instructions, known repository notes
├── CLAUDE.md                         # Project instructions for coding agents
├── pyproject.toml                    # Python package metadata for package `drt`
├── run_experiments.py                # Root entry point for the full experiment suite
├── src/
│   ├── drt/                          # Core DRT package
│   │   ├── __init__.py               # Public re-exports for common package API
│   │   ├── types.py                  # Domain dataclasses and passenger type constants
│   │   ├── candidate.py              # Top-k meeting point candidate generation
│   │   ├── choice.py                 # MNL utility and acceptance probability
│   │   ├── feasibility.py            # Route insertion feasibility constraints
│   │   ├── insertion.py              # Best feasible insertion evaluator
│   │   ├── alns.py                   # ALNS operators and rolling-horizon controller
│   │   └── milp.py                   # Static Gurobi MILP baseline
│   └── drt.egg-info/                 # Editable-install package metadata
├── experiments/
│   ├── __init__.py                   # Experiment package marker
│   ├── config.py                     # Shared constants, scales, seeds, radii, weights
│   ├── scenarios.py                  # Synthetic and Beijing scenario generation
│   ├── variants.py                   # Baselines, ablations, FullModel, variant registry
│   ├── metrics.py                    # Simulation output dataclasses and metric computation
│   ├── runner.py                     # Main experiment matrix runner and CSV writers
│   ├── weight_sensitivity.py         # Weight sensitivity experiment
│   ├── pareto_sweep.py               # Social-welfare Pareto/gamma sweep
│   ├── milp_gap.py                   # MILP-vs-heuristic gap experiment
│   ├── matched_coverage.py           # Matched coverage experiment
│   └── endogenous_matched_coverage.py # Endogenous matched coverage experiment
├── analysis/
│   ├── __init__.py                   # Analysis package marker
│   ├── sensitivity.py                # Walking tolerance and fleet-size sweeps
│   ├── equity.py                     # Passenger-type equity table generation
│   ├── policy.py                     # Policy recommendation generation from result CSVs
│   └── test_sensitivity.py           # Tests for analysis sensitivity outputs
├── tests/                            # Pytest suite for core, experiments, and runner behavior
├── results/                          # Generated CSV/JSON/Markdown experiment outputs
├── manuscript/                       # LaTeX manuscript, compiled PDF, figures, and figure scripts
├── docs/                             # Human-written notes and public dataset notes
├── archive/                          # Historical drafts, old results, debug scripts, logs, adhoc tests
└── .planning/
    └── codebase/                     # GSD codebase maps
```

## Directory Purposes

**`src/drt/`:**
- Purpose: Core reusable DRT algorithm library.
- Contains: Domain dataclasses, candidate generation, MNL choice, feasibility checking, insertion evaluation, ALNS/rolling-horizon heuristic, and MILP baseline.
- Key files: `src/drt/types.py`, `src/drt/candidate.py`, `src/drt/choice.py`, `src/drt/feasibility.py`, `src/drt/insertion.py`, `src/drt/alns.py`, `src/drt/milp.py`, `src/drt/__init__.py`.
- Use this directory for algorithmic behavior that should be independent of a specific experiment or result table.

**`experiments/`:**
- Purpose: Compose core algorithms into repeatable research experiments.
- Contains: Shared constants, scenario generators, model variant classes, metrics, full runner, and focused experiment scripts.
- Key files: `experiments/config.py`, `experiments/scenarios.py`, `experiments/variants.py`, `experiments/metrics.py`, `experiments/runner.py`.
- Use this directory for new simulation campaigns, new baselines/ablations, and new output-producing experiment scripts.

**`analysis/`:**
- Purpose: Post-hoc analysis and policy synthesis over experiment outputs.
- Contains: Sensitivity sweeps, equity analysis, policy recommendation generation, and analysis-specific tests.
- Key files: `analysis/sensitivity.py`, `analysis/equity.py`, `analysis/policy.py`, `analysis/test_sensitivity.py`.
- Use this directory for code that reads generated outputs or runs narrowly scoped analysis variants.

**`tests/`:**
- Purpose: Pytest coverage for core algorithms, experiment composition, scenario generation, metrics, and runner output.
- Contains: One test module per important source area.
- Key files: `tests/test_candidate.py`, `tests/test_feasibility.py`, `tests/test_insertion.py`, `tests/test_alns.py`, `tests/test_milp.py`, `tests/test_scenarios.py`, `tests/test_variants.py`, `tests/test_metrics.py`, `tests/test_runner.py`.
- Add tests here for production source under `src/drt/` and `experiments/`; analysis currently has a colocated test file at `analysis/test_sensitivity.py`.

**`results/`:**
- Purpose: Generated experiment and analysis outputs.
- Contains: CSV, JSON, TXT, and Markdown results such as `results/synthetic_results.csv`, `results/beijing_results.csv`, `results/metrics_table.csv`, `results/sensitivity_walk.csv`, `results/equity_table.csv`, `results/policy_recommendations.md`.
- Key files: Result artifacts, not source-of-truth code.
- Treat as generated data; source changes should happen in `experiments/` or `analysis/`.

**`manuscript/`:**
- Purpose: Current publication manuscript and generated figures.
- Contains: LaTeX files, bibliography, response/cover letter, compiled PDF, section files, figures, and figure-generation scripts.
- Key files: `manuscript/main.tex`, `manuscript/references.bib`, `manuscript/sections/`, `manuscript/figures/`, `manuscript/figures/scripts/`.
- Add paper text under `manuscript/sections/`; add figure-only scripts under `manuscript/figures/scripts/`.

**`docs/`:**
- Purpose: Human-written project notes and dataset notes.
- Contains: Markdown/TXT documentation, including Chinese-language notes.
- Key files: `docs/开题报告-3.30.md`, `docs/工作3讨论-6.14.md`, `docs/工作3公开数据集.txt`.
- Use for explanatory documents that are not executable code or manuscript source.

**`archive/`:**
- Purpose: Historical or superseded project material kept outside active workflows.
- Contains: Old model draft LaTeX, prior result snapshots, debug scripts, adhoc tests, output logs, and old paper text.
- Key files: `archive/model_draft/`, `archive/pre_revision_results/`, `archive/debug_scripts/`, `archive/adhoc_tests/`, `archive/output_logs/`, `archive/paper_full_v3.txt`.
- Do not add new active code here; use it only for reference or intentionally archived material.

**`.planning/codebase/`:**
- Purpose: GSD-generated architecture, structure, stack, testing, and concern maps.
- Contains: Markdown documents consumed by planning/execution commands.
- Key files: `.planning/codebase/ARCHITECTURE.md`, `.planning/codebase/STRUCTURE.md`.

## Key File Locations

**Entry Points:**
- `run_experiments.py`: Root script for running the full experiment matrix and printing summary checks.
- `experiments/runner.py`: Importable and executable experiment runner; owns `run_all_experiments()`.
- `analysis/sensitivity.py`: Entry point for walking-tolerance and fleet-size sensitivity sweeps.
- `analysis/equity.py`: Entry point for passenger-type equity analysis.
- `analysis/policy.py`: Entry point for policy recommendation generation from result CSVs.
- `experiments/weight_sensitivity.py`: Focused weight sensitivity runner.
- `experiments/pareto_sweep.py`: Focused Pareto/social-welfare sweep runner.
- `experiments/milp_gap.py`: Focused MILP benchmark/gap runner.
- `experiments/matched_coverage.py`: Focused matched coverage runner.
- `experiments/endogenous_matched_coverage.py`: Focused endogenous coverage runner.

**Configuration:**
- `pyproject.toml`: Package configuration, Python requirement, dependencies, optional dev dependencies, and `src` package discovery.
- `experiments/config.py`: Research experiment constants: `SEEDS`, `SCALES`, `VEHICLE_COUNTS`, `K_TOP`, `RHO_P`, `RHO_D`, `H_WINDOW`, `DELTA`, `ALNS_ITERATIONS`, `ALPHA_WEIGHTS`, `VEHICLE_CAPACITY`, `MAX_RIDE_TIME`, `MAX_ROUTE_DURATION`, `BEIJING_SCALE`.
- `.gitignore`: Git ignore rules.
- `CLAUDE.md`: Coding-agent project instructions.

**Core Logic:**
- `src/drt/types.py`: Domain dataclasses and passenger type presets.
- `src/drt/candidate.py`: `generate_candidates()` and Euclidean distance helper.
- `src/drt/choice.py`: `mnl_utility()` and `accept_probability()`.
- `src/drt/feasibility.py`: `check_feasibility()` route insertion constraint checker.
- `src/drt/insertion.py`: `InsertionResult`, `_route_distance()`, and `evaluate_insertion()`.
- `src/drt/alns.py`: `ALNSState`, destroy/repair operators, `RollingHorizon`, `benchmark()`.
- `src/drt/milp.py`: `DRTModel` exact optimization baseline.
- `experiments/scenarios.py`: `Scenario`, `generate_synthetic()`, `generate_beijing()`.
- `experiments/variants.py`: `BaseVariant`, concrete variants, and `ALL_VARIANTS`.
- `experiments/metrics.py`: `PassengerRecord`, `SimulationResult`, `MetricsResult`, `compute_metrics()`, `compute_social_welfare()`.

**Output Writers:**
- `experiments/runner.py`: Writes `results/synthetic_results.csv`, `results/beijing_results.csv`, and `results/metrics_table.csv`.
- `src/drt/milp.py`: `DRTModel.write_benchmark()` writes `results/milp_benchmark.json` by default.
- `analysis/sensitivity.py`: Writes `results/sensitivity_walk.csv` and `results/sensitivity_fleet.csv`.
- `analysis/equity.py`: Writes `results/equity_table.csv`.
- `analysis/policy.py`: Writes `results/policy_recommendations.md`.
- `experiments/weight_sensitivity.py`: Writes `results/weight_sensitivity.json`.
- `experiments/pareto_sweep.py`: Writes `results/pareto_gamma_sweep.csv`.
- `experiments/matched_coverage.py`: Writes `results/matched_coverage.csv`.
- `experiments/endogenous_matched_coverage.py`: Writes `results/endogenous_matched_coverage.csv`.

**Testing:**
- `tests/test_candidate.py`: Candidate filtering, sorting, and boundary behavior.
- `tests/test_feasibility.py`: Feasibility reason codes and constraint behavior.
- `tests/test_insertion.py`: Best insertion, infeasible insertions, cost components, timing benchmark.
- `tests/test_alns.py`: ALNS operators, rolling-horizon output keys, timing benchmark.
- `tests/test_milp.py`: Gurobi-guarded MILP behavior and solve metadata.
- `tests/test_scenarios.py`: Synthetic and Beijing scenario invariants.
- `tests/test_variants.py`: Variant registry and variant output behavior.
- `tests/test_metrics.py`: Metric dataclass fields and aggregate metric edge cases.
- `tests/test_runner.py`: Runner smoke output and CSV schema checks.
- `analysis/test_sensitivity.py`: Sensitivity sweep row counts, keys, metrics, and CSV writes.

**Publication:**
- `manuscript/main.tex`: Master LaTeX document.
- `manuscript/sections/`: Paper sections.
- `manuscript/figures/`: Generated PDF/PNG figures.
- `manuscript/figures/scripts/`: Figure generation scripts.
- `manuscript/references.bib`: Bibliography.
- `manuscript/main.pdf`: Compiled output.

## Naming Conventions

**Files:**
- Use lowercase snake_case for Python modules: `src/drt/feasibility.py`, `experiments/weight_sensitivity.py`, `analysis/policy.py`.
- Use `test_*.py` for pytest modules: `tests/test_runner.py`, `analysis/test_sensitivity.py`.
- Use descriptive result filenames keyed by experiment topic: `results/synthetic_results.csv`, `results/milp_gap.json`, `results/policy_recommendations.md`.
- Use figure numbering for manuscript figures and scripts: `manuscript/figures/fig03_algorithm.pdf`, `manuscript/figures/scripts/fig03_algorithm.py`.
- Use uppercase generated GSD map names: `.planning/codebase/ARCHITECTURE.md`, `.planning/codebase/STRUCTURE.md`.

**Directories:**
- Use top-level functional areas: `src/`, `experiments/`, `analysis/`, `tests/`, `results/`, `manuscript/`, `docs/`, `archive/`.
- Keep the installable Python package under `src/drt/` because `pyproject.toml` uses `where = ["src"]`.
- Keep active tests in `tests/` except analysis-specific sensitivity tests currently colocated as `analysis/test_sensitivity.py`.

**Classes:**
- Use PascalCase for dataclasses and model classes: `Request`, `Vehicle`, `MeetingPoint`, `Scenario`, `SimulationResult`, `FullModel`, `RollingHorizon`, `DRTModel`.
- Use `Base*` for abstract variant bases: `BaseVariant`.
- Use descriptive variant names matching output rows: `DoorToDoor`, `DoorToDoorCapped`, `SingleSidedPickup`, `BidirectionalNoChoice`, `FullModel`, `AblationNoRollingHorizon`, `AblationNoChoice`.

**Functions:**
- Use lowercase snake_case: `generate_candidates()`, `check_feasibility()`, `evaluate_insertion()`, `generate_synthetic()`, `run_all_experiments()`, `compute_metrics()`.
- Prefix private helpers with `_`: `_route_distance()`, `_mnl_filter_requests()`, `_make_row()`, `_write_metrics_table()`.
- Use direct verb phrases for script-level functions: `run_sweep()`, `run_equity_analysis()`, `generate_policy_recommendations()`.

**Constants:**
- Use uppercase snake_case for configuration and registries: `SEEDS`, `SCALES`, `VEHICLE_COUNTS`, `RHO_P`, `RHO_D`, `H_WINDOW`, `DELTA`, `ALL_VARIANTS`.
- Keep experiment constants in `experiments/config.py`; do not duplicate them in runner or analysis files.

## Where to Add New Code

**New Core Algorithm Feature:**
- Primary code: `src/drt/`
- Tests: `tests/`
- Add shared data fields to `src/drt/types.py` first when the feature changes the domain contract.
- Add reusable primitive logic to `src/drt/candidate.py`, `src/drt/choice.py`, `src/drt/feasibility.py`, or `src/drt/insertion.py`.
- Add heuristic solver behavior to `src/drt/alns.py`.
- Add exact optimization behavior to `src/drt/milp.py`.

**New Experiment Variant:**
- Primary code: `experiments/variants.py`
- Tests: `tests/test_variants.py`
- Register the variant instance in `ALL_VARIANTS` in `experiments/variants.py`.
- Ensure `variant.name` is unique because the module-level assertion checks uniqueness.
- Reuse `BaseVariant.run()` and implement `_solve(self, scenario: Scenario) -> ALNSState`.

**New Scenario Generator:**
- Primary code: `experiments/scenarios.py`
- Tests: `tests/test_scenarios.py`
- Return the existing `Scenario` dataclass with `requests`, `vehicles`, `meeting_points`, `area_km`, and `name`.
- Enforce practical request caps consistently with `_MAX_REQUESTS`.

**New Metric:**
- Primary code: `experiments/metrics.py`
- Runner schema: `experiments/runner.py`
- Tests: `tests/test_metrics.py`, `tests/test_runner.py`
- Add the field to `MetricsResult`, compute it in `compute_metrics()`, include it in `_RAW_COLS` and `_METRIC_COLS`, and update CSV row construction in `_make_row()`.

**New Full Experiment Script:**
- Primary code: `experiments/`
- Tests: `tests/` when output schema or behavior matters.
- Use `experiments.config`, `experiments.scenarios`, `experiments.variants`, and `experiments.metrics` rather than reimplementing loops.
- Write generated outputs under `results/` with stable CSV/JSON field names.

**New Post-Hoc Analysis:**
- Primary code: `analysis/`
- Tests: `analysis/test_*.py` or `tests/`, following the current sensitivity pattern.
- Read source result files from `results/`.
- Write derived outputs back to `results/`.
- Keep hardcoded publication result readers in `analysis/`, not `src/drt/`.

**New Figure Script:**
- Implementation: `manuscript/figures/scripts/`
- Outputs: `manuscript/figures/`
- Inputs: Prefer stable files in `results/`.
- Keep paper text changes in `manuscript/sections/`.

**Utilities:**
- Shared algorithm helpers: `src/drt/`
- Experiment-only helpers: `experiments/`
- Analysis-only helpers: `analysis/`
- Do not add active helpers to `archive/`.

## Special Directories

**`src/drt.egg-info/`:**
- Purpose: Package metadata from editable install.
- Generated: Yes.
- Committed: Present in the workspace.
- Avoid editing manually; regenerate through packaging tools when needed.

**`results/`:**
- Purpose: Generated experiment outputs consumed by analysis and publication workflows.
- Generated: Yes.
- Committed: Present in the workspace.
- Treat contents as artifacts; update through scripts rather than manual editing when possible.

**`manuscript/figures/`:**
- Purpose: Generated publication figures in PDF/PNG form.
- Generated: Yes.
- Committed: Present in the workspace.
- Update via scripts in `manuscript/figures/scripts/`.

**`archive/`:**
- Purpose: Historical material not in active workflows.
- Generated: Mixed.
- Committed: Present in the workspace.
- Use for reference only; new active code belongs in `src/drt/`, `experiments/`, `analysis/`, or `tests/`.

**`.planning/`:**
- Purpose: GSD workflow state and generated planning/codebase documents.
- Generated: Yes.
- Committed: Workspace-managed.
- Do not use for runtime application code.

---

*Structure analysis: 2026-06-14*
