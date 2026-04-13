---
phase: 12-endogenous-matched-coverage-experiment
reviewed: 2026-04-13T00:00:00Z
depth: standard
files_reviewed: 3
files_reviewed_list:
  - experiments/variants.py
  - experiments/endogenous_matched_coverage.py
  - paper/sections/experiments.tex
findings:
  critical: 0
  warning: 6
  info: 5
  total: 11
status: issues_found
---

# Phase 12: Code Review Report

**Reviewed:** 2026-04-13
**Depth:** standard
**Files Reviewed:** 3
**Status:** issues_found

## Summary

Three files were reviewed: `experiments/variants.py` (seven variant classes totalling ~729 lines), `experiments/endogenous_matched_coverage.py` (the new endogenous comparison experiment, ~159 lines), and `paper/sections/experiments.tex` (the experiments section LaTeX, ~397 lines).

The code is generally well-structured and purposefully commented. No critical security vulnerabilities or data-loss bugs were found. However, six warnings and five info items require attention before results can be considered fully reproducible and correctly interpreted. The most consequential issues are: a logical gap in `_find_stop_info` that silently drops passengers who appear in only one of pickup or dropoff stops; a `hash()` call used as a deterministic RNG seed that is not reproducible across Python processes or platforms; and a numeric inconsistency between the paper text and the table in `experiments.tex` (22.8% vs 23.5%).

---

## Warnings

### WR-01: `_find_stop_info` resets state per route, can fail to return a complete pair

**File:** `experiments/variants.py:294-308`

**Issue:** The method scans routes with `pickup_mp` and `dropoff_mp` initialised to `None` *inside* the outer `for route` loop. If a request's pickup stop is in one route and its dropoff stop is in a different route (which should be impossible by design, but is not enforced), the method silently returns `(None, None, 0.0, 0.0)`. More importantly, if both stops exist in the same route but the dropoff appears before the pickup in the stop list (an illegal schedule, but one that could arise from a buggy `greedy_insertion` call), the method returns a pair with `pickup_time > dropoff_time`. The caller at line 249 clamps this with `max(0.0, dropoff_time - pickup_time)`, effectively masking the ordering error. The real stop-order violation never surfaces as an error.

**Fix:** Add an assertion after recovering the pair, or at minimum add a log warning when `pickup_time >= dropoff_time` for a completed trip:

```python
if pickup_mp is not None and dropoff_mp is not None:
    if pickup_time >= dropoff_time:
        import warnings
        warnings.warn(
            f"Request {request_id}: pickup_time ({pickup_time}) >= "
            f"dropoff_time ({dropoff_time}); stop ordering may be corrupt."
        )
    return pickup_mp, dropoff_mp, pickup_time, dropoff_time
```

---

### WR-02: `hash(request.id)` is not a reproducible RNG seed across Python processes

**File:** `experiments/variants.py:147`

**Issue:** `random.Random(hash(request.id) & 0xFFFFFFFF)` is used as a deterministic seed for Bernoulli acceptance. Python's built-in `hash()` for strings is randomised by default via `PYTHONHASHSEED` (set randomly at interpreter start since Python 3.3). This means that two runs of the same experiment with the same `request.id` values will produce **different** acceptance outcomes, breaking reproducibility. The `& 0xFFFFFFFF` mask does not help — the underlying hash value still changes between processes.

**Fix:** Replace `hash(request.id)` with a deterministic digest such as CRC32 or a truncated SHA-256, which is stable across processes:

```python
import hashlib

def _stable_seed(request_id: str) -> int:
    """Return a stable 32-bit seed from the request ID string."""
    digest = hashlib.sha256(request_id.encode()).digest()
    return int.from_bytes(digest[:4], "little")

# In _mnl_filter_requests, line 147:
rng = random.Random(_stable_seed(request.id))
```

Alternatively, set `PYTHONHASHSEED=0` in the experiment runner, but that is a global environment change — a local fix is safer.

---

### WR-03: `DoorToDoorCapped` cap check fires at strictly equal share, may under-serve by one request

**File:** `experiments/variants.py:435`

**Issue:** The cap check is `accepted_count / total_requests >= self._cap_share`. This fires *before* attempting the insertion for the request that would exactly reach the target. For a target of 0.235 with 200 requests (target = 47 trips), once `accepted_count` reaches 47, the inequality is `47/200 = 0.235 >= 0.235 = True`, so the 48th candidate is rejected. This is the intended behaviour per the docstring ("Threat T-12-01 mitigation: cap check uses >= (not >) to prevent off-by-one"). However, the docstring says "prevents off-by-one", but it actually guarantees the served count *never exceeds* the cap, meaning the achieved share will often be slightly *below* the target (e.g., 47/200 = 23.5% exactly). This is consistent with the paper's reported DoorToDoorCapped share of 23.0% vs target of 22.8%. The behaviour is correct, but the docstring is misleading: it prevents over-serving, not an off-by-one in the usual sense.

More substantively, when `target_share` is computed from FullModel's mean and then passed to DoorToDoorCapped, the cap is applied uniformly across all seeds. If seed-to-seed variation in FullModel's acceptance is large, the per-seed DoorToDoorCapped share can deviate substantially from the per-seed FullModel share — only the *mean* is controlled. The tolerance check at line 113 correctly catches this case, but silently continues writing the CSV rather than raising. In a paper context, a silent tolerance failure can produce an invalid table without any failed assertion.

**Fix:** Make the tolerance failure non-silent for the experiment script (not just a print warning):

```python
if not tolerance_ok:
    import warnings
    warnings.warn(
        f"DoorToDoorCapped mean served_share={mean_dtdc_share:.4f} "
        f"is outside ±3pp of target={target_share:.4f}. "
        f"Results may not support the matched-coverage claim.",
        stacklevel=2,
    )
```

Consider also raising `RuntimeError` in non-interactive contexts where the result would be written to a CSV that feeds the paper directly.

---

### WR-04: `endogenous_matched_coverage_experiment` divides by `len(fm_rows)` without empty-list guard

**File:** `experiments/endogenous_matched_coverage.py:100`

**Issue:** `target_share = sum(r["served_share"] for r in fm_rows) / len(fm_rows)`. If `_run_fullmodel_baseline` returns an empty list (e.g., because `seeds` is an empty list passed by a caller), this raises `ZeroDivisionError`. The same pattern recurs at lines 112, 140, and 141 (`len(dtdc_rows)`). The `main()` function only calls `endogenous_matched_coverage_experiment()` with the default `seeds=SEEDS`, which is non-empty, but the function accepts arbitrary `seeds` from callers.

**Fix:** Add a guard at the top of the function body:

```python
if not seeds:
    raise ValueError("seeds list must be non-empty")
```

---

### WR-05: `_build_records` uses `(request.id not in unassigned_ids)` but `unassigned_ids` may contain duplicates

**File:** `experiments/variants.py:214,219`

**Issue:** `unassigned_ids = {r.id for r in state.unassigned}` correctly builds a set of unique IDs. However, `state.unassigned` is populated by appending to lists across multiple result merges (e.g., in `DoorToDoor._solve`, line 386: `state.unassigned.extend(result_state.unassigned)`). If `greedy_insertion` returns the same request in `unassigned` for two consecutive calls (which could happen if a request is processed twice due to a state copy error), the same `request_id` could be added to `state.unassigned` twice. The set comprehension on line 214 deduplicates, so the membership test on line 219 is correct — but the duplicates in `state.unassigned` mean `len(state.unassigned)` overstates the number of rejected requests. This does not affect `_build_records` (which uses the set), but would affect any code that counts `len(state.unassigned)` directly.

**Fix:** Where `unassigned` lists are accumulated (in `DoorToDoor._solve` and `DoorToDoorCapped._solve`), deduplicate before returning:

```python
# At the end of _solve, before returning state:
seen = set()
deduped = []
for r in state.unassigned:
    if r.id not in seen:
        seen.add(r.id)
        deduped.append(r)
state.unassigned = deduped
```

---

### WR-06: LaTeX text reports 22.8% cap target but code default and footnote say 23.5%

**File:** `paper/sections/experiments.tex:147,165,173,180`

**Issue:** There are two conflicting coverage targets in the paper:

- Line 147: "once the served share reaches FullModel's mean of **22.8%**" (paragraph text)
- Line 173/179: Table caption reads "equal served share ($\approx$**22.8%**)" and table row shows FullModel at "22.8%"
- Line 165 (footnote): "randomly rejecting DoorToDoor passengers to match the **23.5%** target"

The code default in `variants.py` at line 414 is `cap_share: float = 0.235` (23.5%), and the experiment docstring at line 6 of `endogenous_matched_coverage.py` says "~23.5%". The paper text and table use 22.8%, while the code default and the post-hoc footnote reference 23.5%. This is a numeric inconsistency between the implemented experiment and the reported result.

If the actual FullModel mean served share from the three-seed run is 22.8%, the code default (23.5%) should be updated to match. If the seeds produce 23.5%, the paper table must be corrected. Either way, the two values must be reconciled before submission.

**Fix:** After running the endogenous experiment, verify whether the actual FullModel mean is 22.8% or 23.5%, then ensure:
1. The code default `cap_share=0.235` in `DoorToDoorCapped.__init__` matches the observed mean.
2. The paragraph text, table caption, table row, and footnote in `experiments.tex` all cite the same figure.

---

## Info

### IN-01: `rho_p=None` default should be `rho_p: float | None = None` (type annotation gap)

**File:** `experiments/variants.py:343,415,572`

**Issue:** Several `__init__` signatures use `rho_p: float = None` and `rho_d: float = None`. These are inconsistent type annotations: the declared type is `float` but the default is `None`. Python does not enforce type annotations at runtime, but static type checkers (mypy, pyright) will flag these as errors. The correct annotation is `float | None = None` (or `Optional[float] = None`).

**Fix:**
```python
def __init__(
    self,
    rho_p: float | None = None,
    rho_d: float | None = None,
    ...
```

---

### IN-02: `sys.path.insert` in experiment script is brittle

**File:** `experiments/endogenous_matched_coverage.py:28`

**Issue:** `sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))` works when the script is run directly but is fragile. If the package is installed or run via `python -m experiments.endogenous_matched_coverage`, `__file__` may resolve unexpectedly. Other experiment scripts likely have the same pattern; a `pyproject.toml` or `setup.py` with an editable install (`pip install -e .`) would eliminate the need for all these `sys.path` hacks.

**Fix:** Add a `pyproject.toml` with the `experiments` package listed as a source, or at minimum document the required invocation method in a project README.

---

### IN-03: Magic number `0.235` appears in two separate places without a shared constant

**File:** `experiments/variants.py:414`, `experiments/endogenous_matched_coverage.py` (implicitly, via `cap_share` default)

**Issue:** The default cap share of 23.5% is hardcoded in `DoorToDoorCapped.__init__` (line 414). If the FullModel mean served share changes when scenarios are updated, this default must be manually updated. There is no shared constant in `experiments/config.py` that captures the "expected FullModel mean served share".

**Fix:** Add to `experiments/config.py`:
```python
# Endogenous matched-coverage cap (= FullModel mean served share at scale 200, seeds 42-44)
DTDC_CAP_SHARE = 0.235
```
And reference it from `DoorToDoorCapped.__init__` and `endogenous_matched_coverage.py`.

---

### IN-04: Commented-out metric audit block at top of experiments.tex should be removed before submission

**File:** `paper/sections/experiments.tex:4-14`

**Issue:** Lines 4-14 contain a multi-line audit comment documenting historical metric errors and corrections. While useful during development, this block will appear in the compiled PDF as a comment and is not appropriate for final submission. More importantly, it references superseded values ("Abstract 2383.85 vs 3662.33", "Section 5.2 '3022 vs 4268'") that could confuse a future reader or reviewer examining the LaTeX source.

**Fix:** Remove lines 4-14 before submission, or move the audit history to a separate `CHANGELOG.md` or git commit message.

---

### IN-05: `_cost_weights = tuple(ALPHA_WEIGHTS[:4])` silently truncates if ALPHA_WEIGHTS has fewer than 4 elements

**File:** `experiments/variants.py:59`

**Issue:** `ALPHA_WEIGHTS` is defined in `config.py` as a 5-element list `[1.0, 1.0, 1.0, 1.0, 5.0]`. The slice `[:4]` is intentional (excluding the opting-out penalty). However, if `ALPHA_WEIGHTS` is ever changed to fewer than 4 elements, the slice will silently produce a shorter tuple, causing downstream failures in `greedy_insertion` (which expects a 4-element tuple). There is no assertion guarding against this.

**Fix:** Add an assertion immediately after the constant definition:
```python
assert len(ALPHA_WEIGHTS) >= 4, (
    f"ALPHA_WEIGHTS must have at least 4 elements (walk, wait, ivt, price); "
    f"got {len(ALPHA_WEIGHTS)}"
)
_COST_WEIGHTS = tuple(ALPHA_WEIGHTS[:4])
```

---

_Reviewed: 2026-04-13_
_Reviewer: Claude (gsd-code-reviewer)_
_Depth: standard_
