# Codebase Concerns

**Analysis Date:** 2026-06-16

## Tech Debt

**Mixed import roots make execution sensitive to invocation style:**
- Issue: Core modules import the installed package namespace `drt.*`, while experiment modules import repository-root paths such as `src.drt.*`.
- Files: `src/drt/alns.py:19`, `src/drt/insertion.py:21`, `src/drt/feasibility.py:22`, `src/drt/milp.py:26`, `experiments/variants.py:43`, `experiments/scenarios.py:21`
- Impact: `PYTHONPATH=src pytest tests` passes, but root-level archive collection imports `experiments.variants`, then `src.drt.alns`, then `drt.candidate`, which fails when `drt` is not installed or `PYTHONPATH` is not set.
- Fix approach: Standardize all first-party imports on `drt.*` for package code and experiment code. Add a single pytest/package bootstrap in `pyproject.toml` or `tests/conftest.py` instead of relying on command-specific `PYTHONPATH`.

**Dependency metadata omits active runtime imports:**
- Issue: `pyproject.toml` declares only `gurobipy` and `numpy`, but active experiment, validation, and figure paths import `pandas` and `matplotlib`.
- Files: `pyproject.toml:8`, `pyproject.toml:11`, `pyproject.toml:12`, `experiments/runner.py:29`, `experiments/formal_validation.py:12`, `experiments/formal_statistics.py:16`, `run_experiments.py:8`, `manuscript/figures/scripts/fig07_pareto.py:14`
- Impact: A clean install can satisfy package metadata while `python run_experiments.py`, formal validation, or figure generation fails on undeclared packages.
- Fix approach: Add explicit dependencies or extras such as `experiments = ["pandas"]`, `figures = ["matplotlib", "pandas"]`, and keep `pytest`/`pytest-benchmark` in the existing dev extra.

**Route stop representation is implicit and overloaded:**
- Issue: `Route.stops` is an untyped `list`; code uses both plain `(MeetingPoint, time)` tuples and tagged `(MeetingPoint, time, request_id, role)` tuples.
- Files: `src/drt/types.py:202`, `src/drt/types.py:208`, `src/drt/alns.py:73`, `src/drt/alns.py:102`, `src/drt/alns.py:347`, `experiments/variants.py:395`, `src/drt/feasibility.py:93`
- Impact: Tuple-length checks and adapters make it easy to drop request metadata, mis-handle completed trips, or pass a tagged stop into code that expects exactly two tuple fields.
- Fix approach: Introduce a `RouteStop` dataclass with explicit `meeting_point`, `time`, `request_id`, and `role`. Keep any plain-stop adapter narrow and localized at insertion/feasibility boundaries.

**Core ALNS module mixes several responsibilities:**
- Issue: `src/drt/alns.py` contains state containers, cost helpers, destroy operators, repair operators, rolling-horizon simulation, diagnostics, and benchmark generation in one 723-line module.
- Files: `src/drt/alns.py`
- Impact: A small change to rolling-horizon state can affect operators, diagnostics, and benchmark behavior. The local tuple conventions are hard to audit.
- Fix approach: Split into focused modules such as `src/drt/alns_state.py`, `src/drt/operators.py`, `src/drt/rolling_horizon.py`, and `src/drt/benchmark.py` while preserving public imports during migration.

**Stale operational notes conflict with current repository state:**
- Issue: `README.md` contains a "Known Issues" section claiming the git repository is broken and `.planning/` has duplicate `_v2` files, while `git status --short` currently reports only untracked `.planning/phases/`.
- Files: `README.md:98`, `README.md:100`, `README.md:106`, `.planning/codebase/CONCERNS.md`
- Impact: Operators may avoid normal git workflows or spend time investigating already-resolved repository issues.
- Fix approach: Refresh `README.md` known issues from current `git status`, `.planning/`, and test behavior. Move historical cleanup notes into `archive/` if they still matter.

**Unused helper code remains in the algorithm path:**
- Issue: `_assigned_requests` contains a `pass` branch and always returns an empty list.
- Files: `src/drt/alns.py:152`, `src/drt/alns.py:161`, `src/drt/alns.py:163`
- Impact: Future callers can assume it returns assigned `Request` objects and silently receive no assignments.
- Fix approach: Remove the helper if unused, or implement it against an explicit request registry and add tests before using it.

## Known Bugs

**Bare `pytest` fails by collecting archived ad hoc tests:**
- Symptoms: Running `pytest` from the repository root collects `archive/adhoc_tests/*.py` and stops during collection with `ModuleNotFoundError: No module named 'drt'`.
- Files: `archive/adhoc_tests/smoke_test.py`, `archive/adhoc_tests/test_fix.py`, `archive/adhoc_tests/test_scale100.py`, `archive/adhoc_tests/test_scale500.py`, `pyproject.toml`
- Trigger: Run `pytest` from the repository root without restricting collection to `tests/`.
- Workaround: Run `$env:PYTHONPATH='src'; pytest tests` on Windows PowerShell. This scan observed `189 passed, 1 skipped` for that command.
- Fix approach: Add pytest config to `pyproject.toml` with `testpaths = ["tests"]` and `pythonpath = ["src"]`, and exclude or rename archived ad hoc scripts so they are not test-discovery targets.

**Documented test command is not the green test command:**
- Symptoms: `README.md` documents `pytest`, but the passing command requires `PYTHONPATH=src` and `tests` scoping.
- Files: `README.md:83`, `pyproject.toml`, `tests/`, `archive/adhoc_tests/`
- Trigger: Follow the README test instructions from a clean shell.
- Workaround: Use `$env:PYTHONPATH='src'; pytest tests`.
- Fix approach: Make root `pytest` pass, then keep `README.md` aligned with the configured command.

**`MetricsResult.social_welfare` defaults to zero and is not populated by `compute_metrics`:**
- Symptoms: `MetricsResult` exposes `social_welfare`, but `compute_metrics()` returns `MetricsResult(...)` without passing it.
- Files: `experiments/metrics.py:88`, `experiments/metrics.py:131`, `experiments/metrics.py:246`, `experiments/pareto_sweep.py:59`
- Trigger: Any caller reads `compute_metrics(result).social_welfare`.
- Workaround: Call `compute_social_welfare(result.records, gamma)` directly, as `experiments/pareto_sweep.py` does.
- Fix approach: Either remove the field from `MetricsResult` or add a deliberate `gamma` parameter to `compute_metrics()` and populate the value.

**Policy recommendation metrics can silently fall back to hardcoded values:**
- Symptoms: `_extract_metrics_data()` substitutes `2383.85` and `3662.33` when FullModel or DoorToDoor vehicle-km values are missing.
- Files: `analysis/policy.py:149`, `analysis/policy.py:183`, `analysis/policy.py:185`, `analysis/policy.py:203`
- Trigger: Missing or malformed rows in the metrics CSV consumed by `generate_policy_recommendations()`.
- Workaround: Manually inspect generated `results/policy_recommendations.md` and source CSVs before using policy text in the manuscript.
- Fix approach: Raise a validation error or emit an explicit missing-data status instead of substituting constants.

## Security Considerations

**No external secret-reading path detected in active code:**
- Risk: Not detected for `.env` reads, API keys, credential files, or networked external services.
- Files: `src/drt/`, `experiments/`, `analysis/`, `pyproject.toml`
- Current mitigation: Active code uses local generated scenarios, local CSV/JSON outputs, and optional local Gurobi access through `gurobipy`.
- Recommendations: Keep `.env*`, key files, certificates, and solver license details out of outputs. Do not log local license paths or credentials in benchmark artifacts.

**CSV and Markdown outputs overwrite local result files directly:**
- Risk: Experiment and analysis scripts write into `results/` paths without atomic replacement, run isolation, or overwrite confirmation.
- Files: `experiments/runner.py:112`, `experiments/runner.py:409`, `experiments/runner.py:428`, `analysis/policy.py:354`, `analysis/policy.py:355`, `src/drt/milp.py:445`
- Current mitigation: Default paths are hardcoded under the repo rather than user-controlled remote paths.
- Recommendations: Write run outputs to a timestamped or manifest-named directory, then promote canonical artifacts through an explicit copy/alias step.

**Gurobi execution consumes licensed solver resources when available:**
- Risk: `DRTModel.solve()` runs the optimizer with a 300-second default time limit; gap scripts can launch multiple solver runs.
- Files: `src/drt/milp.py:50`, `src/drt/milp.py:63`, `src/drt/milp.py:130`, `src/drt/milp.py:376`, `experiments/milp_gap.py:176`
- Current mitigation: Solver output is disabled with `OutputFlag = 0`, `TimeLimit` is set, and tests skip when Gurobi or a license is unavailable.
- Recommendations: Gate MILP experiments behind an explicit config/CLI flag, record solver status only, and avoid writing license/environment details to result artifacts.

## Performance Bottlenecks

**Insertion evaluation is combinatorial in vehicles, candidates, and route positions:**
- Problem: `evaluate_insertion()` enumerates every vehicle, pickup candidate, dropoff candidate, pickup position, and dropoff position.
- Files: `src/drt/insertion.py:76`, `src/drt/insertion.py:83`, `src/drt/insertion.py:85`, `src/drt/insertion.py:86`, `src/drt/alns.py:391`, `src/drt/alns.py:393`
- Cause: Complexity grows roughly with `vehicles * pickup_candidates * dropoff_candidates * route_length^2` per request, and ALNS repeats similar enumeration in repair operators.
- Improvement path: Cache candidate sets, maintain incremental route schedules/distances, prefilter positions by time-window bounds, and add lower-bound pruning before calling full feasibility checks.

**ALNS operators perform broad deep copies and route conversion:**
- Problem: Destroy and repair operators repeatedly copy the full `ALNSState` and rebuild plain route dictionaries.
- Files: `src/drt/alns.py:182`, `src/drt/alns.py:199`, `src/drt/alns.py:232`, `src/drt/alns.py:272`, `src/drt/alns.py:305`, `src/drt/alns.py:347`
- Cause: Mutable shared route state and untyped stop tuples force defensive full-state copying.
- Improvement path: Use copy-on-write per changed vehicle route, typed immutable route snapshots, or a small state-diff structure for candidate ALNS moves.

**MILP variable construction scales as request x vehicle x pickup-candidate x dropoff-candidate:**
- Problem: `DRTModel.build()` creates binary assignment variables and multiple constraint families over nested request, vehicle, pickup, and dropoff loops.
- Files: `src/drt/milp.py:144`, `src/drt/milp.py:145`, `src/drt/milp.py:146`, `src/drt/milp.py:147`, `src/drt/milp.py:260`, `src/drt/milp.py:275`
- Cause: Candidate sets are expanded into explicit binary variables for every request-vehicle-candidate combination.
- Improvement path: Keep MILP use limited to small diagnostic instances, persist skipped/no-Gurobi status, and add size guards before model construction.

## Fragile Areas

**Feasibility checker approximates existing stop roles by alternating pickup/dropoff:**
- Files: `src/drt/feasibility.py:113`, `src/drt/feasibility.py:121`, `src/drt/feasibility.py:128`, `src/drt/feasibility.py:129`, `src/drt/feasibility.py:131`
- Why fragile: Existing stops without role metadata are assumed to alternate pickup and dropoff. Non-alternating route sequences can produce incorrect capacity decisions.
- Safe modification: Require explicit role metadata or pass an occupancy trace into `check_feasibility()`.
- Test coverage: `tests/test_feasibility.py` covers basic constraints, but it does not cover non-alternating existing routes or tagged route stops.

**Completed rolling-horizon trips lose assignment details used by metrics:**
- Files: `src/drt/alns.py:476`, `src/drt/alns.py:511`, `src/drt/alns.py:655`, `experiments/variants.py:410`, `experiments/variants.py:454`, `experiments/variants.py:455`, `experiments/variants.py:460`
- Why fragile: Completed/pruned requests are tracked by id and pickup time, but pickup/dropoff meeting points are no longer available; metric reconstruction uses zero walking distance and fallback IVT behavior.
- Safe modification: Maintain a per-request service ledger containing pickup/dropoff meeting points, scheduled times, status, and vehicle id. Build `PassengerRecord` from that ledger instead of reconstructing from final route stops.
- Test coverage: `tests/test_alns.py` checks completion bookkeeping, and `tests/test_variants.py` checks ranges/types, but exact walk/IVT reconstruction for completed requests is not asserted.

**MILP model is a static simplified diagnostic, not exact online route sequencing:**
- Files: `src/drt/milp.py:13`, `src/drt/milp.py:15`, `src/drt/milp.py:185`, `src/drt/milp.py:186`, `src/drt/milp.py:312`, `manuscript/sections/experiments.tex:154`
- Why fragile: Capacity is modeled as total requests assigned to a vehicle, operational cost uses pickup-to-dropoff terms, and the model does not include full vehicle route order.
- Safe modification: Keep this MILP labeled as a small static benchmark, or introduce sequence/order variables before using it as a route-sequencing optimum.
- Test coverage: `tests/test_milp.py` validates shapes/statuses and skips on missing Gurobi, but it does not compare against a hand-verified route-sequencing optimum.

**Gamma and rejection penalty are post-hoc rather than behavioral controls:**
- Files: `experiments/config.py:34`, `experiments/config.py:36`, `experiments/variants.py:74`, `experiments/pareto_sweep.py:59`, `experiments/metrics.py:246`
- Why fragile: `ALPHA_WEIGHTS[4]` is explicitly not used in routing, and Pareto social welfare is computed after the run. Users may interpret gamma as changing assignment, acceptance, or routing decisions.
- Safe modification: Keep the post-hoc interpretation explicit in output names and manuscript text, or wire gamma into the objective/choice path with tests showing changed behavior.
- Test coverage: No test asserts that gamma is intentionally post-hoc or that behavior remains unchanged across gamma values.

**Beijing scenario comments encode a model compromise in code:**
- Files: `experiments/scenarios.py:152`, `experiments/scenarios.py:186`, `experiments/scenarios.py:187`, `experiments/scenarios.py:189`
- Why fragile: The code uses an 80-point 9x9 grid with 1875 m spacing while comments note that a planned "~500m spacing" would require a different grid.
- Safe modification: Move the compromise into a named scenario parameter or config manifest, and keep method labels clear that this is semi-realistic synthetic Beijing data.
- Test coverage: `tests/test_scenarios.py` validates current counts/ranges, not empirical representativeness.

## Scaling Limits

**Scenario generation hard-caps demand at 1000 requests:**
- Current capacity: `generate_synthetic()` and `generate_beijing()` accept at most `_MAX_REQUESTS = 1000`.
- Limit: Larger stress or city-scale simulations raise `ValueError`.
- Scaling path: Keep the cap for default developer safety, but expose it through configuration and add chunked/stress-run profiles before increasing it.
- Files: `experiments/scenarios.py:27`, `experiments/scenarios.py:46`, `experiments/scenarios.py:65`, `experiments/scenarios.py:152`, `experiments/scenarios.py:176`

**Formal synthetic grid is bounded to selected scales and methods:**
- Current capacity: `FORMAL_SCALES = [100, 200, 300, 500]`, required seeds are `1..20`, and formal main methods are four behavioral variants.
- Limit: No default formal run covers 1000-request stress, all diagnostic variants, or Beijing scenarios.
- Scaling path: Add separate stress manifests with fewer methods/seeds, explicit hardware/runtime metadata, and opt-in timeouts.
- Files: `experiments/phase06_formal.py:21`, `experiments/phase06_formal.py:23`, `experiments/phase06_formal.py:24`, `experiments/phase06_formal.py:33`

**Exact MILP comparisons are solver- and scale-limited:**
- Current capacity: MILP defaults to a 300-second time limit and the gap experiment uses small instances.
- Limit: Gurobi availability and the simplified formulation limit exact-comparison claims.
- Scaling path: Treat MILP outputs as diagnostic only, store `no_gurobi`/timeout status in manifests, and compare large runs against deterministic heuristics or saved fixtures.
- Files: `src/drt/milp.py:63`, `src/drt/milp.py:130`, `experiments/milp_gap.py:176`, `experiments/milp_gap.py:263`

## Dependencies at Risk

**`gurobipy`:**
- Risk: Declared as a default dependency, but license availability is machine-specific and many tests skip when it is unavailable.
- Impact: Exact-model tests and MILP gap outputs can be unverified on machines without a working Gurobi license.
- Migration plan: Move `gurobipy` to an optional `milp` extra if heuristic/experiment workflows should install without a commercial solver, and keep saved fixture outputs for CI checks.
- Files: `pyproject.toml:11`, `src/drt/milp.py:103`, `src/drt/milp.py:376`, `tests/test_milp.py:138`, `tests/test_milp.py:232`

**`pandas` and `matplotlib`:**
- Risk: Used by active experiment, validation, statistics, and figure scripts but absent from project dependency metadata.
- Impact: Reproducibility depends on globally installed packages outside `pyproject.toml`.
- Migration plan: Add explicit dependency extras and document install commands for experiment reproduction and figure generation.
- Files: `experiments/runner.py:29`, `experiments/formal_statistics.py:16`, `experiments/formal_statistics.py:808`, `run_experiments.py:8`, `manuscript/figures/scripts/fig05_sensitivity.py:8`, `pyproject.toml:8`

**Unpinned dependency versions:**
- Risk: `pyproject.toml` has no upper or lower bounds for `gurobipy` and `numpy` beyond build-system packages.
- Impact: Solver APIs, NumPy percentile behavior, and pandas/matplotlib behavior can drift between environments.
- Migration plan: Add a lockfile or constraints file for paper reproduction, and record dependency versions in formal run manifests.
- Files: `pyproject.toml:8`, `pyproject.toml:11`, `pyproject.toml:12`, `experiments/phase06_formal.py:119`, `experiments/runner.py:199`

## Missing Critical Features

**Root pytest configuration is missing:**
- Problem: There is no `tool.pytest.ini_options` block configuring `testpaths`, `pythonpath`, or archive exclusions.
- Blocks: The documented `pytest` command and common CI defaults.
- Files: `pyproject.toml`, `README.md:83`, `tests/`, `archive/adhoc_tests/`

**Machine-readable dependency and environment provenance is incomplete:**
- Problem: Runner manifests record git hash/status counts, but not Python version, dependency versions, OS, CPU, or Gurobi version/license status.
- Blocks: Exact reproduction of paper tables and timing claims across machines.
- Files: `experiments/runner.py:199`, `experiments/runner.py:240`, `experiments/phase06_formal.py:119`, `experiments/phase06_formal.py:183`

**Real data ingestion is not implemented for the Beijing case:**
- Problem: `generate_beijing()` creates a semi-realistic synthetic scenario rather than loading public trip, road, or meeting-point data.
- Blocks: Claims that require reproducible empirical Beijing data rather than generated demand.
- Files: `experiments/scenarios.py:152`, `docs/工作3公开数据集.txt`, `results/beijing_results.csv`

**Endogenous policy control via gamma is not implemented:**
- Problem: Gamma is available for post-hoc welfare scoring, but not for route choice, offer construction, or acceptance decisions.
- Blocks: Interpreting Pareto outputs as behaviorally endogenous policy optimization.
- Files: `experiments/config.py:34`, `experiments/pareto_sweep.py:59`, `experiments/metrics.py:246`, `experiments/variants.py:74`

## Test Coverage Gaps

**Default test command coverage:**
- What's not tested: Root `pytest` is not green because archived tests are collected and package path setup is missing.
- Files: `pyproject.toml`, `README.md:83`, `archive/adhoc_tests/`, `tests/`
- Risk: New contributors and automation hit collection errors before reaching the maintained suite.
- Priority: High

**Route-stop and completed-trip metric exactness:**
- What's not tested: Exact pickup/dropoff meeting points, walk distances, and IVT for completed rolling-horizon requests after route pruning.
- Files: `src/drt/alns.py:511`, `experiments/variants.py:454`, `experiments/variants.py:455`, `tests/test_alns.py:269`, `tests/test_variants.py`
- Risk: Reported fairness, walking, and detour metrics can diverge from assigned service details.
- Priority: High

**Feasibility with non-alternating existing stops:**
- What's not tested: Capacity correctness when an existing route has pickup/dropoff roles that do not alternate from index zero.
- Files: `src/drt/feasibility.py:128`, `tests/test_feasibility.py:69`
- Risk: Insertion feasibility can reject feasible moves or accept infeasible ones in realistic shared routes.
- Priority: High

**Gamma/Pareto semantics:**
- What's not tested: Whether `FullModel(gamma=...)` should change behavior or remain a post-hoc welfare-only parameter.
- Files: `experiments/config.py:34`, `experiments/pareto_sweep.py:59`, `tests/test_variants.py`, `tests/test_metrics.py`
- Risk: Policy-sweep outputs can be misread as endogenous optimization results.
- Priority: Medium

**Dependency/install smoke tests:**
- What's not tested: A fresh `pip install -e .` plus `python run_experiments.py` in an environment containing only declared dependencies.
- Files: `pyproject.toml:8`, `run_experiments.py:8`, `experiments/runner.py:29`
- Risk: Missing `pandas`/`matplotlib` metadata remains invisible on developer machines that already have those packages installed.
- Priority: Medium

**MILP exactness beyond status smoke tests:**
- What's not tested: Hand-verifiable tiny instances with expected objective value, accepted set, schedule, and route feasibility.
- Files: `src/drt/milp.py`, `tests/test_milp.py:138`, `tests/test_milp.py:250`
- Risk: Simplified exact-model constraints can pass status-oriented tests while supporting claims beyond their diagnostic scope.
- Priority: Medium

---

*Concerns audit: 2026-06-16*
