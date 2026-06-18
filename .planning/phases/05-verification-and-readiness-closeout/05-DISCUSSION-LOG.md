# Phase 5: Verification and Readiness Closeout - Discussion Log

> **Audit trail only.** Do not use as input to planning, research, or execution agents.
> Decisions are captured in CONTEXT.md - this log preserves the alternatives considered.

**Date:** 2026-06-18T19:37:52.5465811+08:00
**Phase:** 5-Verification and Readiness Closeout
**Areas discussed:** Hard readiness gates, Targeted test scope, LaTeX compilation failure handling, Submission package consistency

---

## Hard Readiness Gates

| Option | Description | Selected |
|--------|-------------|----------|
| Strict hard gates | `TR-E submission-ready` is allowed only when all readiness gates pass. | Yes |
| Allow non-impacting failures | Documented exceptions could still permit ready status. | |
| Layered classification | Use fixed readiness classes and impact explanations. | |

**User's choice:** Strict hard gates.
**Notes:** The user selected the strictest posture for the final readiness label.

| Option | Description | Selected |
|--------|-------------|----------|
| Near-ready only for external/tooling blockers | External environment failures may be near-ready; claim or evidence failures are not ready. | Yes |
| Any failure = not ready | Every failed gate, regardless of cause, blocks near-ready status. | |
| Impact-based classification | Classify by whether a failure affects manuscript claims or provenance. | |

**User's choice:** Near-ready only for external/tooling blockers.
**Notes:** Claim, evidence, ledger, prohibited wording, or manuscript content failures cannot be softened into near-ready.

| Option | Description | Selected |
|--------|-------------|----------|
| Only core submission package | Core manuscript/evidence package is hard-gated; README/CLAUDE do not block unless submitted. | Yes |
| Whole repository consistency | All package-facing and historical files must be clean. | |
| Layered requirements | Core package hard-gated; other files tracked as cleanup. | |

**User's choice:** Only core submission package.
**Notes:** Non-submission package-facing files do not block readiness unless they enter the submission package.

---

## Targeted Test Scope

| Option | Description | Selected |
|--------|-------------|----------|
| Active suite full | Run `$env:PYTHONPATH='src'; pytest tests/ analysis/test_sensitivity.py`. | Yes |
| Manuscript-critical subset | Run only metrics, runner, variants, Phase 6, and sensitivity tests. | |
| Two-layer record | Hard-gate a subset and record the active suite as advisory. | |

**User's choice:** Active suite full.
**Notes:** The active maintained suite is the pytest readiness gate.

| Option | Description | Selected |
|--------|-------------|----------|
| Not a hard gate | Bare `pytest` archive collection is a known future hardening issue. | Yes |
| Hard gate | Repository-root `pytest` must pass before ready. | |
| Record but do not block | Run or collect bare pytest and report the issue without blocking. | |

**User's choice:** Not a hard gate.
**Notes:** The archived ad hoc collection issue remains outside the Phase 5 hard gate.

| Option | Description | Selected |
|--------|-------------|----------|
| Skip acceptable but recorded | Gurobi/license skips are acceptable when recorded and aligned with diagnostic MILP scope. | Yes |
| Must run | Gurobi/MILP tests must execute and pass. | |
| Do not run MILP/Gurobi tests | Exclude those tests and document diagnostic limits. | |

**User's choice:** Skip acceptable but recorded.
**Notes:** Skip status must be explicit in the final report.

---

## LaTeX Compilation Failure Handling

| Option | Description | Selected |
|--------|-------------|----------|
| Complete Elsevier sequence | Run `pdflatex main`, `bibtex main`, `pdflatex main`, `pdflatex main` from `manuscript/`. | Yes |
| Two pdflatex passes only | Faster PDF check without full bibliography/reference assurance. | |
| latexmk if available, fallback otherwise | Use latexmk when present and document fallback path. | |

**User's choice:** Complete Elsevier sequence.
**Notes:** Full compile sequence is the hard gate.

| Option | Description | Selected |
|--------|-------------|----------|
| Near-ready external blocker | Missing TeX/BibTeX/class packages can only produce near-ready, not submission-ready. | Yes |
| Not ready | Any local compile failure makes the package not ready. | |
| Manual PDF accepted | Existing PDF can substitute for a failed compile. | |

**User's choice:** Near-ready external blocker.
**Notes:** Exact missing package/tool, failed command, and manuscript impact must be recorded.

| Option | Description | Selected |
|--------|-------------|----------|
| References/citations hard gate, layout warnings recorded | Undefined references/citations block; overfull/underfull boxes are recorded unless readability is affected. | Yes |
| Any warning blocks | Every warning blocks readiness. | |
| Only PDF generation matters | Warnings do not matter if a PDF is produced. | |

**User's choice:** References/citations hard gate, layout warnings recorded.
**Notes:** Reference integrity is a hard readiness requirement.

---

## Submission Package Consistency

| Option | Description | Selected |
|--------|-------------|----------|
| Core submission package scan | Scan manuscript sources, main table/figure notes, claim ledger, and final report. | Yes |
| Extended submission-material scan | Include cover letter and response template. | |
| Whole-repository scan | Include README, CLAUDE, figure scripts, and archive. | |

**User's choice:** Core submission package scan.
**Notes:** The scan does not pull non-submission files into the hard gate.

| Option | Description | Selected |
|--------|-------------|----------|
| Not a Phase 5 readiness hard gate | Cover letter and response template are optional unless explicitly submitted. | Yes |
| Extended scan but non-blocking | Scan and record cleanup items without blocking. | |
| Submission-package hard gate | Must be clean before ready. | |

**User's choice:** Not a Phase 5 readiness hard gate.
**Notes:** These files can be handled later if they become active submission materials.

| Option | Description | Selected |
|--------|-------------|----------|
| Write core checklist | Include manuscript source, PDF, formal evidence provenance, claim ledger, and command results. | Yes |
| Only command results | Keep final verification report shorter. | |
| Full repository checklist | Inventory the entire repository. | |

**User's choice:** Write core checklist.
**Notes:** The checklist should support handoff without widening the submission scope.

## Agent Discretion

- Exact final verification report wording and layout.
- Exact prohibited-wording scan commands and log excerpt format.
- Whether a failed gate triggers a narrow fix or a documented blocker, within the strict readiness rules.

## Deferred Ideas

None.
