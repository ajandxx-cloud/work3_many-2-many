# Phase 2: TR-E Positioning Lock and Claim Ledger - Research

**Researched:** 2026-06-17
**Domain:** Academic manuscript claim provenance, TR-E positioning, formal evidence control
**Confidence:** HIGH

<user_constraints>
## User Constraints (from CONTEXT.md)

[CITED: .planning/phases/02-tr-e-positioning-lock-and-claim-ledger/02-CONTEXT.md]

### Locked Decisions
## Implementation Decisions

### Claim Ledger Granularity And Coverage
- **D-01:** `03_CLAIM_LEDGER.md` must use one row per manuscript claim occurrence. Each claim occurrence gets its own row even when multiple rows share the same underlying idea or evidence source.
- **D-02:** Ledger rows must include `claim_family_id` so related occurrences can be grouped without losing per-location traceability.
- **D-03:** The ledger must cover both current manuscript claims and planned safe replacement claims. It is not only an audit list; it is the executable handoff for Phase 3 manuscript revision and Phase 4 numerical provenance.
- **D-04:** Planned replacement claims in Phase 2 must use non-numeric safe wording. Final percentages, improvement values, confidence intervals, significance language, table numbers, and figure numbers must use Phase 4 placeholders such as `[PHASE4_VERIFIED_VALUE]` until provenance is verified.
- **D-05:** In addition to the mandatory provenance schema, ledger rows should include execution fields: `claim_id`, `claim_family_id`, `manuscript_location`, `current_sentence`, `claim_type`, `comparison`, `metric`, `reported_value`, `phase4_status`, and `action`.
- **D-06:** The mandatory provenance columns remain required for every applicable ledger row: `source_path`, `script_path`, `generation_command`, `metric_formula`, `numerator`, `denominator`, `evidence_role`, `allowed_sentence`, and `prohibited_sentence`.
- **D-07:** Recommended `action` values for the planner to consider are `retain_with_verification`, `replace_non_numeric`, `delete`, `downgrade_to_diagnostic`, `move_to_limitation`, and `phase4_verify_number`. The exact enum may be refined by the planner, but it must preserve these semantics.

### TR-E Positioning Lock Core Narrative
- **D-08:** `02_TR_E_POSITIONING_LOCK.md` should anchor the paper as operational service-design evidence for TR-E. The primary contribution is not a policy validation, a deployable decision tool, or a stronger optimization-method claim.
- **D-09:** The strongest allowed title/abstract/introduction mechanism wording is `passenger-response-aware simulation framework`.
- **D-10:** Prohibit `co-optimization of meeting points, routing, and passenger response` and similar wording that implies endogenous passenger-response-aware routing. The current mechanism is route-then-sample acceptance, not optimization over acceptance probability.
- **D-11:** Journal-fit rationale should be anchored in DRT/DARP operations, meeting-point service consolidation, dynamic routing, fleet operations, and logistics/operations management.
- **D-12:** Passenger choice should be framed as a service-design evaluation mechanism. It must not be presented as empirically calibrated behavioral validation or as a behaviorally endogenous routing-control mechanism.
- **D-13:** Policy and public-service material may appear only as bounded implications or limitations. It must not be the main journal-fit rationale.
- **D-14:** The core allowed sentence should be conservative but contribution-bearing: the study may say that passenger-response-aware bidirectional meeting-point consolidation can reduce routing intensity per served trip under tested synthetic service-design conditions, while creating measurable coverage and passenger-type trade-offs.

### Evidence Role And Blocker Classification
- **D-15:** `05_BLOCKERS_AND_SAFE_CLAIMS.md` must use four claim statuses: `safe`, `safe_with_qualifier`, `downgrade_required`, and `blocker`.
- **D-16:** Known old or risky values, including `18.3%`, `29.1%`, `35.0%`, and `0.1216`, are `blocker until Phase 4 verified`. Phase 3 may not retain them or replace them with final values.
- **D-17:** Diagnostic evidence may appear in the main text only when each relevant claim has an explicit diagnostic qualifier. Diagnostic evidence must not become the headline estimate.
- **D-18:** Matched-coverage evidence must be labeled as a diagnostic coverage-confounding control, not a primary equal-service headline claim.
- **D-19:** Fixed-accepted-set evidence must be labeled as a diagnostic decomposition over fixed accepted sets, not a full dynamic benchmark.
- **D-20:** MILP and algorithm diagnostics must be labeled as simplified ex-post diagnostics and limitations, not ALNS near-optimality proof.
- **D-21:** Gamma/Pareto material must be labeled as post-hoc welfare or sensitivity accounting, not behavioral policy control.
- **D-22:** Fine-grained passenger-burden claims involving walking, IVT, detour, fairness, type burden, or completed-trip precision should be `safe_with_qualifier` or `blocker` unless Phase 4 verifies them. Main metrics such as routing intensity, served share, and vkm per original request can be formal ledger claims with provenance and Phase 4 numerical verification.

### Prohibited Wording And Replacement Rules
- **D-23:** Policy-first framing is prohibited as the main narrative. The manuscript section currently named `Policy Implications` should be reframed in Phase 3 as managerial or operational implications.
- **D-24:** Bounded public-service or service-design implications are allowed when they are clearly limited by the evidence.
- **D-25:** Generic dominance, superiority, and broad `outperforms` wording is prohibited. Metric-specific and evidence-bounded comparisons are allowed, such as lower vkm per served trip under tested settings, while noting lower served share or other trade-offs.
- **D-26:** Behavioral Pareto and endogenous Gamma wording is prohibited. Gamma may be described only as post-hoc welfare or sensitivity accounting, not as a routing, offer-generation, acceptance, or policy-control mechanism.
- **D-27:** `Pareto frontier` should be avoided when it implies behaviorally endogenous optimization or policy control. If retained at all, it must be reframed as a post-hoc welfare or sensitivity display.
- **D-28:** Beijing wording must use a qualifier such as `Beijing-inspired synthetic grid` or `semi-realistic synthetic grid`. Real-world Beijing validation, empirical Beijing case-study, or public-data validation wording is prohibited.
- **D-29:** MILP wording must use a qualifier such as `simplified ex-post diagnostic over fixed accepted sets`. Exact dynamic benchmark, complete benchmark, and ALNS near-optimality proof wording is prohibited.

### Artifact Responsibilities
- **D-30:** `02_TR_E_POSITIONING_LOCK.md` should state allowed framing, prohibited framing, core contribution, journal-fit rationale, and safe core sentences.
- **D-31:** `03_CLAIM_LEDGER.md` should be the occurrence-level claim table with mandatory provenance fields and execution fields. It should map current claims to planned safe replacements without final numerical injection.
- **D-32:** `05_BLOCKERS_AND_SAFE_CLAIMS.md` should classify safe claims, safe-with-qualifier claims, downgrade-required claims, blockers, old numbers, prohibited wording, and diagnostic evidence boundaries.
- **D-33:** Phase 2 may scan manuscript and package-facing text to build the ledger and blocker table, but it must not edit `manuscript/`, `README.md`, `CLAUDE.md`, result files, or code.

### Layered Ledger Scope For Package-Facing Materials
- **D-34:** Phase 2 should use layered coverage. Main manuscript claims in `manuscript/main.tex` and `manuscript/sections/*.tex` enter the full `03_CLAIM_LEDGER.md`; package-facing risks in `README.md`, `CLAUDE.md`, `manuscript/cover_letter.tex`, `manuscript/response_to_reviewers.tex`, and figure-script comments enter `05_BLOCKERS_AND_SAFE_CLAIMS.md` as package-consistency or provenance-risk items unless they are submitted or reused.
- **D-35:** `manuscript/cover_letter.tex` and `manuscript/response_to_reviewers.tex` should be treated as package-consistency risks for now, not as main manuscript ledger scope. Phase 5 decides whether they are final submission-package files and therefore need cleanup or rewrite.
- **D-36:** Figure-script comments, legacy input paths, TR Part A format notes, and Pareto/Gamma naming risks should be recorded as blocker, package-consistency, or provenance-risk items. Claims that appear in figure titles, captions, labels, or manuscript references should be verified through Phase 4 provenance.
- **D-37:** A non-manuscript file should be upgraded to full claim-ledger rows only when it enters the final submission package or when its wording is reused in the manuscript, cover letter, response file, or other submitted material.

### Non-Numeric Claim Provenance
- **D-38:** Every ledger row should preserve the full mandatory schema. For non-numeric positioning, mechanism-scope, or limitation claims, `metric_formula`, `numerator`, and `denominator` should be filled with `not_applicable`, not omitted.
- **D-39:** Non-numeric claim rows should use a two-source pattern: `source_path` points to the claim occurrence, while `supporting_source_path` or notes point to the planning artifact, validation report, or evidence-role source that makes the wording safe.
- **D-40:** `script_path` and `generation_command` should distinguish source type. Manual positioning, scope, or limitation wording uses `not_applicable_manual_text`; claims supported by formal tables, figures, or reports use the actual script and command; blocker rows found by scanning record the relevant scan command.
- **D-41:** `evidence_role` should use a fixed enum, including at minimum `positioning`, `mechanism_scope`, `primary_behavioral`, `diagnostic_matched_coverage`, `diagnostic_fixed_accepted_set`, `robustness_sensitivity`, `equity_type_heterogeneity`, `algorithm_diagnostic`, `limitation`, and `package_consistency`.

### Allowed And Prohibited Sentence Precision
- **D-42:** `allowed_sentence` should be a complete safe sentence that Phase 3 can directly use or lightly polish. Phase 3 may improve academic style, but it must not change the evidence boundary encoded by Phase 2.
- **D-43:** For numerical claims that require Phase 4 provenance, `allowed_sentence` should use structured placeholders such as `[PHASE4_VERIFIED_VALUE]`, `[PHASE4_VERIFIED_CI]`, and `[PHASE4_VERIFIED_TABLE]`. The sentence may be structurally complete, but it must not lock final numbers.
- **D-44:** Unsafe claims such as co-optimization, real-world Beijing validation, policy decision-tool framing, or ALNS near-optimality should receive both a safe replacement sentence and an `action` such as `replace_non_numeric`, `downgrade_to_diagnostic`, or `delete`.
- **D-45:** `prohibited_sentence` should record either the exact current sentence when a concrete hit exists or a prohibited pattern when the risk is generic. This supports later prohibited-wording scans.

### Blocker Table Granularity And Routing
- **D-46:** `05_BLOCKERS_AND_SAFE_CLAIMS.md` should include both category-level rules and a concrete hit list. The rule layer should cover risk families such as old numbers, Part A/TR-A framing, policy-first wording, Gamma/Pareto, Beijing validation, MILP/exactness, dominance/outperform language, legacy result paths, and premature readiness wording.
- **D-47:** Each blocker hit should include `issue_id`, `location`, `matched_text_or_pattern`, `risk_family`, `status`, `evidence_role`, `owner_phase`, `required_action`, `allowed_replacement`, and `verification_check`.
- **D-48:** Blocker `status` should use `safe`, `safe_with_qualifier`, `downgrade_required`, and `blocker`. `owner_phase` should route by gate: wording issues to Phase 3, numerical provenance to Phase 4, package consistency and readiness checks to Phase 5, and out-of-scope model/evidence gaps to future/v2.
- **D-49:** Phase 2 scans should cover fixed risk families at minimum: Part A/TR-A, policy-first wording, old values, dominance/outperform language, Gamma/Pareto, Beijing validation, MILP/exact/near-optimal wording, legacy result paths, and `TR-E submission-ready` or equivalent readiness wording.

### the agent's Discretion
- No user decisions were delegated to agent discretion. Downstream agents should follow the decisions above.

### Deferred Ideas (OUT OF SCOPE)
## Deferred Ideas

None. Discussion stayed within Phase 2 scope.
</user_constraints>

<phase_requirements>
## Phase Requirements

| ID | Description | Research Support |
|----|-------------|------------------|
| PLAN-04 | Project has `05_BLOCKERS_AND_SAFE_CLAIMS.md` identifying claim-critical blockers, safe claims, downgraded claims, and prohibited wording. | Use the blocker taxonomy, risk-family scans, and owner-phase routing documented below. [CITED: .planning/REQUIREMENTS.md] |
| CLAI-01 | Project has `02_TR_E_POSITIONING_LOCK.md` stating allowed paper framing, prohibited framing, core contribution, and journal-fit rationale. | Use TR-E official scope plus Phase 2 decisions D-08 through D-14. [CITED: ScienceDirect TR-E aims and scope; CITED: .planning/phases/02-tr-e-positioning-lock-and-claim-ledger/02-CONTEXT.md] |
| CLAI-02 | Project has `03_CLAIM_LEDGER.md` with mandatory provenance columns plus location, comparison, metric, and reported-number fields. | Use the occurrence-level ledger schema and metric formula table below. [CITED: .planning/REQUIREMENTS.md; CITED: .planning/phases/02-tr-e-positioning-lock-and-claim-ledger/02-CONTEXT.md] |
| CLAI-03 | Every numerical claim in abstract, introduction, experiments, managerial/operational implications, and conclusion appears in the claim ledger. | Use `rg` scans over `manuscript/main.tex` and `manuscript/sections/*.tex`; current scans found risky numerical values across those manuscript areas. [VERIFIED: rg scan 2026-06-17] |
| CLAI-04 | Claims distinguish primary behavioral evidence, matched-coverage diagnostics, fixed-accepted-set diagnostics, robustness/sensitivity, equity/type heterogeneity, algorithm diagnostics, and limitations. | Use the canonical evidence-role map and result manifest inventory below. [CITED: .planning/milestones/tr_e_claim_ready/01_REPO_AND_EVIDENCE_AUDIT.md; VERIFIED: results/formal/phase06/phase06_result_manifest.json] |
</phase_requirements>

## Summary

Phase 2 is a documentation and claim-control phase, not a code or experiment phase. Its core deliverables are three milestone artifacts under `.planning/milestones/tr_e_claim_ready/`: `02_TR_E_POSITIONING_LOCK.md`, `03_CLAIM_LEDGER.md`, and `05_BLOCKERS_AND_SAFE_CLAIMS.md`. [CITED: .planning/ROADMAP.md; CITED: .planning/phases/02-tr-e-positioning-lock-and-claim-ledger/02-CONTEXT.md]

The safe TR-E positioning should anchor the manuscript in logistics and operations service design. ScienceDirect's current TR-E aims and scope states that TR-E is differentiated by specializing in logistics, covers logistics components, and allows analytical, simulation, empirical, experimental, case-study, AI, machine-learning, and network-analysis methods. [CITED: https://www.sciencedirect.com/journal/transportation-research-part-e-logistics-and-transportation-review/about/aims-and-scope] This supports framing the manuscript as `passenger-response-aware simulation framework` and `operational service-design evidence`, while excluding policy-first, empirical Beijing validation, endogenous Gamma, exact dynamic benchmark, or universal dominance claims. [CITED: .planning/phases/02-tr-e-positioning-lock-and-claim-ledger/02-CONTEXT.md]

The ledger should be executable for later phases: one row per claim occurrence, family IDs for repeated ideas, mandatory provenance columns, complete safe replacement sentences, and Phase 4 placeholders for unverified numerical content. Current scans show the manuscript/package contains enough risk hits to justify this rigor: old values were found 24 times; Part A/TR-A/Part A target wording 17 times; policy wording 47 times; Gamma/Pareto/welfare wording 64 times; Beijing/validation wording 20 times; MILP/exact/near-optimal/benchmark wording 57 times; and dominance/outperform/superior/improvement/gain wording 36 times. [VERIFIED: rg scan 2026-06-17]

**Primary recommendation:** Plan Phase 2 as a three-artifact control layer: lock TR-E framing first, build the occurrence-level ledger second, then write blocker/safe-claim rules and concrete hit rows that route each issue to Phase 3, Phase 4, Phase 5, or future/v2. [CITED: .planning/phases/02-tr-e-positioning-lock-and-claim-ledger/02-CONTEXT.md]

## Architectural Responsibility Map

| Capability | Primary Tier | Secondary Tier | Rationale |
|------------|-------------|----------------|-----------|
| TR-E positioning lock | Planning / Manuscript governance | Manuscript source | The lock is a planning artifact that constrains later manuscript edits; Phase 2 must not edit manuscript files. [CITED: .planning/phases/02-tr-e-positioning-lock-and-claim-ledger/02-CONTEXT.md] |
| Claim ledger | Planning / Provenance control | Formal evidence tree | The ledger maps manuscript claim occurrences to evidence paths, scripts, formulas, and safe replacement text. [CITED: .planning/REQUIREMENTS.md] |
| Blocker and safe-claims table | Planning / Risk control | Manuscript/package scans | The table classifies scan hits and claim risks, then routes them to owner phases. [CITED: .planning/phases/02-tr-e-positioning-lock-and-claim-ledger/02-CONTEXT.md] |
| Evidence role separation | Formal evidence artifacts | Planning ledger | Canonical evidence roles are defined by Phase 1 audit and formal manifests, while Phase 2 records allowed/prohibited uses. [CITED: .planning/milestones/tr_e_claim_ready/01_REPO_AND_EVIDENCE_AUDIT.md; VERIFIED: results/formal/phase06/phase06_result_manifest.json] |
| Final numerical values | Phase 4 provenance layer | Formal tables/scripts | Phase 2 must use placeholders for unverified final values; Phase 4 owns final percentages, CIs, significance language, table numbers, and figure numbers. [CITED: .planning/phases/02-tr-e-positioning-lock-and-claim-ledger/02-CONTEXT.md] |

## Project Constraints (from AGENTS.md)

| Directive | Planning Implication |
|-----------|----------------------|
| Formal claims must use `results/formal/phase06/`; smoke tests, archive outputs, root legacy CSVs, and ad hoc outputs are non-canonical by default. [CITED: AGENTS.md] | Ledger `source_path` for formal claims must point under `results/formal/phase06/`; non-canonical hits become diagnostic, package-consistency, or blocker rows. |
| Claims must be conditional, operational, and logistics-oriented; avoid universal dominance, real-world validation, or policy-overreach language. [CITED: AGENTS.md] | Positioning lock should use conditional service-design language, not policy-first or universal superiority wording. |
| Gamma is post-hoc welfare accounting unless future work implements endogenous behavior. [CITED: AGENTS.md] | Gamma/Pareto rows require `post_hoc_welfare` language and should avoid behavioral control or Pareto-frontier claims. |
| Beijing evidence is Beijing-inspired or semi-realistic synthetic grid unless real public-data ingestion exists. [CITED: AGENTS.md] | Beijing rows should prohibit empirical validation or real-world case-study wording. |
| MILP is a simplified ex-post routing diagnostic for fixed accepted sets, not a complete dynamic benchmark. [CITED: AGENTS.md] | MILP rows should be `algorithm_diagnostic` or `limitation`, not primary method validation. |
| Phase 3 may revise structure and non-numeric wording, but final concrete values must wait until Phase 4 verifies provenance. [CITED: AGENTS.md] | `allowed_sentence` for unverified numerical claims must use Phase 4 placeholders. |
| Claim ledger rows must include `source_path`, `script_path`, `generation_command`, `metric_formula`, `numerator`, `denominator`, `evidence_role`, `allowed_sentence`, and `prohibited_sentence`. [CITED: AGENTS.md] | These fields are mandatory in the ledger schema; use `not_applicable` or `not_applicable_manual_text` rather than blanks for manual/non-numeric claims. |
| Fix only manuscript-critical reproducibility issues unless a claim-critical bug is discovered. [CITED: AGENTS.md] | Phase 2 should not edit code, manuscript, README, result files, or dependencies. |
| Generated results, figures, caches, and archive artifacts must stay separate from source and planning artifacts. [CITED: AGENTS.md] | Phase 2 writes only `.planning/` milestone artifacts and its own research artifact. |

## Standard Stack

### Core

| Tool / Artifact | Version | Purpose | Why Standard |
|-----------------|---------|---------|--------------|
| Markdown milestone artifacts | not_applicable | `02_TR_E_POSITIONING_LOCK.md`, `03_CLAIM_LEDGER.md`, `05_BLOCKERS_AND_SAFE_CLAIMS.md` | Existing GSD milestone artifacts are Markdown under `.planning/milestones/tr_e_claim_ready/`. [VERIFIED: filesystem listing 2026-06-17] |
| `rg` | 15.1.0 | Fast manuscript/package scan for claim-risk families | `rg` is available locally and project workflow favors it for text search. [VERIFIED: `rg --version`; CITED: developer instructions] |
| Python standard library `csv` / `json` / `pathlib` | Python 3.12.4 runtime | Inspect CSV/JSON schemas and validate ledger headers without adding dependencies | Phase 2 does not need new packages, and Python is available locally. [VERIFIED: `python --version`] |
| Formal Phase 6 CSV/JSON artifacts | generated 2026-06-16 | Canonical evidence sources for claim provenance | Formal manifest excludes smoke evidence and lists validated packages. [VERIFIED: results/formal/phase06/phase06_result_manifest.json] |
| `experiments/formal_statistics.py` | local project script | Source of result manifest, tables, validation synthesis, and formal-statistics validation command | CLI exposes `--validate`, `--closeout`, table, plot, and results-dir options. [VERIFIED: `python -m experiments.formal_statistics --help`] |

### Supporting

| Tool / Artifact | Version | Purpose | When to Use |
|-----------------|---------|---------|-------------|
| `git` | 2.53.0.windows.1 | Confirm planning-only diff and commit research artifacts | Use after writing Phase 2 artifacts; current status was clean before research write. [VERIFIED: `git status --short`; VERIFIED: `git --version`] |
| `pytest` | 8.4.2 | Existing test framework for downstream validation | Use for Phase 5 or if Phase 2 introduces helper scripts; not required for pure Markdown artifact generation. [VERIFIED: `python -m pytest --version`] |
| `pdflatex` / `bibtex` | MiKTeX paths present | Downstream manuscript compile gate | Available locally, but Phase 2 does not compile manuscript. [VERIFIED: `Get-Command pdflatex`; VERIFIED: `Get-Command bibtex`] |

### Alternatives Considered

| Instead of | Could Use | Tradeoff |
|------------|-----------|----------|
| Markdown table ledger | CSV ledger | CSV is easier to machine-validate, but user decisions require `03_CLAIM_LEDGER.md`; Markdown keeps the artifact aligned with milestone docs. [CITED: .planning/phases/02-tr-e-positioning-lock-and-claim-ledger/02-CONTEXT.md] |
| Manual reading only | `rg` scanner passes | Manual reading is necessary for sentence-level judgment, but scanner passes are needed to prove coverage of fixed risk families. [VERIFIED: rg scan 2026-06-17] |
| Rerun formal experiments | Reuse validated Phase 6 artifacts | Reruns are out of scope unless verification fails or a claim-critical formula bug is discovered. [CITED: .planning/REQUIREMENTS.md; CITED: .planning/milestones/tr_e_claim_ready/00_MILESTONE_PLAN.md] |

**Installation:** No external packages should be installed for this phase. [VERIFIED: phase scope and local tool availability]

## Package Legitimacy Audit

No package installation is recommended for Phase 2, so the package legitimacy gate is not applicable. [VERIFIED: Standard Stack research]

| Package | Registry | Age | Downloads | Source Repo | slopcheck | Disposition |
|---------|----------|-----|-----------|-------------|-----------|-------------|
| none | not_applicable | not_applicable | not_applicable | not_applicable | not_run | No external package install in this phase. |

**Packages removed due to slopcheck [SLOP] verdict:** none
**Packages flagged as suspicious [SUS]:** none

## Architecture Patterns

### System Architecture Diagram

```text
Official TR-E scope + Phase 2 CONTEXT decisions
                  |
                  v
02_TR_E_POSITIONING_LOCK.md
  - allowed framing
  - prohibited framing
  - core contribution
  - journal-fit rationale
                  |
                  v
Manuscript/package scans -----> Formal Phase 6 manifest/tables/validation reports
  manuscript/*.tex                  results/formal/phase06/**
  README.md                         experiments/formal_statistics.py
  CLAUDE.md                         validation scripts
  figure-script comments
                  |                              |
                  v                              v
03_CLAIM_LEDGER.md <-------------- evidence-role map and formulas
  one row per occurrence
  current sentence + safe sentence
  source/script/command/formula/numerator/denominator
                  |
                  v
05_BLOCKERS_AND_SAFE_CLAIMS.md
  category rules + concrete hits
  status enum + owner phase routing
                  |
                  v
Phase 3 non-numeric manuscript revision -> Phase 4 value provenance -> Phase 5 readiness
```

### Recommended Project Structure

```text
.planning/
├── phases/
│   └── 02-tr-e-positioning-lock-and-claim-ledger/
│       ├── 02-CONTEXT.md
│       └── 02-RESEARCH.md
└── milestones/
    └── tr_e_claim_ready/
        ├── 00_MILESTONE_PLAN.md
        ├── 01_REPO_AND_EVIDENCE_AUDIT.md
        ├── 02_TR_E_POSITIONING_LOCK.md
        ├── 03_CLAIM_LEDGER.md
        ├── 04_MANUSCRIPT_ACTION_PLAN.md
        └── 05_BLOCKERS_AND_SAFE_CLAIMS.md
```

### Pattern 1: Occurrence-Level Claim Ledger

**What:** One row per claim occurrence, even when multiple occurrences share the same idea; use `claim_family_id` to group repeated concepts. [CITED: .planning/phases/02-tr-e-positioning-lock-and-claim-ledger/02-CONTEXT.md]

**When to use:** Every current or planned manuscript claim in `manuscript/main.tex` and `manuscript/sections/*.tex`; package-facing files go to blockers unless promoted into the submitted package. [CITED: .planning/phases/02-tr-e-positioning-lock-and-claim-ledger/02-CONTEXT.md]

**Example schema:**

```markdown
| claim_id | claim_family_id | manuscript_location | current_sentence | claim_type | comparison | metric | reported_value | source_path | supporting_source_path | script_path | generation_command | metric_formula | numerator | denominator | evidence_role | phase4_status | action | allowed_sentence | prohibited_sentence |
|----------|-----------------|---------------------|------------------|------------|------------|--------|----------------|-------------|------------------------|-------------|--------------------|----------------|-----------|-------------|---------------|---------------|--------|------------------|---------------------|
| CL-001 | CF-routing-intensity | manuscript/sections/abstract.tex:15 | ... | numerical_result | FullModel vs DoorToDoor | vkm_per_served_trip | 29.1% | manuscript/sections/abstract.tex | results/formal/phase06/tables/paired_differences.csv | experiments/formal_statistics.py | $env:PYTHONPATH='src'; python -m experiments.formal_statistics --validate --results-dir results/formal/phase06 | vehicle_km / n_served | vehicle_km | n_served | primary_behavioral | phase4_verify_number | phase4_verify_number | Under tested synthetic service-design conditions, FullModel achieves [PHASE4_VERIFIED_VALUE] lower vkm per served trip than DoorToDoor, with served-share trade-offs documented in [PHASE4_VERIFIED_TABLE]. | FullModel achieves 29.1% improvement. |
```

### Pattern 2: Evidence-Role Enum

**What:** Use a fixed `evidence_role` enum to prevent diagnostic evidence from becoming headline evidence. [CITED: .planning/phases/02-tr-e-positioning-lock-and-claim-ledger/02-CONTEXT.md]

**Recommended enum:** `positioning`, `mechanism_scope`, `primary_behavioral`, `diagnostic_matched_coverage`, `diagnostic_fixed_accepted_set`, `robustness_sensitivity`, `equity_type_heterogeneity`, `algorithm_diagnostic`, `limitation`, `package_consistency`. [CITED: .planning/phases/02-tr-e-positioning-lock-and-claim-ledger/02-CONTEXT.md]

**Canonical path mapping:**

| Evidence Role | Canonical Source Family | Allowed Use |
|---------------|-------------------------|-------------|
| `primary_behavioral` | `results/formal/phase06/main_behavioral/` and main tables | Main conditional operational-efficiency, coverage, acceptance, rejection, and denominator claims after Phase 4 checks. [CITED: .planning/milestones/tr_e_claim_ready/01_REPO_AND_EVIDENCE_AUDIT.md] |
| `diagnostic_matched_coverage` | `results/formal/phase06/coverage_controls/matched_coverage/` and `matched_coverage_paired_differences.csv` | Coverage-confounding diagnostic, not primary equal-service headline. [CITED: .planning/milestones/tr_e_claim_ready/01_REPO_AND_EVIDENCE_AUDIT.md] |
| `diagnostic_fixed_accepted_set` | `results/formal/phase06/coverage_controls/fixed_accepted_set/` and `fixed_accepted_set_paired_differences.csv` | Fixed accepted-set decomposition, not complete dynamic benchmark. [CITED: .planning/milestones/tr_e_claim_ready/01_REPO_AND_EVIDENCE_AUDIT.md] |
| `robustness_sensitivity` | `results/formal/phase06/robustness/utility_sensitivity/`, `mp_density_walking_radius/`, `fleet_demand_stress/` | Conditional robustness and service-design boundary statements. [CITED: .planning/milestones/tr_e_claim_ready/01_REPO_AND_EVIDENCE_AUDIT.md] |
| `equity_type_heterogeneity` | `results/formal/phase06/robustness/equity_type_outcomes/` and `equity_type_summary.csv` | Limited passenger-type heterogeneity and monitoring implications. [CITED: .planning/milestones/tr_e_claim_ready/01_REPO_AND_EVIDENCE_AUDIT.md] |
| `algorithm_diagnostic` | `results/formal/phase06/robustness/algorithm_diagnostics/` | Simplified ex-post diagnostics and limitations only. [CITED: .planning/milestones/tr_e_claim_ready/01_REPO_AND_EVIDENCE_AUDIT.md] |

### Pattern 3: Blocker Table With Rule Layer And Hit Layer

**What:** `05_BLOCKERS_AND_SAFE_CLAIMS.md` should include category-level rules and concrete scan hits. [CITED: .planning/phases/02-tr-e-positioning-lock-and-claim-ledger/02-CONTEXT.md]

**Concrete hit schema:**

```markdown
| issue_id | location | matched_text_or_pattern | risk_family | status | evidence_role | owner_phase | required_action | allowed_replacement | verification_check |
|----------|----------|-------------------------|-------------|--------|---------------|-------------|-----------------|---------------------|--------------------|
| BLK-001 | manuscript/sections/abstract.tex:15 | 18.3% / 29.1% | old_number | blocker | primary_behavioral | Phase 4 | Verify against formal Phase 6 provenance before retaining or replacing. | Use [PHASE4_VERIFIED_VALUE] placeholder until Phase 4. | `rg -n "18\\.3|29\\.1|35\\.0|0\\.1216" manuscript README.md CLAUDE.md` |
```

### Pattern 4: Denominator Formula Contract

**What:** Ledger numerical rows must record `metric_formula`, `numerator`, and `denominator` according to the formal validation contract. [VERIFIED: experiments/formal_validation.py]

| Metric | Formula | Numerator | Denominator | Source |
|--------|---------|-----------|-------------|--------|
| `served_share` | `n_served / n_requests` | `n_served` | `n_requests` | [VERIFIED: experiments/formal_validation.py] |
| `vkm_per_original_request` | `vehicle_km / n_requests` | `vehicle_km` | `n_requests` | [VERIFIED: experiments/formal_validation.py] |
| `vkm_per_served_trip` | `vehicle_km / n_served` | `vehicle_km` | `n_served` | [VERIFIED: experiments/formal_validation.py] |
| `behavioral_acceptance_rate` | `1 - choice_rejection_rate` | `not_applicable_rate_complement` | `not_applicable_rate_complement` | [VERIFIED: experiments/formal_validation.py] |
| `rejection_partition` | `served_share + choice_rejection_rate + feasibility_rejection_rate = 1` | `not_applicable_partition_sum` | `not_applicable_partition_sum` | [VERIFIED: experiments/formal_validation.py] |
| `total_vehicle_km_alias` | `total_vehicle_km == vehicle_km` | `total_vehicle_km` | `vehicle_km` | [VERIFIED: experiments/formal_validation.py] |
| `social_welfare` | `sum_r[z_r * U_rb* - (1 - z_r) * gamma]` | `accepted utility minus rejected penalty terms` | `not_applicable_sum` | [VERIFIED: experiments/metrics.py] |

### Anti-Patterns to Avoid

- **Using final numbers in Phase 2 allowed sentences:** Phase 2 must use non-numeric wording or Phase 4 placeholders for unverified percentages, CIs, significance language, tables, and figures. [CITED: .planning/phases/02-tr-e-positioning-lock-and-claim-ledger/02-CONTEXT.md]
- **Ledger by claim idea instead of occurrence:** The user locked occurrence-level rows; family IDs preserve grouping. [CITED: .planning/phases/02-tr-e-positioning-lock-and-claim-ledger/02-CONTEXT.md]
- **Treating diagnostics as headline evidence:** Matched coverage, fixed accepted set, MILP, robustness, and equity evidence require diagnostic/limited qualifiers. [CITED: .planning/milestones/tr_e_claim_ready/01_REPO_AND_EVIDENCE_AUDIT.md]
- **Blank provenance fields for non-numeric rows:** Use `not_applicable`, `not_applicable_manual_text`, and supporting-source fields rather than omitting schema fields. [CITED: .planning/phases/02-tr-e-positioning-lock-and-claim-ledger/02-CONTEXT.md]
- **Editing manuscript/package files during Phase 2:** Phase 2 may scan but must not edit `manuscript/`, `README.md`, `CLAUDE.md`, result files, or code. [CITED: .planning/phases/02-tr-e-positioning-lock-and-claim-ledger/02-CONTEXT.md]

## Don't Hand-Roll

| Problem | Don't Build | Use Instead | Why |
|---------|-------------|-------------|-----|
| Evidence generation | New experiment runs or manual numbers | Existing `results/formal/phase06/` tables and validation reports | Formal evidence is already validated and canonical for manuscript claims. [VERIFIED: results/formal/phase06/phase06_verification_report.json] |
| Risk discovery | Ad hoc visual skim only | `rg` scan families plus manual sentence review | Current risk families are widespread and easy to miss manually. [VERIFIED: rg scan 2026-06-17] |
| Metric formulas | Free-text metric descriptions | Formal denominator contract from `experiments/formal_validation.py` and `experiments/metrics.py` | Denominator drift is a known claim risk and already has validation logic. [VERIFIED: experiments/formal_validation.py; CITED: .planning/milestones/tr_e_claim_ready/01_REPO_AND_EVIDENCE_AUDIT.md] |
| Journal-fit scope | Generic "TR-E fit" prose | Official TR-E aims/scope plus locked Phase 2 wording | Official scope supports logistics, OM/SCM, simulation, and OR methods. [CITED: ScienceDirect TR-E aims and scope] |
| Blocker routing | One undifferentiated TODO list | `safe`, `safe_with_qualifier`, `downgrade_required`, `blocker` plus owner phase | The user locked this status enum and routing semantics. [CITED: .planning/phases/02-tr-e-positioning-lock-and-claim-ledger/02-CONTEXT.md] |

**Key insight:** The planner should treat Phase 2 as a claim governance system. The value is not new evidence; it is preventing unsafe evidence promotion before Phase 3 prose edits and Phase 4 numerical provenance. [CITED: .planning/ROADMAP.md; CITED: .planning/milestones/tr_e_claim_ready/00_MILESTONE_PLAN.md]

## Common Pitfalls

### Pitfall 1: "Safe Replacement" Accidentally Locks A Number

**What goes wrong:** `allowed_sentence` rewrites keep values such as `18.3%`, `29.1%`, `35.0%`, `0.1216`, final table numbers, or CI language. [VERIFIED: rg scan 2026-06-17]
**Why it happens:** The current manuscript already contains old values across abstract, introduction, experiments, policy, and conclusion. [VERIFIED: rg scan 2026-06-17]
**How to avoid:** Use `[PHASE4_VERIFIED_VALUE]`, `[PHASE4_VERIFIED_CI]`, and `[PHASE4_VERIFIED_TABLE]` placeholders until Phase 4. [CITED: .planning/phases/02-tr-e-positioning-lock-and-claim-ledger/02-CONTEXT.md]
**Warning signs:** Any Phase 2 artifact contains a concrete percentage or value in a replacement sentence without `phase4_status=phase4_verify_number`. [CITED: .planning/phases/02-tr-e-positioning-lock-and-claim-ledger/02-CONTEXT.md]

### Pitfall 2: Treating "Policy Implications" As TR-E Journal Fit

**What goes wrong:** The manuscript remains framed around Part A policy validation rather than logistics/operations service design. [VERIFIED: rg scan 2026-06-17]
**Why it happens:** `manuscript/main.tex`, `README.md`, `CLAUDE.md`, and package-facing files still contain Part A and policy wording. [VERIFIED: rg scan 2026-06-17]
**How to avoid:** Anchor TR-E fit in logistics, DRT/DARP operations, service consolidation, dynamic routing, fleet operations, OM/SCM, and simulation/OR methods. [CITED: ScienceDirect TR-E aims and scope; CITED: .planning/phases/02-tr-e-positioning-lock-and-claim-ledger/02-CONTEXT.md]
**Warning signs:** "policy decision tool", "TR Part A mandate", "actionable policy recommendations", or "real-world validation" appears as the primary contribution. [CITED: .planning/phases/02-tr-e-positioning-lock-and-claim-ledger/02-CONTEXT.md]

### Pitfall 3: Diagnostic Evidence Becomes The Headline

**What goes wrong:** Matched-coverage, fixed-accepted-set, Gamma/Pareto, equity, or MILP results are written as primary estimates or proof. [CITED: .planning/milestones/tr_e_claim_ready/01_REPO_AND_EVIDENCE_AUDIT.md]
**Why it happens:** Current manuscript sections already mention matched coverage, Gamma, Pareto, MILP gaps, and equity values in narrative positions that need classification. [VERIFIED: rg scan 2026-06-17]
**How to avoid:** Put every diagnostic occurrence in the ledger with explicit `evidence_role` and diagnostic qualifier in `allowed_sentence`. [CITED: .planning/phases/02-tr-e-positioning-lock-and-claim-ledger/02-CONTEXT.md]
**Warning signs:** Phrases such as "primary headline", "complete dynamic benchmark", "ALNS near-optimality", "Pareto frontier", or "policy control" appear near diagnostic material. [CITED: .planning/phases/02-tr-e-positioning-lock-and-claim-ledger/02-CONTEXT.md]

### Pitfall 4: Package-Facing Files Are Either Ignored Or Over-Ledgered

**What goes wrong:** README, CLAUDE, cover letter, response file, and figure comments either escape blocker tracking or bloat the manuscript ledger. [CITED: .planning/phases/02-tr-e-positioning-lock-and-claim-ledger/02-CONTEXT.md]
**Why it happens:** These files contain Part A, policy, old-number, Gamma/Pareto, MILP, and legacy-path wording, but they are not all main manuscript scope. [VERIFIED: rg scan 2026-06-17]
**How to avoid:** Use layered coverage: manuscript claims go to `03_CLAIM_LEDGER.md`; package-facing risks go to `05_BLOCKERS_AND_SAFE_CLAIMS.md` unless final submission use promotes them. [CITED: .planning/phases/02-tr-e-positioning-lock-and-claim-ledger/02-CONTEXT.md]
**Warning signs:** `manuscript/cover_letter.tex` or `manuscript/response_to_reviewers.tex` receives full ledger rows before Phase 5 decides submission-package status. [CITED: .planning/phases/02-tr-e-positioning-lock-and-claim-ledger/02-CONTEXT.md]

## Code Examples

### Risk-Family Scan Commands

```powershell
# Source: verified local rg scan, 2026-06-17
rg -n "18\.3|29\.1|35\.0|0\.1216" manuscript README.md CLAUDE.md
rg -n "Transportation Research Part A|TR Part A|TR-A|Part A" manuscript README.md CLAUDE.md
rg -n "policy|Policy Implications|policy implications|decision tool|recommendation" manuscript README.md CLAUDE.md
rg -n "Gamma|gamma|Pareto|welfare" manuscript README.md CLAUDE.md manuscript\figures\scripts
rg -n "Beijing|real-world|validation|semi-realistic" manuscript README.md CLAUDE.md
rg -n "MILP|exact|near-optimal|optimality gap|benchmark" manuscript README.md CLAUDE.md
rg -n "dominates|dominance|outperform|outperforms|superior|improvement|gain" manuscript README.md CLAUDE.md
```

### Ledger Header Validation

```powershell
# Source: Phase 2 mandatory schema from CONTEXT.md and REQUIREMENTS.md
$required = @(
  "source_path",
  "script_path",
  "generation_command",
  "metric_formula",
  "numerator",
  "denominator",
  "evidence_role",
  "allowed_sentence",
  "prohibited_sentence"
)
# For a Markdown ledger, validate header text:
$content = Get-Content -Raw ".planning\milestones\tr_e_claim_ready\03_CLAIM_LEDGER.md"
$missing = $required | Where-Object { $content -notmatch "\|\s*$($_)\s*\|" }
if ($missing) { throw "Missing required ledger columns: $($missing -join ', ')" }
```

### Evidence Validation Commands For Provenance References

```powershell
# Source: local CLI help and milestone plan
$env:PYTHONPATH='src'; python -m experiments.formal_statistics --validate --results-dir results/formal/phase06
$env:PYTHONPATH='src'; python -m experiments.phase06_formal --validate --results-dir results/formal/phase06/main_behavioral
$env:PYTHONPATH='src'; python -m experiments.phase06_coverage_controls --validate --package all
$env:PYTHONPATH='src'; python -m experiments.phase06_robustness --validate --package all
```

## State of the Art

| Old Approach | Current Approach | When Changed | Impact |
|--------------|------------------|--------------|--------|
| Part A policy-first framing | TR-E logistics/operations service-design framing | Locked in current milestone context, 2026-06-17 | Phase 2 positioning lock must prohibit policy-first contribution framing. [CITED: .planning/phases/02-tr-e-positioning-lock-and-claim-ledger/02-CONTEXT.md] |
| Root legacy CSVs and old manuscript values | Formal Phase 6 evidence under `results/formal/phase06/` | Phase 1 audit, 2026-06-16 | Ledger formal claims must trace to formal paths, not root result CSVs. [CITED: .planning/milestones/tr_e_claim_ready/01_REPO_AND_EVIDENCE_AUDIT.md] |
| Final numbers during prose rewrite | Phase 4-only numerical provenance injection | Roadmap/planning revision | Phase 2 and Phase 3 use placeholders for unverified values. [CITED: .planning/ROADMAP.md; CITED: .planning/phases/02-tr-e-positioning-lock-and-claim-ledger/02-CONTEXT.md] |
| MILP as benchmark/validation | MILP as simplified ex-post diagnostic | Phase 1/2 constraints | MILP claims require diagnostic qualifiers and limitations. [CITED: .planning/milestones/tr_e_claim_ready/01_REPO_AND_EVIDENCE_AUDIT.md] |
| Gamma/Pareto as policy control | Gamma as post-hoc welfare/sensitivity accounting | Phase 1/2 constraints | Gamma cannot be framed as endogenous routing, offer, acceptance, or policy control. [CITED: AGENTS.md; CITED: .planning/phases/02-tr-e-positioning-lock-and-claim-ledger/02-CONTEXT.md] |

**Deprecated/outdated:**
- `Transportation Research Part A: Policy and Practice` as target journal: replaced by Transportation Research Part E: Logistics and Transportation Review for this milestone. [CITED: AGENTS.md; VERIFIED: rg scan 2026-06-17]
- `Policy Implications` as primary section framing: Phase 3 should reframe toward managerial/operational implications. [CITED: .planning/phases/02-tr-e-positioning-lock-and-claim-ledger/02-CONTEXT.md]
- `Pareto frontier` when implying endogenous optimization or policy control: use post-hoc welfare/sensitivity display if retained. [CITED: .planning/phases/02-tr-e-positioning-lock-and-claim-ledger/02-CONTEXT.md]

## Assumptions Log

| # | Claim | Section | Risk if Wrong |
|---|-------|---------|---------------|
| A1 | A Markdown table is sufficient for the claim ledger even though CSV would be easier to machine-validate. [ASSUMED] | Standard Stack | If planner requires stronger automation, it may need an auxiliary validator script or a CSV-export companion. |
| A2 | ASVS applicability is limited because Phase 2 writes planning docs and does not add a service, auth, session, database, or network boundary. [ASSUMED] | Security Domain | If hidden automation is added, security controls must be expanded. |

## Open Questions (RESOLVED)

1. **Should `03_CLAIM_LEDGER.md` include an auxiliary machine-readable appendix?**
   - What we know: The user locked a Markdown artifact path and mandatory columns. [CITED: .planning/phases/02-tr-e-positioning-lock-and-claim-ledger/02-CONTEXT.md]
   - Resolution: No auxiliary CSV or machine-readable appendix is required for Phase 2. The Phase 2 deliverable remains `03_CLAIM_LEDGER.md`; CSV export is deferred/not required unless a later phase explicitly adds it as a new requirement. [RESOLVED]
   - Planning rule: Use Markdown schema and coverage validation snippets inside the plan rather than creating extra artifacts in Phase 2. [RESOLVED]

2. **How many current manuscript claims should be included as full rows?**
   - What we know: One row per manuscript claim occurrence is locked. [CITED: .planning/phases/02-tr-e-positioning-lock-and-claim-ledger/02-CONTEXT.md]
   - Resolution: Phase 2 execution must cover every current and planned manuscript claim in `manuscript/main.tex` and all `manuscript/sections/*.tex`, not only regex-detected numerical hits. Each claim-bearing sentence, bullet, caption-like manuscript reference, or claim-bearing clause gets an occurrence-level `claim_id`; multi-metric sentences are split when evidence roles, denominators, or actions differ. [RESOLVED]
   - Planning rule: `03_CLAIM_LEDGER.md` must include a coverage inventory with reviewed line ranges for every target manuscript file and either mapped claim IDs or an explicit no-claim note. [RESOLVED]

## Environment Availability

| Dependency | Required By | Available | Version | Fallback |
|------------|-------------|-----------|---------|----------|
| Python | CSV/JSON schema checks and optional validation commands | yes | 3.12.4 | Manual Markdown review if not available. [VERIFIED: `python --version`] |
| `rg` | Risk-family scans and claim discovery | yes | 15.1.0 | PowerShell `Select-String`, slower and more verbose. [VERIFIED: `rg --version`] |
| `git` | Confirm planning-only diffs and commit docs | yes | 2.53.0.windows.1 | Manual file diff review if not available. [VERIFIED: `git --version`] |
| `pytest` | Existing downstream test suite | yes | 8.4.2 | Not required for pure docs; use artifact checks. [VERIFIED: `python -m pytest --version`] |
| `pdflatex` | Phase 5 manuscript compile gate | yes | MiKTeX executable found | Not required in Phase 2. [VERIFIED: `Get-Command pdflatex`] |
| `bibtex` | Phase 5 manuscript compile gate | yes | MiKTeX executable found | Not required in Phase 2. [VERIFIED: `Get-Command bibtex`] |

**Missing dependencies with no fallback:** none found for Phase 2. [VERIFIED: environment audit 2026-06-17]

**Missing dependencies with fallback:** none found for Phase 2. [VERIFIED: environment audit 2026-06-17]

## Validation Architecture

### Test Framework

| Property | Value |
|----------|-------|
| Framework | `pytest` 8.4.2 plus shell artifact checks. [VERIFIED: `python -m pytest --version`] |
| Config file | none detected in `pyproject.toml`; active tests exist under `tests/`. [VERIFIED: pyproject.toml; VERIFIED: tests directory listing] |
| Quick run command | `Test-Path .planning\milestones\tr_e_claim_ready\02_TR_E_POSITIONING_LOCK.md; Test-Path .planning\milestones\tr_e_claim_ready\03_CLAIM_LEDGER.md; Test-Path .planning\milestones\tr_e_claim_ready\05_BLOCKERS_AND_SAFE_CLAIMS.md` |
| Full suite command | `$env:PYTHONPATH='src'; pytest tests` for downstream regression if implementation adds helper scripts; not required for Markdown-only Phase 2. [CITED: .planning/milestones/tr_e_claim_ready/00_MILESTONE_PLAN.md] |

### Phase Requirements To Test Map

| Req ID | Behavior | Test Type | Automated Command | File Exists? |
|--------|----------|-----------|-------------------|-------------|
| PLAN-04 | Blockers/safe claims artifact exists and uses required statuses. | artifact/schema | `Test-Path .planning\milestones\tr_e_claim_ready\05_BLOCKERS_AND_SAFE_CLAIMS.md; rg -n "safe_with_qualifier|downgrade_required|blocker" .planning\milestones\tr_e_claim_ready\05_BLOCKERS_AND_SAFE_CLAIMS.md` | No - Wave 0 creates artifact. [VERIFIED: filesystem listing 2026-06-17] |
| CLAI-01 | Positioning lock states allowed/prohibited framing and journal-fit rationale. | artifact/content | `rg -n "allowed|prohibited|journal-fit|logistics|operations|passenger-response-aware simulation framework" .planning\milestones\tr_e_claim_ready\02_TR_E_POSITIONING_LOCK.md` | No - Wave 0 creates artifact. [VERIFIED: filesystem listing 2026-06-17] |
| CLAI-02 | Claim ledger contains mandatory provenance columns. | schema | Use ledger header validation snippet above. | No - Wave 0 creates artifact. [VERIFIED: filesystem listing 2026-06-17] |
| CLAI-03 | Numerical claims in target manuscript sections appear in ledger. | coverage/manual-assisted | `rg -n "18\.3|29\.1|35\.0|0\.1216|%|vkm|Gini|percentage points|confidence|Table~|Figure~" manuscript\sections\abstract.tex manuscript\sections\intro.tex manuscript\sections\experiments.tex manuscript\sections\policy.tex manuscript\sections\conclusion.tex` then cross-check claim IDs. | No - Wave 0 creates artifact. [VERIFIED: rg scan 2026-06-17] |
| CLAI-04 | Evidence roles distinguish primary, diagnostic, robustness, equity, algorithm, and limitation claims. | schema/content | `rg -n "primary_behavioral|diagnostic_matched_coverage|diagnostic_fixed_accepted_set|robustness_sensitivity|equity_type_heterogeneity|algorithm_diagnostic|limitation" .planning\milestones\tr_e_claim_ready\03_CLAIM_LEDGER.md .planning\milestones\tr_e_claim_ready\05_BLOCKERS_AND_SAFE_CLAIMS.md` | No - Wave 0 creates artifact. [VERIFIED: filesystem listing 2026-06-17] |

### Sampling Rate

- **Per task commit:** Run artifact existence/schema checks for the artifact touched by that plan. [ASSUMED]
- **Per wave merge:** Run all artifact checks plus fixed risk-family scans against target artifacts. [ASSUMED]
- **Phase gate:** Confirm all three Phase 2 artifacts exist, ledger mandatory columns exist, blocker statuses exist, evidence-role enum appears, and Phase 2 did not modify `manuscript/`, `README.md`, `CLAUDE.md`, `results/`, `src/`, `experiments/`, or `analysis/`. [CITED: .planning/phases/02-tr-e-positioning-lock-and-claim-ledger/02-CONTEXT.md]

### Wave 0 Gaps

- [ ] `.planning/milestones/tr_e_claim_ready/02_TR_E_POSITIONING_LOCK.md` - covers CLAI-01. [VERIFIED: filesystem listing 2026-06-17]
- [ ] `.planning/milestones/tr_e_claim_ready/03_CLAIM_LEDGER.md` - covers CLAI-02, CLAI-03, CLAI-04. [VERIFIED: filesystem listing 2026-06-17]
- [ ] `.planning/milestones/tr_e_claim_ready/05_BLOCKERS_AND_SAFE_CLAIMS.md` - covers PLAN-04 and supports CLAI-04. [VERIFIED: filesystem listing 2026-06-17]
- [ ] No dedicated automated test file exists for Phase 2 planning artifacts; use shell schema checks unless planner chooses to add a small validator. [VERIFIED: tests directory listing 2026-06-17]

## Security Domain

### Applicable ASVS Categories

| ASVS Category | Applies | Standard Control |
|---------------|---------|-----------------|
| V2 Authentication | no | No authentication surface in a local documentation phase. [ASSUMED] |
| V3 Session Management | no | No session state in a local documentation phase. [ASSUMED] |
| V4 Access Control | no | Keep edits restricted to `.planning/` artifacts and avoid modifying source/manuscript/results in Phase 2. [CITED: .planning/phases/02-tr-e-positioning-lock-and-claim-ledger/02-CONTEXT.md] |
| V5 Input Validation | yes | Treat file paths and scan patterns as repo-relative; do not use generated shell strings from untrusted text. [ASSUMED] |
| V6 Cryptography | no | No cryptographic operation in scope. [ASSUMED] |

### Known Threat Patterns for Documentation/Provenance Stack

| Pattern | STRIDE | Standard Mitigation |
|---------|--------|---------------------|
| Evidence spoofing by referencing non-canonical outputs | Tampering | Require formal claims to trace to `results/formal/phase06/`; classify root legacy/archive/smoke as non-canonical. [CITED: AGENTS.md; CITED: .planning/milestones/tr_e_claim_ready/01_REPO_AND_EVIDENCE_AUDIT.md] |
| Hidden numerical substitution | Tampering | No manual numeric editing; use Phase 4 placeholders until formal provenance checks. [CITED: AGENTS.md; CITED: .planning/phases/02-tr-e-positioning-lock-and-claim-ledger/02-CONTEXT.md] |
| License/secret leakage from local solver environment | Information Disclosure | Phase 2 should not run Gurobi; if diagnostic status is cited, cite existing validation/manifest artifacts only. [CITED: .planning/codebase/CONCERNS.md] |
| Shell injection through scan commands | Elevation of Privilege | Use static scan patterns and repo-relative paths; do not build shell commands from manuscript content. [ASSUMED] |

## Sources

### Primary (HIGH confidence)

- `.planning/phases/02-tr-e-positioning-lock-and-claim-ledger/02-CONTEXT.md` - locked Phase 2 decisions, schema, scope, evidence-role enum, blocker statuses, and artifact responsibilities. [CITED: local file]
- `.planning/REQUIREMENTS.md` - Phase 2 requirement IDs and requirement descriptions. [CITED: local file]
- `.planning/ROADMAP.md` - Phase 2 goal, success criteria, and plan list. [CITED: local file]
- `.planning/milestones/tr_e_claim_ready/00_MILESTONE_PLAN.md` - evidence boundary, phase gates, verification gates, readiness label rules. [CITED: local file]
- `.planning/milestones/tr_e_claim_ready/01_REPO_AND_EVIDENCE_AUDIT.md` - canonical manuscript/evidence sources, evidence-role map, validation snapshot, non-canonical source rules. [CITED: local file]
- `.planning/milestones/tr_e_claim_ready/04_MANUSCRIPT_ACTION_PLAN.md` - manuscript file actions, wording families, Phase 4 numerical gate. [CITED: local file]
- `results/formal/phase06/phase06_result_manifest.json` - formal evidence package manifest, row counts, validation status, smoke exclusion. [VERIFIED: local file]
- `results/formal/phase06/phase06_verification_report.json` - formal verification checks and pass status. [VERIFIED: local file]
- `experiments/formal_validation.py` and `experiments/metrics.py` - denominator checks and metric formula definitions. [VERIFIED: local code]
- ScienceDirect TR-E aims and scope - journal scope, logistics specialization, method openness. [CITED: https://www.sciencedirect.com/journal/transportation-research-part-e-logistics-and-transportation-review/about/aims-and-scope]

### Secondary (MEDIUM confidence)

- ScienceDirect / Elsevier guide for authors - abstract, table, figure, data/reference, and submission checklist guidance. [CITED: https://www.sciencedirect.com/journal/transportation-research-part-e-logistics-and-transportation-review/publish/guide-for-authors]

### Tertiary (LOW confidence)

- Assumptions about optional auxiliary CSV validation and ASVS non-applicability for a documentation-only phase. [ASSUMED]

## Metadata

**Confidence breakdown:**
- Standard stack: HIGH - local tool versions and file inventory were verified; no new packages are needed. [VERIFIED: environment audit 2026-06-17]
- Architecture: HIGH - artifact responsibilities and evidence boundaries are locked in Phase 2 context and Phase 1 milestone files. [CITED: .planning/phases/02-tr-e-positioning-lock-and-claim-ledger/02-CONTEXT.md]
- Pitfalls: HIGH - risk families are both locked by user decisions and present in current manuscript/package scans. [CITED: .planning/phases/02-tr-e-positioning-lock-and-claim-ledger/02-CONTEXT.md; VERIFIED: rg scan 2026-06-17]

**Research date:** 2026-06-17
**Valid until:** 2026-07-17 for local repository findings; re-check official journal scope before submission package finalization if submission occurs later. [ASSUMED]
