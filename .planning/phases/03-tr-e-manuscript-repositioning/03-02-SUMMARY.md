---
phase: 03-tr-e-manuscript-repositioning
plan: 03-02
subsystem: manuscript
tags: [literature, model, algorithm, gamma, milp, synthetic-scenario]
requires:
  - phase: 03-01
    provides: TR-E front matter and introduction frame
provides:
  - TR-E operations literature positioning
  - model-scope wording for binary-logit response, Gamma, passenger types, and scenarios
  - algorithm-scope wording for rolling-horizon heuristic and MILP diagnostics
affects: [phase-04-numerical-provenance, manuscript, limitations]
tech-stack:
  added: []
  patterns: [diagnostic qualifier lock, synthetic scenario qualifier, post-hoc Gamma qualifier]
key-files:
  created: []
  modified:
    - manuscript/sections/literature.tex
    - manuscript/sections/model.tex
    - manuscript/sections/algorithm.tex
key-decisions:
  - "Passenger types are simulation-range constructs for monitoring service-design heterogeneity."
  - "Gamma does not affect routing, offer generation, or acceptance."
  - "MILP is a simplified ex-post diagnostic over fixed accepted sets."
patterns-established:
  - "Middle-section diagnostics use explicit qualifiers rather than optimality or validation claims."
  - "Beijing-related scenario wording is synthetic and not field validation."
requirements-completed: [POSE-03, CLAI-06, CLAI-07, CLAI-08, MANU-04, MANU-08]
duration: 8 min
completed: 2026-06-17
---

# Phase 03 Plan 03-02: Middle-Section Scope Summary

**Literature, model, and algorithm sections now support a TR-E operations manuscript without overstating evidence scope.**

## Performance

- **Duration:** 8 min
- **Started:** 2026-06-17T21:08:08+08:00
- **Completed:** 2026-06-17T21:16:00+08:00
- **Tasks:** 3
- **Files modified:** 3

## Accomplishments

- Rebuilt the literature review around DARP/DRT operations, meeting-point service consolidation, passenger choice, and rolling-horizon logistics.
- Clarified that binary-logit response and passenger types are simulation mechanisms, not empirical behavioral validation.
- Recast the MILP discussion as a simplified ex-post diagnostic over fixed accepted sets, while keeping ALNS as a rolling-horizon heuristic.

## Task Commits

1. **Task 1: Strengthen literature review around TR-E operations domains** - `92b8265` (docs)
2. **Task 2: Clarify model mechanism, Gamma, passenger-type, and synthetic-scenario semantics** - `f11bb97` (docs)
3. **Task 3: Clarify rolling-horizon heuristic and MILP diagnostic scope** - `dc2cbd1` (docs)

## Files Created/Modified

- `manuscript/sections/literature.tex` - Repositioned related work toward logistics, operations, service consolidation, and dynamic DRT.
- `manuscript/sections/model.tex` - Added explicit Gamma, passenger-type, and synthetic-scenario scope boundaries.
- `manuscript/sections/algorithm.tex` - Weakened MILP language to fixed-accepted-set diagnostic scope.

## Decisions Made

- Did not add new bibliography entries because the existing cited sources supported the narrowed TR-E operations positioning.
- Kept exact numerical parameter examples in the model section where they define simulation parameters rather than final experimental claims.
- Replaced scanner-sensitive negated phrases with alternative limitation wording to keep automated prohibited-wording scans clean.

## Deviations from Plan

None - plan executed exactly as written.

## Issues Encountered

None.

## User Setup Required

None - no external service configuration required.

## Next Phase Readiness

Ready for Plan 03-03 experiments narrative restructuring. Phase 4 still owns numerical values, final table/figure references, and provenance checks.

---
*Phase: 03-tr-e-manuscript-repositioning*
*Completed: 2026-06-17*
