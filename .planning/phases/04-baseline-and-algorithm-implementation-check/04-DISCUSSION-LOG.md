# Phase 4: Baseline and Algorithm Implementation Check - Discussion Log

> **Audit trail only.** Do not use as input to planning, research, or execution agents.
> Decisions are captured in CONTEXT.md. This log preserves the alternatives considered.

**Date:** 2026-06-15T17:22:40+08:00
**Phase:** 4-Baseline and Algorithm Implementation Check
**Areas discussed:** Baseline family and method labeling, Shared choice integration validation, ALNS/greedy/no-rolling-horizon diagnostics, MILP and exact diagnostic boundary, Unified outputs and failure rows

---

## Baseline Family and Method Labeling

| Question | Options Considered | User's Choice | Notes |
|---|---|---|---|
| Phase 4 behavioral baseline minimum set | All four behavioral baselines; DoorToDoor and BidirectionalMP first; Other set | All four behavioral baselines | DoorToDoor + Choice, SingleSidedPickup + Choice, SingleSidedDropoff + Choice, and BidirectionalMP + Choice are all required. |
| SingleSidedDropoff implementation symmetry | Fully symmetric with SingleSidedPickup; Minimum code change; Diagnostic/prototype only | Fully symmetric with SingleSidedPickup | Change the meeting-point side from pickup to dropoff. |
| Code variant names versus paper/result labels | Keep code names but output concept labels; Rename code classes; Keep both and explain in mapping | Keep code names but output concept labels, with stronger output requirements | Do not rush class renames. Results must use concept labels and structured method fields. Create VARIANT_MAPPING.md. |
| Runner separation | Shared runner with evidence_family/diagnostic_role; Separate scripts/runners; Documentation-only distinction | Shared runner with evidence_family/diagnostic_role | Shared runner is acceptable if rows make evidence family explicit. |

## Shared Choice Integration Validation

| Question | Options Considered | User's Choice | Notes |
|---|---|---|---|
| Old proxy-before-routing MNL filter in behavioral paths | Must prove old filter is not used; Only require new path exists; Document only | Must prove old filter is not used | Tests should monkeypatch or assert behavioral variants do not call `_mnl_filter_requests`. |
| Choice validation granularity | Validate every behavioral baseline; Validate BidirectionalMP and DoorToDoor only; Choice helper unit tests only | Validate every behavioral baseline | Each baseline needs integration-level validation. |
| DoorToDoor choice attributes | Same choice model with zero walk and actual offer attributes; Partial utility logging; Deterministic DoorToDoor outside behavioral family | Same choice model with zero walk and actual offer attributes | DoorToDoor must not remain deterministic in behavioral comparisons. |
| Randomness and paired fairness gate | Seeded request-level type consistency and reproducible draws; Overall seeded reproducibility only; Leave to pilot | Seeded request-level type consistency plus paired acceptance draw streams | Acceptance draws must not depend on RNG consumption order. |

## ALNS, Greedy, and No-Rolling-Horizon Diagnostics

| Question | Options Considered | User's Choice | Notes |
|---|---|---|---|
| Greedy baseline gate | Named diagnostic baseline; Internal ALNS repair only; Test-only coverage | Named diagnostic baseline | Expose GreedyInsertionBaseline with the same diagnostic schema. |
| No rolling horizon diagnostic role | Required rolling-horizon diagnostic; Keep existing ablation without full alignment; Defer to formal supplementary phase | Required rolling-horizon diagnostic | Same service design and choice semantics, with reoptimization disabled. |
| ALNS convergence diagnostic minimum | Per-iteration trace and run diagnostics; Run-level runtime and final objective only; No convergence artifacts | Per-iteration trace and run diagnostics | Record objective traces, best objective, runtime, accepted counts, and unassigned counts. |
| Operator contribution diagnostics | Record operator contribution statistics; Only prove operators run; Exclude from Phase 4 | Record operator contribution statistics | Track selection counts and improvement or accepted-improvement counts. |
| Runtime-quality tradeoff scope | Small multi-budget diagnostic; Default 50-iteration smoke only; Defer runtime-quality | Small multi-budget diagnostic, but only as smoke/diagnostic | This is not a large-scale formal runtime-quality experiment. |

## MILP and Exact Diagnostic Boundary

| Question | Options Considered | User's Choice | Notes |
|---|---|---|---|
| MILP evidence role in Phase 4 | Small static snapshot diagnostic; Move toward full exact benchmark; Shape smoke test only | Small static snapshot diagnostic | Do not present current MILP as a full online benchmark. |
| Hand-verified tiny instances | Hand-verified tiny instances; Existing Gurobi smoke tests only; Only if Gurobi is available | Hand-verified tiny instances, with no-Gurobi fallback | Gurobi solve may skip, but pure Python fixture checks must still run. |
| MILP versus ALNS gap reporting | Report only in semantically matched diagnostics; Keep current script semantics; Report only MILP status | Report only in semantically matched diagnostics | State objective units and mark incomparable cases. |
| No-Gurobi Phase 4 path | Skip solver tests but keep no-Gurobi diagnostic path; Require Gurobi; Skip MILP scope entirely | Skip solver tests but keep no-Gurobi diagnostic path | Phase 4 must not be blocked by local license availability. |
| MILP route-sequencing scope | No full route-sequencing requirement; Implement route sequencing if gap is large; Documentation only | No full route-sequencing requirement | Document simplified scope and fix obvious bugs/schema issues only. |

## Unified Outputs and Failure Rows

| Question | Options Considered | User's Choice | Notes |
|---|---|---|---|
| Minimum result output fields | Full provenance and method-schema fields; Only status/metric fields; Keep current CSV mostly unchanged | Full provenance and method-schema fields, plus traceability additions | Include result_schema_version, timestamp_utc, artifact_dir, git_commit_or_code_hash, n_requests, n_offered, and n_served. |
| Failure, timeout, and infeasible row handling | Durable rows for all outcomes; Runner-level failures only; Log-only recording | Durable rows for all outcomes | Aggregate tables must expose status or exclusion rules. |
| Runner timeout known bug | Mandatory bounded timeout fix; Test only and defer fix; Do not handle timeout | Mandatory bounded timeout fix | Current ThreadPoolExecutor behavior is a Phase 4 blocker. |
| Formal output metric names | Ban old vkm_per_trip formal field; Keep legacy plus new fields; Document only | Ban old vkm_per_trip formal field | Use vkm_per_served_trip and vkm_per_original_request. |
| Phase 4 delivery document organization | Three validation documents plus VARIANT_MAPPING.md; Single audit document; Test logs only | Three validation documents plus VARIANT_MAPPING.md | Required docs are 04_IMPLEMENTATION_AUDIT.md, 04_BASELINE_VALIDATION.md, 04_ALGORITHM_VALIDATION.md, and VARIANT_MAPPING.md. |

## the agent's Discretion

- Exact helper names, fixture layout, diagnostic artifact filenames, and test split are left to the planner/executor.

## Deferred Ideas

- None.
