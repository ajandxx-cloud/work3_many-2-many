---
phase: 13-paper-fixes-literature-update
reviewed: 2026-04-13T00:00:00Z
depth: standard
files_reviewed: 9
files_reviewed_list:
  - paper/main.tex
  - paper/response_to_reviewers.tex
  - paper/sections/abstract.tex
  - paper/sections/algorithm.tex
  - paper/sections/conclusion.tex
  - paper/sections/experiments.tex
  - paper/sections/intro.tex
  - paper/sections/literature.tex
  - paper/sections/model.tex
findings:
  critical: 0
  warning: 4
  info: 5
  total: 9
status: issues_found
---

# Phase 13: Code Review Report

**Reviewed:** 2026-04-13
**Depth:** standard
**Files Reviewed:** 9
**Status:** issues_found

## Summary

All nine LaTeX source files were reviewed for numerical consistency, citation correctness, LaTeX syntax, and internal coherence. The v3.0 key numbers (35.0%, 29.2%, 11.1 vs 17.1 vkm/trip, 15.1 vs 21.3 vkm/trip) are consistently propagated across abstract, intro, experiments, and conclusion. The `fielbaum2021` and `wu2025` citation keys resolve correctly in `references.bib`. No stale numbers (2383.85, 3662.33, 34.9%) were found in any reviewed file.

Four warnings were found: a numerical inconsistency in the Gini coefficient between `experiments.tex` and `policy.tex`, a stale matched-coverage claim in `response_to_reviewers.tex` that contradicts the current primary result in the manuscript, a weight-sensitivity table that reports raw vkm totals rather than vkm/trip, and a cross-reference to a subsection label that does not exist. Five info items cover minor style and consistency issues.

---

## Warnings

### WR-01: Gini coefficient inconsistency between experiments and policy sections

**File:** `paper/sections/experiments.tex:276` and `paper/sections/policy.tex:112`
**Issue:** `experiments.tex` line 276 reports the Gini coefficient as **0.1216**, while `policy.tex` line 112 reports it as **0.122**. These are the same quantity (Gini of per-type acceptance rates) and must match. The abstract (line 24) uses 0.1216, so `policy.tex` is the outlier.
**Fix:** Change `policy.tex` line 112 from `\textbf{0.122}` to `\textbf{0.1216}` to match the value in `experiments.tex` and `abstract.tex`.

---

### WR-02: Stale matched-coverage claim in response_to_reviewers.tex (FIX-02 section)

**File:** `paper/response_to_reviewers.tex:158-165`
**Issue:** The FIX-02 subsection states "This is now the primary efficiency claim in Section~5.2 and the abstract" for the post-hoc matched-coverage result (10.9 vs 42.3 vkm/trip, 74.3%). However, the current manuscript (`experiments.tex` lines 154-169 and `abstract.tex` lines 15-23) makes the **endogenous** matched-coverage result (11.1 vs 17.1, 35.0%) the primary claim, and demotes the post-hoc figure to a footnote. The response-to-reviewers document therefore misrepresents the current state of the manuscript, which could confuse editors or reviewers comparing the two documents.
**Fix:** Update the FIX-02 paragraph in `response_to_reviewers.tex` to reflect that the endogenous re-routing result (11.1 vs 17.1, 35.0%) is the primary claim, and the post-hoc figure (10.9 vs 42.3, 74.3%) is retained as a footnote lower bound. The matched-coverage target should also be corrected from "23.5%" (line 159) to "22.8%" (the value used in `experiments.tex` line 148 and `abstract.tex` line 15).

---

### WR-03: Weight-sensitivity table reports raw vkm totals, not vkm/trip

**File:** `paper/sections/experiments.tex:376-379`
**Issue:** Table `tab:weight-sensitivity` (lines 376-379) reports values such as `$2155 \pm 378$` and `$3107 \pm 128$` under the column header "FullModel vkm/trip" and "DoorToDoor vkm/trip". These numbers are in the thousands, inconsistent with the vkm/trip values reported elsewhere (11.1, 15.1, 17.1, 21.3 — all single-digit or low double-digit). The column header says "vkm/trip" but the magnitude suggests these are raw vkm totals (comparable to the 628.5 and 2603.7 total vkm in Table 1). The stated reductions (30.5%–31.4%) are arithmetically consistent with the raw vkm values, not with per-trip values. This is either a mislabelled column or the wrong denominator was applied.
**Fix:** Verify the denominator used for this table. If these are raw vkm totals, rename the column headers to "FullModel vkm" and "DoorToDoor vkm". If they are intended to be vkm/trip, divide by the accepted trip count ($n \cdot \hat{\alpha}$) and update the numbers. The caption and surrounding text (lines 383-387) should be updated to match.

---

### WR-04: Cross-reference to non-existent label `\ref{subsec:vot-mapping}`

**File:** `paper/sections/model.tex:301`
**Issue:** The footnote at line 301 contains `Table~\ref{tab:vot-mapping} (Section~\ref{subsec:vot-mapping})`. The label `\subsec:vot-mapping` is defined in `policy.tex` as `\subsection{...}\label{subsec:vot-mapping}` (line 199 of `policy.tex`). However, `model.tex` is compiled before `policy.tex` in `main.tex` (line 37 vs line 40), so the forward reference is valid in principle — but the label name used in the `\ref` call must exactly match the `\label` declaration. Checking `policy.tex` line 199: the label is `\label{subsec:vot-mapping}`, which matches. This is not a broken reference per se, but the `\ref` will produce a section number pointing to a policy subsection from within the model section footnote, which may confuse readers. More critically, if `policy.tex` is ever restructured, this cross-reference will silently break.
**Fix:** This is low-risk but worth noting. Consider replacing `Section~\ref{subsec:vot-mapping}` with `Section~\ref{sec:policy}` for robustness, or add a comment near the `\label{subsec:vot-mapping}` in `policy.tex` noting that `model.tex` depends on it.

---

## Info

### IN-01: `response_to_reviewers.tex` references stale vkm-per-rate numbers in R1 response body

**File:** `paper/response_to_reviewers.tex:63`
**Issue:** The R1 response body (line 63) still contains the old per-rate figures: "FullModel achieves 3{,}022\,vkm per unit acceptance rate, compared to 4{,}268 for DoorToDoor --- a \textbf{29.2\% improvement}". These 3022 and 4268 values are the pre-FIX-01 numbers (vkm divided by acceptance rate fraction, not by trip count). FIX-01 (lines 141-151) correctly documents the correction, but the R1 response body was not updated to use the corrected 15.1 and 21.3 figures. The 29.2% improvement figure is correct, but the raw numbers are stale.
**Fix:** Update line 63 to read: "FullModel achieves 15.1\,vkm/trip compared to 21.3\,vkm/trip for DoorToDoor --- a \textbf{29.2\% improvement}".

### IN-02: `model.tex` beta parameters marked "provisional" — should be confirmed or caveat removed

**File:** `paper/sections/model.tex:268-269`
**Issue:** Lines 268-269 contain the comment "(provisional --- to be confirmed against Work~1/2 calibration before Phase~3)". This is a development note that should not appear in a submission-ready manuscript. The parameters are used in all experiments, so they are effectively confirmed.
**Fix:** Remove the parenthetical "(provisional --- to be confirmed against Work~1/2 calibration before Phase~3)" from the text.

### IN-03: `experiments.tex` comment block at top contains internal audit notes

**File:** `paper/sections/experiments.tex:1-13`
**Issue:** Lines 1-13 contain a multi-line LaTeX comment block labelled "METRIC AUDIT (Phase 10, 2026-04-13)" with internal development notes. While LaTeX comments do not appear in the compiled PDF, they are visible in the source file submitted to the journal and may appear unprofessional.
**Fix:** Remove or condense the audit comment block before final submission.

### IN-04: `literature.tex` cites `\citet{benakiva1985}` with a likely typo in the key

**File:** `paper/sections/literature.tex:33`
**Issue:** The citation key used is `benakiva1985` (line 33). The `references.bib` entry (line 67) uses the key `benakiva1985` — this matches, so it will compile. However, the standard spelling of the author's name is "Ben-Akiva", and the key `benakiva1985` omits the hyphen. This is not a compilation error but is inconsistent with the author's name as spelled in the bib entry (`Ben-Akiva`). If any other file in the project uses `ben-akiva1985` or `benakiva1985` with a different capitalisation, it will silently fail to resolve.
**Fix:** No immediate action required — the key resolves correctly. For consistency, consider standardising to `benakiva1985` throughout (already the case here).

### IN-05: `main.tex` appendix table uses `\textbf` in header row without `booktabs` column separator

**File:** `paper/main.tex:55-57`
**Issue:** The appendix notation table (lines 55-57) uses `\textbf{Symbol}`, `\textbf{Description}`, `\textbf{Unit}` in the header row. The other tables in the paper (e.g., `tab:constraints` in `model.tex`) use plain text headers with `\toprule`/`\midrule`/`\bottomrule` from `booktabs`. The inconsistency is minor but visible in the compiled output.
**Fix:** Either remove `\textbf` from the appendix table header to match the style of other tables, or add `\textbf` to the headers of all other tables for consistency.

---

_Reviewed: 2026-04-13_
_Reviewer: Claude (gsd-code-reviewer)_
_Depth: standard_
