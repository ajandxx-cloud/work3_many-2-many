# Phase 2: Experimental Contract and Metric Standardization - Context

**Gathered:** 2026-06-15
**Status:** Ready for planning

<domain>
## Phase Boundary

Phase 2 defines the experiment contract and metric standardization rules that later phases must follow before any new formal evidence is generated. It locks how service variants, passenger response assumptions, routing diagnostics, coverage controls, metric denominators, statistical comparisons, and claim boundaries should be documented.

In scope:
- Define fair experiment families for behavioral service-design evidence and supplementary diagnostics.
- Standardize the baseline taxonomy across service design, passenger response, routing algorithm, and diagnostic role.
- Define metric formulas, denominators, units, valid interpretations, and forbidden/high-risk metric language.
- Specify coverage-confounding controls, including matched-coverage and fixed accepted-set diagnostics.
- Specify statistical comparison methods without locking the final formal-experiment sample size.
- Produce a later-phase code-change task list for Phase 4/5 schema, variant, runner, and output updates.

Out of scope:
- Running new experiments.
- Rebuilding or calibrating the passenger choice model; that belongs to Phase 3.
- Implementing baseline, schema, runner, ALNS, MILP, or metric code changes; those belong to Phase 4/5.
- Defining detailed ALNS/MILP exact diagnostic scope; that belongs to Phase 4.
- Approving final manuscript claims; that belongs to Phase 8.

</domain>

<decisions>
## Implementation Decisions

### Experiment Family Boundary
- **D-01:** The main evidence should present the full tradeoff among coverage, behavioral acceptance, and operating efficiency for bidirectional meeting-point service design. It must not reduce the central question to vehicle-km savings alone.
- **D-02:** Behavioral choice experiments and deterministic feasibility/routing diagnostics must be strictly separated. Behavioral choice experiments provide the main service-design evidence; deterministic diagnostics explain mechanisms and implementation behavior.
- **D-03:** Fixed accepted-set routing comparisons are core supplementary diagnostics. Their role is to answer whether routing efficiency differences persist when the passenger set is held constant.
- **D-04:** Detailed ALNS/MILP exact diagnostic scope is not defined in Phase 2. Phase 2 may name the need for algorithm diagnostics, but Phase 4 must define and validate the ALNS/MILP scope.

### Baseline Taxonomy Naming
- **D-05:** The baseline taxonomy must use four axes: service design, passenger response, routing algorithm, and diagnostic role. Downstream plans should avoid code-variant names as the primary conceptual taxonomy.
- **D-06:** Replace the current `FullModel` label in planning and paper-facing contracts with a descriptive method label such as `BidirectionalMP + Choice + RollingHorizon/ALNS`.
- **D-07:** `SingleSidedPickup` and `SingleSidedDropoff` should both be formal service-design baselines using the same passenger-response and routing setup as the main behavioral comparison.
- **D-08:** `DoorToDoor` must use the same passenger choice model as meeting-point services in behavioral experiments, with walk distance set to zero and service attributes adapted to the offered bundle. It must not remain deterministic all-accept in the main behavioral comparison.

### Metric Denominator Contract
- **D-09:** Main behavioral tables must report `served_share`, `behavioral_acceptance_rate`, `choice_rejection_rate`, and `feasibility_rejection_rate` together so coverage and rejection mechanisms cannot be hidden.
- **D-10:** `served_share` means final served or completed requests divided by original requests.
- **D-11:** The ambiguous label `vkm_per_trip` is forbidden for new formal evidence. Use `vkm_per_served_trip` and `vkm_per_original_request` instead.
- **D-12:** Every request must have a durable row-level status such as `choice_rejected`, `feasibility_rejected`, `served`, `failed`, `timeout`, or equivalent. Aggregate metrics must be derivable from request-level status rows.
- **D-13:** The metric definitions output must include a forbidden/high-risk metric section covering ambiguous `vkm_per_trip`, post-hoc `gamma`/Pareto-frontier language, and mixed acceptance denominators.

### Coverage Confounding Controls
- **D-14:** Matched-coverage should be a core supplementary experiment in the main manuscript, not merely an appendix robustness check and not a replacement for unconstrained behavioral results.
- **D-15:** The matched-coverage control should use a target `served_share` cap so each service design is compared near the same coverage level.
- **D-16:** If unconstrained behavioral results show BidirectionalMP has lower vehicle-km but also lower `served_share`, the result must be framed as a coverage-efficiency tradeoff. It must not support an unconditional "overall superior" claim.
- **D-17:** Fixed accepted-set diagnostics should use the intersection of requests commonly serviceable/accepted by all methods. This avoids bias toward any one service design, including BidirectionalMP or DoorToDoor.
- **D-18:** Fixed accepted-set diagnostics are diagnostic experiments only. They do not replace the behavioral main evidence.

### Output File Granularity
- **D-19:** Phase 2 should produce one main experiment contract plus two standalone appendices: a metric definitions appendix and a statistical plan appendix.
- **D-20:** The main experiment contract should lock experiment design, service variants, main/supplementary evidence roles, and claim boundaries.
- **D-21:** Metric definitions and the statistical plan should be standalone so later code and manuscript tables can cite them directly.
- **D-22:** The statistical plan should specify paired seeds, paired differences, confidence intervals, and concrete computation methods, but should not lock the final formal-experiment sample size.
- **D-23:** Phase 2 should output a Phase 4/5 code-change task list for schema, variant, runner, metric, and output changes. Phase 2 must not implement those code changes.

### the agent's Discretion

The planner may choose exact document filenames and section organization as long as the structure preserves one main contract plus standalone metric and statistical appendices. A recommended file set is:
- `.planning/phases/02-experimental-contract-and-metric-standardization/02_EXPERIMENT_CONTRACT.md`
- `.planning/phases/02-experimental-contract-and-metric-standardization/02_METRICS_DEFINITIONS.md`
- `.planning/phases/02-experimental-contract-and-metric-standardization/02_STATISTICAL_PLAN.md`
- optional embedded or separate Phase 4/5 code task list, if the planner judges a separate file clearer.

</decisions>

<canonical_refs>
## Canonical References

**Downstream agents MUST read these before planning or implementing.**

### Project and Phase Definition
- `.planning/ROADMAP.md` - Phase 2 goal, requirements, success criteria, and expected outputs.
- `.planning/REQUIREMENTS.md` - EXP-01 through EXP-04 and MET-01 through MET-03; also Phase 6 experiment split constraints.
- `.planning/PROJECT.md` - Core value, active requirements, constraints, and project-level decisions about TR-E rigor and conditional claims.
- `.planning/STATE.md` - Current status, Phase 1 carry-forward decisions, and active blockers.
- `.planning/CLAIMS_AND_RISKS.md` - Risk register and forbidden claim language relevant to Phase 2.

### Prior Phase Audit Inputs
- `.planning/phases/00-repository-and-manuscript-audit/00_CURRENT_EXPERIMENT_MAP.md` - Current variant registry, experiment families, metric surface, provenance risks, and required future taxonomy.
- `.planning/phases/00-repository-and-manuscript-audit/00_MANUSCRIPT_CLAIM_AUDIT.md` - Current claim classifications and evidence risks, including coverage confounding and mixed response mechanisms.
- `.planning/phases/00-repository-and-manuscript-audit/00_REPOSITORY_AUDIT.md` - Current repository/module map and Phase 2 routed concerns.
- `.planning/phases/01-literature-and-novelty-audit/01-CONTEXT.md` - Prior decisions on conservative novelty standards and TR-E-level rigor.
- `.planning/phases/01-literature-and-novelty-audit/01_NOVELTY_POSITIONING.md` - Approved integrated-framework framing and forbidden novelty wording.
- `.planning/phases/01-literature-and-novelty-audit/01_REVISED_RESEARCH_QUESTIONS.md` - RQ links to matched-coverage and fixed accepted-set designs.

### Codebase Maps
- `.planning/codebase/STACK.md` - Python/experiment stack, dependency expectations, and result-generation context.
- `.planning/codebase/ARCHITECTURE.md` - Existing experiment architecture, variant layer, metrics layer, runner layer, and output flow.
- `.planning/codebase/CONCERNS.md` - Known metric, coverage, choice, gamma, runner, ALNS/MILP, and provenance concerns that Phase 2 must address in contracts.

</canonical_refs>

<code_context>
## Existing Code Insights

### Reusable Assets
- `experiments/variants.py`: Existing variant implementations include `DoorToDoor`, `DoorToDoorCapped`, `SingleSidedPickup`, `BidirectionalNoChoice`, `FullModel`, `AblationNoRollingHorizon`, and `AblationNoChoice`. Phase 2 should map these into the four-axis taxonomy and identify missing `SingleSidedDropoff`.
- `experiments/metrics.py`: Existing `MetricsResult`, `compute_metrics()`, and `vkm_per_trip()` provide the current metric surface but need a stricter denominator contract.
- `experiments/runner.py`: Existing raw/aggregate CSV writer is the likely integration point for request status, config, seed, failure, and standardized metric outputs.
- `experiments/endogenous_matched_coverage.py`: Current closest implementation to served-share cap matched coverage; Phase 2 should define the desired formal semantics before Phase 4/5 implementation.
- `experiments/matched_coverage.py`: Current post-hoc random-rejection diagnostic; Phase 2 should distinguish it from the chosen served-share cap method.

### Established Patterns
- Experiment behavior is composed through `BaseVariant` subclasses and `ALL_VARIANTS` in `experiments/variants.py`.
- Scenario and output dataclasses form the contract between variants, metrics, and runner code.
- Result artifacts are CSV/JSON files under `results/`; Phase 2 should require future formal outputs to include enough provenance and row-level status for traceability.
- Current `FullModel` applies MNL filtering before actual route offer and `gamma` is post-hoc only. Phase 2 must avoid any final-evidence language that treats current gamma sweeps as an endogenous frontier.

### Integration Points
- Phase 3 will rebuild the passenger choice model that Phase 2 requires all behavioral service designs to share.
- Phase 4 will implement or validate missing variants, schema changes, deterministic diagnostics, and ALNS/MILP scope.
- Phase 5 will pilot-test the standardized outputs, request statuses, matched-coverage cap logic, and fixed accepted-set diagnostics.
- Phase 6 will run paired formal experiments using the Phase 2 contract.

</code_context>

<specifics>
## Specific Ideas

- Use `matched-coverage` as a main-text core supplementary experiment with a target `served_share` cap.
- Use fixed accepted-set only as a diagnostic, based on the intersection of requests commonly serviceable/accepted by all methods.
- Make the final evidence story about coverage, acceptance, and efficiency tradeoffs rather than unconditional method superiority.
- Keep metric definitions and statistical methods standalone so code and manuscript tables can cite them directly.

</specifics>

<deferred>
## Deferred Ideas

- Passenger choice calibration, service ASC, outside option, and passenger-type sensitivity belong to Phase 3.
- Detailed ALNS/MILP exact diagnostic scope and implementation validation belong to Phase 4.
- Pilot execution and code smoke-testing belong to Phase 5.
- Formal sample size and final seed count belong to Phase 6, after runtime and pilot results are known.
- Final claim approval and manuscript wording belong to Phase 8 and Phase 9.

</deferred>

---

*Phase: 2-Experimental Contract and Metric Standardization*
*Context gathered: 2026-06-15*
