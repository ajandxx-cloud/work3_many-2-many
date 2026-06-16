# TR_E_Bidirectional_MeetingPoint_DRT_Experiment_Rebuild

## What This Is

This is a brownfield GSD research project to rebuild the experimental workflow and evidence chain for a many-to-many DRT manuscript on bidirectional pickup/dropoff meeting-point assignment, passenger response, and dynamic routing. The target is Transportation Research Part E or a comparable high-quality transport/operations journal, with the paper framed as a rigorous choice-aware dynamic service-design simulation study rather than as an unconditional claim that bidirectional meeting points are always superior.

The repository already contains Python simulation code, ALNS and MILP diagnostic modules, experiment runners, results, analysis scripts, and a LaTeX manuscript. The project will audit those artifacts first, then rebuild baselines, metrics, calibration, algorithm validation, formal experiments, evidence synthesis, and manuscript structure under strict phase gates.

## Core Value

Produce reproducible, reviewer-resistant evidence that supports only defensible conditional claims about when bidirectional meeting-point DRT improves efficiency, how passenger response changes coverage, and what equity trade-offs arise across passenger types.

## Requirements

### Validated

- Existing Python package `drt` defines core DRT dataclasses, candidate generation, passenger choice, feasibility, insertion, ALNS, and MILP diagnostic modules.
- Existing experiment layer defines scenarios, variants, metrics, runner scripts, sensitivity analysis, equity analysis, and result CSV/JSON outputs.
- Existing manuscript source exists under `manuscript/` with LaTeX sections, bibliography, figures, and compiled PDF.
- Existing GSD codebase map exists under `.planning/codebase/` and identifies architecture, stack, conventions, testing, and concerns.
- Phase 0 mapped current manuscript results and claims to result files, scripts, or explicit ambiguity markers.
- Phase 0 translated review-note weaknesses into routed risks and future phase gates.
- Phase 1 audited literature and novelty positioning, forbidding broad first/only and pickup-side-only claims unless later full-text evidence supports a precise scoped version.
- Phase 1 resolved the venue-positioning conflict for planning by adopting TR-E-level rigor as the evidence bar while keeping policy language secondary and simulation-based.
- Phase 2 defined the fair-comparison contract separating service design, passenger response, routing algorithm, and diagnostic role.
- Phase 2 standardized metric denominators and row-level status vocabulary so served share, behavioral acceptance, feasibility rejection, choice rejection, inserted share, and vehicle-km denominators cannot be mixed.
- Phase 2 locked coverage-confounding controls through unconstrained behavioral, matched-coverage, and fixed accepted-set designs before any new formal runs.
- Phase 4 implemented and validated the behavioral baseline family: DoorToDoor, SingleSidedPickup, SingleSidedDropoff, and BidirectionalMeetingPoint under shared actual-offer choice semantics.
- Phase 4 standardized runner outputs with method metadata, durable failure/timeout rows, explicit vehicle-km denominator fields, and provenance/count fields.
- Phase 4 validated greedy, no-rolling-horizon, ALNS trace, and MILP static-snapshot diagnostics as algorithm evidence only, including a no-Gurobi path.
- Phase 5 ran readiness-only pilot experiments over seeds 42/43/44 at scale 20 for the behavioral method family, with durable raw outputs, status rows, and provenance.
- Phase 5 closed the matched-coverage pilot blockers with per-seed integer target counts based on the minimum serviceable count across FullModel and uncapped DoorToDoorCapped controls.
- Phase 5 closed the fixed accepted-set smoke blocker with an explicit `common_candidate_serviceable` fallback, recorded as pilot readiness evidence only and not as a formal-results construction rule.
- Phase 7 audited case-study data availability and closed as a bounded Beijing-inspired synthetic case. No real or semi-real OD, road-network, transit-stop/POI, request-time, passenger-preference, or fleet data are present in the current repository.
- Phase 8 completed the claim-evidence gate. Every manuscript-facing claim is inventoried, linked to evidence or limitation sources, graded strong/moderate/exploratory/unsupported, and routed to supported wording or delete/rewrite/limitations actions.
- Phase 9 produced and verified the TR-E manuscript architecture, revised abstract plan, revised introduction plan, experiment-section evidence-family plan, and table/figure/managerial-insight plan.
- Phase 9 locked final manuscript wording behind Phase 8 claim-gate artifacts, kept Beijing language bounded to a synthetic scenario, and removed legacy effect-size values from the new planning artifacts.
- Phase 9 refresh consumed the completed Phase 8 claim gate and replaced placeholder-driven manuscript planning with claim-gated structure, abstract, introduction, experiment, table/figure, managerial-insight, limitation, audit, and verification artifacts.

### Active

- [ ] Use the Phase 2 experiment contract when rebuilding choice, baseline, runner, metric, pilot, and formal experiment code.
- [ ] Add credible passenger-choice calibration logic, including service ASC, outside-option sensitivity, type shares, and literature-based or explicitly simulated ranges.
- [ ] Use Phase 5 pilot diagnostics when designing Phase 6 formal controls, while keeping pilot/tuning results separate from final evidence.
- [ ] Run formal paired-seed experiments with at least 20 seeds for synthetic results, preferably 30 if runtime permits.

### Out of Scope

- New experiments before Phase 0 passes, because the current artifact and claim provenance must be audited first.
- Universal policy prescriptions for Chinese city operators from synthetic scenarios, because current data are Beijing-inspired synthetic rather than real or semi-real.
- Any headline claim that bidirectional meeting-point DRT is generally superior to door-to-door service unless matched, calibrated, reproducible evidence supports the exact comparison condition.
- Retuning parameters after seeing formal results without creating a new preregistration and archiving prior outputs as exploratory or failed.

## Context

The user-provided rebuild brief requires a strict GSD phase-gated process. It identifies the current manuscript's central weaknesses: unfair baselines because only FullModel uses binary logit response, coverage-confounded vkm/trip results, uncalibrated utility parameters, insufficient ALNS validation, synthetic-data policy overreach, and unsupported or overstrong claims.

The review note `docs/工作3讨论-6.14.md` reinforces the same risk set. It flags novelty overclaiming around DARP with meeting points, the need to audit Cortenbach et al. (2024), Fielbaum et al. (2021), and Wu et al. (2025), the lack of calibrated passenger-choice parameters, coverage confounding in the 29.1% vkm/trip improvement, inconsistent response mechanisms across variants, large MILP-vs-ALNS gaps, incomplete MILP formulation, too few seeds, synthetic Beijing policy overreach, post-hoc gamma/Pareto interpretation problems, and overinterpreted equity diagnostics.

The current README says the target journal is Transportation Research Part A, while the rebuild prompt asks for Transportation Research Part E or comparable quality. Phase 1 resolved this for planning: use TR-E-level rigor as the evidence bar, and keep TR-A-style policy claims secondary unless later case-study evidence supports them.

## Constraints

- **Strict phase gates**: Do not enter the next phase until the current phase passes success criteria.
- **No hidden failed results**: Failed, mixed, inconclusive, timeout, and infeasible runs must be recorded.
- **Pilot/formal separation**: Pilot and tuning runs must not become final evidence.
- **Paired experiments**: Use the same seeds, request streams, fleet settings, meeting-point sets, and demand realizations across method comparisons where possible.
- **Evidence-graded claims**: Strong, moderate, exploratory, and unsupported claims must be separated before manuscript rewriting.
- **Reproducibility**: Save raw results, processed results, configs, seeds, logs, failure rows, and provenance.
- **Synthetic-data honesty**: Beijing-inspired synthetic grids must not be described as real Beijing case evidence.

## Key Decisions

| Decision | Rationale | Outcome |
|----------|-----------|---------|
| Initialize this as a brownfield GSD project | The repository already has code, manuscript, results, and `.planning/codebase` maps | Complete |
| Start with Phase 0 only | The rebuild brief explicitly forbids new experiments before repository and manuscript audit pass | Complete |
| Treat current positive efficiency findings as provisional | Served share and passenger-response differences confound existing vkm/trip comparisons | Confirmed by Phase 0 audit |
| Use TR-E-level contribution framing | Phase 1 approved the integrated choice-aware dynamic service-design framework as the safe contribution center | Complete |
| Forbid broad first/only novelty language | Phase 1 found prior work already narrows bidirectional walking and meeting-point novelty | Complete |
| Treat Phase 0 current results as exploratory provenance inputs, not final evidence | Main table, matched coverage, gamma, weight sensitivity, and policy outputs all have caveats | Complete |
| Keep algorithm diagnostics separate from behavioral evidence | Phase 4 validated greedy, no-RH, ALNS, and MILP diagnostics as algorithm evidence only | Complete |
| Treat Phase 5 pilot closure as readiness evidence only | Gap closure fixed pilot blockers without creating formal experiment evidence or manuscript claims | Complete |
| Treat Phase 9 manuscript restructuring as claim-gated planning, not direct LaTeX rewriting | Phase 8 supported/unsupported claim artifacts are absent, so final prose and captions must remain placeholders | Complete |
| Keep Phase 7 as a Beijing-inspired synthetic boundary, not a real case study | The repository has generated OD, generated meeting points, simulated times, and no imported real/semi-real case data | Complete |
| Treat Phase 8 as the source of truth for final manuscript claims | The claim gate maps formal Phase 6 evidence and Phase 7 case limitations to allowed, forbidden, and downgraded wording | Complete |
| Refresh Phase 9 after Phase 8 before Phase 10 | The earlier Phase 9 artifacts were preliminary because Phase 8 did not exist yet | Complete |

## Evolution

This document evolves at phase transitions and milestone boundaries.

**After each phase transition**:
1. Requirements invalidated? Move to Out of Scope with reason.
2. Requirements validated? Move to Validated with phase reference.
3. New requirements emerged? Add to Active.
4. Decisions to log? Add to Key Decisions.
5. "What This Is" still accurate? Update if drifted.

**After each milestone**:
1. Full review of all sections.
2. Core Value check: still the right priority?
3. Audit Out of Scope: reasons still valid?
4. Update Context with current state.

---
*Last updated: 2026-06-16 after Phase 9 claim-gated manuscript refresh*
