# Phase 02 Pattern Map: Experimental Contract and Metric Standardization

**Phase:** 02 - Experimental Contract and Metric Standardization
**Date:** 2026-06-15
**Status:** complete

## Pattern Mapping Complete

Phase 2 itself should create planning/contract documents. The code patterns below are integration anchors for later Phase 4/5 implementation tasks referenced by the contracts.

## Artifact Patterns

| Target artifact | Closest existing pattern | Notes |
|---|---|---|
| `02_EXPERIMENT_CONTRACT.md` | `.planning/phases/01-literature-and-novelty-audit/01_NOVELTY_POSITIONING.md` | Use explicit allowed/risky/forbidden language and downstream phase ownership. |
| `02_BASELINE_TAXONOMY.md` | `.planning/phases/00-repository-and-manuscript-audit/00_CURRENT_EXPERIMENT_MAP.md` | Use tables mapping current variants to conceptual roles and future actions. |
| `02_METRICS_DEFINITIONS.md` | `.planning/phases/00-repository-and-manuscript-audit/00_CURRENT_EXPERIMENT_MAP.md` metric surface | Expand into formula/denominator/unit/valid-range contract. |
| `02_COVERAGE_CONFOUNDING_PLAN.md` | Phase 0 matched-coverage audit rows | Separate unconstrained, matched-coverage, and fixed accepted-set evidence roles. |
| `02_STATISTICAL_PLAN.md` | `.planning/phases/01-literature-and-novelty-audit/01_REVISED_RESEARCH_QUESTIONS.md` downstream evidence map | Use paired-seed and paired-difference planning without locking final sample size. |
| `02_PHASE45_CODE_TASKS.md` | `.planning/codebase/CONCERNS.md` and `.planning/codebase/ARCHITECTURE.md` | Translate contract requirements into later code-change tasks without implementing them now. |

## Code Integration Anchors

| Area | Current files | Contract implication |
|---|---|---|
| Variant registry | `experiments/variants.py` | Current `ALL_VARIANTS` mixes service design, response, routing, and diagnostics; Phase 2 must define four-axis taxonomy and route missing `SingleSidedDropoff` downstream. |
| Passenger response | `experiments/variants.py`, `src/drt/choice.py` | `FullModel` MNL filtering happens before routing with proxy meeting points. Phase 2 should require shared response assumptions across behavioral service variants; Phase 3/4 own implementation. |
| Metrics | `experiments/metrics.py` | `MetricsResult` lacks status-specific rejection metrics. Phase 2 should define formulas and status categories before schema changes. |
| Runner output | `experiments/runner.py` | Current raw rows are aggregate per run and error rows are zero-filled. Phase 2 should require provenance and durable failure/status rows for later implementation. |
| Matched coverage | `experiments/matched_coverage.py`, `experiments/endogenous_matched_coverage.py` | Existing scripts represent exploratory variants. Phase 2 should define target served-share cap semantics and fixed accepted-set intersection semantics. |
| Gamma/welfare | `experiments/pareto_sweep.py`, `experiments/metrics.py` | Gamma is post-hoc in current code. Phase 2 should forbid Pareto-frontier claims unless later code makes gamma endogenous. |
| MILP/ALNS diagnostics | `src/drt/alns.py`, `src/drt/milp.py`, `experiments/milp_gap.py` | Phase 2 can define diagnostic roles, but Phase 4 owns exact scope and validation details. |

## Executor Guidance

- Treat Phase 2 outputs as source-of-truth contracts for later phases.
- Do not edit code or results while executing Phase 2 plans.
- Prefer tables with explicit requirement IDs, decision IDs, and downstream phase owners.
- Use exact metric names from the plan to avoid denominator drift.

