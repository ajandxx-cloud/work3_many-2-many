# Coding Conventions

**Analysis Date:** 2026-06-16

## Naming Patterns

**Files:**
- Use lowercase `snake_case.py` for Python modules, as in `src/drt/candidate.py`, `src/drt/feasibility.py`, `experiments/phase06_formal.py`, `experiments/phase06_coverage_controls.py`, and `analysis/test_sensitivity.py`.
- Test files use pytest's `test_*.py` naming pattern, as in `tests/test_candidate.py`, `tests/test_runner.py`, `tests/test_phase06_formal.py`, and `analysis/test_sensitivity.py`.
- Package initialization files stay minimal, as in `src/drt/__init__.py`, `experiments/__init__.py`, and `analysis/__init__.py`.
- Archived one-off scripts also use `test_*.py` names under `archive/adhoc_tests/`; do not copy this placement for active tests because default pytest discovery reaches those files.

**Functions:**
- Public functions use lowercase `snake_case` verbs or verb phrases, as in `generate_candidates()` in `src/drt/candidate.py`, `check_feasibility()` in `src/drt/feasibility.py`, `evaluate_insertion()` in `src/drt/insertion.py`, `compute_metrics()` in `experiments/metrics.py`, and `run_all_experiments()` in `experiments/runner.py`.
- Internal helpers use a leading underscore, as in `_binary_logit_probability()` in `src/drt/choice.py`, `_route_distance()` in `src/drt/insertion.py`, `_make_error_row()` in `experiments/runner.py`, `_validate_formal_scales()` in `experiments/phase06_formal.py`, and `_check_columns()` in `experiments/phase06_robustness.py`.
- Test helper factories use `make_*` or `_make_*`, as in `make_offer()` in `tests/test_choice.py`, `make_record()` in `tests/test_metrics.py`, `_make_small_instance()` in `tests/test_milp.py`, and `_raw_row()` in `tests/test_phase06_formal.py`.
- Script entry points use `main()` and `if __name__ == "__main__"` or `raise SystemExit(main())`, as in `experiments/runner.py`, `experiments/phase06_formal.py`, `experiments/phase06_robustness.py`, and `run_experiments.py`.

**Variables:**
- Use `snake_case` for ordinary variables and row dictionaries, as in `pickup_candidates` in `tests/test_milp.py`, `synthetic_rows` and `utility_rows` in `experiments/runner.py`, and `acceptance_probability` in `src/drt/choice.py`.
- Use domain names that match DRT notation where helpful: `rho_p`, `rho_d`, `k_top`, `pos_p`, `pos_d`, `pickup_mp`, and `dropoff_mp` appear in `src/drt/candidate.py`, `src/drt/insertion.py`, `src/drt/feasibility.py`, and `src/drt/types.py`.
- Use all-caps constants for shared experiment parameters and registries, as in `SCALES`, `SEEDS`, `VEHICLE_COUNTS`, `RHO_P`, `RHO_D`, and `ALPHA_WEIGHTS` in `experiments/config.py`.
- Use leading underscores for module-private constants and column schemas, as in `_VARIANT_TIMEOUT_S`, `_RAW_COLS`, `_METRIC_COLS`, and `_UTILITY_COLS` in `experiments/runner.py`.
- Use explicit status strings for lifecycle state: `served`, `choice_rejected`, `feasibility_rejected`, `completed`, `timeout`, `failed`, `passed`, and `no_gurobi` appear across `src/drt/choice.py`, `experiments/runner.py`, `experiments/milp_gap.py`, and tests in `tests/`.

**Types:**
- Data containers use PascalCase dataclasses, as in `Request`, `Vehicle`, `MeetingPoint`, `Bundle`, `OfferAttributes`, `ChoiceParameters`, `ChoiceEvaluation`, and `PassengerType` in `src/drt/types.py`.
- Result objects use the `*Result` suffix, as in `InsertionResult` in `src/drt/insertion.py`, `SimulationResult` and `MetricsResult` in `experiments/metrics.py`, and `ALNSState` in `src/drt/alns.py`.
- Variant classes use PascalCase names that match experiment concepts, as in `DoorToDoor`, `SingleSidedPickup`, `SingleSidedDropoff`, `BidirectionalNoChoice`, `GreedyInsertionBaseline`, `FullModel`, `AblationNoRollingHorizon`, and `AblationNoChoice` in `experiments/variants.py`.

## Code Style

**Formatting:**
- No formatter configuration is detected. `pyproject.toml` has build and dependency metadata only; no `black`, `ruff`, `isort`, `mypy`, or pytest tool sections are present.
- Use 4-space indentation and PEP 8 spacing, matching `src/drt/candidate.py`, `src/drt/choice.py`, `experiments/metrics.py`, and `tests/test_runner.py`.
- Prefer type hints on public functions and dataclass fields, as in `src/drt/types.py`, `src/drt/choice.py`, `experiments/metrics.py`, `experiments/scenarios.py`, and `experiments/phase06_formal.py`.
- Use `from __future__ import annotations` in new Python modules, matching most active files such as `src/drt/choice.py`, `src/drt/alns.py`, `experiments/runner.py`, `tests/test_choice.py`, and `tests/test_phase06_formal.py`.
- Use explicit multi-line calls for dataclass construction and long function calls, as in `tests/test_choice.py`, `tests/test_milp.py`, `experiments/runner.py`, and `src/drt/choice.py`.
- Module docstrings are common and should state purpose, phase, or algorithm role, as in `src/drt/milp.py`, `src/drt/alns.py`, `experiments/metrics.py`, `tests/test_runner.py`, and `analysis/test_sensitivity.py`.
- Keep output file writes explicit about encoding when reading or writing text/CSV outside pandas, as in `experiments/runner.py`, `analysis/test_sensitivity.py`, and `experiments/formal_statistics.py`.

**Linting:**
- No linting configuration is detected. No `.eslintrc*`, `eslint.config.*`, `biome.json`, `ruff.toml`, `.ruff.toml`, `mypy.ini`, `pyrightconfig.json`, or `setup.cfg` lint section is present at the repository root.
- Follow the existing local style rather than introducing a new formatter style in isolated edits.
- Existing tests sometimes use `# noqa: E402` after manual `sys.path` mutation, as in `tests/test_phase05_pilot.py` and `tests/test_phase06_formal.py`; prefer editable install imports for new tests, but keep `# noqa: E402` when modifying files that already use that pattern.

## Import Organization

**Order:**
1. Future imports first: `from __future__ import annotations`, as in `src/drt/choice.py`, `experiments/phase06_formal.py`, and `tests/test_runner.py`.
2. Standard library imports next: `csv`, `json`, `math`, `os`, `random`, `subprocess`, `sys`, `time`, `traceback`, `dataclasses`, `datetime`, and `pathlib`, as in `experiments/runner.py`, `experiments/formal_statistics.py`, and `tests/test_milp.py`.
3. Third-party imports after standard library imports: `numpy as np`, `pandas as pd`, `pytest`, and optional `gurobipy`, as in `experiments/metrics.py`, `experiments/runner.py`, `tests/test_milp.py`, and `tests/test_phase06_formal.py`.
4. Local imports last: `from drt.types import ...`, `from experiments.metrics import ...`, and `from experiments.variants import ...`, as in `src/drt/choice.py`, `experiments/variants.py`, `tests/test_runner.py`, and `tests/test_variants.py`.

**Path Aliases:**
- The package is installed from `src/` by `pyproject.toml`; active library imports should use `drt.*` where possible, as in `src/drt/alns.py`, `src/drt/insertion.py`, `tests/test_candidate.py`, and `tests/test_choice.py`.
- Some experiment modules import `src.drt.*`, as in `experiments/scenarios.py` and `experiments/variants.py`; match the surrounding file when editing existing modules.
- Several tests mutate `sys.path`, including `tests/test_milp.py`, `tests/test_runner.py`, `tests/test_metrics.py`, `tests/test_variants.py`, and `tests/test_phase06_formal.py`. New tests should live under `tests/` and rely on `pip install -e .` unless the target file already follows the manual path pattern.

## Error Handling

**Patterns:**
- Use return values for expected domain outcomes: `check_feasibility()` returns `(bool, reason)` in `src/drt/feasibility.py`, and tests assert reason codes such as `capacity`, `tw_late`, `ride_time`, `precedence`, `route_duration`, and `tw_early` in `tests/test_feasibility.py`.
- Use `None` for expected no-solution paths, as in `evaluate_insertion()` returning `InsertionResult | None` in `src/drt/insertion.py` and `tests/test_insertion.py`.
- Raise `ValueError` for invalid inputs and configuration bounds, as in `assign_passenger_type()` in `src/drt/choice.py`, request-count caps in `experiments/scenarios.py`, formal-scale validation in `experiments/phase06_formal.py`, and control validation in `experiments/phase06_coverage_controls.py`.
- Defer optional dependency failures to the boundary that needs them, as in `src/drt/milp.py` raising `ImportError` when `gurobipy` is unavailable and `tests/test_milp.py` using `pytest.importorskip()`.
- Use `RuntimeError` for invalid execution state or planned test failures, as in `DRTModel.write_benchmark()` in `src/drt/milp.py` and `FailingVariant` in `tests/test_runner.py`.
- Long-running experiment runners convert timeouts and exceptions into durable result rows rather than aborting the whole batch, as in `_run_variant_with_timeout()` and `_make_error_row()` in `experiments/runner.py`.
- Validation packages return dictionaries with `passed`, `errors`, and check details, as in `experiments/pilot_validation.py`, `experiments/phase06_formal.py`, `experiments/phase06_coverage_controls.py`, and `experiments/phase06_robustness.py`.

## Logging

**Framework:** `print` / `stderr`

**Patterns:**
- Use `print()` for experiment progress and CLI summaries, as in `experiments/runner.py`, `experiments/matched_coverage.py`, `experiments/weight_sensitivity.py`, `analysis/sensitivity.py`, and `run_experiments.py`.
- Use `file=sys.stderr` for runner failures and timeouts, as in `_run_variant_with_timeout()` in `experiments/runner.py`.
- Use JSON output for machine-readable command results, as in `experiments/phase06_formal.py`, `experiments/phase06_coverage_controls.py`, `experiments/phase06_robustness.py`, and `experiments/formal_statistics.py`.
- No structured logging framework is configured; keep new progress output concise and deterministic enough for tests.

## Comments

**When to Comment:**
- Use comments to connect code to algorithm phases, model assumptions, units, or validation gates, as in `src/drt/types.py`, `src/drt/feasibility.py`, `src/drt/milp.py`, `experiments/metrics.py`, and `experiments/scenarios.py`.
- Use section dividers in large modules and test files to separate coherent groups, as in `src/drt/alns.py`, `src/drt/milp.py`, `tests/test_metrics.py`, and `tests/test_runner.py`.
- Preserve threat or validation comments when editing guarded paths, such as comments in `experiments/scenarios.py`, `experiments/runner.py`, and `experiments/variants.py`.
- Avoid comments that restate simple assignments; prefer comments that explain units, denominators, status semantics, reproducibility, or why an archived/gated path exists.

**JSDoc/TSDoc:**
- Not applicable. This repository is Python and LaTeX.
- Python docstrings use a mix of plain prose, NumPy-style sections, and short one-line summaries. Match the surrounding file: `src/drt/choice.py` uses parameter/return sections, `experiments/metrics.py` documents formulas and units, and `tests/test_runner.py` uses short test-purpose docstrings.

## Function Design

**Size:** Keep core helpers focused and testable in `src/drt/` and use larger orchestration functions only for experiment workflows. Small functions such as `euclidean()` in `src/drt/candidate.py`, `vkm_per_trip()` in `experiments/metrics.py`, and `_stable_int()` in `src/drt/choice.py` are preferred for reusable calculations. Larger runners such as `run_all_experiments()` in `experiments/runner.py` and `run_all()` in `experiments/phase06_robustness.py` should coordinate existing helpers rather than embedding unrelated calculations.

**Parameters:** Use explicit typed parameters rather than generic dictionaries for core model APIs, as in `generate_candidates()` in `src/drt/candidate.py`, `check_feasibility()` in `src/drt/feasibility.py`, and `evaluate_single_offer()` in `src/drt/choice.py`. Dictionaries are acceptable for CSV rows, manifests, validation reports, and method metadata in `experiments/runner.py`, `experiments/variants.py`, and `experiments/formal_statistics.py`.

**Return Values:** Prefer dataclasses for structured in-memory results (`ChoiceEvaluation`, `InsertionResult`, `SimulationResult`, `MetricsResult`) and dictionaries for serialized experiment rows or validation reports (`experiments/runner.py`, `experiments/milp_gap.py`, `experiments/phase06_formal.py`). Use `0.0` defaults instead of `None` for numeric metrics when denominators are empty, matching `compute_metrics()` in `experiments/metrics.py`.

## Module Design

**Exports:** Keep `src/drt/__init__.py` as the public package surface for stable primitives such as `Request`, `Vehicle`, `Bundle`, `accept_probability`, `evaluate_single_offer`, and `assign_passenger_type`. Import from specific modules for implementation details, as in `experiments/variants.py` and `tests/test_variants.py`.

**Barrel Files:** `src/drt/__init__.py` is the only active barrel-style file. `experiments/__init__.py` and `analysis/__init__.py` are package markers only. Do not add broad re-export barrels unless a stable public API is needed.

---

*Convention analysis: 2026-06-16*
