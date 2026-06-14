# Coding Conventions

**Analysis Date:** 2026-06-14

## Naming Patterns

**Files:**
- Use lowercase `snake_case.py` for Python modules, as in `src/drt/candidate.py`, `src/drt/feasibility.py`, `experiments/weight_sensitivity.py`, and `analysis/test_sensitivity.py`.
- Test files use pytest's `test_*.py` naming pattern, as in `tests/test_candidate.py`, `tests/test_runner.py`, and `analysis/test_sensitivity.py`.
- Package initialization files are minimal `__init__.py` files, as in `src/drt/__init__.py`, `experiments/__init__.py`, and `analysis/__init__.py`.

**Functions:**
- Public functions use lowercase `snake_case` verbs or verb phrases, as in `generate_candidates()` in `src/drt/candidate.py`, `check_feasibility()` in `src/drt/feasibility.py`, `evaluate_insertion()` in `src/drt/insertion.py`, `compute_metrics()` in `experiments/metrics.py`, and `run_all_experiments()` in `experiments/runner.py`.
- Internal helpers are prefixed with `_`, as in `_route_distance()` in `src/drt/insertion.py`, `_get_assigned_ids()` in `src/drt/alns.py`, `_make_error_row()` in `experiments/runner.py`, and `_normal_clamp()` in `experiments/scenarios.py`.
- Test helper factories use short `make_*` or `_make_*` names, as in `make_request()` in `tests/test_insertion.py`, `make_vehicle()` in `tests/test_feasibility.py`, and `_make_small_instance()` in `tests/test_milp.py`.

**Variables:**
- Use domain-specific identifiers that match DRT notation where helpful: `rho_p`, `rho_d`, `k_top`, `pos_p`, `pos_d`, `mp_p`, and `mp_d` appear in `src/drt/insertion.py`, `src/drt/feasibility.py`, and `experiments/config.py`.
- Use `snake_case` for ordinary variables and records, as in `pickup_candidates` in `src/drt/insertion.py`, `acceptance_rate` in `experiments/metrics.py`, and `synthetic_rows` in `experiments/runner.py`.
- Use all-caps constants for shared experiment parameters, as in `RANDOM_SEED`, `K_TOP`, `RHO_P`, `RHO_D`, `H_WINDOW`, and `ALPHA_WEIGHTS` in `experiments/config.py`.
- Use leading underscores for module-level private constants, as in `_VARIANT_TIMEOUT_S`, `_RAW_COLS`, and `_METRIC_COLS` in `experiments/runner.py`, `_MAX_REQUESTS` in `experiments/scenarios.py`, and `_COST_WEIGHTS` in `experiments/variants.py`.

**Types:**
- Data containers use PascalCase dataclasses, as in `Request`, `Vehicle`, `MeetingPoint`, `Bundle`, `Route`, and `PassengerType` in `src/drt/types.py`.
- Result objects use `*Result` suffixes, as in `InsertionResult` in `src/drt/insertion.py`, `SimulationResult` and `MetricsResult` in `experiments/metrics.py`.
- Variant classes use PascalCase names matching experiment labels, as in `DoorToDoor`, `FullModel`, and `AblationNoChoice` in `experiments/variants.py`.

## Code Style

**Formatting:**
- No formatter configuration is detected in `pyproject.toml`; no `.prettierrc`, `ruff.toml`, `black`, or `isort` config files are present in the repository root.
- Use 4-space indentation and conventional PEP 8 spacing, matching `src/drt/candidate.py`, `src/drt/insertion.py`, and `experiments/metrics.py`.
- Prefer explicit line breaks for long function signatures and long expressions, as in `check_feasibility()` in `src/drt/feasibility.py`, `RollingHorizon.__init__()` in `src/drt/alns.py`, and `run_all_experiments()` in `experiments/runner.py`.
- Use module docstrings at the top of active source and test modules to state purpose and algorithm phase, as in `src/drt/milp.py`, `src/drt/alns.py`, `tests/test_alns.py`, and `tests/test_runner.py`.
- Most active modules include `from __future__ import annotations`; keep using it in new library, experiment, analysis, and test modules such as `src/drt/insertion.py`, `experiments/variants.py`, and `tests/test_insertion.py`.

**Linting:**
- No linting configuration is detected in `pyproject.toml`; no `.eslintrc*`, `eslint.config.*`, `biome.json`, `ruff.toml`, `.ruff.toml`, `mypy.ini`, or `pyrightconfig.json` is present.
- Follow the style already used in `src/drt/` and `experiments/`: type hints on public APIs, dataclasses for structured records, descriptive assertion messages in tests, and explicit helper functions for repeated setup.

## Import Organization

**Order:**
1. Future imports first, as in `from __future__ import annotations` in `src/drt/alns.py`, `experiments/runner.py`, and `tests/test_runner.py`.
2. Standard library imports next, as in `math`, `random`, `time`, `os`, `sys`, `csv`, and `concurrent.futures` in `src/drt/alns.py` and `experiments/runner.py`.
3. Third-party imports after standard library imports, as in `numpy as np` in `experiments/metrics.py`, `pandas as pd` in `experiments/runner.py`, and `pytest` in `tests/test_runner.py`.
4. Local imports last, as in `from drt.types import ...` in `src/drt/insertion.py` and `tests/test_candidate.py`, and `from experiments.metrics import ...` in `experiments/variants.py` and `tests/test_metrics.py`.

**Path Aliases:**
- The installed package root is `src/drt`, configured by `pyproject.toml`; imports from package code commonly use `drt.*`, as in `src/drt/insertion.py`, `src/drt/alns.py`, and `tests/test_insertion.py`.
- Some experiment modules import through `src.drt.*`, as in `experiments/scenarios.py` and `experiments/variants.py`; match the surrounding file when editing those modules.
- Some tests manually add paths with `sys.path.insert`, as in `tests/test_alns.py`, `tests/test_milp.py`, `tests/test_metrics.py`, and `tests/test_scenarios.py`; prefer relying on editable install (`pip install -e .`) for new tests unless a local file already uses this pattern.

## Error Handling

**Patterns:**
- Use typed return values for expected business outcomes, as in `check_feasibility()` returning `(False, "capacity")` or `(True, "")` in `src/drt/feasibility.py`.
- Use `None` for expected "no feasible solution" outcomes, as in `evaluate_insertion()` returning `InsertionResult | None` in `src/drt/insertion.py`.
- Raise `ValueError` for invalid input constraints, as in the request-count cap in `generate_synthetic()` and `generate_beijing()` in `experiments/scenarios.py`.
- Raise dependency-specific errors at the boundary where optional tools are required, as in deferred `gurobipy` imports raising `ImportError` in `src/drt/milp.py`.
- Use explicit runtime errors for invalid call order, as in `DRTModel.write_benchmark()` raising `RuntimeError` when `solve()` has not been called in `src/drt/milp.py`.
- Long-running experiment orchestration catches timeout and generic exceptions, prints diagnostics to stderr, and returns zero-filled result rows in `experiments/runner.py`.
- Use warnings for recoverable data inconsistencies that should be visible to callers, as in `warnings.warn(..., RuntimeWarning)` in `experiments/variants.py`.

## Logging

**Framework:** `print` / `stderr`

**Patterns:**
- Experiment scripts report progress with `print()`, as in `experiments/runner.py` and `run_experiments.py`.
- Error paths in experiment execution write to `sys.stderr`, as in `_run_variant_with_timeout()` in `experiments/runner.py`.
- No structured logging framework is configured; keep new progress output concise and reserve verbose diagnostics for experiment runners or command-line scripts such as `run_experiments.py`.

## Comments

**When to Comment:**
- Use comments to connect implementation to algorithm labels, mathematical constraints, or threat mitigations, as in `src/drt/feasibility.py`, `src/drt/milp.py`, `experiments/scenarios.py`, and `experiments/variants.py`.
- Use section dividers sparingly for large modules with clear phases, as in `src/drt/alns.py`, `src/drt/milp.py`, and `tests/test_feasibility.py`.
- Avoid comments that repeat simple code. Prefer comments that explain model assumptions, units, complexity, or why a guard exists, as in `experiments/metrics.py` and `experiments/scenarios.py`.

**JSDoc/TSDoc:**
- Not applicable; this is a Python codebase.
- Use Python docstrings instead. Module, class, and public-function docstrings are common in `src/drt/types.py`, `src/drt/choice.py`, `experiments/metrics.py`, and `tests/test_runner.py`.
- Use NumPy-style sections for algorithm-facing public functions when parameters and returns need explanation, as in `src/drt/candidate.py`, `src/drt/feasibility.py`, `src/drt/milp.py`, and `experiments/scenarios.py`.

## Function Design

**Size:** Keep small mathematical helpers focused, as in `euclidean()` in `src/drt/candidate.py`, `_travel_time()` in `src/drt/feasibility.py`, and `_gini()` in `experiments/metrics.py`. Larger orchestration functions are present in `src/drt/alns.py`, `src/drt/milp.py`, and `experiments/runner.py`; when adding behavior there, prefer extracting private helpers rather than extending already large methods.

**Parameters:** Use explicit typed parameters for public APIs, as in `generate_synthetic(n_requests: int, n_vehicles: int, seed: int)` in `experiments/scenarios.py`, `evaluate_insertion(...)` in `src/drt/insertion.py`, and `DRTModel.__init__(...)` in `src/drt/milp.py`. Defaults are common for algorithm knobs such as `travel_speed`, `cost_weights`, `time_limit`, and `mip_gap`.

**Return Values:** Return dataclasses for structured domain records, as in `Scenario` from `experiments/scenarios.py`, `MetricsResult` from `experiments/metrics.py`, and `InsertionResult` from `src/drt/insertion.py`. Return plain dictionaries for dynamic run summaries and benchmark outputs, as in `RollingHorizon.reoptimize()` and `benchmark()` in `src/drt/alns.py`, and `DRTModel.solve()` in `src/drt/milp.py`.

## Module Design

**Exports:** Public modules expose a small set of domain functions/classes, such as `generate_candidates()` in `src/drt/candidate.py`, `check_feasibility()` in `src/drt/feasibility.py`, `DRTModel` in `src/drt/milp.py`, `compute_metrics()` in `experiments/metrics.py`, and `run_all_experiments()` in `experiments/runner.py`.

**Barrel Files:** `src/drt/__init__.py` re-exports core dataclasses and choice functions from `src/drt/types.py` and `src/drt/choice.py`. No comparable barrel file is used for `experiments/` or `analysis/`.

---

*Convention analysis: 2026-06-14*
