# Phase 3: Passenger Choice Model Rebuild - Context

**Gathered:** 2026-06-15T14:34:20+08:00
**Status:** Ready for planning

<domain>
## Phase Boundary

Phase 3 rebuilds the passenger choice model so passenger response is credible,
interpretable, consistently shared across behavioral service designs, and
sensitivity-tested before pilot or formal experiments.

In scope:
- Replace the current proxy-before-routing MNL filtering with acceptance based
  on an actual feasible single-offer service bundle.
- Define the choice-model contract, including service ASC, outside option,
  passenger type parameters, passenger type shares, seeded type assignment,
  and utility-component logging.
- Define parameter calibration documentation with baseline values, low/high
  sensitivity values or multipliers, source tags, and literature-anchored vs
  simulation-range labels.
- Define the sensitivity-grid scope for later pilot and formal runs.
- Add tests or test requirements for choice probabilities, status separation,
  paired type assignment, and utility logging.

Out of scope:
- Multi-offer choice-set behavior beyond interface extensibility.
- Fallback offers after passenger rejection.
- Formal experiment execution, pilot execution, ALNS/MILP diagnostics, and
  final manuscript claim approval.

</domain>

<decisions>
## Implementation Decisions

### Offer Bundle Timing and Status Handling
- **D-01:** Passenger choice must be based on an actual feasible service bundle,
  not a nearest-meeting-point proxy computed before routing.
- **D-02:** Phase 3 implements a single-offer acceptance model. The interface
  should be shaped so future multi-offer choice sets are possible, but Phase 3
  must not implement multi-offer selection.
- **D-03:** A passenger refusal is a final `choice_rejected` state in Phase 3.
  Rejected passengers do not receive fallback offers and do not proceed into
  feasibility or routing.
- **D-04:** Requests without any feasible offer should aggregate as
  `feasibility_rejected`, while row-level outputs preserve detailed reasons
  such as `no_candidate_mp` and `no_feasible_route`.

### Utility and Calibration Structure
- **D-05:** The main model uses a unified DRT service ASC. Design-specific ASC
  values are tested only in sensitivity analysis.
- **D-06:** Add an explicit `outside_option_constant` parameter. The main model
  uses one baseline value; sensitivity analysis tests stronger and weaker
  outside-option attractiveness.
- **D-07:** Passenger type parameters should use literature-anchored main values
  plus explicitly labeled simulation ranges. Do not describe these as real-data
  calibration unless real choice data are later introduced.
- **D-08:** Passenger type shares should be scenario parameters. Type assignment
  must be seeded at request level so the same seed/request has the same passenger
  type across all service designs in paired comparisons.

### Sensitivity Grid Scope
- **D-09:** The main sensitivity design should be one-at-a-time. Supplementary
  analysis may include a few targeted interaction checks, but no full factorial
  grid is required by Phase 3.
- **D-10:** Main-paper sensitivity should focus on reviewer-critical weaknesses:
  ASC, outside option, passenger type shares, and walk sensitivity.
- **D-11:** Wait, IVT, and fare coefficients should appear in the parameter table
  and supplementary sensitivity, but not as the main sensitivity figures unless
  later evidence makes them central.
- **D-12:** Main sensitivity values should be low / baseline / high. Optional
  supplementary five-level or targeted grids are allowed only if Phase 6 runtime
  permits.
- **D-13:** `03_PARAMETER_CALIBRATION.md` should document baseline values,
  low/high values or multipliers, source tags, and whether each value is
  literature-anchored or a simulation range.

### Utility-Component Logging
- **D-14:** Formal row-level logging should include explainability fields:
  status, detailed reason, passenger type, offer attributes, utility components,
  total utility, outside utility, acceptance probability, and random draw.
  Candidate lists and route snapshots are debug outputs only.
- **D-15:** Logged offer attributes must include `pickup_walk`, `dropoff_walk`,
  `wait_time`, `ivt`, `fare`, `service_design`, `pickup_mp_id`,
  `dropoff_mp_id`, `vehicle_id`, `scheduled_pickup`, and `scheduled_dropoff`.
- **D-16:** `choice_rejected` rows record the complete utility of the actual
  offered bundle. `feasibility_rejected` rows must not fabricate proxy utility;
  they record feasibility reason and missing-offer cause instead.
- **D-17:** Use a two-layer output structure: raw passenger rows keep status and
  key probability fields, while complete utility components are stored in a
  separate artifact linked by `run_id`, `seed`, `scenario`, `method`, and
  `request_id`.

### the agent's Discretion

The planner may choose exact filenames, dataclass names, and helper boundaries
as long as the implementation preserves the decisions above and remains
consistent with the existing `src/drt/` core plus `experiments/` composition
layers.

</decisions>

<canonical_refs>
## Canonical References

**Downstream agents MUST read these before planning or implementing.**

### Project and Phase Definition
- `.planning/ROADMAP.md` - Phase 3 goal, requirements, success criteria, and expected outputs.
- `.planning/REQUIREMENTS.md` - CHO-01 through CHO-04 and Phase 2/6 constraints affecting choice experiments.
- `.planning/PROJECT.md` - Core value, TR-E rigor, strict phase gates, paired experiment constraints, and synthetic-data honesty.
- `.planning/STATE.md` - Current project status and active blockers entering Phase 3.

### Prior Phase Contracts
- `.planning/phases/02-experimental-contract-and-metric-standardization/02-CONTEXT.md` - Shared-response requirement, row-level status vocabulary, metric denominator contract, and coverage-confounding controls.
- `.planning/phases/02-experimental-contract-and-metric-standardization/02_EXPERIMENT_CONTRACT.md` - Fair-comparison family contract that Phase 3 choice logic must support.
- `.planning/phases/02-experimental-contract-and-metric-standardization/02_METRICS_DEFINITIONS.md` - Metric formulas and status vocabulary that utility logging must feed.
- `.planning/phases/02-experimental-contract-and-metric-standardization/02_COVERAGE_CONFOUNDING_PLAN.md` - Matched-coverage and fixed accepted-set context affected by choice outcomes.

### Codebase Maps
- `.planning/codebase/ARCHITECTURE.md` - Existing layered architecture, choice helper location, variant layer, metrics layer, and runner outputs.
- `.planning/codebase/TESTING.md` - Active pytest patterns and relevant test locations.
- `.planning/codebase/CONCERNS.md` - Current MNL proxy weakness, gamma/post-hoc concern, metric/status issues, and test gaps.

### Source Integration Points
- `src/drt/choice.py` - Existing MNL utility and binary logit acceptance functions.
- `src/drt/types.py` - Existing `Bundle`, `PassengerType`, request, vehicle, meeting-point, and route dataclasses.
- `experiments/variants.py` - Current `_mnl_filter_requests`, `FullModel`, `AblationNoRollingHorizon`, and behavioral variant integration points.
- `experiments/metrics.py` - Existing `PassengerRecord`, `SimulationResult`, `MetricsResult`, and welfare helper.
- `experiments/config.py` - Existing experiment constants, cost weights, and note that gamma is currently post-hoc only.

</canonical_refs>

<code_context>
## Existing Code Insights

### Reusable Assets
- `src/drt/choice.py`: Existing `mnl_utility()` and `accept_probability()` can be extended or wrapped for ASC, outside option, utility components, and actual-offer bundle evaluation.
- `src/drt/types.py`: Existing `Bundle` and `PassengerType` are natural contracts to extend, but changes must preserve compatibility with current callers.
- `experiments/variants.py`: Existing `BaseVariant.run()` and variant registry are the likely integration point for applying shared passenger response across DoorToDoor, SingleSidedPickup, SingleSidedDropoff, and BidirectionalMP-style methods.
- `experiments/metrics.py`: Existing passenger records should be extended or paired with a separate utility-components artifact rather than overloading aggregate metrics.

### Established Patterns
- Core choice and routing primitives live under `src/drt/`; experiment-specific composition and output writing live under `experiments/`.
- Behavioral variants are composed as `BaseVariant` subclasses. Phase 3 should avoid adding a special-case runner path for only one method.
- Tests use deterministic generated scenarios and local factory helpers. Phase 3 tests should keep seeded choice/type assignment deterministic.
- Result artifacts are CSV/JSON style files under `results/`; Phase 3 should define schemas that Phase 4/5 can implement and smoke-test.

### Integration Points
- Replace or retire `_mnl_filter_requests()` in `experiments/variants.py` because it currently evaluates nearest meeting-point proxies before routing.
- DoorToDoor and meeting-point service designs must share the same passenger response logic in behavioral experiments, with service design differences reflected through actual offer attributes and sensitivity settings.
- Row-level status fields and utility logs must feed Phase 2 metrics without mixing `choice_rejected`, `feasibility_rejected`, `served`, `failed`, or `timeout`.
- Phase 4 will need to align baseline implementation and algorithm checks with the Phase 3 choice contract.

</code_context>

<specifics>
## Specific Ideas

- Treat the choice model as a single-offer acceptance model for the paper, not as a full choice-set model.
- Keep design-specific ASC out of the main evidence so main results are not driven by free service-design constants.
- Use paired, seeded passenger type assignment to preserve fair comparisons across service designs.
- Keep full utility-component logs separate from raw passenger rows, but joinable by run and request identifiers.

</specifics>

<deferred>
## Deferred Ideas

- Multi-offer passenger choice sets may be a future extension, but Phase 3 only implements single-offer acceptance.
- Fallback offers after rejection may be studied later, but are outside Phase 3.
- Full route snapshots, candidate bundle lists, and route-state debug traces are development/debug artifacts, not formal Phase 3 evidence outputs.

</deferred>

---

*Phase: 3-Passenger Choice Model Rebuild*
*Context gathered: 2026-06-15T14:34:20+08:00*
