---
phase: "02-experimental-contract-and-metric-standardization"
status: passed
verified: 2026-06-15
plans: [02-01, 02-02, 02-03]
requirements: [EXP-01, EXP-02, EXP-03, EXP-04, MET-01, MET-02, MET-03]
---

# Phase 02 Verification: Experimental Contract and Metric Standardization

## Verdict

**Status:** passed

Phase 2 achieved its goal: fair-comparison contracts and metric standards are defined before any new formal experiments are run.

## Goal Check

**Roadmap goal:** Define fair comparisons and prevent metric ambiguity.

| Goal element | Evidence | Result |
|---|---|---|
| Fair comparison families | `02_EXPERIMENT_CONTRACT.md`, `02_BASELINE_TAXONOMY.md` | passed |
| Behavioral/deterministic separation | `02_EXPERIMENT_CONTRACT.md`, `02_BASELINE_TAXONOMY.md` | passed |
| Coverage-confounding controls | `02_COVERAGE_CONFOUNDING_PLAN.md` | passed |
| Metric formula/denominator/unit contract | `02_METRICS_DEFINITIONS.md` | passed |
| Paired statistical reporting plan | `02_STATISTICAL_PLAN.md` | passed |
| Downstream implementation routing | `02_PHASE45_CODE_TASKS.md` | passed |

## Requirement Traceability

| Requirement | Evidence | Result |
|---|---|---|
| EXP-01 | Four-axis taxonomy separates service design, passenger response, routing algorithm, and diagnostic role. | passed |
| EXP-02 | Behavioral comparison requires shared passenger-response assumptions across service variants. | passed |
| EXP-03 | Deterministic diagnostics are explicitly separated from behavioral comparisons. | passed |
| EXP-04 | Unconstrained behavioral, matched-coverage, and fixed accepted-set controls are defined. | passed |
| MET-01 | Metric dictionary includes formulas, denominators, units, valid ranges, interpretations, and forbidden uses. | passed |
| MET-02 | Served share, behavioral acceptance, feasibility rejection, choice rejection, and deterministic inserted share are distinct. | passed |
| MET-03 | Main table minimum columns include total vehicle-km, vehicle-km per served trip, vehicle-km per original request, and served share together. | passed |

## Decision Coverage

`gsd-sdk query check.decision-coverage-plan` reported:

- total: 23
- covered: 23
- uncovered: 0

All D-01 through D-23 decisions from `02-CONTEXT.md` are represented in Phase 2 plans and outputs.

## Automated Checks

| Check | Result |
|---|---|
| Required Phase 2 files exist | passed |
| EXP-01, EXP-02, EXP-03, EXP-04, MET-01, MET-02, MET-03 appear in Phase 2 outputs | passed |
| D-01 through D-23 appear in Phase 2 outputs | passed |
| Three plan summaries exist | passed |
| Scope boundary: no intentional Phase 2 edits under `results/`, `experiments/`, `src/`, or `manuscript/sections/` | passed with note |

## Scope Boundary Note

The working tree already contains pre-existing dirty/generated files under `results/`, `experiments/__pycache__`, and `src/drt/__pycache__`. Phase 2 commits did not stage or modify those files. They remain unrelated repository hygiene debt.

## Artifacts Created

- `02-RESEARCH.md`
- `02-PATTERNS.md`
- `02-01-PLAN.md`
- `02-02-PLAN.md`
- `02-03-PLAN.md`
- `02_EXPERIMENT_CONTRACT.md`
- `02_BASELINE_TAXONOMY.md`
- `02_METRICS_DEFINITIONS.md`
- `02_COVERAGE_CONFOUNDING_PLAN.md`
- `02_STATISTICAL_PLAN.md`
- `02_PHASE45_CODE_TASKS.md`
- `02-01-SUMMARY.md`
- `02-02-SUMMARY.md`
- `02-03-SUMMARY.md`

## Residual Risks

- Phase 3 must rebuild the passenger-choice model before behavioral evidence can be generated.
- Phase 4 must implement and validate the schema, variants, metrics, matched-coverage cap, fixed accepted-set diagnostic, and ALNS/MILP diagnostic scope.
- Phase 5 must pilot the contract before Phase 6 formal experiments.
- Current historical result files remain exploratory and should not be reused as final evidence.

## Final Result

Phase 2 passes verification and is ready to close.

