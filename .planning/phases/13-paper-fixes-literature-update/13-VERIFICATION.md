---
phase: 13-paper-fixes-literature-update
verified: 2026-04-13T12:00:00Z
status: passed
score: 10/10 must-haves verified
overrides_applied: 0
re_verification:
  previous_status: gaps_found
  previous_score: 9/10
  gaps_closed:
    - "Section 5.1 of experiments.tex contains a 3-seed justification sentence citing Wu et al. (2025) as precedent"
  gaps_remaining: []
  regressions: []
---

# Phase 13: Paper Fixes & Literature Update Verification Report

**Phase Goal:** All old numbers are corrected throughout the paper, behavioral consistency materials are added, the missing reference is integrated, and Table 1 has confidence intervals
**Verified:** 2026-04-13T12:00:00Z
**Status:** passed
**Re-verification:** Yes — after gap closure (ROB-02 citation fix)

## Goal Achievement

### Observable Truths

| # | Truth | Status | Evidence |
|---|-------|--------|----------|
| 1 | "2383.85", "3662.33", "-34.9%" do not appear in rendered paper content | ✓ VERIFIED | grep finds only a `%` comment at experiments.tex:5 (not rendered LaTeX) |
| 2 | intro.tex contribution item 3 cites 35.0% endogenous and 29.2% unconstrained with correct vkm/trip values | ✓ VERIFIED | intro.tex:83-86 — "35.0% vehicle efficiency gain... FullModel 11.1 vs. DoorToDoor(capped) 17.1 vkm/trip... 29.2% gain (15.1 vs. 21.3 vkm/trip)" |
| 3 | conclusion.tex paragraph 1 and contribution item 3 use v3.0 numbers (11.1 vs 17.1, 35.0%; 15.1 vs 21.3, 29.2%) | ✓ VERIFIED | conclusion.tex:13-17 (opening paragraph) and :30-31 (contribution item 3) both contain 35.0% and 29.2% |
| 4 | abstract.tex leads with endogenous 35.0% as primary claim; post-hoc 74.3% is parenthetical | ✓ VERIFIED | abstract.tex:15-23 — 35.0% is the bolded primary claim; 74.3% appears as "For reference... providing a conservative lower bound" |
| 5 | A notation/units table (tab:notation) exists in the paper appendix listing all symbols with units | ✓ VERIFIED | main.tex:46-88 — appendix section with \label{tab:notation}, 26 symbols, units in seconds/minutes/meters/CNY/utils |
| 6 | A worked utility example with explicit numbers appears in model.tex | ✓ VERIFIED | model.tex:304-328 — walk-sensitive passenger, d_walk=300m, t_wait=5min, t_ivt=20min, p=8CNY, U=-7.0, P_accept≈0.119 |
| 7 | A commitment assumption paragraph appears in algorithm.tex after the committed-nodes sentence | ✓ VERIFIED | algorithm.tex:177-188 — paragraph defines delta_commit=5min, explains locking of accepted bundles |
| 8 | Fielbaum et al. (2021) is cited in Section 2.2 of literature.tex with a positioning sentence | ✓ VERIFIED | literature.tex:20-29 — paragraph with \citet{fielbaum2021} twice, "bidirectional walking flexibility", "online re-optimisation" |
| 9 | Table 1 (tab:main-results) in experiments.tex has ± notation on acceptance rate, vkm, and vkm/trip columns | ✓ VERIFIED | experiments.tex:93-98 — all 6 data rows have $X \pm Y$ on Accept., vkm, and vkm/trip columns |
| 10 | Section 5.1 of experiments.tex contains a 3-seed justification sentence citing Wu et al. (2025) as precedent | ✓ VERIFIED | experiments.tex:32 — "consistent with standard practice in DRT simulation \citep{wu2025}; standard deviations are reported in Table~\ref{tab:main-results}." |

**Score:** 10/10 truths verified

### Required Artifacts

| Artifact | Expected | Status | Details |
|----------|----------|--------|---------|
| `paper/sections/intro.tex` | Corrected contribution item 3 with v3.0 numbers | ✓ VERIFIED | Contains "35.0%" at line 83 |
| `paper/sections/conclusion.tex` | Corrected efficiency numbers throughout | ✓ VERIFIED | Contains "35.0%" at lines 13 and 30 |
| `paper/sections/abstract.tex` | Abstract leading with endogenous 35.0% as primary claim | ✓ VERIFIED | Contains "35.0%" at line 17 as primary bolded claim |
| `paper/main.tex` | Appendix section with notation table | ✓ VERIFIED | tab:notation label at line 54; appendix at lines 46-88 |
| `paper/sections/model.tex` | Worked utility example with beta values | ✓ VERIFIED | "Worked utility example" paragraph at line 304; beta_1 at line 306 |
| `paper/sections/algorithm.tex` | Commitment assumption paragraph | ✓ VERIFIED | Paragraph at line 177; "commitment horizon" at line 186 |
| `paper/sections/literature.tex` | Fielbaum 2021 citation in Section 2.2 | ✓ VERIFIED | fielbaum2021 at lines 20 and 26 |
| `paper/sections/experiments.tex` | Table 1 with ± notation; 3-seed note with wu2025 citation | ✓ VERIFIED | ± notation on all 6 rows; \citep{wu2025} at line 32 |
| `paper/response_to_reviewers.tex` | Note about Fielbaum addition | ✓ VERIFIED | "Fielbaum" and "fielbaum2021" at lines 215-223 |

### Key Link Verification

| From | To | Via | Status | Details |
|------|----|-----|--------|---------|
| paper/sections/intro.tex | contribution item 3 | \item Empirical demonstration | ✓ WIRED | "35.0" found at line 83 |
| paper/sections/conclusion.tex | opening paragraph | "demonstrated that" | ✓ WIRED | "35.0" found at lines 13 and 30 |
| paper/main.tex | appendix notation table | tab:notation | ✓ WIRED | label defined at line 54; referenced in model.tex |
| paper/sections/algorithm.tex | committed nodes sentence | commitment | ✓ WIRED | paragraph at line 177 follows committed-nodes sentence at line 174 |
| paper/sections/literature.tex | Section 2.2 after Cortenbach discussion | \citet{fielbaum2021} | ✓ WIRED | paragraph at lines 20-29 follows Cortenbach paragraph |
| paper/sections/experiments.tex | Table 1 acceptance rate column | \pm | ✓ WIRED | ± present in all 6 data rows |
| paper/sections/experiments.tex | 3-seed note | \citep{wu2025} | ✓ WIRED | Citation present at line 32 |

### Data-Flow Trace (Level 4)

Not applicable — this phase modifies LaTeX source files (static text), not components rendering dynamic data.

### Behavioral Spot-Checks

Step 7b: SKIPPED — no runnable entry points for LaTeX source verification. All checks are grep-based.

### Requirements Coverage

| Requirement | Source Plan | Description | Status | Evidence |
|-------------|------------|-------------|--------|----------|
| TEXT-01 | 13-01 | Replace old numbers in intro.tex | ✓ SATISFIED | intro.tex:83 contains "35.0%"; "2383", "3662", "34.9" absent |
| TEXT-02 | 13-01 | Replace old numbers in conclusion.tex | ✓ SATISFIED | conclusion.tex:13,30 contain "35.0%"; old numbers absent |
| TEXT-03 | 13-01 | No other occurrences of old numbers in paper | ✓ SATISFIED | grep -rn "2383\|3662\|34\.9" paper/ returns only a % comment |
| BEHAV-01 | 13-02 | Units/variables reference table | ✓ SATISFIED | tab:notation in main.tex appendix with time/walk/fare units |
| BEHAV-02 | 13-02 | Worked numerical utility example | ✓ SATISFIED | model.tex:304-328 with explicit beta values and P_accept=0.119 |
| BEHAV-03 | 13-02 | Commitment assumption paragraph | ✓ SATISFIED | algorithm.tex:177-188 with delta_commit=5min definition |
| LIT-01 | 13-03 | Add Fielbaum et al. (2021) to references.bib | ✓ SATISFIED | references.bib:309 contains @article{fielbaum2021,...} |
| LIT-02 | 13-03 | Cite Fielbaum in Section 2.2 with positioning | ✓ SATISFIED | literature.tex:20-29 — positioning paragraph present |
| ROB-01 | 13-03 | Table 1 mean ± std notation | ✓ SATISFIED | experiments.tex:93-98 — all rows have ± on accept/vkm/vkm-trip |
| ROB-02 | 13-03 | 3-seed note in Section 5.1 citing Wu et al. (2025) | ✓ SATISFIED | experiments.tex:32 — \citep{wu2025} present in 3-seed sentence |

### Anti-Patterns Found

| File | Line | Pattern | Severity | Impact |
|------|------|---------|----------|--------|
| paper/sections/experiments.tex | 5 | `% - Abstract 2383.85 vs 3662.33` | ℹ️ Info | Comment only; not rendered. Historical note, no impact on paper output. |

### Human Verification Required

None — all checks are programmatically verifiable via grep on LaTeX source.

### Gaps Summary

No gaps. The single gap from the initial verification (ROB-02: missing `\citep{wu2025}` in the 3-seed sentence) has been closed. experiments.tex line 32 now reads "consistent with standard practice in DRT simulation \citep{wu2025}; standard deviations are reported in Table~\ref{tab:main-results}." All 10/10 must-haves are verified and all 10 requirements (BEHAV-01 through ROB-02) are satisfied.

---

_Verified: 2026-04-13T12:00:00Z_
_Verifier: Claude (gsd-verifier)_
