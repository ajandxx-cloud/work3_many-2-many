<!-- refreshed: 2026-06-16 -->
# Architecture

**Analysis Date:** 2026-06-16

## System Overview

```text
+-------------------------------------------------------------+
|                    Experiment Entry Points                   |
| `run_experiments.py` | `experiments/phase05_pilot.py`        |
| `experiments/phase06_formal.py` | phase06 control modules    |
+---------------------+---------------------------------------+
                      |
                      v
+-------------------------------------------------------------+
|                 Experiment Orchestration Layer               |
| `experiments/runner.py`                                     |
| generates scenarios, invokes variants, computes metrics,     |
| writes CSV/JSON/manifest artifacts                           |
+---------------------+---------------------------------------+
                      |
                      v
+-------------------------------------------------------------+
|                    Variant Adapter Layer                     |
| `experiments/variants.py`                                   |
| maps service designs and evidence labels to DRT algorithms   |
+-------------+---------------+---------------+---------------+
              |               |               |
              v               v               v
+-------------+----+  +-------+--------+  +---+---------------+
| Choice Model     |  | Heuristic DRT  |  | Exact Diagnostic  |
| `src/drt/choice.py`| | `src/drt/alns.py`| | `src/drt/milp.py`|
| `src/drt/types.py` | | `insertion.py` | | Gurobi snapshot  |
+-------------+----+  | `feasibility.py`| +-------------------+
              |       | `candidate.py`  |
              |       +-------+---------+
              |               |
              v               v
+-------------------------------------------------------------+
|               Analysis, Tables, Figures, Manuscript          |
| `analysis/` | `experiments/formal_statistics.py`             |
| `manuscript/figures/scripts/` | `results/` | `manuscript/`  |
+-------------------------------------------------------------+
```

## Component Responsibilities

| Component | Responsibility | File |
|-----------|----------------|------|
| Core data model | Dataclasses for requests, vehicles, meeting points, offers, choice logs, routes, and passenger types. | `src/drt/types.py` |
| Candidate generator | Filters and ranks pickup/dropoff meeting points by walking radius and top-k distance. | `src/drt/candidate.py` |
| Feasibility checker | Checks insertion precedence, time windows, capacity, ride time, and route duration. | `src/drt/feasibility.py` |
| Insertion evaluator | Enumerates vehicle/position/meeting-point combinations and returns the lowest-cost feasible insertion. | `src/drt/insertion.py` |
| Choice model | Computes MNL/binary-logit utility, deterministic passenger type assignment, and offer evaluation logs. | `src/drt/choice.py` |
| ALNS and rolling horizon | Maintains mutable route state, applies destroy/repair operators, and reoptimizes active requests over a rolling horizon. | `src/drt/alns.py` |
| Exact diagnostic model | Builds and solves a static Gurobi MILP snapshot for small/diagnostic comparisons. | `src/drt/milp.py` |
| Scenario generation | Builds synthetic and Beijing-style `Scenario` inputs used by all variants. | `experiments/scenarios.py` |
| Variant adapter layer | Defines service-design variants, translates `Scenario` inputs into algorithm calls, and converts route states into `SimulationResult`. | `experiments/variants.py` |
| Experiment runner | Runs variant matrices across scales/seeds/scenarios, handles per-variant timeout rows, writes raw and aggregate CSV files. | `experiments/runner.py` |
| Metrics layer | Converts `SimulationResult` records into acceptance, vehicle-km, wait, walk, IVT, detour, fairness, and rejection metrics. | `experiments/metrics.py` |
| Phase 5 harness | Runs a pilot-only subset of behavioral variants into isolated pilot outputs. | `experiments/phase05_pilot.py` |
| Phase 6 formal harness | Writes manifests, runs the formal synthetic matrix, validates outputs, and aliases artifacts. | `experiments/phase06_formal.py` |
| Phase 6 controls | Runs matched-coverage and fixed-accepted-set controls isolated from main formal outputs. | `experiments/phase06_coverage_controls.py` |
| Phase 6 robustness | Runs utility, meeting-point density, fleet stress, equity, and algorithm diagnostic packages. | `experiments/phase06_robustness.py` |
| Statistical closeout | Builds formal tables, plots, manifests, verification reports, and markdown synthesis from persisted results. | `experiments/formal_statistics.py` |
| Post-hoc analysis | Generates sensitivity, equity, and policy recommendation artifacts from result CSVs. | `analysis/sensitivity.py`, `analysis/equity.py`, `analysis/policy.py` |
| Publication figures | Regenerates manuscript figures from result artifacts. | `manuscript/figures/scripts/` |

## Pattern Overview

**Overall:** Layered research simulation pipeline with a reusable domain package and script-oriented experiment harnesses.

**Key Characteristics:**
- Keep reusable DRT primitives in `src/drt/`; these modules should not know about CSV outputs, Phase 05/06 folders, manuscript files, or pytest fixtures.
- Treat `experiments/variants.py` as the main adapter between algorithm primitives and publication/evidence concepts such as method labels, service designs, choice models, routing solvers, and evidence families.
- Treat `experiments/runner.py` as the generic matrix executor; phase-specific files narrow the matrix, isolate output directories, and validate persisted artifacts.
- Generated artifacts live under `results/`; active paper source lives under `manuscript/`; historical and throwaway material lives under `archive/`.

## Layers

**Domain Data Layer:**
- Purpose: Define the stable in-memory contract shared by algorithms and experiments.
- Location: `src/drt/types.py`
- Contains: `Request`, `Vehicle`, `MeetingPoint`, `Bundle`, `OfferAttributes`, `ChoiceParameters`, `UtilityComponents`, `ChoiceEvaluation`, `Route`, `PassengerType`.
- Depends on: Python dataclasses only.
- Used by: `src/drt/*`, `experiments/scenarios.py`, `experiments/variants.py`, tests in `tests/`.

**Core Algorithm Layer:**
- Purpose: Implement reusable meeting-point candidate search, insertion, feasibility, choice, ALNS, rolling-horizon, and exact MILP diagnostics.
- Location: `src/drt/`
- Contains: `src/drt/candidate.py`, `src/drt/feasibility.py`, `src/drt/insertion.py`, `src/drt/choice.py`, `src/drt/alns.py`, `src/drt/milp.py`.
- Depends on: `src/drt/types.py`, standard library, optional `gurobipy` inside `DRTModel.build()`, and `numpy` only outside core algorithms.
- Used by: `experiments/variants.py`, diagnostic experiment modules, pytest tests.

**Scenario Layer:**
- Purpose: Create repeatable input bundles for all variants.
- Location: `experiments/scenarios.py`
- Contains: `Scenario`, `generate_synthetic()`, `generate_beijing()`.
- Depends on: `src.drt.types`.
- Used by: `experiments/runner.py`, Phase 05/06 harnesses, robustness/control modules, tests.

**Variant Adapter Layer:**
- Purpose: Convert service-design definitions into solver calls and normalize outputs into passenger records.
- Location: `experiments/variants.py`
- Contains: `BaseVariant`, behavioral baselines, `FullModel`, ablations, diagnostics, and `ALL_VARIANTS`.
- Depends on: `experiments/config.py`, `experiments/metrics.py`, `experiments/scenarios.py`, and core `src/drt` modules.
- Used by: `experiments/runner.py`, Phase 05/06 harnesses, coverage controls, robustness diagnostics, tests.

**Experiment Execution Layer:**
- Purpose: Run reproducible matrices, enforce timeouts, collect utility logs, and write raw/aggregated outputs.
- Location: `experiments/runner.py`
- Contains: `run_all_experiments()`, `_run_variant_with_timeout()`, `_make_row()`, `_write_csv()`, `_write_metrics_table()`.
- Depends on: `experiments/config.py`, `experiments/scenarios.py`, `experiments/variants.py`, `experiments/metrics.py`, pandas.
- Used by: `run_experiments.py`, `experiments/phase05_pilot.py`, `experiments/phase06_formal.py`, tests.

**Phase-Specific Evidence Layer:**
- Purpose: Isolate formal/pilot/control/robustness outputs and enforce evidence-family constraints.
- Location: `experiments/phase05_pilot.py`, `experiments/phase06_formal.py`, `experiments/phase06_coverage_controls.py`, `experiments/phase06_robustness.py`, `experiments/phase06_supplementary.py`.
- Contains: CLI entry points, output constants, run manifests, validators, reduced method factories, package-specific schemas.
- Depends on: `experiments/runner.py`, `experiments/variants.py`, `experiments/formal_validation.py`, `experiments/formal_statistics.py`, result CSVs.
- Used by: CLI invocations, tests in `tests/test_phase05_pilot.py`, `tests/test_phase06_formal.py`, `tests/test_phase06_coverage_controls.py`, `tests/test_phase06_robustness.py`.

**Analysis and Publication Layer:**
- Purpose: Turn result files into interpretation artifacts, figures, and manuscript material.
- Location: `analysis/`, `manuscript/figures/scripts/`, `manuscript/sections/`, `manuscript/main.tex`.
- Contains: CSV readers, policy/equity/sensitivity summaries, plotting scripts, LaTeX source.
- Depends on: persisted files under `results/`, pandas/numpy/matplotlib in scripts.
- Used by: manual publication workflow and figure/report regeneration.

## Data Flow

### Generic Experiment Path

1. Root CLI starts a full run in `run_experiments.py:8` by importing `run_all_experiments()` from `experiments/runner.py`.
2. `experiments/runner.py:93` chooses scales, seeds, and variants from `experiments/config.py` and `experiments/variants.py`.
3. `experiments/runner.py:116` creates synthetic inputs with `generate_synthetic()` from `experiments/scenarios.py`.
4. `experiments/runner.py:137` optionally creates Beijing inputs with `generate_beijing()` from `experiments/scenarios.py`.
5. `experiments/runner.py:332` runs each variant in a one-worker thread with a timeout.
6. `experiments/variants.py:179` normalizes every variant through `BaseVariant.run()`, returning `experiments.metrics.SimulationResult`.
7. `experiments/metrics.py:131` computes summary metrics from passenger records.
8. `experiments/runner.py:151` writes `synthetic_results.csv`, `beijing_results.csv`, `metrics_table.csv`, and `utility_components.csv` under the configured results directory.

### FullModel Behavioral Path

1. `experiments/variants.py:926` defines `FullModel` as the main bidirectional meeting-point, binary-logit, rolling-horizon ALNS variant.
2. `experiments/variants.py:959` sorts incoming scenario requests by earliest pickup time.
3. `experiments/variants.py:963` turns the current tagged route state into plain routes for insertion screening.
4. `experiments/variants.py:964` calls `evaluate_insertion()` from `src/drt/insertion.py`.
5. `src/drt/insertion.py:49` generates pickup/dropoff candidates with `src/drt/candidate.py` and checks each proposed insertion with `src/drt/feasibility.py`.
6. `experiments/variants.py:975` assigns a deterministic passenger type through `assign_passenger_type()` from `src/drt/choice.py`.
7. `experiments/variants.py:1015` builds actual `OfferAttributes` from the chosen insertion.
8. `experiments/variants.py:1022` evaluates the offer with `evaluate_single_offer()` from `src/drt/choice.py`.
9. `experiments/variants.py:1026` applies accepted offers to the screening state with `_apply_insertion()` from `src/drt/alns.py`.
10. `experiments/variants.py:1032` runs `RollingHorizon` from `src/drt/alns.py` for accepted requests.
11. `experiments/variants.py:1070` marks accepted-but-unassigned requests as feasibility rejections if rolling-horizon routing drops them.
12. `experiments/variants.py:1081` returns `ALNSState` with routes, unassigned requests, completed IDs, accumulated vehicle-km, pickup times, and choice evaluations.

### Sequential Behavioral Baseline Path

1. `experiments/variants.py:263` defines `_run_actual_offer_sequence()` shared by `DoorToDoor`, `SingleSidedPickup`, `SingleSidedDropoff`, and `AblationNoRollingHorizon`.
2. `experiments/variants.py:278` assigns passenger types before offer generation.
3. `experiments/variants.py:297` calls `evaluate_insertion()` against service-design-specific meeting points.
4. `experiments/variants.py:323` evaluates actual offers with `evaluate_single_offer()`.
5. `experiments/variants.py:327` applies accepted insertions into tagged routes.
6. `experiments/variants.py:333` stores `choice_evaluations` on the returned `ALNSState`.

### Phase 6 Formal Path

1. `experiments/phase06_formal.py:411` parses CLI options for formal main runs, manifests-only runs, ledger initialization, or validation.
2. `experiments/phase06_formal.py:307` validates selected scales and seeds, writes manifests, initializes the rerun ledger, narrows `runner_module.ALL_VARIANTS`, and calls `runner_module.run_all_experiments()`.
3. `experiments/phase06_formal.py:133` copies legacy runner artifact names to formal aliases such as `raw_results.csv`, `processed_results.csv`, and `utility_logs.csv`.
4. `experiments/phase06_formal.py:350` validates persisted formal outputs through `experiments/formal_validation.py`.
5. `experiments/formal_statistics.py:1305` reads persisted formal outputs and writes tables, plots, manifests, markdown reports, and synthesis artifacts.

### Coverage-Control and Robustness Paths

1. `experiments/phase06_coverage_controls.py:697` runs matched-coverage controls from the formal main outputs in `results/formal/phase06/main_behavioral`.
2. `experiments/phase06_coverage_controls.py:1019` runs fixed-accepted-set controls for diagnostic operating-efficiency comparisons.
3. `experiments/phase06_robustness.py:629`, `:709`, `:763`, `:832`, and `:968` run utility sensitivity, meeting-point density/walking-radius, fleet stress, equity type outcomes, and algorithm diagnostics.
4. `experiments/phase06_robustness.py:1669` coordinates all robustness packages into `results/formal/phase06/robustness`.

**State Management:**
- Algorithm state is in-memory dataclasses and dictionaries: `ALNSState.routes`, `ALNSState.unassigned`, `RollingHorizon.active_requests`, `RollingHorizon.completed_request_ids`, and `RollingHorizon.pickup_times` in `src/drt/alns.py`.
- Experiment state is persisted as CSV/JSON artifacts under `results/` and phase ledgers/manifests under `.planning/phases/`.
- There is no database, service container, web server, or long-lived daemon state.

## Key Abstractions

**Scenario:**
- Purpose: Bundle one simulation input matrix cell.
- Examples: `experiments/scenarios.py:31`, `generate_synthetic()` at `experiments/scenarios.py:46`, `generate_beijing()` at `experiments/scenarios.py:152`.
- Pattern: Dataclass with lists of `Request`, `Vehicle`, and `MeetingPoint`.

**Passenger and Offer Dataclasses:**
- Purpose: Keep choice-model inputs and logs explicit.
- Examples: `src/drt/types.py:97`, `src/drt/types.py:115`, `src/drt/types.py:131`, `src/drt/types.py:145`.
- Pattern: Frozen dataclasses for offer/utility/choice logs so rows can be safely flattened through `ChoiceEvaluation.as_log_row()`.

**BaseVariant:**
- Purpose: Common contract for all experimental methods.
- Examples: `experiments/variants.py:179`, `_run_actual_offer_sequence()` at `experiments/variants.py:263`, `_build_records()` at `experiments/variants.py:372`.
- Pattern: Abstract adapter with method metadata, `_solve()` override, and output normalization.

**ALNSState:**
- Purpose: Mutable route state shared by greedy insertion, ALNS, and variant conversion.
- Examples: `src/drt/alns.py:30`, `experiments/variants.py:252`, `experiments/variants.py:1081`.
- Pattern: Dataclass with route dict, unassigned request list, cost, completed IDs, accumulated kilometers, and pickup times.

**RollingHorizon:**
- Purpose: Online reoptimization controller for dynamic request arrivals.
- Examples: `src/drt/alns.py:431`, `src/drt/alns.py:673`, `experiments/variants.py:1032`, `experiments/variants.py:1154`.
- Pattern: Stateful controller that advances vehicle state, prunes completed route stops, runs destroy/repair iterations, and returns route/unassigned/cost summaries.

**DRTModel:**
- Purpose: Exact static diagnostic optimization model.
- Examples: `src/drt/milp.py:30`, `src/drt/milp.py:81`.
- Pattern: Deferred `gurobipy` import inside `build()` so the package remains importable without a Gurobi installation.

**MetricsResult:**
- Purpose: Stable summary schema for experiment CSV aggregation.
- Examples: `experiments/metrics.py:76`, `compute_metrics()` at `experiments/metrics.py:131`.
- Pattern: Dataclass with zero defaults for edge cases with no accepted passengers.

## Entry Points

**Full experiment run:**
- Location: `run_experiments.py`
- Triggers: `python run_experiments.py`
- Responsibilities: Add project root to `sys.path`, run the full matrix through `experiments.runner.run_all_experiments()`, print summary checks from `results/metrics_table.csv`.

**Generic runner module:**
- Location: `experiments/runner.py`
- Triggers: `python experiments/runner.py` or `python -m experiments.runner`
- Responsibilities: Run all variants over configured synthetic and Beijing scenarios, write CSV outputs, print core thesis checks.

**Phase 5 pilot:**
- Location: `experiments/phase05_pilot.py`
- Triggers: `python -m experiments.phase05_pilot` or direct script execution.
- Responsibilities: Run only behavioral-main pilot variants at scale 20 into `results/pilot/phase05`.

**Phase 6 formal main:**
- Location: `experiments/phase06_formal.py`
- Triggers: `python -m experiments.phase06_formal [--validate|--manifests-only|--init-ledger]`
- Responsibilities: Isolate formal main outputs, predeclare seeds/scales, write manifests, run or validate the formal matrix.

**Phase 6 coverage controls:**
- Location: `experiments/phase06_coverage_controls.py`
- Triggers: `python -m experiments.phase06_coverage_controls`
- Responsibilities: Run matched coverage and fixed accepted set control packages.

**Phase 6 robustness:**
- Location: `experiments/phase06_robustness.py`
- Triggers: `python -m experiments.phase06_robustness`
- Responsibilities: Run reduced robustness, sensitivity, equity, fleet, and algorithm diagnostic packages.

**Formal closeout:**
- Location: `experiments/formal_statistics.py`
- Triggers: `python -m experiments.formal_statistics`
- Responsibilities: Generate tables, plots, manifests, markdown reports, and verification artifacts from formal results.

**Analysis scripts:**
- Location: `analysis/sensitivity.py`, `analysis/equity.py`, `analysis/policy.py`
- Triggers: direct script execution.
- Responsibilities: Read result CSVs and write post-hoc analysis artifacts.

**Figure scripts:**
- Location: `manuscript/figures/scripts/`
- Triggers: direct script execution from inside `manuscript/`.
- Responsibilities: Generate publication figures into `manuscript/figures/`.

## Architectural Constraints

- **Threading:** `experiments/runner.py:332` uses `concurrent.futures.ThreadPoolExecutor(max_workers=1)` to enforce a per-variant timeout. Algorithm code itself is single-process and mostly single-threaded.
- **Global state:** `experiments/variants.py:1191` defines singleton variant instances in `ALL_VARIANTS`. `experiments/phase05_pilot.py:34` and `experiments/phase06_formal.py:98` temporarily replace `runner_module.ALL_VARIANTS` inside context managers; add new phase filters through this context-manager pattern.
- **Filesystem state:** Generic runner outputs default to `results/`; Phase 05/06 harnesses override `results_dir` to keep evidence families isolated.
- **Optional solver:** `src/drt/milp.py:81` defers `gurobipy` import until MILP model construction. Do not import `gurobipy` at module import time.
- **Import roots:** Core modules mostly import `drt.*`; experiment modules include `src.drt.*` imports. When editing an existing file, match that file's current import root unless the change is a dedicated import-normalization refactor.
- **Generated files:** Do not treat `results/`, `manuscript/figures/*.png`, `manuscript/figures/*.pdf`, `.pytest_cache/`, or `__pycache__/` as source-of-truth code.
- **Request scale guard:** `experiments/scenarios.py:26` caps generated requests at 1000 to avoid accidental large runs.
- **Phase evidence boundaries:** `experiments/phase06_formal.py:25` and `experiments/phase06_formal.py:26` define allowed formal scales and method labels; do not expand formal evidence families by changing `ALL_VARIANTS` alone.

## Anti-Patterns

### Putting Experiment Output Logic in `src/drt`

**What happens:** Core algorithm modules gain CSV, manifest, phase, or manuscript output logic.
**Why it's wrong:** `src/drt/` is the reusable package layer and is imported by tests, experiments, and diagnostic scripts. Output concerns couple algorithm primitives to one evidence pipeline.
**Do this instead:** Keep output writers in `experiments/runner.py`, phase modules such as `experiments/phase06_formal.py`, analysis modules under `analysis/`, or figure scripts under `manuscript/figures/scripts/`.

### Bypassing `BaseVariant` for New Methods

**What happens:** A new service design calls `src/drt` algorithms directly from a phase harness and writes rows manually.
**Why it's wrong:** Runner rows, utility logs, method metadata, and metrics depend on the `BaseVariant.run()` -> `SimulationResult` contract.
**Do this instead:** Add a `BaseVariant` subclass in `experiments/variants.py`, set `method_label`, `service_design`, `choice_model`, `reoptimization`, `routing_solver`, `evidence_family`, and `diagnostic_role`, then add phase filters where needed.

### Writing Formal Results to Root `results/`

**What happens:** Formal, control, or robustness runs use the default `experiments/runner.py` output directory.
**Why it's wrong:** Root files such as `results/synthetic_results.csv` are generic/legacy outputs; Phase 05/06 code expects isolated evidence folders and manifests.
**Do this instead:** Use `results/pilot/phase05`, `results/formal/phase06/main_behavioral`, `results/formal/phase06/coverage_controls`, or `results/formal/phase06/robustness` via phase harness constants.

### Adding New Formal Methods Through `ALL_VARIANTS` Only

**What happens:** A method is added to `experiments/variants.py:1191` and assumed to participate in Phase 06 evidence.
**Why it's wrong:** Phase 06 main evidence is gated by `FORMAL_MAIN_METHOD_LABELS` in `experiments/phase06_formal.py:26`; controls and robustness have their own method factories and schemas.
**Do this instead:** Update the relevant phase label sets, validators, tests, and artifact schemas explicitly.

### Putting Publication Computation in LaTeX or Figure Scripts

**What happens:** Figure scripts or LaTeX sections recompute core simulation results.
**Why it's wrong:** The experiment pipeline already persists validated CSV/JSON artifacts; figures and manuscript files should consume evidence, not create it.
**Do this instead:** Put simulation logic in `src/drt/` and `experiments/`, summary logic in `experiments/formal_statistics.py` or `analysis/`, and plotting-only code in `manuscript/figures/scripts/`.

## Error Handling

**Strategy:** Simulation and formal evidence code prefers structured failure rows and validation reports over process-wide crashes. Core algorithms return `None`/reason tuples for infeasible insertions.

**Patterns:**
- `src/drt/insertion.py:49` returns `InsertionResult | None` for feasible vs rejected insertion.
- `src/drt/feasibility.py:46` returns `(bool, reason)` with reason codes such as `precedence`, `capacity`, `tw_early`, `tw_late`, `ride_time`, and `route_duration`.
- `src/drt/choice.py:185` creates explicit no-offer `ChoiceEvaluation` rows for feasibility rejection.
- `experiments/runner.py:332` converts timeout or exception failures into CSV rows with `status`, `detailed_reason`, and `error_message`.
- `experiments/phase06_formal.py:350` writes validation gate results and updates manifests instead of relying only on console output.

## Cross-Cutting Concerns

**Logging:** Console progress is printed by runner and CLI modules such as `experiments/runner.py`, `run_experiments.py`, and phase scripts. Persisted machine-readable logs are CSV/JSON artifacts under `results/` and `.planning/phases/`.

**Validation:** Input validation is local to generators and phase harnesses: request cap in `experiments/scenarios.py`, formal scale/seed checks in `experiments/phase06_formal.py`, output schema checks in `experiments/formal_validation.py`, coverage-control validators in `experiments/phase06_coverage_controls.py`, and robustness validators in `experiments/phase06_robustness.py`.

**Authentication:** Not applicable. The repo has no web/API authentication layer.

**Reproducibility:** Seeds and global experiment constants live in `experiments/config.py`; formal manifests in `experiments/phase06_formal.py` capture selected scales, seeds, method labels, run status, and artifact aliases.

**Publication Boundary:** `manuscript/` is the current paper source. Scripts in `manuscript/figures/scripts/` should read curated outputs and write figure assets only.

---

*Architecture analysis: 2026-06-16*
