# Technology Stack

**Analysis Date:** 2026-06-14

## Languages

**Primary:**
- Python >=3.10 - Core package, experiment orchestration, analysis scripts, tests, and figure generation. Declared in `pyproject.toml`; package code lives in `src/drt/`, experiments in `experiments/`, analysis in `analysis/`, and tests in `tests/`.

**Secondary:**
- LaTeX - Manuscript source in `manuscript/main.tex`, `manuscript/sections/*.tex`, `manuscript/references.bib`, `manuscript/cover_letter.tex`, and `manuscript/response_to_reviewers.tex`.
- Markdown / plain text - Project documentation in `README.md`, `CLAUDE.md`, and `docs/`.
- CSV / JSON - Local result artifacts in `results/*.csv`, `results/*.json`, and archived snapshots under `archive/pre_revision_results/`.

## Runtime

**Environment:**
- Python 3.12.4 observed in the active shell.
- Project supports Python >=3.10 via `pyproject.toml`.
- Gurobi runtime is required only for exact MILP paths. Imports are deferred in `src/drt/milp.py` and `experiments/milp_gap.py`, so heuristic and analysis modules can import without a Gurobi installation.

**Package Manager:**
- pip 26.0.1 observed in the active shell.
- Install pattern from `README.md`: `pip install -e .` for the package and `pip install -e ".[dev]"` for tests.
- Lockfile: missing. No `requirements.txt`, `poetry.lock`, `uv.lock`, `Pipfile.lock`, or `environment.yml` detected.

## Frameworks

**Core:**
- setuptools >=42 - Package build backend declared in `pyproject.toml`.
- gurobipy, unpinned - Exact static MILP solver client used by `src/drt/milp.py` and benchmarked by `experiments/milp_gap.py`.
- numpy, unpinned - Numeric statistics and array operations used by `experiments/metrics.py` and figure scripts under `manuscript/figures/scripts/`.

**Testing:**
- pytest, unpinned - Declared in `pyproject.toml` under `[project.optional-dependencies].dev`; test suite lives in `tests/` plus `analysis/test_sensitivity.py`.
- pytest-benchmark, unpinned - Declared as a dev optional dependency in `pyproject.toml`; timing benchmarks appear in tests such as `tests/test_alns.py` and `tests/test_insertion.py`.

**Build/Dev:**
- setuptools package discovery - `pyproject.toml` uses `[tool.setuptools.packages.find]` with `where = ["src"]`.
- pandas, undeclared runtime import - Used by `run_experiments.py`, `experiments/runner.py`, `tests/test_runner.py`, and figure scripts such as `manuscript/figures/scripts/fig04_baseline_comparison.py`.
- matplotlib, undeclared runtime import - Used for publication figure generation under `manuscript/figures/scripts/`; scripts set the non-interactive `Agg` backend before writing PDF/PNG outputs.
- bibtex / pdflatex toolchain - Manuscript build instructions in `README.md` require `pdflatex`, `bibtex`, and the `elsarticle.cls` LaTeX class.

## Key Dependencies

**Critical:**
- `gurobipy` - Required by exact optimization in `src/drt/milp.py`; `DRTModel.build()` creates the Gurobi model and `DRTModel.solve()` maps Gurobi statuses to project-level result statuses.
- `numpy` - Required by metrics computation in `experiments/metrics.py`, including mean, percentile, clipping, sorting, and Gini calculations.
- `pandas` - Required by experiment aggregation and validation in `experiments/runner.py` and `run_experiments.py`; also required by figure scripts that read `results/*.csv`.
- `matplotlib` - Required by publication figure generation scripts in `manuscript/figures/scripts/`.

**Infrastructure:**
- Python standard library `csv` - Writes experiment and analysis tables in `experiments/runner.py`, `analysis/sensitivity.py`, `analysis/equity.py`, `experiments/matched_coverage.py`, `experiments/endogenous_matched_coverage.py`, and `experiments/pareto_sweep.py`.
- Python standard library `json` - Writes solver and sensitivity outputs in `src/drt/milp.py`, `experiments/milp_gap.py`, and `experiments/weight_sensitivity.py`.
- Python standard library `concurrent.futures` - Enforces per-variant execution timeout in `experiments/runner.py`.
- Python standard library `dataclasses` - Defines domain structures in `src/drt/types.py`, `experiments/scenarios.py`, and `experiments/metrics.py`.

## Configuration

**Environment:**
- Runtime configuration is code-based, not environment-based. No `.env` file was detected, and active Python code does not read `os.environ`, `os.getenv`, or `dotenv`.
- Shared experiment constants live in `experiments/config.py`: seeds, request scales, vehicle counts, walking radii, rolling-horizon window, ALNS iterations, cost weights, vehicle capacity, max ride time, and Beijing scenario scale.
- Gurobi parameters are set in code in `src/drt/milp.py`: `TimeLimit`, `MIPGap`, and `OutputFlag`.

**Build:**
- `pyproject.toml` is the package and build configuration source.
- No lint, type-check, formatter, tox, nox, or pytest config file was detected at repo root.
- No Dockerfile, docker-compose file, pre-commit config, or CI workflow file was detected.

## Platform Requirements

**Development:**
- Python >=3.10.
- Install editable package with `pip install -e .`.
- Install test dependencies with `pip install -e ".[dev]"`.
- Install practical undeclared dependencies before running experiment reporting or figures: `pandas` and `matplotlib`.
- Install Gurobi plus a valid local Gurobi license before using `src/drt/milp.py` exact solver paths or `experiments/milp_gap.py`.
- Run experiments from project root with `python run_experiments.py`; it writes to `results/` and reads back `results/metrics_table.csv`.
- Run figure scripts from `manuscript/`; they use relative paths such as `results/metrics_table.csv` and output under `manuscript/figures/`.

**Production:**
- Not applicable. This repo is a local research/optimization and manuscript project, not a deployed service.
- Durable outputs are committed local artifacts under `results/`, `manuscript/figures/`, and `manuscript/main.pdf`.

---

*Stack analysis: 2026-06-14*
