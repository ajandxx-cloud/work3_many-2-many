---
phase: 04-baseline-and-algorithm-implementation-check
plan: 04-01
subsystem: experiments
tags: [variants, choice, baselines, metadata]
requires:
  - phase: 03-passenger-choice-model-rebuild
    provides: actual-offer choice semantics
provides:
  - SingleSidedDropoff behavioral baseline
  - concept-level method metadata for variants
  - Phase 04 variant mapping and baseline audit
affects: [phase-05-pilot-runs, phase-06-formal-experiments]
tech-stack:
  added: []
  patterns: [method_metadata on BaseVariant, shared actual-offer baseline harness]
key-files:
  created:
    - .planning/phases/04-baseline-and-algorithm-implementation-check/VARIANT_MAPPING.md
    - .planning/phases/04-baseline-and-algorithm-implementation-check/04_IMPLEMENTATION_AUDIT.md
  modified:
    - experiments/variants.py
    - tests/test_variants.py
key-decisions:
  - "Kept legacy implementation class names while exposing paper-facing concept labels through method_metadata."
  - "Registered SingleSidedDropoff as the symmetric dropoff-side behavioral service baseline."
patterns-established:
  - "Behavioral variants identify evidence_family and diagnostic_role explicitly."
  - "Legacy class names are provenance only, not paper-facing labels."
requirements-completed: [ALG-01, ALG-02]
duration: 35 min
completed: 2026-06-15
---

# Phase 04 Plan 01: Shared Behavioral Baselines and Method Mapping Summary

**SingleSidedDropoff and concept-level variant metadata make behavioral baselines paper-safe before pilot runs**

## Performance

- **Duration:** 35 min
- **Started:** 2026-06-15T09:40:00Z
- **Completed:** 2026-06-15T10:15:00Z
- **Tasks:** 4
- **Files modified:** 4

## Accomplishments

- Added `SingleSidedDropoff` under the shared actual-offer choice sequence.
- Added `method_metadata` for behavioral, supplementary, deterministic, and algorithm diagnostic variants.
- Extended variant tests to cover the four behavioral service designs as a comparable family.
- Created the variant mapping and baseline implementation audit documents.

## Task Commits

1. **Tasks 1-4: shared behavioral baseline mapping** - `913b056` (feat)

## Files Created/Modified

- `experiments/variants.py` - Added `SingleSidedDropoff`, concept metadata fields, and registry entry.
- `tests/test_variants.py` - Added behavioral-family tests for dropoff walking, metadata, legacy-filter bypass, declined insertion, and passenger type pairing.
- `.planning/phases/04-baseline-and-algorithm-implementation-check/VARIANT_MAPPING.md` - Maps code variants to concept labels and evidence roles.
- `.planning/phases/04-baseline-and-algorithm-implementation-check/04_IMPLEMENTATION_AUDIT.md` - Records D-01 through D-11 baseline-family status.

## Decisions Made

- Kept `FullModel` as the implementation class for compatibility, while exposing `BidirectionalMP_Choice_RH_ALNS` as the concept label.
- Used `behavioral_main` as the evidence family for the four shared-response service-design variants.

## Deviations from Plan

None - plan executed exactly as written.

## Issues Encountered

- The `pytest` launcher did not expose the repository root when `PYTHONPATH=src` was set in this shell. Added the same explicit test path bootstrap already used by other tests.

## Verification

```bash
PYTHONPATH=src pytest tests/test_variants.py -q
```

Result: 21 passed.

## User Setup Required

None - no external service configuration required.

## Next Phase Readiness

Behavioral service-design baselines and method labels are ready for the runner schema work in `04-02` and pilot smoke consumption in Phase 5.

---
*Phase: 04-baseline-and-algorithm-implementation-check*
*Completed: 2026-06-15*

