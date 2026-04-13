---
phase: 14-paper-response-letter-fixes
review_fix_iteration: 1
source_review: 14-REVIEW.md
fixed: 2026-04-13T00:00:00Z
findings_addressed:
  warnings: 3
  info: 1
  skipped: 1
status: clean
---

# Phase 14: Code Review Fix Report

**Source:** 14-REVIEW.md (4 warnings, 3 info)
**Iteration:** 1 of 3 (--auto)
**Status:** All warnings resolved; no re-review needed

## Fixes Applied

### WR-01 — Fixed
**File:** `paper/sections/experiments.tex:152`
Changed `23.5\% target` → `22.8\% target` in the post-hoc footnote.
Now consistent with the endogenous cap target throughout the paper.

### WR-02 — Fixed
**File:** `paper/sections/experiments.tex:362–364`
Recomputed weight-sensitivity table values using correct denominator
(`vkm / (n × accept_rate)`, n=200). Old values (~2000–3000) were
`vkm / accept_rate`; corrected values are in the 10–15 range:

| Config | FullModel vkm/trip | DoorToDoor vkm/trip | Reduction |
|---|---|---|---|
| Efficiency-focused | $10.8 \pm 1.9$ | $15.5 \pm 0.6$ | 30.8% |
| Equity-focused | $10.7 \pm 2.6$ | $15.5 \pm 0.8$ | 31.4% |
| Balanced | $10.6 \pm 2.1$ | $15.2 \pm 0.8$ | 30.5% |

Reduction percentages were already correct (n cancels in ratio).

### WR-03 — Fixed
**File:** `paper/sections/experiments.tex:159–162` (table caption)
Added parenthetical explaining the 0.2pp overshoot:
> "DoorToDoor (capped) achieves 23.0%, a 0.2 pp overshoot due to discrete request granularity."

**File:** `paper/response_to_reviewers.tex:159`
Changed "At equal coverage:" → "At approximately equal coverage (FullModel 22.8%, DoorToDoor (capped) 23.0%; the 0.2 pp overshoot is due to discrete request granularity):"

### WR-04 — Skipped (no fix needed)
**File:** `paper/sections/policy.tex:46`
The `\ref{subsec:vot-mapping}` on line 46 is a valid self-reference within
policy.tex (the label exists at line 199). The reference correctly directs
readers to the VOT mapping subsection within the same section. No change needed.

## Info Items

### IN-01 — Fixed (via WR-03 fix to response letter)
Response letter FIX-02 now acknowledges the 22.8% vs 23.0% discrepancy.

### IN-02 — Deferred
`model.tex:319` worked example uses non-zero outside option. Pre-existing
inconsistency; not introduced in Phase 14. Deferred to future cleanup.

### IN-03 — Deferred
`experiments.tex:29–31` MNL notation mismatch with model.tex. Pre-existing;
not introduced in Phase 14. Deferred to future cleanup.

## Verification

- `grep "23\.5" paper/sections/experiments.tex` → 0 matches ✓
- `grep "2155\|3107\|2135\|3093\|2121\|3040" paper/sections/experiments.tex` → 0 matches ✓
- `grep "10\.8.*1\.9" paper/sections/experiments.tex` → match at line 362 ✓
- `grep "approximately equal" paper/sections/experiments.tex` → match at line 160 ✓
- `grep "approximately equal" paper/response_to_reviewers.tex` → match at line 159 ✓

_Fixed: 2026-04-13_
_Fixer: Kiro (gsd-code-fixer)_
_Iteration: 1_
