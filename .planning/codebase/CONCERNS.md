# Codebase Concerns

**Analysis Date:** 2026-06-14

## Tech Debt

**Mixed import roots make execution environment fragile:**
- Issue: Core library modules import `drt.*` from the editable package path, while experiment modules import `src.drt.*` from the repository root. Tests patch `sys.path` inconsistently, and direct `pytest` collection fails when `drt` is not installed editable.
- Files: `src/drt/alns.py:19`, `src/drt/insertion.py:21`, `src/drt/feasibility.py:22`, `src/drt/milp.py:20`, `experiments/variants.py:38`, `experiments/scenarios.py:21`, `tests/test_alns.py:17`, `tests/test_scenarios.py:15`
- Impact: Running from a clean checkout without `pip install -e .` produces `ModuleNotFoundError: No module named 'drt'`. Running from an installed package context can also expose `src.drt` imports as repository-only assumptions.
- Fix approach: Standardize imports on the installed package namespace `drt.*` for library code and experiment code. Add one test bootstrap mechanism, preferably `pyproject.toml` pytest config with `pythonpath = ["src", "."]` or a root `conftest.py`, rather than per-test `sys.path.insert`.

**Dependency metadata omits runtime imports:**
- Issue: `pyproject.toml` declares only `gurobipy` and `numpy`, but runtime experiment and figure scripts import `pandas` and `matplotlib`.
- Files: `pyproject.toml:8`, `experiments/runner.py:27`, `run_experiments.py:8`, `tests/test_runner.py:16`, `manuscript/figures/scripts/fig04_baseline_comparison.py:8`, `manuscript/figures/scripts/fig07_pareto.py:14`
- Impact: Fresh environment installs can pass package installation but fail when running `python run_experiments.py`, `python -m experiments.runner`, runner tests, or figure generation.
- Fix approach: Add runtime dependencies used by the main experiment path to `[project].dependencies` and separate manuscript/figure dependencies into an optional extra such as `figures = ["matplotlib", "pandas"]`. Keep `pytest` and benchmarking tools in the existing `dev` extra.

**Route stop representation is implicit and inconsistent:**
- Issue: `Route.stops` is typed as an unstructured `list`; code alternates between plain `(MeetingPoint, time)` stops and tagged `(MeetingPoint, time, request_id, role)` stops. Helpers depend on tuple length checks and conversions.
- Files: `src/drt/types.py:97`, `src/drt/alns.py:73`, `src/drt/alns.py:102`, `src/drt/alns.py:347`, `experiments/variants.py:211`, `experiments/variants.py:295`, `src/drt/feasibility.py:93`
- Impact: New code can silently drop request metadata through `_to_plain_routes`, fail tuple unpacking if a tagged stop reaches `check_feasibility`, or produce incomplete passenger metrics when completed stops are pruned.
- Fix approach: Introduce a `RouteStop` dataclass with explicit `meeting_point`, `time`, `request_id`, and `role` fields. Convert feasibility/insertion code to operate on this type or a narrow adapter, and add tests for both in-route and completed/pruned requests.

**Core algorithm module is oversized and mixes responsibilities:**
- Issue: `src/drt/alns.py` contains state containers, route-cost helpers, destroy operators, repair operators, rolling-horizon simulation, and benchmark generation in one large module.
- Files: `src/drt/alns.py`
- Impact: Small changes to rolling-horizon state can affect operator behavior, benchmarking, and metric reconstruction. The module is harder to test in isolation, and local helper assumptions are easy to miss.
- Fix approach: Split into `src/drt/alns_state.py`, `src/drt/operators.py`, `src/drt/rolling_horizon.py`, and `src/drt/benchmark.py` while preserving public imports during migration.

**Version-control state is heavily drifted from the working tree:**
- Issue: `git status --short` reports many deleted tracked paths such as `.planning/PROJECT.md`, `paper/`, `paper_work3/`, `figures/`, and root debug scripts, while current trees such as `README.md`, `archive/`, `docs/`, and `manuscript/` are untracked. `.gitignore` ignores `__pycache__/`, but tracked pycache paths still appear in git status.
- Files: `.gitignore:1`, `README.md:96`, `manuscript/main.tex`, `archive/`, `.planning/config.json`
- Impact: Commits and diffs are noisy, generated files can remain tracked, and phase/state files under `.planning/` appear deleted from git even though current `.planning/codebase/` exists.
- Fix approach: Reconcile the rename/reorganization in one repository-maintenance commit: remove tracked generated artifacts, add current canonical source/manuscript paths, restore or intentionally remove `.planning` state files, and keep `.planning/codebase/*.md` tracked if GSD maps are part of project state.

**README and source text show mojibake encoding damage:**
- Issue: Several comments and README sections contain garbled sequences such as `鈥?`, `鈫?`, and `脳`, especially in mathematical notation and directory descriptions.
- Files: `README.md:1`, `README.md:96`, `src/drt/types.py:4`, `src/drt/milp.py:30`, `experiments/config.py:14`
- Impact: Mathematical notation, paper workflow instructions, and project descriptions are harder to review and may propagate into generated documentation.
- Fix approach: Normalize all text files to UTF-8, repair affected prose from manuscript/source context, and add an editorconfig or encoding check for Markdown, Python, and LaTeX sources.

## Known Bugs

**Bare `pytest` fails by collecting archived ad hoc tests:**
- Symptoms: `pytest -q` collects `archive/adhoc_tests/*.py` and fails with `ModuleNotFoundError: No module named 'drt'` before the normal test suite runs.
- Files: `archive/adhoc_tests/smoke_test.py`, `archive/adhoc_tests/test_fix.py`, `archive/adhoc_tests/test_scale100.py`, `archive/adhoc_tests/test_scale500.py`, `pyproject.toml`
- Trigger: Run `pytest -q` from repository root without editable installation or pytest collection config.
- Workaround: Run targeted tests with `PYTHONPATH=src pytest tests -q`, or run a small subset such as `PYTHONPATH=src pytest tests/test_metrics.py tests/test_candidate.py tests/test_feasibility.py -q`.
- Fix approach: Add pytest config to restrict `testpaths = ["tests"]`, set the package path, and exclude `archive/`. Keep archived scripts named without the `test_*.py` pattern or move them outside pytest discovery.

**Runner timeout does not actually bound variant execution:**
- Symptoms: `_run_variant_with_timeout` returns an error row on `TimeoutError`, but the surrounding `with ThreadPoolExecutor(...)` exits by calling `shutdown(wait=True)`, which waits for the still-running task.
- Files: `experiments/runner.py:29`, `experiments/runner.py:186`, `experiments/runner.py:193`, `experiments/runner.py:202`
- Trigger: Any variant run exceeding `_VARIANT_TIMEOUT_S = 120` seconds.
- Workaround: None reliable in the current code; interrupting the parent Python process is required if the worker keeps running.
- Fix approach: Use a process-based timeout for experiment isolation, or explicitly call `executor.shutdown(wait=False, cancel_futures=True)` outside a `with` block. Prefer `ProcessPoolExecutor` for CPU-heavy or non-cooperative algorithms.

**`FullModel(gamma=...)` does not affect acceptance, routing, or offered bundle choice:**
- Symptoms: `FullModel.__init__` stores `_gamma`, but `_gamma` is not referenced in `_solve` or `_mnl_filter_requests`. `experiments/pareto_sweep.py` varies gamma and only applies it after the run in `compute_social_welfare`.
- Files: `experiments/variants.py:590`, `experiments/variants.py:595`, `experiments/variants.py:615`, `experiments/pareto_sweep.py:50`, `experiments/pareto_sweep.py:59`, `experiments/metrics.py:210`
- Trigger: Run `python experiments/pareto_sweep.py`; `served_share` and `vkm_per_served_trip` are governed by the same FullModel behavior for every gamma value.
- Workaround: Interpret the current Pareto sweep as a post-hoc welfare scoring sweep only, not as an endogenous policy or rejection-penalty experiment.
- Fix approach: Pass gamma into the choice/routing decision where rejection penalty is supposed to alter acceptance or objective tradeoffs, then add tests asserting monotonic or at least non-identical behavior across gamma values.

**Social-welfare field is declared but never populated by `compute_metrics`:**
- Symptoms: `MetricsResult.social_welfare` defaults to `0.0`, and `compute_metrics` returns `MetricsResult(...)` without passing a social welfare value.
- Files: `experiments/metrics.py:65`, `experiments/metrics.py:77`, `experiments/metrics.py:177`, `experiments/metrics.py:210`
- Trigger: Any consumer reading `compute_metrics(result).social_welfare`.
- Workaround: Call `compute_social_welfare(result.records, gamma)` directly.
- Fix approach: Either remove `social_welfare` from `MetricsResult` or add an optional `gamma` parameter to `compute_metrics` and populate the field deliberately.

**Weight sensitivity uses acceptance rate as the trip denominator instead of accepted trip count:**
- Symptoms: `run_weight_sensitivity` computes `vehicle_km / acceptance_rate`, even though `experiments.metrics.vkm_per_trip` defines the denominator as `n_requests * acceptance_rate`.
- Files: `experiments/weight_sensitivity.py:85`, `experiments/weight_sensitivity.py:87`, `experiments/metrics.py:190`
- Trigger: Run `python experiments/weight_sensitivity.py`; reported `*_vkm_per_trip` values are inflated by a factor of `n_requests`.
- Workaround: Recompute from output as `vehicle_km / (200 * acceptance_rate)` for the default `N = 200`.
- Fix approach: Replace the local formula with `vkm_per_trip(fm_vkm, n_requests, fm_acc)` and `vkm_per_trip(dd_vkm, n_requests, dd_acc)`.

**Policy recommendations can silently use hardcoded fallback values:**
- Symptoms: `_extract_metrics_data` substitutes `2383.85` and `3662.33` if FullModel or DoorToDoor vehicle-km values are missing.
- Files: `analysis/policy.py:149`, `analysis/policy.py:181`, `analysis/policy.py:183`, `analysis/policy.py:185`, `results/policy_recommendations.md`
- Trigger: Missing or malformed `results/metrics_table.csv` rows for `FullModel` or `DoorToDoor`.
- Workaround: Inspect logs and generated recommendations for fallback usage; there is no explicit warning in the returned data.
- Fix approach: Raise a clear exception or include an explicit "data missing" marker instead of substituting paper-specific constants.

## Security Considerations

**No secret-reading path detected in active code:**
- Risk: Not detected for external API keys, credential files, or `.env` reads.
- Files: `src/drt/`, `experiments/`, `analysis/`, `pyproject.toml`
- Current mitigation: Active code uses generated scenarios, local CSV/JSON files, and optional local Gurobi licensing through `gurobipy`.
- Recommendations: Keep `.env*`, `*.key`, `*.pem`, and credential files ignored. Do not write license or solver credential details into result logs.

**CSV/Markdown output paths are local but overwrite without confirmation:**
- Risk: Experiment and analysis scripts overwrite committed outputs under `results/` without atomic writes or backup checks.
- Files: `experiments/runner.py:129`, `experiments/runner.py:218`, `experiments/pareto_sweep.py:74`, `experiments/weight_sensitivity.py:117`, `analysis/policy.py:203`
- Current mitigation: Paths are hardcoded under `results/`; there is no user-provided path injection in the default scripts.
- Recommendations: Write to a timestamped run directory or temporary file plus atomic replace. Keep canonical paper tables generated from a manifest that records code version, seeds, and config.

**Gurobi execution can consume licensed solver resources without central gating:**
- Risk: `DRTModel.solve()` runs the optimizer directly when `gurobipy` is available; experiment gap scripts can launch multiple 300-second solves.
- Files: `src/drt/milp.py:56`, `src/drt/milp.py:122`, `src/drt/milp.py:380`, `experiments/milp_gap.py:127`
- Current mitigation: MILP defaults include `time_limit=300.0`, `mip_gap=0.05`, and solver output is suppressed.
- Recommendations: Add a documented config flag for MILP runs, lower default time limits for tests, and log solver status without exposing license/environment details.

## Performance Bottlenecks

**Insertion and regret repair are combinatorial over vehicles, candidates, and positions:**
- Problem: `_all_insertion_costs` and `evaluate_insertion` enumerate every vehicle, pickup candidate, dropoff candidate, pickup insertion index, and dropoff insertion index.
- Files: `src/drt/insertion.py:76`, `src/drt/insertion.py:83`, `src/drt/insertion.py:85`, `src/drt/alns.py:385`, `src/drt/alns.py:391`, `src/drt/alns.py:393`
- Cause: Complexity grows roughly with `vehicles * pickup_candidates * dropoff_candidates * route_length^2` per request, and ALNS repeats this inside multiple iterations.
- Improvement path: Cache candidate sets, cap route positions by time-window feasibility, maintain incremental route schedules, and short-circuit candidates using lower-bound cost filters.

**Deep-copy heavy ALNS operators add avoidable memory and CPU overhead:**
- Problem: Destroy/repair operators repeatedly call `deepcopy(state)` and rebuild plain route dictionaries.
- Files: `src/drt/alns.py:182`, `src/drt/alns.py:199`, `src/drt/alns.py:232`, `src/drt/alns.py:272`, `src/drt/alns.py:305`, `src/drt/alns.py:547`
- Cause: Mutable shared `ALNSState` objects and untyped `Route.stops` make copy boundaries broad.
- Improvement path: Make route states structurally immutable or implement targeted copy-on-write for the changed vehicle routes only.

**Full test suite can exceed practical command time:**
- Problem: `PYTHONPATH=src pytest tests -q` exceeded the 120-second command limit during mapping, while a fast subset (`tests/test_metrics.py`, `tests/test_candidate.py`, `tests/test_feasibility.py`) completed with 48 passing tests in 0.10s.
- Files: `tests/test_alns.py:168`, `tests/test_runner.py:28`, `tests/test_runner.py:32`, `experiments/runner.py:69`
- Cause: Benchmark and runner smoke tests execute real algorithm runs, including `benchmark(n_requests=200, n_vehicles=15, ...)` and all variants at smoke scale.
- Improvement path: Mark long tests with `@pytest.mark.slow`, lower default benchmark sizes in unit tests, and keep full experiment smoke tests opt-in for CI nightly or release validation.

## Fragile Areas

**Rolling-horizon completed-request accounting affects metrics:**
- Files: `src/drt/alns.py:498`, `src/drt/alns.py:506`, `src/drt/alns.py:609`, `src/drt/alns.py:613`, `experiments/variants.py:211`, `experiments/variants.py:229`, `experiments/variants.py:247`
- Why fragile: `completed_request_ids` is populated both when stops are pruned by time and when requests are merely accepted into current routes. Completed/pruned requests lose pickup/dropoff meeting point details, and metrics substitute zero walking distance plus Euclidean fallback IVT.
- Safe modification: Preserve a per-request assignment ledger with pickup/dropoff MPs, scheduled pickup/dropoff times, accepted/rejected status, and completion status. Build `PassengerRecord` from that ledger instead of reconstructing from final route stops.
- Test coverage: Current variant tests assert result types and metric ranges, but do not assert exact accepted sets, walk distances, or scheduled times for completed requests.

**Feasibility checker approximates existing occupancy by alternating pickup/dropoff roles:**
- Files: `src/drt/feasibility.py:113`, `src/drt/feasibility.py:120`, `src/drt/feasibility.py:123`, `src/drt/feasibility.py:129`
- Why fragile: Existing stops without labels are assumed to alternate pickup/dropoff starting with pickup. This can reject feasible insertions or accept infeasible ones when route order is not alternating.
- Safe modification: Require role metadata on every stop before feasibility checks, or pass an explicit occupancy trace with the route.
- Test coverage: `tests/test_feasibility.py` covers basic capacity and time-window cases, but it does not cover mixed existing routes with non-alternating pickup/dropoff roles or tagged route stops.

**MILP model is a simplified assignment snapshot rather than a full route-sequencing model:**
- Files: `src/drt/milp.py:178`, `src/drt/milp.py:234`, `src/drt/milp.py:282`, `src/drt/milp.py:304`, `experiments/milp_gap.py:165`
- Why fragile: Capacity is bounded by total requests assigned to a vehicle, not time-varying occupancy; operational cost uses pickup-to-dropoff distances, not complete vehicle route sequence; time variables are per request/vehicle without route order variables.
- Safe modification: Keep using the current MILP only as a static benchmark with clearly documented scope, or add sequence/order variables if exact route feasibility is required.
- Test coverage: `tests/test_milp.py` smoke-tests status and accepted IDs, but does not compare MILP schedules against a hand-verified route-sequencing optimum.

**MNL filtering uses nearest meeting points before routing rather than the actual offered route bundle:**
- Files: `experiments/variants.py:78`, `experiments/variants.py:123`, `experiments/variants.py:139`, `experiments/variants.py:147`, `src/drt/choice.py:26`
- Why fragile: Passenger acceptance is simulated from nearest pickup/dropoff proxies before insertion and scheduling. The final route can offer different meeting points, wait time, and IVT than the bundle used for acceptance.
- Safe modification: Generate candidate route bundles first, compute acceptance probability for the actual best offered bundle, and only commit insertion when accepted.
- Test coverage: No tests assert that MNL probability inputs match assigned pickup/dropoff MPs or scheduled pickup time.

## Scaling Limits

**Scenario generation hard-caps requests at 1000:**
- Current capacity: Synthetic and Beijing scenario generators accept up to 1000 requests.
- Limit: `generate_synthetic` and `generate_beijing` raise `ValueError` above `_MAX_REQUESTS = 1000`.
- Scaling path: Keep the cap for developer safety, but expose it through config and add streaming/batched scenario generation before raising it.
- Files: `experiments/scenarios.py:27`, `experiments/scenarios.py:65`, `experiments/scenarios.py:176`

**Published full experiment grid is capped at 500 synthetic requests and 200 Beijing requests:**
- Current capacity: `SCALES = [100, 200, 300, 500]`, `BEIJING_SCALE = 200`, with vehicle counts up to 30.
- Limit: Full-grid experiments are not configured for 1000-request stress runs or dense urban meeting-point grids.
- Scaling path: Add a separate stress profile with fewer variants/seeds, explicit timeout behavior, and recorded hardware/runtime metadata.
- Files: `experiments/config.py:13`, `experiments/config.py:14`, `experiments/config.py:44`, `experiments/runner.py:93`

**MILP benchmark scale remains small and solver-dependent:**
- Current capacity: Gap experiments run only `n=20` and `n=30` with 300-second MILP time limits.
- Limit: Gurobi availability and simplified MILP formulation constrain exact-comparison scope.
- Scaling path: Keep MILP benchmarks separate from default tests, store solver status in outputs, and compare ALNS against smaller exact instances or deterministic baselines with known optima.
- Files: `experiments/milp_gap.py:4`, `experiments/milp_gap.py:134`, `experiments/milp_gap.py:205`

## Dependencies at Risk

**`gurobipy`:**
- Risk: Required in `pyproject.toml` but license availability is environment-specific. Tests skip when unavailable, so MILP behavior can remain unverified on many machines.
- Impact: `src/drt/milp.py` and `experiments/milp_gap.py` either fail, skip, or emit `no_gurobi`, leaving exact benchmark claims dependent on local solver setup.
- Migration plan: Move `gurobipy` to an optional `milp` extra if the heuristic path is the default install, and add a small pure-Python fallback or saved fixture for CI assertions.
- Files: `pyproject.toml:10`, `src/drt/milp.py:95`, `tests/test_milp.py:17`, `experiments/milp_gap.py:110`

**`pandas` and `matplotlib`:**
- Risk: Used by runner/tests/figures but absent from `pyproject.toml`.
- Impact: Reproducibility depends on preinstalled packages outside project metadata.
- Migration plan: Add explicit version-bounded dependencies or optional extras for `experiments` and `figures`.
- Files: `experiments/runner.py:27`, `run_experiments.py:8`, `manuscript/figures/scripts/fig01_system_overview.py:1`, `manuscript/figures/scripts/fig05_sensitivity.py:8`, `pyproject.toml:8`

**Git-tracked generated artifacts:**
- Risk: `git status --short` shows tracked `__pycache__` and generated result files despite `.gitignore` rules.
- Impact: Running tests and experiments modifies tracked generated files and makes source diffs noisy.
- Migration plan: Remove generated artifacts from the index with `git rm --cached`, keep `.gitignore` coverage, and regenerate outputs through scripts.
- Files: `.gitignore:1`, `results/synthetic_results.csv`, `results/metrics_table.csv`, `src/drt/__pycache__/alns.cpython-312.pyc`, `experiments/__pycache__/runner.cpython-312.pyc`

## Missing Critical Features

**Endogenous rejection penalty is not implemented in FullModel behavior:**
- Problem: Gamma exists as a constructor parameter but does not affect choice, assignment, routing objective, or accepted-set selection.
- Blocks: Pareto frontier claims where `gamma` should trade off social welfare, served share, and vehicle-km per served trip.
- Files: `experiments/variants.py:590`, `experiments/variants.py:595`, `experiments/pareto_sweep.py:50`

**Experiment provenance is not captured in machine-readable outputs:**
- Problem: CSV/JSON outputs store metrics but not code revision, dependency versions, config snapshot, command, hardware/runtime, or whether timeouts/errors occurred.
- Blocks: Reproducible paper results and clean comparison of archive/current outputs.
- Files: `experiments/runner.py:129`, `experiments/runner.py:151`, `experiments/weight_sensitivity.py:91`, `experiments/milp_gap.py:182`, `results/`

**Real Beijing data ingestion is not present:**
- Problem: `generate_beijing` creates a semi-realistic synthetic grid; no input loader or schema for public Beijing trip/road/meeting-point data is present.
- Blocks: Claims requiring reproducibility against public datasets instead of generated scenarios.
- Files: `experiments/scenarios.py:152`, `docs/工作3公开数据集.txt`, `results/beijing_results.csv`

## Test Coverage Gaps

**No root-level test configuration:**
- What's not tested: The default developer command `pytest` as documented in `README.md` is not kept green.
- Files: `README.md:83`, `pyproject.toml`, `archive/adhoc_tests/`, `tests/`
- Risk: New contributors and automation run the wrong test surface and hit archived failures before active tests.
- Priority: High

**Runner timeout and error rows are not behaviorally tested:**
- What's not tested: A hanging variant should return in bounded wall time and produce an error row without blocking executor shutdown.
- Files: `experiments/runner.py:186`, `tests/test_runner.py:28`
- Risk: Full experiment runs can stall despite a visible timeout constant.
- Priority: High

**Gamma/Pareto semantics are not tested:**
- What's not tested: `FullModel(gamma=0)` versus `FullModel(gamma=100)` should have a defined expected relationship or deliberately identical routing if the sweep is post-hoc only.
- Files: `experiments/variants.py:590`, `experiments/pareto_sweep.py:37`, `tests/test_variants.py:130`
- Risk: Pareto outputs can look meaningful while only social-welfare arithmetic changes.
- Priority: High

**Metric exactness for completed/pruned trips is not tested:**
- What's not tested: Passenger records after rolling-horizon pruning should preserve pickup/dropoff walk, wait, IVT, and accepted status.
- Files: `src/drt/alns.py:498`, `experiments/variants.py:229`, `experiments/variants.py:247`, `tests/test_metrics.py`, `tests/test_variants.py`
- Risk: Reported acceptance, walking, fairness, and detour results can diverge from actual scheduled route details.
- Priority: High

**Experiment formulas are not cross-checked against shared metric helpers:**
- What's not tested: `experiments/weight_sensitivity.py` should match `experiments.metrics.vkm_per_trip`.
- Files: `experiments/weight_sensitivity.py:87`, `experiments/metrics.py:190`, `tests/test_metrics.py`
- Risk: Derived paper tables can use inconsistent formulas even when base metrics tests pass.
- Priority: Medium

**MILP exactness tests are smoke-level only:**
- What's not tested: Known small instances with expected accepted set, route cost, feasibility, and objective value.
- Files: `tests/test_milp.py:131`, `tests/test_milp.py:160`, `src/drt/milp.py`
- Risk: Simplified or incorrect exact-model constraints can pass tests that only validate result shape.
- Priority: Medium

---

*Concerns audit: 2026-06-14*
