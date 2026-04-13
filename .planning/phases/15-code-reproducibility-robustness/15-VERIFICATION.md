---
phase: 15-code-reproducibility-robustness
verified: 2026-04-13T00:00:00Z
status: passed
score: 5/5 must-haves verified
overrides_applied: 0
---

# Phase 15: Code Reproducibility and Robustness Verification Report

**Phase Goal:** The experiment codebase produces bit-identical results across processes and platforms, and all silent failure modes are replaced with explicit warnings or errors.
**Verified:** 2026-04-13
**Status:** passed
**Re-verification:** No — initial verification

## Goal Achievement

### Observable Truths

| # | Truth | Status | Evidence |
|---|-------|--------|----------|
| 1 | CODE-01: `hash(request.id)` gone; SHA-256 seed used | VERIFIED | `experiments/variants.py` line 149: `hashlib.sha256(request.id.encode()).digest()[:4]` — no `hash()` call anywhere in file |
| 2 | ROB-01: `pickup_time >= dropoff_time` triggers `warnings.warn` in `_build_records` | VERIFIED | `variants.py` lines 251-257: `warnings.warn(f"Request {request.id}: pickup_time ... >= dropoff_time ...", RuntimeWarning, stacklevel=3)` |
| 3 | ROB-02: tolerance failure uses `warnings.warn` not `print("WARNING...")` | VERIFIED | `endogenous_matched_coverage.py` lines 120-126: `warnings.warn(f"DoorToDoorCapped mean served_share=...", UserWarning, stacklevel=2)` |
| 4 | ROB-03: empty seeds raises `ValueError` before any `ZeroDivisionError` | VERIFIED | `endogenous_matched_coverage.py` lines 97-100: `if not seeds: raise ValueError("...seeds list must not be empty")` — precedes `len(fm_rows)` division at line 105 |
| 5 | ROB-04: `_existing_ids` dedup logic present in both `DoorToDoor._solve` and `DoorToDoorCapped._solve` | VERIFIED | `variants.py` lines 395-399 (`DoorToDoor`) and lines 477-481 (`DoorToDoorCapped`): identical `_existing_ids = {r.id for r in state.unassigned}` guard pattern |

**Score:** 5/5 truths verified

### Required Artifacts

| Artifact | Expected | Status | Details |
|----------|----------|--------|---------|
| `experiments/variants.py` | SHA-256 seeding, ROB-01 warn, ROB-04 dedup | VERIFIED | All three criteria confirmed at lines 149, 251-257, 395-399, 477-481 |
| `experiments/endogenous_matched_coverage.py` | ROB-02 warn, ROB-03 ValueError | VERIFIED | Both criteria confirmed at lines 97-100, 120-126 |

### Anti-Patterns Found

None. No `hash(request.id)` calls, no `print("WARNING...")` for tolerance failure, no silent ZeroDivisionError path.

### Human Verification Required

None. All five criteria are mechanically verifiable via static code inspection.

### Gaps Summary

No gaps. All five success criteria are satisfied in the current codebase.

---

_Verified: 2026-04-13_
_Verifier: Kiro (gsd-verifier)_
