---
phase: 05-pilot-experiments
plan: 05-04
subsystem: experiments
tags: [phase05, matched-coverage, fixed-accepted-set, pilot, diagnostics]

requires:
  - phase: 05-pilot-experiments
    provides: Phase 5 pilot artifacts and verification blockers
provides:
  - Per-seed integer target-count matched-coverage diagnostics
  - Fixed accepted-set smoke rerun with explicit candidate-serviceable fallback
  - Closed Phase 5 blocker ledger rows for BUG-05-001 through BUG-05-003
affects: [phase06-formal-synthetic-experiments, coverage-control, pilot-readiness]

tech-stack:
  added: []
  patterns: [readiness-only pilot diagnostics, durable blocker ledger, explicit diagnostic fallbacks]

key-files:
  created:
    - .planning/phases/05-pilot-experiments/05-04-SUMMARY.md
  modified:
    - experiments/phase05_coverage_smoke.py
    - tests/test_phase05_pilot.py
    - .planning/phases/05-pilot-experiments/05_BUG_LEDGER.csv
    - .planning/phases/05-pilot-experiments/05_PILOT_RESULTS.md
    - .planning/STATE.md
    - results/pilot/phase05/matched_coverage_pilot.csv
    - results/pilot/phase05/fixed_accepted_set_smoke.json

key-decisions:
  - "Matched-coverage targets are per-seed integer request counts, not a cross-seed mean share."
  - "Seed 42 target adjustment is explicitly recorded because uncapped DoorToDoorCapped can only serve one request in the pilot diagnostic."
  - "The fixed accepted-set smoke records common_candidate_serviceable when stricter served and actual-offer serviceable intersections are empty."

patterns-established:
  - "Pilot gap closure artifacts retain original blocker IDs and close them by rerun evidence instead of deleting history."
  - "Fallback diagnostic construction rules are persisted in JSON/report outputs so they cannot be mistaken for formal evidence."

requirements-completed: [REP-03]

duration: 34min
completed: 2026-06-15
---

# Phase 05 Plan 04: Pilot Gap Closure Summary

**Phase 5 pilot readiness blockers were closed with per-seed matched-coverage targets, a fixed-set routing fallback, regenerated artifacts, and zero remaining Phase 6 blocker rows.**

## Performance

- **Duration:** 34 min
- **Started:** 2026-06-15T21:48:08+08:00
- **Completed:** 2026-06-15T22:22:04+08:00
- **Tasks:** 3
- **Files modified:** 7

## Accomplishments

- Replaced cross-seed mean matched-coverage targeting with per-seed integer target counts.
- Added regression coverage for prior seed 42 and seed 44 matched-coverage failures.
- Added fixed-set construction telemetry for served, actual-offer serviceable, and candidate-serviceable intersections.
- Regenerated `matched_coverage_pilot.csv` and `fixed_accepted_set_smoke.json`.
- Closed `BUG-05-001`, `BUG-05-002`, and `BUG-05-003` in the Phase 5 blocker ledger.

## Task Commits

1. **Task 1 RED: coverage gap closure tests** - `2dc2c90` (test)
2. **Task 2 RED: candidate fallback test coverage** - `d38c6fc` (test)
3. **Tasks 1-2 GREEN: coverage diagnostic implementation** - `eb2ebfa` (fix)
4. **Task 3: rerun artifacts and reports** - `ac5d4f5` (docs)

**Plan metadata:** this summary commit.

## Files Created/Modified

- `experiments/phase05_coverage_smoke.py` - Implements per-seed target-count matched coverage and fixed-set fallback telemetry.
- `tests/test_phase05_pilot.py` - Covers prior matched-coverage failures, durable failed rows, serviceable fallback, and default seed 42 routing.
- `results/pilot/phase05/matched_coverage_pilot.csv` - Regenerated with target count fields and all capped rows passing tolerance.
- `results/pilot/phase05/fixed_accepted_set_smoke.json` - Regenerated with `common_candidate_serviceable`, 16 retained requests, and completed greedy routing.
- `.planning/phases/05-pilot-experiments/05_BUG_LEDGER.csv` - Marks all three blocker rows fixed and non-blocking for Phase 6.
- `.planning/phases/05-pilot-experiments/05_PILOT_RESULTS.md` - Adds gap-closure rerun evidence and preserves the no-formal-claims boundary.
- `.planning/STATE.md` - Removes active BUG-05-001 through BUG-05-003 blocker state.

## Decisions Made

- Used per-seed integer target counts for matched coverage so seed-specific feasibility is not hidden by a cross-seed mean.
- Preserved `tolerance=0.03` and closed matched coverage by target semantics rather than threshold relaxation.
- Added `common_candidate_serviceable` as an explicit fallback because seed 42 has empty served and actual-offer serviceable intersections.
- Kept the fixed-set fallback readiness-only; Phase 6 should revisit strict fixed accepted-set construction before formal evidence.

## Deviations from Plan

### Auto-fixed Issues

**1. [Rule 1 - Bug] Actual-offer serviceable intersection remained empty for seed 42**
- **Found during:** Task 2 (fixed accepted-set smoke)
- **Issue:** The planned served -> serviceable fallback still produced an empty set for seed 42 because `SingleSidedDropoff` had no served or choice-rejected offer rows.
- **Fix:** Added a third, explicit `common_candidate_serviceable` fallback based on utility rows with candidate service geometry (`detailed_reason != no_candidate_mp`).
- **Files modified:** `experiments/phase05_coverage_smoke.py`, `tests/test_phase05_pilot.py`, `05_PILOT_RESULTS.md`
- **Verification:** `fixed_accepted_set_smoke.json` records 16 retained requests and `routing_status == completed`.
- **Committed in:** `eb2ebfa` and `ac5d4f5`

---

**Total deviations:** 1 auto-fixed (1 bug).
**Impact on plan:** The fallback is explicitly labeled and confined to pilot readiness. It closes the Phase 5 blocker without converting the diagnostic into formal Phase 6 evidence.

## Issues Encountered

- Existing repository state was already dirty with unrelated deletions, generated bytecode changes, and new files. Commits were scoped only to Phase 5 gap-closure files.

## User Setup Required

None - no external service configuration required.

## Verification

- `$env:PYTHONPATH='src'; pytest tests/test_phase05_pilot.py -q` - PASSED (`15 passed`)
- `$env:PYTHONPATH='src'; python -m experiments.phase05_coverage_smoke` - PASSED
- `$env:PYTHONPATH='src'; pytest tests/test_phase05_pilot.py tests/test_runner.py tests/test_metrics.py tests/test_variants.py -q` - PASSED (`92 passed`)
- Matched coverage capped rows for seeds 42, 43, and 44 all have `abs_gap <= tolerance` with `tolerance == 0.03`.
- Fixed accepted-set smoke has `retained_request_count == 16`, `status == passed`, and `routing_status == completed`.
- Ledger unresolved blocker check returned `unresolved blockers: 0`.

## Self-Check: PASSED

- [x] All tasks executed
- [x] Each task committed or documented in task commit history
- [x] SUMMARY.md created in plan directory
- [x] Acceptance criteria verified
- [x] No unresolved `blocks_phase6=true` ledger rows remain

## Next Phase Readiness

Phase 6 can be planned after phase-level verification reruns. The main caution is that seed 42's fixed-set smoke closes a pilot blocker through `common_candidate_serviceable`; formal Phase 6 design should decide whether to keep, replace, or predeclare that fallback before using fixed accepted-set evidence in claims.

---
*Phase: 05-pilot-experiments*
*Completed: 2026-06-15*
