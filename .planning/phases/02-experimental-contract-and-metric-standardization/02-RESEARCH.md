# Phase 02 Research: Experimental Contract and Metric Standardization

**Phase:** 02 - Experimental Contract and Metric Standardization
**Date:** 2026-06-15
**Status:** complete

## Research Complete

Phase 2 should be planned as a documentation and contract phase. It should not run new experiments or edit production experiment code. Its value is to lock fair-comparison semantics before Phase 3 passenger-choice work, Phase 4 implementation validation, Phase 5 pilots, and Phase 6 formal paired-seed experiments.

## Planning Question

What does the planner need to know to define fair comparisons and unambiguous metrics for bidirectional meeting-point DRT?

## Findings

### 1. Current comparisons mix experiment families

The current variant registry in `experiments/variants.py` combines service-design variants, passenger-response assumptions, routing algorithms, and diagnostics under variant names such as `DoorToDoor`, `SingleSidedPickup`, `BidirectionalNoChoice`, `FullModel`, `AblationNoRollingHorizon`, and `AblationNoChoice`.

Planning implication:

- Phase 2 needs a four-axis taxonomy: service design, passenger response, routing algorithm, and diagnostic role.
- Code labels should not be the primary conceptual taxonomy for paper-facing evidence.
- `FullModel` should be renamed in contracts to a descriptive label such as `BidirectionalMP + Choice + RollingHorizon/ALNS`.
- `SingleSidedDropoff` is missing from the current formal service-design set and must be listed as a Phase 4 implementation/validation need.

### 2. Main behavioral evidence must use consistent passenger response

The audits show the current headline comparison is not fair as final evidence because `DoorToDoor` is deterministic all-feasible insertion while `FullModel` applies MNL filtering before routing. This makes served share, rejection, and vehicle-km results partly artifacts of mixed behavioral assumptions.

Planning implication:

- Behavioral service-design comparisons must use the same passenger-choice model across `DoorToDoor`, `SingleSidedPickup`, `SingleSidedDropoff`, and `BidirectionalMeetingPoint`.
- Door-to-door behavioral service should set walk distance to zero while still using the same choice/utility framework.
- Deterministic all-feasible variants should remain diagnostics, not main behavioral evidence.

### 3. Coverage confounding is the central contract risk

Phase 0 verified that the current main table has much lower served share for `FullModel` than `DoorToDoor`, so vehicle-km per served trip can look favorable while coverage is worse. Matched coverage and fixed accepted-set experiments are therefore not optional polish; they are core safeguards against misleading claims.

Planning implication:

- Main behavioral results should report unconstrained coverage, acceptance, rejection, and efficiency together.
- Matched coverage should use a target `served_share` cap and be a core supplementary manuscript result.
- Fixed accepted-set routing diagnostics should use the intersection of requests commonly serviceable/accepted by all methods.
- Fixed accepted-set diagnostics explain routing efficiency conditional on identical passengers; they do not replace behavioral evidence.

### 4. Metric names and denominators need a hard standard

`experiments/metrics.py` currently exposes `acceptance_rate`, `vehicle_km`, wait/walk/IVT, detour, fairness, CPU, and a default `social_welfare` field. Existing outputs and scripts use `vkm_per_trip` ambiguously; `experiments/weight_sensitivity.py` has already demonstrated denominator drift by using `vehicle_km / acceptance_rate`.

Planning implication:

- The ambiguous label `vkm_per_trip` should be forbidden for new formal evidence.
- Use `vkm_per_served_trip = total_vkm / served_requests`.
- Use `vkm_per_original_request = total_vkm / original_requests`.
- Report `served_share`, `behavioral_acceptance_rate`, `choice_rejection_rate`, `feasibility_rejection_rate`, and deterministic inserted/share diagnostics as separate quantities.
- Require formula, denominator, unit, valid range, interpretation, and forbidden uses for every metric.

### 5. Row-level status is the future schema anchor

Current `PassengerRecord` only records accepted/rejected and does not distinguish choice rejection, feasibility rejection, failed, timeout, infeasible, or completed status. The runner writes error rows but does not persist a full request-level status ledger.

Planning implication:

- Phase 2 should require durable request/run status categories, but leave implementation to Phase 4/5.
- Aggregate metrics should be derivable from row-level status rows.
- Phase 4/5 code tasks should cover schema changes in `PassengerRecord`, `SimulationResult`, `MetricsResult`, runner CSVs, and failure/provenance outputs.

### 6. Gamma and welfare must remain diagnostic unless redesigned

`FullModel(gamma=...)` stores `_gamma` but does not use it in acceptance, routing, or offered bundle selection. `experiments/pareto_sweep.py` applies gamma post-hoc through `compute_social_welfare`.

Planning implication:

- Phase 2 must forbid Pareto-frontier language for current gamma sweeps.
- Social welfare can only support final claims if Phase 4+ makes gamma endogenous or explicitly labels the output as post-hoc scoring.

### 7. ALNS/MILP scope belongs downstream

Phase 2 can name the need for deterministic routing and exact/MILP diagnostics, but it should not define detailed ALNS/MILP exact scope. Phase 4 owns algorithm validation.

Planning implication:

- Phase 2 should include algorithm diagnostics in the evidence taxonomy.
- It should route detailed exact model scope, convergence diagnostics, greedy baseline, and runtime-quality trade-offs to Phase 4.

## Recommended Phase 2 Output Contract

Produce these artifacts:

1. `02_EXPERIMENT_CONTRACT.md`
   - Experiment families, service variants, behavioral vs deterministic boundaries, evidence roles, claim boundaries.
2. `02_BASELINE_TAXONOMY.md`
   - Four-axis taxonomy mapping conceptual methods to current/missing code variants.
3. `02_METRICS_DEFINITIONS.md`
   - Formula, denominator, unit, valid range, interpretation, and forbidden/high-risk language.
4. `02_COVERAGE_CONFOUNDING_PLAN.md`
   - Unconstrained behavioral, matched-coverage, and fixed accepted-set designs.
5. `02_STATISTICAL_PLAN.md`
   - Paired seed design, paired differences, confidence intervals, non-final sample-size guidance, and formal/pilot separation.
6. Optional but useful: `02_PHASE45_CODE_TASKS.md`
   - Later implementation checklist for schema, variants, runner outputs, metrics, and diagnostics.

## Validation Architecture

Phase 2 execution should be considered valid only if:

- No files under `results/` are modified.
- No new experiment command is run.
- All Phase 2 requirement IDs appear in the final artifacts: EXP-01, EXP-02, EXP-03, EXP-04, MET-01, MET-02, MET-03.
- Each decision D-01 through D-23 from `02-CONTEXT.md` is represented in at least one artifact.
- The contract clearly separates behavioral comparisons, deterministic diagnostics, matched-coverage controls, fixed accepted-set diagnostics, and later ALNS/MILP validation.
- The metric definitions forbid ambiguous `vkm_per_trip`, mixed acceptance denominators, post-hoc gamma frontier language, and any unconditional superiority claim based on coverage-confounded results.

## Risks for Planning

- If the plan only asks for prose deliverables, execution may miss traceability. Add explicit acceptance criteria that check exact metric names, formulas, status categories, and decision IDs.
- If Phase 2 plans include code edits, they will violate the context boundary. Route code changes into `02_PHASE45_CODE_TASKS.md`.
- If matched coverage is treated as appendix-only, the final paper can still overclaim unconstrained efficiency. The plan must make matched coverage a core supplementary design.
- If fixed accepted-set diagnostics use one method's accepted set instead of the intersection across methods, the diagnostic can bias toward that method.

## Research Complete

Phase 2 is ready for executable planning.

