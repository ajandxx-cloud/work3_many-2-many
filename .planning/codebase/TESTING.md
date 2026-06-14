# Testing Patterns

**Analysis Date:** 2026-06-14

## Test Framework

**Runner:**
- `pytest` from the `dev` optional dependency in `pyproject.toml`.
- `pytest-benchmark` is listed in `pyproject.toml`, but benchmark tests currently use manual `time.perf_counter()` timing in `tests/test_insertion.py` and `src/drt/alns.py`.
- Config: Not detected. No `pytest.ini`, `tox.ini`, `setup.cfg`, or pytest section in `pyproject.toml` is present.

**Assertion Library:**
- Native pytest `assert` statements, as in `tests/test_candidate.py`, `tests/test_feasibility.py`, `tests/test_metrics.py`, and `tests/test_variants.py`.
- `pytest.approx` is used for floating-point equality in `tests/test_variants.py`.
- `pytest.raises` is used for input-validation checks in `tests/test_scenarios.py`.

**Run Commands:**
```bash
pytest                      # Run all tests under tests/ plus discovered analysis tests
pytest tests/               # Run the main pytest suite
pytest tests/test_milp.py   # Run Gurobi smoke tests; skips when gurobipy/license is unavailable
pytest tests/test_runner.py # Run experiment runner smoke tests that write CSVs to tmp_path
```

## Test File Organization

**Location:**
- Main unit and smoke tests live in `tests/`, with one file per source area: `tests/test_candidate.py`, `tests/test_feasibility.py`, `tests/test_insertion.py`, `tests/test_alns.py`, `tests/test_milp.py`, `tests/test_metrics.py`, `tests/test_scenarios.py`, `tests/test_runner.py`, and `tests/test_variants.py`.
- Analysis tests are colocated in `analysis/test_sensitivity.py`.
- Historical one-off scripts live under `archive/adhoc_tests/`; treat `archive/adhoc_tests/smoke_test.py`, `archive/adhoc_tests/test_scale100.py`, and related files as archived material, not the active pytest suite.

**Naming:**
- Test modules use `test_*.py`, as in `tests/test_candidate.py` and `analysis/test_sensitivity.py`.
- Test functions use `test_*`, as in `test_within_radius()` in `tests/test_candidate.py`, `test_valid_insertion()` in `tests/test_feasibility.py`, and `test_run_all_experiments_smoke()` in `tests/test_runner.py`.
- Grouped test classes use `Test*` names without inheritance, as in `TestGenerateSynthetic` in `tests/test_scenarios.py` and `TestGiniCoefficient` in `tests/test_metrics.py`.

**Structure:**
```text
tests/
├── test_candidate.py      # HEUR-01 candidate generation
├── test_feasibility.py    # HEUR-03 feasibility constraints
├── test_insertion.py      # HEUR-02 insertion evaluator
├── test_alns.py           # HEUR-04/05/06 ALNS and rolling horizon
├── test_milp.py           # EXACT-01/02/03/04 Gurobi smoke tests
├── test_metrics.py        # metrics dataclasses and metric calculations
├── test_scenarios.py      # synthetic and Beijing scenario generation
├── test_runner.py         # experiment runner CSV smoke tests
└── test_variants.py       # variant registry and behavioral guarantees
```

## Test Structure

**Suite Organization:**
```python
# Pattern from tests/test_feasibility.py and tests/test_insertion.py
def make_request(...):
    return Request(...)

def make_vehicle(...):
    return Vehicle(...)

def test_valid_insertion():
    vehicle = make_vehicle(...)
    request = make_request(...)
    route = Route(vehicle_id="v1", stops=[])

    ok, reason = check_feasibility(...)

    assert ok is True
    assert reason == ""
```

**Patterns:**
- Put lightweight local factory helpers near the top of the test file, as in `make_request()` and `make_mp()` in `tests/test_candidate.py`, `_make_meeting_points()` and `_make_requests()` in `tests/test_alns.py`, and `make_record()` in `tests/test_metrics.py`.
- Use explicit scenario setup inside each test when the setup is short, as in `tests/test_feasibility.py` and `tests/test_insertion.py`.
- Use grouped test classes when a module has many related metric or scenario assertions, as in `tests/test_metrics.py` and `tests/test_scenarios.py`.
- Include assertion messages for failure modes where domain context matters, as in `tests/test_insertion.py`, `tests/test_alns.py`, `tests/test_scenarios.py`, and `tests/test_variants.py`.
- Keep deterministic tests deterministic by using fixed seeds, as in `random.Random(42)` in `tests/test_insertion.py`, `seed=42` in `tests/test_scenarios.py`, and `generate_synthetic(..., seed=42)` in `tests/test_variants.py`.

## Mocking

**Framework:** Not detected

**Patterns:**
```python
# Pattern from tests/test_milp.py: skip optional external solver instead of mocking it
gp = pytest.importorskip("gurobipy", reason="gurobipy not installed")

@pytest.mark.skipif(not _licensed, reason="Gurobi license unavailable")
def test_scale_instance():
    ...
```

**What to Mock:**
- No mocking framework is currently used in `tests/` or `analysis/test_sensitivity.py`.
- Prefer deterministic generated inputs over mocks for algorithm behavior, following `tests/test_scenarios.py`, `tests/test_insertion.py`, and `tests/test_alns.py`.
- For optional external dependencies, prefer `pytest.importorskip()` or `pytest.mark.skipif()` over mocks, following `tests/test_milp.py`.

**What NOT to Mock:**
- Do not mock core algorithm functions such as `generate_candidates()` in `src/drt/candidate.py`, `check_feasibility()` in `src/drt/feasibility.py`, `evaluate_insertion()` in `src/drt/insertion.py`, or `compute_metrics()` in `experiments/metrics.py`; tests exercise real implementations.
- Do not mock generated scenarios for variant behavior; `tests/test_variants.py` uses real `generate_synthetic()` output from `experiments/scenarios.py`.

## Fixtures and Factories

**Test Data:**
```python
# Pattern from tests/test_runner.py
@pytest.fixture(scope="session")
def smoke_results(tmp_path_factory):
    tmp_path = tmp_path_factory.mktemp("runner_smoke")
    syn_rows, bei_rows = run_all_experiments(
        scales=[20],
        seeds=[42],
        beijing=True,
        results_dir=str(tmp_path),
    )
    return syn_rows, bei_rows, tmp_path
```

**Location:**
- Local factory functions live inside each test module, as in `tests/test_candidate.py`, `tests/test_feasibility.py`, `tests/test_insertion.py`, `tests/test_alns.py`, and `tests/test_metrics.py`.
- A session-scoped fixture is used only for expensive runner smoke tests in `tests/test_runner.py`.
- Shared production scenario generators live in `experiments/scenarios.py` and are used directly by `tests/test_scenarios.py` and `tests/test_variants.py`.

## Coverage

**Requirements:** None enforced

**View Coverage:**
```bash
pytest                      # No coverage tool is configured
```

## Test Types

**Unit Tests:**
- Candidate filtering and sorting are covered in `tests/test_candidate.py`.
- Feasibility constraints and reason codes are covered in `tests/test_feasibility.py`.
- Insertion selection, infeasible cases, and timing thresholds are covered in `tests/test_insertion.py`.
- Metrics edge cases, p95 calculations, Gini behavior, and detour ratio behavior are covered in `tests/test_metrics.py`.

**Integration Tests:**
- ALNS operators and `RollingHorizon.reoptimize()` are exercised together in `tests/test_alns.py`.
- Scenario generation contracts are exercised in `tests/test_scenarios.py`.
- Experiment variant classes are run against real synthetic scenarios in `tests/test_variants.py`.
- The runner writes CSV outputs into a temporary directory in `tests/test_runner.py`.
- Gurobi-backed MILP smoke tests are in `tests/test_milp.py` and skip when solver support is missing.

**E2E Tests:**
- No browser or UI E2E framework is used.
- The closest end-to-end checks are experiment smoke runs in `tests/test_runner.py` and top-level experiment execution through `run_experiments.py`.

## Common Patterns

**Async Testing:**
```python
# Pattern from experiments/runner.py verified through tests/test_runner.py:
# long variants run through ThreadPoolExecutor with a timeout, then tests assert CSV outputs.
syn_rows, bei_rows = run_all_experiments(
    scales=[20],
    seeds=[42],
    beijing=True,
    results_dir=str(tmp_path),
)
```

**Error Testing:**
```python
# Pattern from tests/test_scenarios.py
with pytest.raises(ValueError):
    generate_synthetic(1001, 10, 42)
```

```python
# Pattern from tests/test_feasibility.py
ok, reason = check_feasibility(...)
assert ok is False
assert reason == "capacity"
```

---

*Testing analysis: 2026-06-14*
