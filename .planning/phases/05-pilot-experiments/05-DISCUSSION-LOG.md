# Phase 5: Pilot Experiments - Discussion Log

> **Audit trail only.** Do not use as input to planning, research, or execution agents.
> Decisions are captured in CONTEXT.md; this log preserves the alternatives considered.

**Date:** 2026-06-15T21:20:04+08:00
**Phase:** 5-Pilot Experiments
**Areas discussed:** Pilot run matrix, Pass/fail gates, Pilot artifact boundary, Coverage-control smoke depth

---

## Pilot Run Matrix

| Question | Option | Description | Selected |
|----------|--------|-------------|----------|
| Scenario scope | Small synthetic only | Run 3-5 small synthetic seeds only; fastest way to expose code and schema problems without case-study interpretation burden. | Yes |
| Scenario scope | Synthetic + Beijing-inspired smoke | Add a Beijing-inspired smoke to catch case path issues earlier, with higher runtime and interpretation cost. | |
| Scenario scope | Agent decides | Let the agent choose a conservative minimum matrix. | |
| Seed count | 3 seeds | Roadmap minimum; fast enough for a readiness gate. | Yes |
| Seed count | 5 seeds | More stable, but heavier and closer to a pre-formal experiment. | |
| Seed count | Start with 3 and add 2 if needed | Add seeds if volatility or coverage instability appears. | |
| Methods | Four core behavioral methods | DoorToDoor + Choice, SingleSidedPickup + Choice, SingleSidedDropoff + Choice, and BidirectionalMP + Choice + RH/ALNS. | Yes |
| Methods | Behavioral core + diagnostics | Include diagnostics in the main pilot matrix, with risk of mixing evidence families. | |
| Methods | Only key comparison | Run DoorToDoor and BidirectionalMP only; fastest but less complete. | |
| Scale | Single small scale | Use one small scale such as n_requests=20 to check schema, status, and metrics quickly. | Yes |
| Scale | Two small scales | More scale-sensitive signal, but heavier for Phase 5. | |
| Scale | Agent decides | Let the planner choose the smallest useful scale. | |

**User's choice:** Small synthetic only; 3 seeds; four core behavioral methods; single small scale.
**Notes:** Diagnostics should stay separate from the main behavioral pilot evidence family. Phase 5 remains a readiness gate rather than formal evidence.

---

## Pass/Fail Gates

| Question | Option | Description | Selected |
|----------|--------|-------------|----------|
| Failure/timeout policy | Zero failed/zero timeout | Any core behavioral failed or timeout row blocks Phase 5 until fixed and rerun. | Yes |
| Failure/timeout policy | Allow non-core diagnostic failures | Core behavioral matrix must pass; diagnostics may record non-blocking statuses. | |
| Failure/timeout policy | Allow small failures if recorded | Recorded failures do not necessarily block; weaker gate. | |
| Metric sanity strictness | Strict basic ranges | Ratios in [0,1], non-negative vehicle_km/vkm/wait/walk/IVT, no NaN or infinity. | Yes |
| Metric sanity strictness | Ranges + mechanism consistency | Also check identities such as status proportions and n_served <= n_offered <= n_requests. | |
| Metric sanity strictness | Only obvious bad values | Catch NaN, infinity, negative values, and crashes only. | |
| Abnormal served_share | Mark for investigation only | Record anomalies as risks unless paired with hard schema/status/metric problems. | Yes |
| Abnormal served_share | Hard thresholds | Make zero or unexpectedly low served_share a hard failure. | |
| Abnormal served_share | Agent judges | Let the planner decide based on context. | |
| Logs/provenance | Hard failure | Missing joinable utility logs or required provenance blocks Phase 5. | Yes |
| Logs/provenance | Provenance hard, utility warning | Provenance required; utility logs may be fixed later. | |
| Logs/provenance | Both warnings | Raw metrics are enough for pilot pass. | |

**User's choice:** Zero failed/timeout rows; strict basic metric ranges; abnormal served_share is investigative; missing utility logs/provenance is hard failure.
**Notes:** Main Phase 5 failure conditions should focus on execution, schema, status, metric validity, and traceability, not early interpretation of behavioral outcomes.

---

## Pilot Artifact Boundary

| Question | Option | Description | Selected |
|----------|--------|-------------|----------|
| Report style | Gate report | Matrix, pass/fail state, sanity checks, bugs, fixes, and rerun records without conclusions. | Yes |
| Report style | Small results report | Include preliminary method comparisons and explanations; higher misuse risk. | |
| Report style | Minimal run log | Only commands, files, and pass/fail state. | |
| Output isolation | Independent pilot directory | Write pilot CSV/JSON under a path such as results/pilot/phase05/. | Yes |
| Output isolation | results root with prefix | Use names such as pilot_synthetic_results.csv. | |
| Output isolation | Planning artifact only | Keep summary only; do not retain full CSV/JSON. | |
| Plots | Diagnostic plots only | Status distribution, metric ranges, failure/timeout counts, missing-field checks. | Yes |
| Plots | Comparison plots | Method comparison plots that are easier to misuse as evidence. | |
| Plots | No plots | Tables and checks only. | |
| Bug list | Structured bug ledger | Track bug_id, config, affected method/seed, symptom, fix status, rerun result, and Phase 6 blocker status. | Yes |
| Bug list | Markdown bullet list | Lightweight list of issues and handling. | |
| Bug list | Only blocking bugs | Omit non-blocking anomalies from formal artifacts. | |

**User's choice:** Gate report; independent pilot output directory; diagnostic plots only; structured bug ledger.
**Notes:** Pilot artifacts should make Phase 6 planning trustworthy while preventing accidental reuse as paper evidence.

---

## Coverage-Control Smoke Depth

| Question | Option | Description | Selected |
|----------|--------|-------------|----------|
| Matched-coverage depth | Minimal viable smoke | Verify cap/target logic, output fields, and tolerance check only. | |
| Matched-coverage depth | Complete small-sample diagnostic | Run a small-sample diagnostic for Phase 6 readiness without making claims. | Yes |
| Matched-coverage depth | Do not run matched coverage | Leave matched coverage to Phase 6. | |
| Matched-coverage tolerance | Blocking | Tolerance failure blocks Phase 6 until fixed or design-adjusted. | Yes |
| Matched-coverage tolerance | Non-blocking but recorded | Record as bug/risk; planner decides later. | |
| Matched-coverage tolerance | Agent judges | Planner decides based on failure size and cause. | |
| Fixed accepted-set | Minimal intersection smoke | Build common accepted/serviceable intersection and run at least one fixed-set routing diagnostic. | Yes |
| Fixed accepted-set | All core methods fixed-set | More complete but heavier. | |
| Fixed accepted-set | Generate file only | Do not actually run a routing diagnostic. | |
| ALNS/MILP gap | Optional non-blocking diagnostic | Run if Gurobi is available; otherwise record no_gurobi as non-blocking. | Yes |
| ALNS/MILP gap | Must run small instance | Stronger but solver/license dependent. | |
| ALNS/MILP gap | Do not touch MILP | Leave MILP entirely out of Phase 5. | |

**User's choice:** Complete small-sample matched-coverage diagnostic; tolerance failure blocks; minimal fixed accepted-set intersection smoke; optional non-blocking ALNS/MILP diagnostic.
**Notes:** Coverage-control diagnostics are readiness checks only. They should not be used to support method-superiority claims.

---

## the agent's Discretion

- Exact seed IDs.
- Exact small scale value, with `n_requests=20` preferred by local runner-smoke precedent.
- Exact pilot directory, CSV/JSON filenames, plot filenames, and bug ledger format.
- Exact matched-coverage tolerance value, as long as failure is blocking once defined.

## Deferred Ideas

None. Discussion stayed within Phase 5 scope.
