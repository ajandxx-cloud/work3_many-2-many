---
phase: 15-code-reproducibility-robustness
review_fix_iteration: 1
source_review: 15-REVIEW.md
fixed: 2026-04-13T00:00:00Z
findings_addressed:
  warnings: 2
  info: 0
  skipped: 2
status: clean
---

# Phase 15: Code Review Fix Report

**Source:** 15-REVIEW.md (0 critical, 2 warnings, 2 info)
**Iteration:** 1 of 3 (--auto)
**Status:** Both warnings resolved; info items deferred

## Fixes Applied

### WR-01 — Fixed
**File:** `experiments/variants.py:256`
Changed `stacklevel=2` → `stacklevel=3` in the `warnings.warn` call inside
`_build_records`. The call chain is `user code → run() → _build_records() → warn()`,
so stacklevel=3 correctly attributes the warning to the user's `variant.run(scenario)`
call site rather than the internal `run()` frame.

### WR-02 — Fixed
**File:** `experiments/endogenous_matched_coverage.py:146-148`
Added guard before the `len(fm)` and `len(dtdc)` divisions in `main()`:
```python
if not fm or not dtdc:
    print("WARNING: no rows found for one or both variants; skipping summary.")
    return
```
Prevents `ZeroDivisionError` if rows are unexpectedly empty after variant filtering.

## Info Items (Deferred)

### IN-01 — Deferred
`SingleSidedPickup._solve` still uses bare `extend` without dedup. Pre-existing
inconsistency; `SingleSidedPickup` is not a primary comparison variant and the
dedup risk is theoretical. Deferred to future cleanup.

### IN-02 — Deferred
SHA-256 4-byte truncation is correct and sufficient for current scales.
Future-proofing note only; no action needed.

## Verification

- `grep "stacklevel" experiments/variants.py` → `stacklevel=3` at line 256 ✓
- `grep "not fm or not dtdc" experiments/endogenous_matched_coverage.py` → match at line 146 ✓

_Fixed: 2026-04-13_
_Fixer: Kiro (gsd-code-fixer)_
_Iteration: 1_
