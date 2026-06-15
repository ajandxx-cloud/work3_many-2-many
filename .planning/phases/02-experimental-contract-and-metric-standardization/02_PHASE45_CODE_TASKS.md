# Phase 02 Downstream Code Task List for Phase 4/5

**Phase:** 02 - Experimental Contract and Metric Standardization
**Status:** downstream implementation checklist

## Purpose

This file translates the Phase 2 experiment and metric contracts into later implementation tasks. Phase 2 does not implement code changes. Phase 4 owns implementation/validation; Phase 5 owns pilot smoke tests.

## Phase 4 Implementation and Validation Tasks

| Task group | Target files | Prerequisite contract | Required action | Verification expectation |
|---|---|---|---|---|
| Variant registry and missing service variants | `experiments/variants.py` | `02_BASELINE_TAXONOMY.md` | Add or validate `SingleSidedDropoff`; expose conceptual method mapping without relying on paper-facing `FullModel` wording. | Unit/integration tests show DoorToDoor, SingleSidedPickup, SingleSidedDropoff, and BidirectionalMeetingPoint can run under the same comparison harness. |
| Shared passenger-response hooks | `experiments/variants.py`, `src/drt/choice.py` | `02_EXPERIMENT_CONTRACT.md` | Apply one shared behavioral choice model across service variants; DoorToDoor uses zero walk distance but same response semantics. | Behavioral comparison rows include common response fields and no deterministic all-accept baseline is mixed into the main family. |
| Row-level request status schema | `experiments/metrics.py`, `experiments/runner.py`, possibly `src/drt/types.py` | `02_METRICS_DEFINITIONS.md` | Add durable row-level request status values: `choice_rejected`, `feasibility_rejected`, `served`, `failed`, `timeout`. | Aggregate metrics are derivable from row-level statuses. |
| Metric dataclass and CSV outputs | `experiments/metrics.py`, `experiments/runner.py`, tests under `tests/` | `02_METRICS_DEFINITIONS.md` | Add `served_share`, `behavioral_acceptance_rate`, `choice_rejection_rate`, `feasibility_rejection_rate`, `deterministic_inserted_share`, `total_vkm`, `vkm_per_served_trip`, and `vkm_per_original_request`. | Tests verify formulas and CSV columns; `vkm_per_trip` is absent from new formal outputs. |
| Matched-coverage cap implementation | `experiments/endogenous_matched_coverage.py`, runner/config code as needed | `02_COVERAGE_CONFOUNDING_PLAN.md` | Implement target served_share cap semantics with explicit achieved coverage and failure rows. | Pilot can show target cap, achieved served share, and tolerance for each method/seed. |
| Fixed accepted-set diagnostic implementation | new or existing focused experiment script under `experiments/` | `02_COVERAGE_CONFOUNDING_PLAN.md` | Construct intersection of requests commonly serviceable/accepted by all methods and run routing diagnostics on that set. | Output includes retained request count, retained share, method statuses, and diagnostic label. |
| Provenance and failure-row outputs | `experiments/runner.py`, result writers | `02_STATISTICAL_PLAN.md` | Save config ID, seed, scenario, method, code revision, runtime, status, and error message. | Failed, timeout, and infeasible runs are durable rows, not silent omissions. |
| Gamma/welfare semantics | `experiments/variants.py`, `experiments/pareto_sweep.py`, `experiments/metrics.py` | `02_METRICS_DEFINITIONS.md` | Either keep gamma as post-hoc welfare scoring with explicit diagnostic label or make gamma endogenous in routing/acceptance before using frontier language. | Tests or docs prove whether gamma affects decisions; frontier language is blocked if not. |
| ALNS/MILP diagnostic validation | `src/drt/alns.py`, `src/drt/milp.py`, `experiments/milp_gap.py`, tests | `02_EXPERIMENT_CONTRACT.md` | Define exact diagnostic scope, greedy comparison, convergence diagnostics, runtime-quality trade-offs, and operator contribution outputs. | Phase 4 validation report states what exact/MILP does and does not prove. |

## Phase 5 Pilot Smoke-Test Tasks

| Task group | Inputs | Required pilot check | Pass signal |
|---|---|---|---|
| Standardized behavioral output | Phase 4 shared-response variants | Run 3 to 5 pilot seeds with all behavioral service designs. | Every row has status, metric columns, config ID, seed, and method. |
| Matched-coverage cap smoke test | Phase 4 cap implementation | Run target served-share cap on pilot seeds. | Achieved served share and tolerance are recorded per method. |
| Fixed accepted-set smoke test | Phase 4 accepted-set diagnostic | Build common intersection and run all methods on it. | Retained set size and diagnostic metrics are recorded. |
| Failure-row durability | runner timeout/error path | Force or simulate at least one failure/timeout path if safe. | Failure row persists with status and error message. |
| Metric regeneration | metric definitions | Recompute aggregate table from raw/status rows. | Aggregates match formulas in `02_METRICS_DEFINITIONS.md`. |

## Non-Implementation Boundary

Phase 2 does not implement code changes. This task list is the handoff to Phase 4 and Phase 5. No file under `experiments/`, `src/`, `results/`, or `manuscript/sections/` should be modified by Phase 2 execution.

## Requirements and Decision Trace

- D-23: Phase 2 outputs this Phase 4/5 code-change task list for schema, variant, runner, metric, and output changes.
- EXP-01 through EXP-04 and MET-01 through MET-03 are implementation drivers for the task groups above.

