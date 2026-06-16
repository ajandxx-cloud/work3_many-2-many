# Testing Patterns

**Analysis Date:** 2026-06-16

## Test Framework

**Runner:**
- `pytest` from the `dev` optional dependency in `pyproject.toml`.
- `pytest-benchmark` is listed in `pyproject.toml`, but current performance checks use manual `time.perf_counter()` timing in `tests/test_insertion.py`, `tests/test_alns.py`, and `experiments/runner.py`.
- Config: Not detected. No `pytest.ini`, `tox.ini`, `setup.cfg`, or `[tool.pytest.ini_options]` section in `pyproject.toml` is present.
- Current discovery note: `pytest --collect-only -q` collected 200 active tests, then failed on four archived files in `archive/adhoc_tests/` because default discovery recurses into archive paths.

**Assertion Library:**
- Native pytest `assert` statements are the main assertion style, as in `tests/test_candidate.py`, `tests/test_feasibility.py`, `tests/test_metrics.py`, `tests/test_runner.py`, and `tests/test_variants.py`.
- Use `pytest.approx` for floating-point comparisons, as in `tests/test_variants.py`, `tests/test_metrics.py`, and `tests/test_milp.py`.
- Use `pytest.raises` for validation errors, as in `tests/test_choice.py` and `tests/test_scenarios.py`.
- Use `pytest.importorskip` and `pytest.skip` for optional Gurobi behavior, as in `tests/test_milp.py`.

**Run Commands:**
```bash
pytest tests/ analysis/test_sensitivity.py  # Run active tests while avoiding archived ad-hoc tests
pytest tests/                               # Run the main pytest suite
pytest analysis/test_sensitivity.py         # Run analysis sensitivity tests
pytest tests/test_milp.py                   # Run Gurobi smoke tests; skips when gurobipy/license is unavailable
pytest tests/test_runner.py                 # Run experiment runner smoke tests using tmp_path outputs
pytest --collect-only -q                    # Currently exposes archive/adhoc_tests collection errors
```

## Test File Organization

**Location:**
- Main tests live in `tests/`, with one file per implementation area: `tests/test_candidate.py`, `tests/test_feasibility.py`, `tests/test_insertion.py`, `tests/test_alns.py`, `tests/test_milp.py`, `tests/test_metrics.py`, `tests/test_scenarios.py`, `tests/test_runner.py`, `tests/test_variants.py`, `tests/test_phase05_pilot.py`, `tests/test_phase06_formal.py`, `tests/test_phase06_coverage_controls.py`, and `tests/test_phase06_robustness.py`.
- Analysis tests are colocated in `analysis/test_sensitivity.py`; include this file explicitly when using `pytest tests/` as the default active-suite command.
- Archived one-off scripts live under `archive/adhoc_tests/`, including `archive/adhoc_tests/smoke_test.py`, `archive/adhoc_tests/test_fix.py`, `archive/adhoc_tests/test_scale100.py`, and `archive/adhoc_tests/test_scale500.py`. Treat these as historical scripts, not active tests.

**Naming:**
- Test modules use `test_*.py`, as in `tests/test_choice.py`, `tests/test_runner.py`, `tests/test_phase06_formal.py`, and `analysis/test_sensitivity.py`.
- Test functions use `test_*`, as in `test_within_radius()` in `tests/test_candidate.py`, `test_invalid_type_shares_raise_clear_error()` in `tests/test_choice.py`, and `test_validate_phase06_main_outputs_blocks_missing_cells()` in `tests/test_phase06_formal.py`.
- Grouped test classes use `Test*` names without inheritance, as in `TestMetricsResultStructure`, `TestEmptyResult`, and `TestGiniCoefficient` in `tests/test_metrics.py`, and `TestGenerateSynthetic` and `TestGenerateBeijing` in `tests/test_scenarios.py`.
- Local helper functions in tests use `make_*` or `_make_*`, as in `tests/test_choice.py`, `tests/test_metrics.py`, `tests/test_milp.py`, and `tests/test_alns.py`.

**Structure:**
```text
tests/
├── test_candidate.py                 # HEUR-01 candidate generation
├── test_feasibility.py               # feasibility reason codes
├── test_insertion.py                 # insertion evaluator and timing benchmark
├── test_alns.py                      # ALNS, rolling horizon, diagnostics
├── test_milp.py                      # exact MILP smoke tests and no-Gurobi path
├── test_metrics.py                   # metrics dataclasses and calculations
├── test_scenarios.py                 # synthetic and Beijing scenario generation
├── test_runner.py                    # experiment runner CSV/error/timeout behavior
├── test_variants.py                  # variant registry and behavioral guarantees
├── test_phase05_pilot.py             # pilot run and validation outputs
├── test_phase06_formal.py            # formal run manifests, validation, tables
├── test_phase06_coverage_controls.py # matched/fixed coverage controls
└── test_phase06_robustness.py        # robustness package validation

analysis/
└── test_sensitivity.py               # sensitivity sweep behavior and CSV outputs
```

## Test Structure

**Suite Organization:**
```python
# Pattern from tests/test_choice.py
def make_offer(**overrides) -> OfferAttributes:
    values = {
        "request_id": "req_1",
        "service_design": "BidirectionalMeetingPoint",
        "pickup_walk": 0.2,
        "dropoff_walk": 0.1,
        "wait_time": 5.0,
        "ivt": 12.0,
        "fare": 0.0,
    }
    values.update(overrides)
    return OfferAttributes(**values)

def test_service_asc_increases_acceptance_probability():
    offer = make_offer()
    ptype = make_ptype()

    low = evaluate_single_offer(offer, ptype, ChoiceParameters(service_asc=-1.0), random_draw=0.5)
    high = evaluate_single_offer(offer, ptype, ChoiceParameters(service_asc=1.0), random_draw=0.5)

    assert high.acceptance_probability > low.acceptance_probability
```

**Patterns:**
- Place lightweight factories near the top of the test file, as in `make_offer()` in `tests/test_choice.py`, `make_record()` in `tests/test_metrics.py`, `_make_meeting_points()` in `tests/test_milp.py`, and `_raw_row()` in `tests/test_phase06_formal.py`.
- Use deterministic seeds for simulation and choice behavior, as in `generate_synthetic(..., seed=42)` in `tests/test_variants.py`, `random.Random(42)` in `tests/test_milp.py`, and `ChoiceParameters(choice_seed=...)` paths tested in `tests/test_choice.py`.
- Use `tmp_path` or `tmp_path_factory` for tests that write files, as in `tests/test_runner.py`, `tests/test_phase05_pilot.py`, `tests/test_phase06_formal.py`, `tests/test_phase06_coverage_controls.py`, and `tests/test_phase06_robustness.py`.
- Use grouped classes for large families of related assertions, as in `tests/test_metrics.py` and `tests/test_scenarios.py`; use flat functions for smaller modules, as in `tests/test_candidate.py` and `tests/test_choice.py`.
- Assert both success and failure states for validation gates, as in `tests/test_phase05_pilot.py`, `tests/test_phase06_formal.py`, `tests/test_phase06_coverage_controls.py`, and `tests/test_phase06_robustness.py`.

## Mocking

**Framework:** pytest built-in fixtures (`monkeypatch`, `tmp_path`, `tmp_path_factory`) plus local fake classes.

**Patterns:**
```python
# Pattern from tests/test_runner.py
class FailingVariant:
    name = "FailingVariant"
    method_metadata = {
        "method_label": "FailingVariant_Diagnostic",
        "evidence_family": "algorithm_diagnostic",
        "diagnostic_role": "failure_fixture",
    }

    def run(self, scenario):
        raise RuntimeError("planned fixture failure")

def test_failed_rows_are_written_to_csv(tmp_path, monkeypatch):
    monkeypatch.setattr(runner_module, "ALL_VARIANTS", [FailingVariant()])

    syn_rows, _ = run_all_experiments(
        scales=[8],
        seeds=[42],
        beijing=False,
        results_dir=str(tmp_path),
    )

    assert syn_rows[0]["status"] == "failed"
```

**What to Mock:**
- Mock module constants and variant registries to reduce runtime or isolate behavior, as in `tests/test_runner.py` monkeypatching `_VARIANT_TIMEOUT_S` and `ALL_VARIANTS`.
- Mock runner functions when validating orchestration and output scoping, as in `tests/test_phase06_formal.py` monkeypatching `runner_module.run_all_experiments`.
- Mock expensive or unavailable solver paths, as in `tests/test_milp.py` monkeypatching `DRTModel.solve` and `milp_gap.FullModel`.
- Mock helper functions to force validation edge cases, as in `tests/test_phase05_pilot.py` monkeypatching coverage-smoke helpers.

**What NOT to Mock:**
- Do not mock core arithmetic and model primitives in `src/drt/candidate.py`, `src/drt/choice.py`, `src/drt/feasibility.py`, `src/drt/insertion.py`, or `experiments/metrics.py`; tests exercise these directly.
- Do not mock `generate_synthetic()` for variant behavior tests in `tests/test_variants.py`; deterministic real scenarios provide integration coverage.
- Do not mock CSV validation schemas when testing Phase 05/06 validation gates; construct reduced real `pandas.DataFrame` fixtures instead, as in `tests/test_phase05_pilot.py`, `tests/test_phase06_formal.py`, and `tests/test_phase06_coverage_controls.py`.

## Fixtures and Factories

**Test Data:**
```python
# Pattern from tests/test_metrics.py
def make_record(
    request_id: str = "req_0",
    passenger_type: str = "time_sensitive",
    accepted: bool = True,
    wait_time: float = 300.0,
    pickup_walk: float = 200.0,
    dropoff_walk: float = 150.0,
    ivt: float = 900.0,
    direct_time: float = 600.0,
    total_disutility: float = -5.0,
    status: str | None = None,
) -> PassengerRecord:
    return PassengerRecord(...)
```

**Location:**
- Keep factories local to the test module that owns the scenario shape, as in `tests/test_candidate.py`, `tests/test_choice.py`, `tests/test_metrics.py`, `tests/test_milp.py`, and `tests/test_phase06_formal.py`.
- Use pytest fixtures only when setup is expensive or shared across many assertions. `tests/test_runner.py` uses a session-scoped `smoke_results` fixture to run `run_all_experiments()` once and share CSV outputs.
- Module-level scenario constants are acceptable for small deterministic integration tests, as in `SMALL_SCENARIO` and `MEDIUM_SCENARIO` in `tests/test_variants.py`.

## Coverage

**Requirements:** No coverage threshold or coverage tool configuration is detected in `pyproject.toml` or repository root config files.

**View Coverage:**
```bash
pytest tests/ analysis/test_sensitivity.py --cov=src --cov=experiments --cov=analysis
```

Coverage command note: `pytest-cov` is not declared in `pyproject.toml`; install it separately before using the command above.

## Test Types

**Unit Tests:**
- Core unit tests cover candidate generation, feasibility, insertion, choice utilities, and metric calculations in `tests/test_candidate.py`, `tests/test_feasibility.py`, `tests/test_insertion.py`, `tests/test_choice.py`, and `tests/test_metrics.py`.
- Scenario unit tests verify request/vehicle counts, coordinate ranges, reproducibility, and caps in `tests/test_scenarios.py`.

**Integration Tests:**
- Variant integration tests run real deterministic scenarios across all registered variants in `tests/test_variants.py`.
- Runner integration tests execute a reduced experiment matrix and verify CSV schemas, timeout rows, failure rows, utility logs, and Beijing smoke behavior in `tests/test_runner.py`.
- Phase validation integration tests construct reduced result packages and validate manifests, denominator gates, missing-row detection, and schema checks in `tests/test_phase05_pilot.py`, `tests/test_phase06_formal.py`, `tests/test_phase06_coverage_controls.py`, and `tests/test_phase06_robustness.py`.

**E2E Tests:**
- No browser or full external-system E2E framework is used.
- The closest E2E coverage is command/workflow-level experiment validation in `tests/test_runner.py`, `tests/test_phase05_pilot.py`, `tests/test_phase06_formal.py`, and `analysis/test_sensitivity.py`, all of which write real temporary or result files.

## Common Patterns

**Async Testing:**
```python
# Pattern from tests/test_runner.py
def test_timeout_row_returns_without_waiting_for_worker(tmp_path, monkeypatch):
    monkeypatch.setattr(runner_module, "_VARIANT_TIMEOUT_S", 0.01)

    row = _run_variant_with_timeout(
        SleepingVariant(),
        scenario,
        scale=8,
        seed=42,
        results_dir=str(tmp_path),
    )

    assert row["status"] == "timeout"
    assert "timeout" in row["detailed_reason"]
```

**Error Testing:**
```python
# Pattern from tests/test_choice.py and tests/test_milp.py
with pytest.raises(ValueError, match="non-negative"):
    assign_passenger_type("req_1", types, {"price_sensitive": -1.0}, seed=42)

pytest.importorskip("gurobipy", reason="gurobipy not installed")
```

**Schema Testing:**
- Assert required columns explicitly after writing CSVs, as in `tests/test_runner.py`, `tests/test_phase05_pilot.py`, and `tests/test_phase06_coverage_controls.py`.
- Assert status and detail fields alongside numeric outputs, as in `tests/test_runner.py`, `tests/test_milp.py`, `tests/test_phase05_pilot.py`, and `tests/test_phase06_formal.py`.

**Performance Testing:**
- Use deterministic manual timing thresholds for heuristic smoke tests, as in `tests/test_insertion.py` and `tests/test_alns.py`.
- Keep performance tests at reduced scales for unit test runs; large formal experiments are represented by Phase 05/06 smoke and validation tests rather than full production-scale execution.

---

*Testing analysis: 2026-06-16*
