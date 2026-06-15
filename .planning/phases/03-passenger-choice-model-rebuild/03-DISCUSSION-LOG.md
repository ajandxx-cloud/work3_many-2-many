# Phase 3: Passenger Choice Model Rebuild - Discussion Log

> **Audit trail only.** Do not use as input to planning, research, or execution agents.
> Decisions are captured in CONTEXT.md; this log preserves the alternatives considered.

**Date:** 2026-06-15T14:34:20+08:00
**Phase:** 3-Passenger Choice Model Rebuild
**Areas discussed:** Offer bundle timing and status handling, Utility and calibration structure, Sensitivity grid scope, Utility-component logging

---

## Offer Bundle Timing and Status Handling

| Decision Point | Options Considered | Selected |
|----------------|--------------------|----------|
| Passenger choice offer basis | Actual feasible service bundle; candidate bundle proxy; keep nearest-point proxy and document limits | Actual feasible service bundle |
| Number of offers | Single-offer; small choice set; Phase 3 single-offer with future choice-set extensibility | Phase 3 single-offer with future choice-set extensibility |
| Passenger refusals | Choice rejection is final; allow fallback offer; fallback only in diagnostics | Choice rejection is final |
| No feasible offer status | `feasibility_rejected`; detailed feasibility reasons; `unserved` | Aggregate as `feasibility_rejected` with row-level details |

**User's choice:** Actual feasible single-offer bundle; no fallback after rejection; detailed feasibility reasons.
**Notes:** Multi-offer and fallback behavior were identified as future extensions, not Phase 3 scope.

---

## Utility and Calibration Structure

| Decision Point | Options Considered | Selected |
|----------------|--------------------|----------|
| Service ASC | Design-specific ASC; unified DRT ASC only; unified main ASC plus design-specific sensitivity | Unified main ASC plus design-specific sensitivity |
| Outside option | Fixed `U_outside = 0`; explicit `outside_option_constant`; passenger-type-specific outside option | Explicit `outside_option_constant` |
| Parameter source | Literature-anchored main parameters plus simulation-range sensitivity; pure simulation ranges; full empirical calibration | Literature-anchored main parameters plus simulation-range sensitivity |
| Passenger type shares | Fixed equal shares; share scenarios; seeded paired assignment; share scenarios plus seeded paired assignment | Share scenarios plus seeded paired assignment |

**User's choice:** Use a conservative main specification with explicit sensitivity and paired passenger type assignment.
**Notes:** The discussion explicitly rejected implying empirical calibration without real choice data.

---

## Sensitivity Grid Scope

| Decision Point | Options Considered | Selected |
|----------------|--------------------|----------|
| Grid organization | One-at-a-time; small factorial; main one-at-a-time plus targeted supplementary interactions | Main one-at-a-time plus targeted supplementary interactions |
| Main sensitivity dimensions | All seven dimensions; walk/wait/ASC/outside/type shares; ASC/outside/type shares/walk | ASC, outside option, type shares, and walk sensitivity |
| Value granularity | Low / baseline / high; five-point grid; main three-level plus optional supplementary grid | Main three-level plus optional supplementary grid |
| Calibration document detail | Principles only; baseline plus low/high and source tags; complete formal-experiment table | Baseline plus low/high and source tags |

**User's choice:** Keep the main sensitivity interpretable and focused on reviewer weaknesses.
**Notes:** Wait, IVT, and fare remain documented and available for supplementary sensitivity, but are not the main Phase 3 story.

---

## Utility-Component Logging

| Decision Point | Options Considered | Selected |
|----------------|--------------------|----------|
| Logging granularity | Minimal fields; explainability fields; full debug fields | Explainability fields |
| Offer attributes | Core choice attributes; core plus route/meeting-point identifiers; core plus full route geometry | Core plus route/meeting-point identifiers |
| Rejected utility fields | Choice-rejected utility only; all rejected utility zero; proxy utility for feasibility rejection | Choice-rejected utility only |
| Utility artifact structure | Embed in raw rows; separate utility log only; raw rows plus separate complete utility-components artifact | Raw rows plus separate complete utility-components artifact |

**User's choice:** Formal logs should be explainable and reproducible without becoming full routing debug traces.
**Notes:** Feasibility-rejected rows must not reintroduce nearest-proxy utility.

## the agent's Discretion

- Exact filenames, dataclass names, and helper boundaries can be chosen during planning and implementation.
- The implementation may choose how to preserve compatibility with existing `Bundle`, `PassengerType`, `PassengerRecord`, and variant interfaces.

## Deferred Ideas

- Multi-offer passenger choice sets.
- Fallback offers after passenger rejection.
- Full candidate-bundle and route-state debug traces as formal evidence artifacts.
