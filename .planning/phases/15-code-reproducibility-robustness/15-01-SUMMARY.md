---
phase: 15-code-reproducibility-robustness
plan: 01
status: complete
completed: 2026-04-13T00:00:00Z
files_modified:
  - experiments/variants.py
  - experiments/endogenous_matched_coverage.py
requirements_satisfied:
  - CODE-01
  - ROB-01
  - ROB-02
  - ROB-03
  - ROB-04
---

# Phase 15 Plan 01 Summary

## Changes Applied

### CODE-01 — SHA-256 seed (experiments/variants.py:149)
Replaced `random.Random(hash(request.id) & 0xFFFFFFFF)` with
`random.Random(int.from_bytes(hashlib.sha256(request.id.encode()).digest()[:4], "big"))`.
`hash()` is non-deterministic across Python processes (PYTHONHASHSEED); SHA-256 is
platform-independent and produces bit-identical seeds in every process.

### ROB-01 — Stop ordering warning (experiments/variants.py:251-258)
Added `warnings.warn(RuntimeWarning)` when `pickup_time >= dropoff_time` in
`_build_records`. Previously the code silently fell back to Euclidean IVT; now
the anomaly is surfaced immediately.

### ROB-04 — Unassigned deduplication (experiments/variants.py:395-399, 477-481)
Both `DoorToDoor._solve` and `DoorToDoorCapped._solve` now deduplicate
`state.unassigned` by request ID when merging `result_state.unassigned`.
Prevents duplicate request IDs from accumulating across insertion iterations.

### ROB-03 — Empty seeds guard (experiments/endogenous_matched_coverage.py:98-101)
Added `if not seeds: raise ValueError(...)` before the FullModel baseline loop.
Prevents a silent `ZeroDivisionError` at `sum(...) / len(fm_rows)` when called
with an empty list.

### ROB-02 — Tolerance warning (experiments/endogenous_matched_coverage.py:120-126)
Changed `print("WARNING: ...")` to `warnings.warn(..., UserWarning)` for the
±3pp tolerance check. Callers can now catch or filter this warning programmatically.

## Verification

- `grep "hash(request.id)" experiments/variants.py` → 0 matches ✓
- `grep "hashlib.sha256" experiments/variants.py` → match at line 149 ✓
- `grep "warnings.warn" experiments/variants.py` → match at line 252 ✓
- `grep "_existing_ids" experiments/variants.py` → matches at lines 395, 477 ✓
- `grep "raise ValueError" experiments/endogenous_matched_coverage.py` → match at line 98 ✓
- `grep "warnings.warn" experiments/endogenous_matched_coverage.py` → match at line 120 ✓
- `grep "print.*WARNING" experiments/endogenous_matched_coverage.py` → 0 matches ✓
