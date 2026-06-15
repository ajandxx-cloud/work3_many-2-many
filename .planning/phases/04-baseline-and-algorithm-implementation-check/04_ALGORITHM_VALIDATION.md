# Phase 04 Algorithm Validation

## Purpose

Validate algorithm diagnostic surfaces before Phase 5 pilots. This report covers
ALG-01 feasibility and route-commitment checks, ALG-02 named greedy and
no-rolling-horizon diagnostics, and ALG-03 ALNS trace/operator diagnostics.

## Feasibility and Route Commitment

ALG-01 is covered by focused pytest checks for:

- Capacity violations.
- Pickup time-window early and late violations.
- Maximum ride-time violations.
- Pickup-before-dropoff precedence.
- Route-duration consistency.
- Walking-radius candidate failure.
- Tagged route stops preserving request IDs and pickup/dropoff roles after
  insertion.
- Rolling-horizon pruning preserving completed request IDs and pickup times.

Known limitation: route stops remain tuple-based and compatibility code still
converts between plain `(MeetingPoint, time)` and tagged
`(MeetingPoint, time, request_id, role)` forms. The new tests prevent silently
losing request IDs or pickup times in the current representation, but a future
route-stop dataclass would be safer.

## Greedy Diagnostic

D-12 and ALG-02 are covered by `GreedyInsertionBaseline`, a named algorithm
diagnostic variant with:

- `evidence_family = "algorithm_diagnostic"`
- `diagnostic_role = "greedy_insertion"`
- Runner-compatible method metadata and result rows.

This diagnostic uses the existing greedy insertion/evaluate-insertion path on a
small scenario or fixed accepted-set style input. It is diagnostic evidence only.

## No-Rolling-Horizon Diagnostic

D-13 and ALG-02 are covered by `AblationNoRollingHorizon`, which retains shared
choice semantics while disabling rolling-horizon reoptimization. Its metadata
separates it from behavioral main evidence:

- `evidence_family = "algorithm_diagnostic"`
- `diagnostic_role = "no_rolling_horizon_diagnostic"`

## ALNS Trace Diagnostics

D-14, D-15, and ALG-03 are covered by optional `RollingHorizon` diagnostics.
When `collect_diagnostics=True`, trace entries include:

- `iteration`
- `objective`
- `best_objective`
- `runtime_ms`
- `accepted_count`
- `unassigned_count`
- `destroy_operator`
- `repair_operator`
- `improved`
- `accepted_improvement`
- `accepted`

The returned result also includes operator selection counts and improvement
counts. The flag defaults to `False`, so callers that do not request diagnostics
keep default behavior.

## Multi-Budget Smoke

D-16 and ALG-03 are covered by `experiments.algorithm_diagnostics.run_alns_budget_smoke`.
The default budgets are `[5, 20, 50]`. Rows include:

- `budget_iterations`
- `best_objective`
- `runtime_s`
- `n_accepted`
- `n_unassigned`
- `operator_selection_counts`
- `improvement_counts`
- `evidence_family = "algorithm_diagnostic"`
- `diagnostic_role = "alns_budget_smoke"`

This multi-budget run is algorithm smoke evidence only. It is not a formal
runtime-quality experiment and must not be used as service-design superiority
evidence.

## MILP Diagnostic Boundary

D-17 through D-21 and ALG-04 are covered by the static MILP diagnostic path.
`src/drt/milp.py` is a static snapshot assignment/scheduling diagnostic with a
simplified capacity bound. It is not a full route-sequencing exact online DRT
benchmark and is not a stochastic online policy benchmark.

Valid uses:

- Fixed accepted-set diagnostics.
- Static tiny instances with hand-verified feasibility or objective-unit checks.
- Small solver-backed smoke checks when Gurobi and a license are available.

Invalid uses:

- Full online DRT benchmark claims.
- Behavioral service-design superiority claims.
- Gap reporting when MILP status, objective units, or accepted-set semantics do
  not match the ALNS/greedy comparator.

## No-Gurobi Path

D-18 and D-20 require validation to continue when Gurobi is absent. The pure
Python tests cover candidate filtering, a hand-built tiny feasibility/objective
unit check, and a monkeypatched no-solver path for
`experiments.milp_gap.run_gap_experiment`.

The no-Gurobi diagnostic row uses:

- `status = "no_gurobi"`
- `milp_status = "no_gurobi"`
- `gap_pct = None`
- `comparable_gap = False`
- non-empty `detailed_reason`

## Comparable Gap Rules

D-19 and ALG-02 are enforced in `experiments/milp_gap.py` by returning
diagnostic metadata on every row and computing `gap_pct` only when:

- the MILP status is `optimal` or `feasible`;
- the MILP objective can be expressed in the documented weighted-cost units;
- the comparison is a fixed accepted-set/static snapshot comparison.

For `no_gurobi`, `no_accepted`, `infeasible`, `timeout`, and `error` rows, the
gap is suppressed with `gap_pct = None` and `comparable_gap = False`.

## Limitations

- Trace collection is intended for small diagnostics; full runtime-quality
  evidence remains out of scope for Phase 04.
- The tuple-based route-stop representation is still fragile and should be
  replaced in a later structural cleanup before making stronger route-ledger
  claims.
- Full route-sequencing exact online DRT remains out of Phase 04 scope.

## Commands

```bash
PYTHONPATH=src pytest tests/test_feasibility.py tests/test_insertion.py tests/test_alns.py tests/test_variants.py -q
PYTHONPATH=src python -m experiments.algorithm_diagnostics
PYTHONPATH=src pytest tests/test_milp.py -q
```

Latest local results:

- `tests/test_feasibility.py tests/test_insertion.py tests/test_alns.py tests/test_variants.py`: 42 passed.
- `python -m experiments.algorithm_diagnostics`: emitted budget rows for 5, 20, and 50 iterations with objective/runtime/operator/accepted/unassigned fields.
- `tests/test_milp.py`: 7 passed, 1 skipped.

## Decision Trace

- D-12: Greedy insertion is exposed as a named diagnostic.
- D-13: No-rolling-horizon remains an algorithm diagnostic under shared choice semantics.
- D-14: ALNS diagnostics record objective, runtime, accepted counts, and unassigned counts.
- D-15: ALNS diagnostics record destroy/repair operator counts and improvement counts.
- D-16: Small multi-budget smoke diagnostics are defined and labeled non-formal.
- D-17: MILP scope is limited to static snapshot diagnostics.
- D-18: Pure-Python tiny-instance checks run without Gurobi.
- D-19: MILP-vs-ALNS gaps are suppressed unless static/fixed-set semantics and units are comparable.
- D-20: No-Gurobi diagnostic rows are durable and non-blocking.
- D-21: Full route-sequencing exact online DRT is explicitly out of scope.
