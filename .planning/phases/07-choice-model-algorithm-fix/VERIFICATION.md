---
phase: 07-choice-model-algorithm-fix
verified: 2026-04-12T00:00:00Z
status: passed
score: 4/4
overrides_applied: 0
re_verification: false
---

# Phase 7: Choice Model & Algorithm Fix — Verification Report

**Phase Goal:** The paper and code consistently implement binary logit single-offer acceptance, eliminating the behavioral inconsistency flagged as CRITICAL by the reviewer.
**Verified:** 2026-04-12
**Status:** PASSED
**Re-verification:** No — initial verification

---

## Goal Achievement

### Observable Truths

| # | Truth | Status | Evidence |
|---|-------|--------|----------|
| 1 | `choice.py` exposes `accept_probability(bundle, request, ptype, current_time)` returning a scalar in (0,1) | VERIFIED | `def accept_probability` at line 67 of `src/drt/choice.py`; formula `exp_bundle / (exp_outside + exp_bundle)` matches spec exactly |
| 2 | The multi-bundle `choice_probability` function is removed or replaced | VERIFIED | No occurrence of `choice_probability` anywhere in `src/drt/` — zero grep hits |
| 3 | `model.tex` Section 4.2 defines binary logit single-offer acceptance with formula `P_accept(b*) = exp(U_b*) / (exp(U_0) + exp(U_b*))` | VERIFIED | Subsection at line 211: "Single-Offer Mechanism and Binary Logit Acceptance"; `eq:binary-logit` label at line 225 with correct formula |
| 4 | `algorithm.tex` Algorithm 1 pseudocode contains an explicit binary logit acceptance step | VERIFIED | Line 152: `p_{acc} <- exp(U_{rb*}^{k_r}) / (1 + exp(U_{rb*}^{k_r}))` with comment "Binary logit acceptance (Eq. ref{eq:binary-logit})" |

**Score:** 4/4 truths verified

---

## Required Artifacts

| Artifact | Expected | Status | Details |
|----------|----------|--------|---------|
| `src/drt/choice.py` | Binary logit acceptance probability function | VERIFIED | 99 lines; `accept_probability` defined at line 67; `mnl_utility` helper at line 26; no stubs, no TODOs |
| `paper/sections/model.tex` | Section 4.2 with binary logit formulation | VERIFIED | `P_{\text{accept}}` present; `eq:binary-logit` label defined; "Single-Offer Mechanism" subsection present |
| `paper/sections/algorithm.tex` | Algorithm 1 pseudocode with binary logit step | VERIFIED | Complete `\begin{algorithm}...\end{algorithm}` block; no PLACEHOLDER; binary logit step at line 152 |

---

## Key Link Verification

| From | To | Via | Status | Details |
|------|----|-----|--------|---------|
| `src/drt/choice.py` | public API callers | `accept_probability` exported from `src/drt/__init__.py` | WIRED | `__init__.py` re-exports `accept_probability`; listed in `__all__`; docstring example shows `from drt import Request, accept_probability` |
| `model.tex eq:binary-logit` | `algorithm.tex` Algorithm 1 | `\ref{eq:binary-logit}` cross-reference | WIRED | Two references in `algorithm.tex`: line 85 (prose) and line 153 (pseudocode comment) both point to `eq:binary-logit` |
| `model.tex eq:binary-logit` | Section 5 Layer 2 paragraph | `\ref{eq:binary-logit}` in Layer 2 prose | WIRED | `model.tex` line 335: "accepts with probability $P_{\text{accept}}(b^*)$ (Equation~\ref{eq:binary-logit})" |

---

## Stale Reference Audit

| Check | Expected | Result |
|-------|----------|--------|
| `eq:choice-prob` anywhere in `paper/sections/` | Zero occurrences | CLEAN — 0 matches |
| `eq:outside-prob` anywhere in `paper/sections/` | Zero occurrences | CLEAN — 0 matches |
| `eq:acceptance-prob` anywhere in `paper/sections/` | Zero occurrences | CLEAN — 0 matches |
| Multi-bundle sum `sum_{b'...mathcal{B}_r}` in `model.tex` | Zero occurrences | CLEAN — 0 matches |
| `PLACEHOLDER` in `algorithm.tex` | Zero occurrences | CLEAN — 0 matches |

All stale multi-bundle MNL references have been fully removed.

---

## Requirements Coverage

| Requirement | Source Plan | Description | Status | Evidence |
|-------------|------------|-------------|--------|----------|
| REV-01 | 07-01 | Binary logit `P_accept(b*) = exp(U_b*) / (exp(U_0) + exp(U_b*))` replacing multi-bundle MNL in code | SATISFIED | `choice.py` line 98: `return exp_bundle / (exp_outside + exp_bundle)` with `exp_outside = 1.0` (U_0 = 0) |
| REV-02 | 07-01 | `choice.py` updated — `accept_probability(bundle, request, ptype, t)` exists; old `choice_probability()` removed | SATISFIED | `accept_probability` at line 67; zero occurrences of `choice_probability` in entire `src/drt/` tree |
| REV-03 | 07-02 | `model.tex` Section 4.2 updated — binary logit formulation with single-offer mechanism definition | SATISFIED | Subsection renamed at line 211; `eq:binary-logit` defined at line 225; outside option explained at lines 213–221 |
| REV-04 | 07-02 | `algorithm.tex` Algorithm 1 pseudocode shows binary logit acceptance step explicitly | SATISFIED | Lines 152–155: compute `p_acc`, sample `z_r ~ Bernoulli(p_acc)`, with equation cross-reference |

---

## Commit Verification

| Commit | Description | Exists |
|--------|-------------|--------|
| `4b43d75` | feat(07-01): replace `choice_probability` with binary logit `accept_probability` | VERIFIED |
| `25db4d5` | feat(07-02): rewrite `model.tex` Section 4.2 — binary logit single-offer acceptance | VERIFIED |
| `18c4253` | feat(07-02): fill in `algorithm.tex` Algorithm 1 pseudocode with binary logit step | VERIFIED |

---

## Anti-Patterns Found

None. No TODOs, FIXMEs, placeholders, or hollow implementations detected in any modified file.

---

## Behavioral Spot-Checks

Step 7b: Not applicable — this phase modifies a Python module and LaTeX source files. The Python module (`choice.py`) has no runnable entry point; it is a library. No server or CLI to invoke without test harness. Spot-checks skipped with reason: library-only artifacts.

---

## Human Verification Required

None. All requirements are verifiable through static code and document inspection.

---

## Gaps Summary

No gaps. All four requirements (REV-01 through REV-04) are fully satisfied:

- The binary logit formula is implemented correctly in `choice.py` with the correct signature and math.
- The old multi-bundle `choice_probability` is completely absent.
- `model.tex` Section 4.2 has been renamed and rewritten with the single-offer mechanism narrative and the `eq:binary-logit` equation.
- `algorithm.tex` Algorithm 1 is a complete pseudocode block (no placeholder) with an explicit binary logit acceptance step referencing `eq:binary-logit`.
- All cross-references in the paper point to `eq:binary-logit`; no stale references to removed equations remain.

The behavioral inconsistency flagged by the reviewer is eliminated. Code and paper are now consistent.

---

_Verified: 2026-04-12_
_Verifier: Claude (gsd-verifier)_
