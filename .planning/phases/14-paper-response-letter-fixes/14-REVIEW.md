---
phase: 14-paper-response-letter-fixes
reviewed: 2026-04-13T00:00:00Z
depth: standard
files_reviewed: 4
files_reviewed_list:
  - paper/sections/policy.tex
  - paper/response_to_reviewers.tex
  - paper/sections/experiments.tex
  - paper/sections/model.tex
findings:
  critical: 0
  warning: 4
  info: 3
  total: 7
status: issues_found
---

# Phase 14: Code Review Report

**Reviewed:** 2026-04-13
**Depth:** standard
**Files Reviewed:** 4
**Status:** issues_found

## Summary

Four files were reviewed after targeted substitutions in phase 14. The Gini
correction (0.1216), the FIX-02 primary/footnote restructuring, the metric
correction (15.1/21.3 vkm/trip), and the cross-reference update
(`subsec:vot-mapping` → `sec:policy`) are all present and syntactically
correct. No stale occurrences of the old Gini value (0.122) or old raw counts
(3022/4268) were found.

Four warnings were identified: a stale coverage target in the footnote
(23.5% vs. the corrected 22.8%), a numerical inconsistency between the
weight-sensitivity table (vkm/trip in the 2000s range) and the main results
table (vkm/trip ~15–21), a mismatch between the FIX-02 narrative and the
matched-coverage table's DoorToDoor served share (23.0% vs. 22.8%), and a
cross-reference label in `policy.tex` that still points to the old subsection
label. Three info items cover minor consistency and clarity issues.

---

## Warnings

### WR-01: Stale 23.5% coverage target in experiments.tex footnote

**File:** `paper/sections/experiments.tex:152`
**Issue:** The footnote describing the post-hoc lower bound still reads
"randomly rejecting DoorToDoor passengers to match the **23.5%** target."
FIX-02 updated the primary cap target to **22.8%** throughout, but this
footnote was not updated. The 23.5% figure is now inconsistent with the
22.8% value stated in the FIX-02 narrative (response_to_reviewers.tex:159)
and in the endogenous cap paragraph (experiments.tex:134).

**Fix:**
```latex
% line 152 — change 23.5 to 22.8
(randomly rejecting DoorToDoor passengers to match the 22.8\% target)
```

---

### WR-02: vkm/trip scale mismatch in weight-sensitivity table

**File:** `paper/sections/experiments.tex:362–364`
**Issue:** Table `tab:weight-sensitivity` reports vkm/trip values in the
thousands (e.g., FullModel `2155 ± 378`, DoorToDoor `3107 ± 128`). The main
results table (`tab:main-results`, line 79–84) reports vkm/trip for the same
200-request, 15-vehicle scenario as 15.1 (FullModel) and 21.3 (DoorToDoor).
The weight-sensitivity values are roughly 140× larger, which is inconsistent
with the corrected denominator (accepted trip count = n × α̂). Either the
weight-sensitivity table uses the old dimensionally incorrect denominator
(vkm / acceptance rate), or the values are from a different scale scenario
that is not disclosed. This is a numerical consistency bug that undermines
the robustness claim.

**Fix:** Recompute weight-sensitivity vkm/trip using the same denominator as
the main results (accepted trip count). Expected corrected values should be
in the 10–25 range, consistent with Table 1. If the weight-sensitivity
experiment used a different n, state it explicitly in the table caption.

---

### WR-03: Matched-coverage table DoorToDoor share is 23.0%, not 22.8%

**File:** `paper/sections/experiments.tex:167`
**Issue:** Table `tab:matched-coverage` shows DoorToDoor (capped) served
share as **23.0%**, while the endogenous cap is described as targeting
FullModel's mean of **22.8%** (line 134 and response_to_reviewers.tex:159).
A 0.2 pp overshoot is plausible due to discrete request counts, but the
discrepancy is unexplained. The FIX-02 narrative in the response letter
states "equal coverage" without acknowledging the 0.2 pp gap, which a
reviewer may flag.

**Fix:** Add a parenthetical in the table caption or the paragraph explaining
the small overshoot:
```latex
% After "At equal coverage (Table~\ref{tab:matched-coverage}),"
% add: "(DoorToDoor\,(capped) achieves 23.0\%, a 0.2\,pp overshoot
% due to discrete request granularity)"
```
Alternatively, adjust the cap to achieve exactly 22.8% if the simulation
allows finer control.

---

### WR-04: policy.tex cross-reference still uses old subsection label

**File:** `paper/sections/policy.tex:46`
**Issue:** The generalizability caveat paragraph in R1 references
`\ref{subsec:vot-mapping}` (line 46: `Section~\ref{subsec:vot-mapping}`).
The phase notes state the cross-reference was updated from
`subsec:vot-mapping` → `sec:policy`, but the label `\subsec:vot-mapping`
still exists in policy.tex at line 199 (`\label{subsec:vot-mapping}`), and
the reference on line 46 points to it. The model.tex footnote (line 300)
correctly uses `Section~\ref{sec:policy}`. The inconsistency is that
policy.tex line 46 references the subsection label within the same file,
which is a self-reference that will resolve but may not be the intended
target. If the intent was to point readers to the VOT table (which is in
`sec:policy`), the reference is redundant (already in the same section).
If the intent was to point to model.tex's footnote cross-reference, the
label is correct. Clarify intent.

**Fix:** If the reference on line 46 is meant to direct readers to the VOT
mapping subsection within policy.tex, it is a valid self-reference and can
be left as-is. If it was meant to be removed (since the reader is already
in Section 7), delete the parenthetical:
```latex
% Remove or clarify:
% (see Table~\ref{tab:passenger-types} and Section~\ref{subsec:vot-mapping})
% If keeping, confirm \label{subsec:vot-mapping} is the intended anchor.
```

---

## Info

### IN-01: FIX-02 response letter does not acknowledge the 23.0% vs 22.8% discrepancy

**File:** `paper/response_to_reviewers.tex:159`
**Issue:** The FIX-02 section states the cap targets "FullModel's mean served
share of ≈22.8%" and presents the result as "at equal coverage." The
experiments table shows DoorToDoor (capped) at 23.0%. A careful reviewer
will notice this. The response letter should either acknowledge the small
overshoot or use the same ≈ qualifier consistently.

**Fix:** Change "At equal coverage:" to "At approximately equal coverage
(22.8\% vs.\ 23.0\%):" in the response letter, or add a sentence noting
the discrete granularity.

---

### IN-02: Worked utility example in model.tex uses non-zero outside option

**File:** `paper/sections/model.tex:319`
**Issue:** The worked example (line 319) computes acceptance probability
using `e^{-5.0}` as the outside option denominator, implying
U_0 = -5.0. However, Section 4.2 (line 220) normalizes the outside option
to U_0 = 0. The example is internally inconsistent with the model's own
normalization convention. This was pre-existing but is worth flagging as it
could confuse readers.

**Fix:**
```latex
% Replace the worked example acceptance probability with:
P_{\text{accept}} = \frac{e^{-7.0}}{1 + e^{-7.0}} \approx 0.00091
```
Or, if the intent is to show a non-zero outside option, explicitly state
that $\mu_0 = 5.0$ is a scenario-specific outside option utility (not the
normalized zero), and reconcile with Equation~\ref{eq:utility-outside}.

---

### IN-03: experiments.tex MNL parameter block uses different beta notation than model.tex

**File:** `paper/sections/experiments.tex:29–31`
**Issue:** The experimental setup paragraph (lines 29–31) describes MNL
parameters as `β_price = -0.012`, `β_time = -0.008`, `β_walk = -0.015`,
using a single-subscript notation that does not match the four-coefficient
vector notation `(β_1^k, β_2^k, β_3^k, β_4^k)` defined in model.tex
(lines 270–276). The experiments section appears to use a different
parameterization or a simplified summary. This inconsistency may confuse
readers trying to reproduce the results.

**Fix:** Either align the experiments.tex notation with model.tex (citing
the specific β values from Equations \ref{eq:beta-price}–\ref{eq:beta-walk}),
or add a sentence clarifying that the single-subscript values are the
dominant sensitivity coefficients used for the scenario sweep, distinct from
the full four-coefficient vectors.

---

_Reviewed: 2026-04-13_
_Reviewer: Kiro (gsd-code-reviewer)_
_Depth: standard_
