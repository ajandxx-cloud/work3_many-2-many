---
phase: 04-baseline-and-algorithm-implementation-check
plan: 04-02
subsystem: experiments
tags: [runner, metrics, schema, timeout]
requires:
  - phase: 04-01
    provides: method metadata and behavioral variant mapping
provides:
  - expanded raw runner result schema
  - durable failure and timeout rows
  - formal vehicle-km denominator metrics
  - baseline validation report
affects: [phase-05-pilot-runs, phase-06-formal-experiments]
tech-stack:
  added: []
  patterns: [schema_fields helper, durable error row construction]
key-files:
  created:
    - .planning/phases/04-baseline-and-algorithm-implementation-check/04_BASELINE_VALIDATION.md
  modified:
    - experiments/runner.py
    - experiments/metrics.py
    - tests/test_runner.py
    - tests/test_metrics.py
    - .planning/phases/04-baseline-and-algorithm-implementation-check/04_IMPLEMENTATION_AUDIT.md
key-decisions:
  - "Preserved legacy vkm_per_trip helper for older diagnostics but kept new runner outputs on explicit denominator fields."
  - "Fixed timeout behavior by avoiding ThreadPoolExecutor context-manager shutdown on timeout."
patterns-established:
  - "Raw result rows carry method, provenance, status, count, and schema version fields."
  - "Failure and timeout rows use the same schema as completed rows."
requirements-completed: [ALG-01, ALG-02]
duration: 45 min
completed: 2026-06-15
---

# Phase 04 Plan 02: Unified Runner Schema, Failure Rows, and Baseline Validation Summary

**Runner outputs now carry Phase 04 provenance, method decomposition, durable status rows, and explicit vehicle-km denominator metrics**

## Performance

- **Duration:** 45 min
- **Started:** 2026-06-15T10:15:00Z
- **Completed:** 2026-06-15T11:00:00Z
- **Tasks:** 4
- **Files modified:** 6

## Accomplishments

- Expanded raw runner rows with run, method, provenance, status, schema, and count fields.
- Added `vkm_per_served_trip` and `vkm_per_original_request` to metric outputs and metrics tables.
- Replaced the blocking timeout pattern with a bounded failure row path.
- Added tests for expanded schemas, denominator formulas, timeout rows, and failed-row CSV durability.
- Created `04_BASELINE_VALIDATION.md` and updated the implementation audit.

## Task Commits

1. **Tasks 1-4: runner schema and failure rows** - `0333c34` (feat)

## Files Created/Modified

- `experiments/runner.py` - Adds schema helpers, metadata enrichment, bounded timeout rows, and durable failure rows.
- `experiments/metrics.py` - Adds explicit served-trip and original-request vehicle-km metrics.
- `tests/test_runner.py` - Validates schema fields, timeout behavior, failure-row CSV persistence, and metrics table fields.
- `tests/test_metrics.py` - Validates denominator formulas and zero-denominator behavior.
- `.planning/phases/04-baseline-and-algorithm-implementation-check/04_BASELINE_VALIDATION.md` - Documents D-22 through D-27 validation.
- `.planning/phases/04-baseline-and-algorithm-implementation-check/04_IMPLEMENTATION_AUDIT.md` - Links schema/failure-row validation status.

## Decisions Made

- Kept old diagnostic scripts untouched even though they still use legacy `vkm_per_trip` naming; the new Phase 04 formal runner outputs use explicit denominator fields.
- Used thread-pool `shutdown(wait=False, cancel_futures=True)` on timeout to avoid waiting for the sleeping worker path that previously defeated the timeout.

## Deviations from Plan

None - plan executed exactly as written.

## Issues Encountered

- Broad `rg vkm_per_trip` still finds pre-existing legacy diagnostic scripts and planning text. No new runner CSV field named `vkm_per_trip` was added.

## Verification

```bash
PYTHONPATH=src pytest tests/test_runner.py tests/test_metrics.py -q
```

Result: 54 passed.

Smoke check:

```text
run_all_experiments(scales=[8], seeds=[42], beijing=False)
```

Result: 8 rows, no missing Phase 04 schema fields, statuses `completed`.

## User Setup Required

None - no external service configuration required.

## Next Phase Readiness

Wave 1 is complete. Algorithm diagnostics in `04-03` can consume explicit method metadata and schema-consistent runner outputs.

---
*Phase: 04-baseline-and-algorithm-implementation-check*
*Completed: 2026-06-15*

