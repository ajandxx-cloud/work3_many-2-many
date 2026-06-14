<!-- refreshed: 2026-06-14 -->
# Architecture

**Analysis Date:** 2026-06-14

## System Overview

```text
┌─────────────────────────────────────────────────────────────┐
│                    Execution / Reporting                     │
├──────────────────┬──────────────────┬───────────────────────┤
│ Experiment runs  │ Analysis scripts │ Manuscript figures    │
│ `run_experiments.py` │ `analysis/`  │ `manuscript/figures/scripts/` │
│ `experiments/runner.py` │          │                       │
└────────┬─────────┴────────┬─────────┴──────────┬────────────┘
         │                  │                     │
         ▼                  ▼                     ▼
┌─────────────────────────────────────────────────────────────┐
│                  Scenario / Variant Layer                    │
│ `experiments/scenarios.py`, `experiments/variants.py`,       │
│ `experiments/metrics.py`, `experiments/config.py`            │
└────────────────────────────┬────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────┐
│                  Core DRT Algorithm Library                  │
│ `src/drt/types.py`, `src/drt/candidate.py`,                  │
│ `src/drt/insertion.py`, `src/drt/feasibility.py`,            │
│ `src/drt/alns.py`, `src/drt/choice.py`, `src/drt/milp.py`    │
└────────────────────────────┬────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────┐
│                  Outputs / Publication Artifacts             │
│ `results/`, `manuscript/`, `docs/`, `archive/`               │
└─────────────────────────────────────────────────────────────┘
```

## Component Responsibilities

| Component | Responsibility | File |
|-----------|----------------|------|
| Domain dataclasses | Owns `Request`, `Vehicle`, `MeetingPoint`, `Bundle`, `Route`, and `PassengerType`; use these as the shared data contract across algorithms and experiments. | `src/drt/types.py` |
| Public package API | Re-exports common domain types and choice helpers for `from drt import ...` callers. | `src/drt/__init__.py` |
| Candidate generation | Filters meeting points by walking radius and returns nearest top-k pickup or dropoff candidates. | `src/drt/candidate.py` |
| Passenger choice | Computes MNL utility and binary logit acceptance probability for one offered service bundle. | `src/drt/choice.py` |
| Feasibility checking | Validates proposed pickup/dropoff route insertions against capacity, time-window, ride-time, precedence, and route-duration constraints. | `src/drt/feasibility.py` |
| Insertion evaluator | Enumerates vehicles, insertion positions, pickup candidates, and dropoff candidates; returns the lowest-cost feasible insertion. | `src/drt/insertion.py` |
| ALNS heuristic | Maintains mutable routing state, destroy/repair operators, greedy/regret insertion, and online rolling-horizon simulation. | `src/drt/alns.py` |
| Exact MILP baseline | Builds and solves static Gurobi assignment/scheduling snapshots for small or benchmark cases. | `src/drt/milp.py` |
| Experiment constants | Centralizes seeds, scales, vehicle counts, walking radii, rolling-horizon windows, and cost weights. | `experiments/config.py` |
| Scenario generators | Creates synthetic and Beijing scenario dataclasses with requests, vehicles, meeting points, area size, and scenario name. | `experiments/scenarios.py` |
| Model variants | Defines runnable experimental units that adapt core algorithms into baselines, ablations, and `FullModel`. | `experiments/variants.py` |
| Metrics | Converts per-passenger simulation records into aggregate acceptance, wait, walk, detour, fairness, CPU, and welfare metrics. | `experiments/metrics.py` |
| Experiment runner | Orchestrates variants across scales/seeds, catches per-variant errors/timeouts, and writes result CSVs. | `experiments/runner.py` |
| Root runner | Runs the full experiment suite and prints summary validation from `results/metrics_table.csv`. | `run_experiments.py` |
| Analysis scripts | Runs post-hoc sensitivity, equity, and policy analyses from experiment outputs. | `analysis/sensitivity.py`, `analysis/equity.py`, `analysis/policy.py` |

## Pattern Overview

**Overall:** Layered research simulation package with a reusable algorithm core, experiment composition layer, and file-based result pipeline.

**Key Characteristics:**
- Keep core algorithm code in `src/drt/` independent of `experiments/`, `analysis/`, `results/`, and manuscript generation.
- Treat `experiments/scenarios.py` and `experiments/metrics.py` dataclasses as the contract between scenario generation, variants, runners, and analysis.
- Compose model behavior through `BaseVariant` subclasses in `experiments/variants.py`; do not fork the runner for each algorithm comparison.
- Persist experiment outputs as CSV/JSON/Markdown under `results/`, then let `analysis/` and `manuscript/figures/scripts/` consume those outputs.

## Layers

**Core Domain Model:**
- Purpose: Define the typed objects every algorithm passes around.
- Location: `src/drt/types.py`
- Contains: Python dataclasses for requests, vehicles, routes, meeting points, service bundles, and passenger types.
- Depends on: Standard library `dataclasses`.
- Used by: `src/drt/candidate.py`, `src/drt/choice.py`, `src/drt/feasibility.py`, `src/drt/insertion.py`, `src/drt/alns.py`, `src/drt/milp.py`, `experiments/scenarios.py`, `experiments/variants.py`.
- Use this layer when adding fields that are part of the system-wide DRT data contract.

**Primitive Algorithm Services:**
- Purpose: Provide small, reusable operations used by both exact and heuristic solvers.
- Location: `src/drt/candidate.py`, `src/drt/choice.py`, `src/drt/feasibility.py`, `src/drt/insertion.py`
- Contains: Euclidean distance helpers, candidate filters, MNL utility/probability, feasibility checks, and best-insertion search.
- Depends on: `src/drt/types.py`; `src/drt/insertion.py` also depends on `src/drt/candidate.py` and `src/drt/feasibility.py`.
- Used by: `src/drt/alns.py`, `src/drt/milp.py`, `experiments/variants.py`.
- Use this layer for behavior that should be available outside a specific experiment variant.

**Optimization Layer:**
- Purpose: Implement solver strategies over the primitive services.
- Location: `src/drt/alns.py`, `src/drt/milp.py`
- Contains: `ALNSState`, destroy/repair operators, `RollingHorizon`, simulation benchmark helpers, and `DRTModel`.
- Depends on: `src/drt/types.py`, `src/drt/candidate.py`, `src/drt/feasibility.py`, `src/drt/insertion.py`, and optional `gurobipy` in `src/drt/milp.py`.
- Used by: `experiments/variants.py`, `experiments/milp_gap.py`, tests under `tests/`.
- Keep long-running or solver-specific behavior here rather than embedding it in `experiments/runner.py`.

**Experiment Composition Layer:**
- Purpose: Turn solvers into comparable research variants and produce uniform metrics.
- Location: `experiments/config.py`, `experiments/scenarios.py`, `experiments/variants.py`, `experiments/metrics.py`
- Contains: parameter grids, scenario generators, `BaseVariant` subclasses, `PassengerRecord`, `SimulationResult`, and `MetricsResult`.
- Depends on: `src/drt/` core algorithms and dataclasses.
- Used by: `experiments/runner.py`, `analysis/`, `tests/`, root `run_experiments.py`.
- Add a new model comparison by creating a new `BaseVariant` subclass in `experiments/variants.py` and registering it in `ALL_VARIANTS`.

**Run Orchestration Layer:**
- Purpose: Execute experiment matrices and write durable result files.
- Location: `run_experiments.py`, `experiments/runner.py`, focused experiment modules such as `experiments/weight_sensitivity.py`, `experiments/pareto_sweep.py`, `experiments/matched_coverage.py`, `experiments/endogenous_matched_coverage.py`, `experiments/milp_gap.py`
- Contains: loops over scales/seeds/variants, per-variant timeout isolation, CSV/JSON writers, console summaries.
- Depends on: `experiments/config.py`, `experiments/scenarios.py`, `experiments/variants.py`, `experiments/metrics.py`.
- Used by: humans running experiments and tests under `tests/test_runner.py`.
- Keep new result-producing scripts in `experiments/` when they run simulations; keep post-hoc readers in `analysis/`.

**Post-Hoc Analysis Layer:**
- Purpose: Convert result files into policy, sensitivity, and equity artifacts.
- Location: `analysis/sensitivity.py`, `analysis/equity.py`, `analysis/policy.py`
- Contains: sensitivity sweeps, equity aggregation, and policy recommendation generation.
- Depends on: `experiments/` APIs and CSV files in `results/`.
- Used by: publication workflow and `analysis/test_sensitivity.py`.
- Use this layer for analysis that reads existing outputs or writes derived CSV/Markdown.

**Publication Artifact Layer:**
- Purpose: Store the manuscript, figure sources, generated figures, and archived materials.
- Location: `manuscript/`, `manuscript/figures/scripts/`, `docs/`, `archive/`
- Contains: LaTeX paper files, figure scripts, proposal/notes, historical outputs, and superseded drafts.
- Depends on: CSV/JSON results and local plotting scripts.
- Used by: manual publication workflow.
- Keep executable research code out of `manuscript/` except figure-specific scripts under `manuscript/figures/scripts/`.

## Data Flow

### Primary Experiment Path

1. Root script starts the full experiment suite (`run_experiments.py:1`).
2. The runner loads shared scales, seeds, and variant registry (`experiments/runner.py:32`, `experiments/variants.py:733`).
3. For each scale/seed, scenarios are generated as `Scenario` dataclasses (`experiments/runner.py:103`, `experiments/scenarios.py:30`, `experiments/scenarios.py:46`, `experiments/scenarios.py:152`).
4. Each registered variant executes `variant.run(scenario)` through the common `BaseVariant` template method (`experiments/runner.py:188`, `experiments/variants.py:161`).
5. Variant-specific `_solve()` implementations call greedy insertion, rolling horizon, MNL filtering, or synthetic door-to-door meeting points (`experiments/variants.py:361`, `experiments/variants.py:554`, `experiments/variants.py:598`, `experiments/variants.py:650`, `experiments/variants.py:694`).
6. Core algorithms generate candidates, check feasibility, and update route state (`src/drt/candidate.py:19`, `src/drt/feasibility.py:46`, `src/drt/insertion.py:49`, `src/drt/alns.py:480`).
7. `BaseVariant.run()` converts the final state into per-passenger records and a `SimulationResult` (`experiments/variants.py:166`, `experiments/variants.py:211`).
8. `compute_metrics()` turns records into aggregate metrics (`experiments/metrics.py:114`).
9. The runner writes raw and aggregate CSVs under `results/` (`experiments/runner.py:129`, `experiments/runner.py:218`, `experiments/runner.py:227`).
10. The root runner reads `results/metrics_table.csv` and prints the thesis-check summary (`run_experiments.py:15`).

### Rolling-Horizon FullModel Flow

1. `FullModel._solve()` builds a vehicle dictionary and constructs `RollingHorizon` with scenario meeting points and experiment constants (`experiments/variants.py:598`, `experiments/variants.py:601`).
2. Requests are sorted by earliest time and filtered through deterministic MNL Bernoulli acceptance (`experiments/variants.py:615`, `experiments/variants.py:619`, `experiments/variants.py:78`).
3. `RollingHorizon.run_simulation()` streams request arrivals and triggers `reoptimize()` at `DELTA` intervals (`src/drt/alns.py:626`, `src/drt/alns.py:644`, `src/drt/alns.py:653`).
4. `RollingHorizon.reoptimize()` prunes completed stops, filters active requests by horizon, and builds an `ALNSState` (`src/drt/alns.py:480`, `src/drt/alns.py:491`, `src/drt/alns.py:530`, `src/drt/alns.py:557`).
5. Destroy operators remove assigned requests and repair operators reinsert requests with greedy/regret insertion (`src/drt/alns.py:569`, `src/drt/alns.py:583`, `src/drt/alns.py:590`).
6. Feasible route changes are accepted when they reduce unassigned requests or tie-break on cost (`src/drt/alns.py:598`).
7. `FullModel._solve()` converts `RollingHorizon` state back to `ALNSState` with completed IDs, accumulated vehicle-km, and pickup times (`experiments/variants.py:623`, `experiments/variants.py:630`).

### MILP Benchmark Flow

1. Experiment code instantiates `DRTModel` with requests, vehicles, meeting points, radii, weights, time limit, and MIP gap (`src/drt/milp.py:24`, `src/drt/milp.py:47`, `experiments/milp_gap.py:111`).
2. `DRTModel.build()` lazily imports `gurobipy`, generates candidate pickup/dropoff sets, creates the model, and sets solver controls (`src/drt/milp.py:88`, `src/drt/milp.py:95`, `src/drt/milp.py:110`, `src/drt/milp.py:122`).
3. `DRTModel.solve()` optimizes, maps Gurobi statuses to plain strings, and returns objective, gap, runtime, and accepted request IDs (`src/drt/milp.py:357`, `src/drt/milp.py:383`, `src/drt/milp.py:391`).
4. `write_benchmark()` persists benchmark JSON under `results/` (`src/drt/milp.py:410`).

### Analysis Path

1. Sensitivity scripts run selected variants over alternate walking radii or fleet sizes and write `results/sensitivity_walk.csv` and `results/sensitivity_fleet.csv` (`analysis/sensitivity.py:49`, `analysis/sensitivity.py:111`).
2. Equity analysis runs `FullModel` across configured seeds, groups `PassengerRecord` objects by passenger type, and writes `results/equity_table.csv` (`analysis/equity.py:38`, `analysis/equity.py:98`).
3. Policy generation reads hardcoded result CSVs and writes `results/policy_recommendations.md` (`analysis/policy.py:203`, `analysis/policy.py:217`).

**State Management:**
- Core dataclasses are plain Python objects; most state is passed explicitly through function parameters and return values.
- `ALNSState` in `src/drt/alns.py` is mutable and is copied with `deepcopy()` during destroy/repair search.
- `RollingHorizon` stores controller state on the instance: `routes`, `active_requests`, `request_registry`, `completed_request_ids`, `accumulated_vehicle_km`, and `pickup_times`.
- Experiment-wide constants are module-level values in `experiments/config.py`; inject alternate parameters through variant constructors where supported, as in `analysis/sensitivity.py`.
- Result persistence is file-based under `results/`; analysis scripts read CSVs and write derived artifacts.

## Key Abstractions

**Request / Vehicle / MeetingPoint / Bundle / Route / PassengerType:**
- Purpose: Shared vocabulary for all routing, choice, and experiment code.
- Examples: `src/drt/types.py`, `experiments/scenarios.py`, `experiments/variants.py`
- Pattern: Dataclass-based domain model. Add system-wide fields here before threading them through algorithms.

**Scenario:**
- Purpose: Bundles requests, vehicles, meeting points, operating area, and scenario name as one simulation input.
- Examples: `experiments/scenarios.py:30`, `experiments/scenarios.py:46`, `experiments/scenarios.py:152`
- Pattern: Dataclass input contract consumed by every `BaseVariant.run()` implementation.

**InsertionResult:**
- Purpose: Represents the best feasible insertion for one request, including vehicle ID, pickup/dropoff positions, chosen meeting points, and incremental cost.
- Examples: `src/drt/insertion.py:27`, `src/drt/alns.py:102`
- Pattern: Small result object from search functions; apply through `_apply_insertion()` instead of mutating route state inside candidate enumeration.

**ALNSState:**
- Purpose: Holds route assignments, unassigned requests, cost, completed IDs, completed vehicle-km, and pickup times during heuristic solving.
- Examples: `src/drt/alns.py:30`, `experiments/variants.py:193`, `experiments/variants.py:630`
- Pattern: Mutable search state copied between ALNS iterations; route stops carry tuple metadata.

**RollingHorizon:**
- Purpose: Online controller that receives arrivals, prunes completed stops, reoptimizes active requests over a fixed horizon, and accumulates completed work.
- Examples: `src/drt/alns.py:431`, `experiments/variants.py:601`, `experiments/variants.py:697`
- Pattern: Stateful service object used by rolling-horizon variants.

**BaseVariant and ALL_VARIANTS:**
- Purpose: Provides a uniform `run(scenario) -> SimulationResult` interface for all experiment units.
- Examples: `experiments/variants.py:161`, `experiments/variants.py:733`
- Pattern: Template method. Implement `_solve()`, reuse `_build_records()` and `_total_vehicle_km()`, then register in `ALL_VARIANTS`.

**PassengerRecord / SimulationResult / MetricsResult:**
- Purpose: Separates route solving from metric aggregation.
- Examples: `experiments/metrics.py:40`, `experiments/metrics.py:55`, `experiments/metrics.py:64`
- Pattern: Dataclass outputs. New metrics should extend `MetricsResult`, `_METRIC_COLS`, `_RAW_COLS`, tests, and CSV writers together.

**DRTModel:**
- Purpose: Exact static snapshot optimizer for MILP benchmarks and small-scale validation.
- Examples: `src/drt/milp.py:24`, `experiments/milp_gap.py`
- Pattern: Build/solve object with lazy solver import and serializable result dict.

## Entry Points

**Full experiment suite:**
- Location: `run_experiments.py`
- Triggers: `python run_experiments.py` from project root.
- Responsibilities: Adds the project root to `sys.path`, calls `experiments.runner.run_all_experiments()`, reads `results/metrics_table.csv`, and prints summary comparisons.

**Experiment runner module:**
- Location: `experiments/runner.py`
- Triggers: `python experiments/runner.py`, `python -m experiments.runner`, tests, or root runner.
- Responsibilities: Generates scenarios, runs every `ALL_VARIANTS` member with timeout isolation, writes `results/synthetic_results.csv`, `results/beijing_results.csv`, and `results/metrics_table.csv`.

**Focused experiments:**
- Location: `experiments/weight_sensitivity.py`, `experiments/pareto_sweep.py`, `experiments/matched_coverage.py`, `experiments/endogenous_matched_coverage.py`, `experiments/milp_gap.py`
- Triggers: Direct script execution or imported function calls.
- Responsibilities: Run narrower research experiments and write dedicated files under `results/`.

**Analysis scripts:**
- Location: `analysis/sensitivity.py`, `analysis/equity.py`, `analysis/policy.py`
- Triggers: Direct script execution, tests, or manual publication workflow.
- Responsibilities: Produce sensitivity CSVs, equity CSVs, and policy recommendation Markdown from simulations/results.

**Core package import:**
- Location: `src/drt/__init__.py`
- Triggers: `from drt import Request, accept_probability` after editable install.
- Responsibilities: Provides the small public API for domain types and MNL helpers.

**MILP solver API:**
- Location: `src/drt/milp.py`
- Triggers: Imported by benchmark scripts/tests or instantiated manually.
- Responsibilities: Build and solve exact static MILP snapshots when `gurobipy` and a license are available.

## Architectural Constraints

- **Threading:** Main algorithms run synchronously. `experiments/runner.py` uses `concurrent.futures.ThreadPoolExecutor(max_workers=1)` only to enforce a per-variant timeout.
- **Global state:** Experiment constants live in `experiments/config.py`; variant registry instances live in `experiments/variants.py` as `ALL_VARIANTS`; passenger-type constants live in `src/drt/types.py`.
- **Mutable route state:** `Route.stops` is an untyped list in `src/drt/types.py`; core algorithms use both plain `(MeetingPoint, time)` tuples and tagged `(MeetingPoint, time, request_id, role)` tuples.
- **Optional solver dependency:** `src/drt/milp.py` defers `gurobipy` import until `build()` or `solve()` so non-MILP code can import the module without Gurobi installed.
- **File outputs:** Runners and analysis scripts write directly under `results/`; callers must pass alternate `results_dir` only where APIs expose it, such as `experiments/runner.py:69`.
- **Request scale cap:** Scenario generation rejects `n_requests > 1000` in `experiments/scenarios.py` to avoid accidental memory-heavy runs.
- **Import path assumptions:** The package is configured for editable install from `src/` in `pyproject.toml`, but some experiment modules import `src.drt.*` directly while tests import `drt.*`.
- **Circular imports:** No core circular imports detected among `src/drt/` modules. Direction flows from `types` to utilities to optimization to experiments.

## Anti-Patterns

### Mixing Import Roots

**What happens:** Some experiment code imports `src.drt.*` (`experiments/scenarios.py`, `experiments/variants.py`) while core and tests import `drt.*` (`src/drt/alns.py`, `tests/test_alns.py`).

**Why it's wrong:** It couples experiments to the repository layout and can create duplicate module identities if both `src.drt` and installed `drt` are loaded in the same process.

**Do this instead:** Use package imports from the configured package root, e.g. `from drt.types import Request` as in `src/drt/alns.py` and `tests/test_candidate.py`.

### Mutating Route Stops With Ad Hoc Tuples

**What happens:** `Route.stops` is declared as a bare `list` in `src/drt/types.py`, while `src/drt/alns.py` reads both 2-tuples and 4-tuples.

**Why it's wrong:** Consumers need defensive `len(stop)` checks, and route meaning is not discoverable from the type contract.

**Do this instead:** Preserve existing tuple compatibility when touching current algorithms, but put any new stop metadata behind a typed abstraction or helper functions close to `src/drt/alns.py` and `src/drt/types.py`.

### Putting New Experiment Logic In The Root Script

**What happens:** `run_experiments.py` is a thin launcher and summary printer.

**Why it's wrong:** Adding variant loops or result writers to the root script bypasses testable APIs in `experiments/runner.py`.

**Do this instead:** Add reusable orchestration to `experiments/runner.py` or a focused script in `experiments/`, then keep `run_experiments.py` as a CLI-style entry point.

## Error Handling

**Strategy:** Use explicit guard clauses for invalid inputs, solver availability, and failed experiment runs; keep full experiment outputs structurally consistent even when one variant fails.

**Patterns:**
- Raise `ValueError` for oversized generated scenarios in `experiments/scenarios.py`.
- Raise `ImportError` with install guidance when `gurobipy` is unavailable in `src/drt/milp.py`.
- Return `(False, reason)` from `check_feasibility()` in `src/drt/feasibility.py` rather than raising for expected infeasible insertions.
- Return `None` from `evaluate_insertion()` in `src/drt/insertion.py` when no feasible insertion exists.
- Catch timeout and generic exceptions per variant in `experiments/runner.py` and emit zero-filled error rows so CSV schemas remain stable.
- Return zero-valued metrics for empty or all-rejected results in `experiments/metrics.py`.

## Cross-Cutting Concerns

**Logging:** Console `print()` is used by runners and analysis scripts (`run_experiments.py`, `experiments/runner.py`, `analysis/sensitivity.py`, `analysis/equity.py`). Core `src/drt/` modules avoid runtime logging.

**Validation:** Unit tests under `tests/` validate candidates, feasibility, insertion, ALNS, MILP behavior, scenarios, variants, metrics, and runner output. Runtime guards live in `experiments/scenarios.py`, `src/drt/milp.py`, `experiments/runner.py`, and module-level unique-name assertion in `experiments/variants.py`.

**Authentication:** Not applicable. This repo has no detected web service, auth provider, user accounts, or secret-backed runtime integration.

**Configuration:** Use `experiments/config.py` for experiment parameters. Use constructor injection for variant-specific overrides, as shown by `FullModel(rho_p=..., rho_d=...)` and `DoorToDoor(rho_p=..., rho_d=...)` in `analysis/sensitivity.py`.

**Persistence:** Treat `results/` as generated experiment output. Treat `manuscript/` and `docs/` as publication/documentation artifacts. Do not make core algorithms depend on files in `results/`.

---

*Architecture analysis: 2026-06-14*
