---
phase: 15-code-reproducibility-robustness
reviewed: 2026-04-13T00:00:00Z
depth: standard
files_reviewed: 2
files_reviewed_list:
  - experiments/variants.py
  - experiments/endogenous_matched_coverage.py
findings:
  critical: 0
  warning: 2
  info: 2
  total: 4
status: issues_found
---

# Phase 15: Code Review Report

**Reviewed:** 2026-04-13
**Depth:** standard
**Files Reviewed:** 2
**Status:** issues_found

## Summary

Both files are structurally sound. The five Phase 15 changes (CODE-01, ROB-01 through ROB-04) are all logically correct in their primary intent. Two warning-level issues were found: the `stacklevel` in `_build_records` points to an internal frame rather than the user's call site, and `main()` in `endogenous_matched_coverage.py` has unguarded divisions that could raise `ZeroDivisionError` if the `rows` list is unexpectedly empty after filtering. Two info-level issues cover a dedup inconsistency in `SingleSidedPickup` and a minor SHA-256 truncation note.

---

## Warnings

### WR-01: Wrong `stacklevel` in `_build_records` warning (ROB-01)

**File:** `experiments/variants.py:256`

**Issue:** `warnings.warn(..., stacklevel=2)` is called inside `_build_records`, which is itself called by `run()`. With `stacklevel=2` the warning points to `run()` (an internal method), not to the user's `variant.run(scenario)` call site. The user sees a warning attributed to an internal frame they cannot act on.

The call chain is:
```
user code                  ← stacklevel=3 would point here
  BaseVariant.run()        ← stacklevel=2 currently points here
    _build_records()       ← stacklevel=1 (warn() call site)
      warnings.warn()
```

**Fix:**
```python
warnings.warn(
    f"Request {request.id}: pickup_time ({pickup_time:.1f}) >= "
    f"dropoff_time ({dropoff_time:.1f}); using Euclidean fallback for IVT.",
    RuntimeWarning,
    stacklevel=3,   # was 2; points to variant.run() caller
)
```

---

### WR-02: Unguarded division in `main()` after row filtering

**File:** `experiments/endogenous_matched_coverage.py:146-147`

**Issue:** `main()` filters `rows` into `fm` and `dtdc` lists at lines 144-145, then immediately divides by `len(fm)` and `len(dtdc)` at lines 146-147 without checking that either list is non-empty. If `endogenous_matched_coverage_experiment()` returns rows but none match `"FullModel"` or `"DoorToDoorCapped"` (e.g., due to a future variant rename), both divisions raise `ZeroDivisionError` with no diagnostic message.

The `ValueError` guard added at lines 97-100 protects the experiment function itself but does not cover this downstream filtering in `main()`.

```python
# current — unguarded
fm_mean_vkm = sum(r["vkm_per_trip"] for r in fm) / len(fm)      # line 146
dtdc_mean_vkm = sum(r["vkm_per_trip"] for r in dtdc) / len(dtdc) # line 147
```

**Fix:**
```python
if not fm or not dtdc:
    print("WARNING: no rows found for one or both variants; skipping summary.")
    return
fm_mean_vkm = sum(r["vkm_per_trip"] for r in fm) / len(fm)
dtdc_mean_vkm = sum(r["vkm_per_trip"] for r in dtdc) / len(dtdc)
```

---

## Info

### IN-01: Dedup inconsistency — `SingleSidedPickup` not updated (ROB-04 partial)

**File:** `experiments/variants.py:534`

**Issue:** ROB-04 added dedup logic to `DoorToDoor._solve` (lines 395-399) and `DoorToDoorCapped._solve` (lines 477-481), but `SingleSidedPickup._solve` still uses a bare `extend` without dedup:

```python
if result_state.unassigned:
    state.unassigned.extend(result_state.unassigned)   # line 534 — no dedup
```

If `greedy_insertion` ever returns a request that was already in `state.unassigned` (e.g., due to a retry or state copy), `SingleSidedPickup` will accumulate duplicates while the other two variants will not. The inconsistency is a latent correctness risk and makes the dedup fix incomplete.

**Fix:** Apply the same pattern used in `DoorToDoor`:
```python
if result_state.unassigned:
    _existing_ids = {r.id for r in state.unassigned}
    for _req in result_state.unassigned:
        if _req.id not in _existing_ids:
            state.unassigned.append(_req)
            _existing_ids.add(_req.id)
```

---

### IN-02: SHA-256 seed uses only 32 bits — note on collision probability (CODE-01)

**File:** `experiments/variants.py:149`

**Issue:** The seed derivation truncates SHA-256 to 4 bytes (32 bits):
```python
rng = random.Random(int.from_bytes(hashlib.sha256(request.id.encode()).digest()[:4], "big"))
```

`random.Random` internally uses a Mersenne Twister with a 19937-bit state. Seeding it with a 32-bit integer means only 2³² (~4 billion) distinct RNG streams are possible. For typical experiment scales (tens to hundreds of requests) this is more than sufficient and collision probability is negligible. However, if request IDs are sequential integers (e.g., `"0"`, `"1"`, ...), the SHA-256 prefix distribution is uniform and there is no practical concern.

This is not a bug — the fix is correct and deterministic. The note is informational: if future work scales to millions of requests, consider using more bytes (e.g., 8 bytes / 64 bits) to reduce the theoretical collision floor.

**Fix (optional, future-proofing only):**
```python
rng = random.Random(int.from_bytes(hashlib.sha256(request.id.encode()).digest()[:8], "big"))
```

---

_Reviewed: 2026-04-13_
_Reviewer: Kiro (gsd-code-reviewer)_
_Depth: standard_
