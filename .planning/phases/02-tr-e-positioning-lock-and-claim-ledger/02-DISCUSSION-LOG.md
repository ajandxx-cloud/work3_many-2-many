# Phase 2: TR-E Positioning Lock and Claim Ledger - Discussion Log

> **Audit trail only.** Do not use as input to planning, research, or execution agents.
> Decisions are captured in CONTEXT.md - this log preserves the alternatives considered.

**Date:** 2026-06-17T17:01:05.3846057+08:00
**Phase:** 2-TR-E Positioning Lock and Claim Ledger
**Areas discussed:** Ledger line granularity and coverage, TR-E positioning lock core narrative, Evidence-role and blocker classification, Phase 3 prohibited wording and replacement rules, Ledger coverage scope, Non-numeric claim provenance, Allowed sentence precision, Blocker table granularity

---

## Ledger Line Granularity And Coverage

| Option | Description | Selected |
|--------|-------------|----------|
| One row per manuscript occurrence | Each concrete manuscript claim occurrence gets its own ledger row; related claims are connected through `claim_family_id`. | yes |
| One row per claim family | One row per shared idea with multiple manuscript locations in a field. | |
| Mixed granularity | Numerical claims use occurrence rows; qualitative framing claims use family rows. | |
| Agent discretion | Let the agent choose based on Phase 2 readiness risk. | |

**User's choice:** One row per manuscript occurrence.
**Notes:** The user chose the most traceable approach. This supports 100% coverage and precise Phase 3/4 edits.

| Option | Description | Selected |
|--------|-------------|----------|
| Current claims plus planned replacement claims | Ledger covers current manuscript claims and safe planned replacement claims. | yes |
| Current manuscript claims only | Ledger acts only as an audit list. | |
| Current claims plus high-risk replacements only | Planned replacements are written only for old numbers and high-risk semantic claims. | |
| Agent discretion | Let the agent choose. | |

**User's choice:** Current claims plus planned replacement claims.
**Notes:** The ledger should function as an execution handoff, not only an audit artifact.

| Option | Description | Selected |
|--------|-------------|----------|
| Non-numeric safe sentences with Phase 4 placeholders | Allowed sentences avoid final numbers and use placeholders for Phase 4 verification. | yes |
| Use existing formal-table numbers but mark for Phase 4 verification | Earlier numerical fill-in with later verification. | |
| Only provide prohibited_sentence | Phase 2 says what not to write; Phase 3 writes replacements. | |
| Agent discretion | Let the agent choose. | |

**User's choice:** Non-numeric safe sentences with Phase 4 placeholders.
**Notes:** This preserves the milestone rule that Phase 4 performs final numerical injection.

| Option | Description | Selected |
|--------|-------------|----------|
| Add full execution fields | Add `claim_id`, `claim_family_id`, `manuscript_location`, `current_sentence`, `claim_type`, `comparison`, `metric`, `reported_value`, `phase4_status`, and `action`. | yes |
| Only mandatory fields plus manuscript location | Simpler table with less execution detail. | |
| Mandatory fields plus minimal execution fields | Add only claim ID, family ID, location, current sentence, and action. | |
| Agent discretion | Let the agent choose. | |

**User's choice:** Add full execution fields.
**Notes:** The ledger should support Phase 3 and Phase 4 filtering, not just provenance review.

---

## TR-E Positioning Lock Core Narrative

| Option | Description | Selected |
|--------|-------------|----------|
| Operational service-design evidence | Anchor the paper as evidence about service-design trade-offs under tested conditions. | yes |
| Method framework contribution | Emphasize a passenger-response-aware bidirectional meeting-point framework. | |
| Managerial decision-tool contribution | Emphasize fleet deployment and operator decision support. | |
| All three with hierarchy | Include all, with one primary anchor. | |

**User's choice:** Operational service-design evidence.
**Notes:** Method and management content can appear, but must be subordinate to the TR-E operations evidence anchor.

| Option | Description | Selected |
|--------|-------------|----------|
| passenger-response-aware simulation framework | Safe strongest mechanism wording without implying endogenous acceptance-aware routing. | yes |
| passenger-response-aware operational design framework | More managerial but slightly broader. | |
| co-optimization of meeting points, routing, and passenger response | Stronger wording but unsafe for current route-then-sample mechanism. | |
| Agent discretion | Let the agent choose. | |

**User's choice:** `passenger-response-aware simulation framework`.
**Notes:** `co-optimization of meeting points, routing, and passenger response` is prohibited.

| Option | Description | Selected |
|--------|-------------|----------|
| DRT/DARP operations and service consolidation | Anchor journal fit in many-to-many DRT, DARP, meeting-point consolidation, dynamic routing, and fleet operations. | yes |
| Passenger choice and behavioral operations | Emphasize passenger response as the central field contribution. | |
| Urban mobility policy and public transit planning | Preserve more of the current Part A-style framing. | |
| All three with DRT/DARP operations primary | Include all with operations as primary. | |

**User's choice:** DRT/DARP operations and service consolidation.
**Notes:** Passenger choice is a service-design evaluation mechanism; policy/public service is bounded implication or limitation.

| Option | Description | Selected |
|--------|-------------|----------|
| Conservative but contribution-bearing | Say the design can reduce routing intensity per served trip under tested synthetic settings while creating trade-offs. | yes |
| Extremely conservative | Only say the study evaluates trade-offs. | |
| More forceful efficiency-improvement wording | Use stronger improvement language before final numerical verification. | |
| Agent discretion | Let the agent choose. | |

**User's choice:** Conservative but contribution-bearing.
**Notes:** The safe core sentence may have a clear contribution, but must be conditional and trade-off-aware.

---

## Evidence-Role And Blocker Classification

| Option | Description | Selected |
|--------|-------------|----------|
| Four-level status taxonomy | Use `safe`, `safe_with_qualifier`, `downgrade_required`, and `blocker`. | yes |
| Three-level status taxonomy | Use `safe`, `diagnostic_only`, and `blocker`. | |
| Evidence-role-only classification | Classify by evidence family without separate severity status. | |
| Agent discretion | Let the agent choose. | |

**User's choice:** Four-level status taxonomy.
**Notes:** This gives the blockers/safe-claims table enough precision for downstream action.

| Option | Description | Selected |
|--------|-------------|----------|
| Blocker until Phase 4 verified | Old/risky values cannot be retained or replaced with final values before Phase 4. | yes |
| Downgrade required | Phase 3 may convert to non-numeric wording or leave as pending. | |
| Classify by currently identifiable source | Values found in formal tables may be considered safe with qualifier. | |
| Agent discretion | Let the agent choose. | |

**User's choice:** Blocker until Phase 4 verified.
**Notes:** Applies to known values such as `18.3%`, `29.1%`, `35.0%`, and `0.1216`.

| Option | Description | Selected |
|--------|-------------|----------|
| Main text allowed with explicit diagnostic qualifier | Diagnostic evidence may appear, but every relevant claim must be explicitly qualified. | yes |
| Supplementary or limitations only | Diagnostic evidence stays out of main results. | |
| Main text allowed with only paragraph/table-note qualifier | A single qualifier can cover multiple diagnostic claims. | |
| Agent discretion | Let the agent choose. | |

**User's choice:** Main text allowed with explicit diagnostic qualifier.
**Notes:** Diagnostic evidence can explain mechanisms and boundaries but cannot become the headline estimate.

| Option | Description | Selected |
|--------|-------------|----------|
| Fine-grained passenger-burden claims are safe_with_qualifier or blocker | Walk, IVT, detour, fairness, type burden, and completed-trip precision need limitation or Phase 4 verification. | yes |
| Only fairness/equity require qualifier | Walk and IVT can be treated normally. | |
| Ban all related passenger-burden metrics | Remove or avoid all such claims. | |
| Agent discretion | Let the agent choose. | |

**User's choice:** Fine-grained passenger-burden claims are `safe_with_qualifier` or `blocker`.
**Notes:** Main metrics such as routing intensity, served share, and vkm per original request may remain formal ledger objects with provenance and Phase 4 numerical verification.

---

## Phase 3 Prohibited Wording And Replacement Rules

| Option | Description | Selected |
|--------|-------------|----------|
| Ban policy-first framing but allow bounded public-service implications | Reframe `Policy Implications` as managerial/operational implications while preserving limited public-service implications. | yes |
| Completely ban policy/policy implications | Remove policy language entirely. | |
| Keep policy but reframe as TR-E logistics policy | Less disruptive but keeps a policy flavor. | |
| Agent discretion | Let the agent choose. | |

**User's choice:** Ban policy-first framing but allow bounded public-service implications.
**Notes:** This supports TR-E positioning without erasing public-service context.

| Option | Description | Selected |
|--------|-------------|----------|
| Ban generic comparisons; allow metric-specific evidence-bounded comparisons | Avoid dominance/superiority wording; allow lower vkm per served trip with trade-off qualifiers. | yes |
| Completely ban these comparison words | Avoid all strong comparison terms. | |
| Allow outperforms when followed by a metric | More readable but riskier. | |
| Agent discretion | Let the agent choose. | |

**User's choice:** Ban generic comparisons; allow metric-specific evidence-bounded comparisons.
**Notes:** Comparisons must be metric-specific and paired with coverage/passenger-response trade-offs.

| Option | Description | Selected |
|--------|-------------|----------|
| Ban behavioral Pareto/endogenous Gamma; allow post-hoc welfare or sensitivity accounting | Keep Gamma as post-hoc only. | yes |
| Completely ban Pareto frontier; keep Gamma only in formula explanation | More conservative. | |
| Allow Pareto frontier if every use says post-hoc | Retain current term with qualifiers. | |
| Agent discretion | Let the agent choose. | |

**User's choice:** Ban behavioral Pareto/endogenous Gamma; allow post-hoc welfare or sensitivity accounting.
**Notes:** Gamma cannot be framed as routing, offer, acceptance, or policy-control behavior.

| Option | Description | Selected |
|--------|-------------|----------|
| Use qualifier templates for Beijing and MILP; ban near-optimal/exact dynamic/real-world validation | Beijing is synthetic/inspired; MILP is simplified ex-post diagnostic. | yes |
| Keep Beijing case study and MILP benchmark wording | More concise but riskier. | |
| Remove Beijing and MILP from main text | Safest but loses explanatory material. | |
| Agent discretion | Let the agent choose. | |

**User's choice:** Use qualifier templates for Beijing and MILP; ban near-optimal/exact dynamic/real-world validation.
**Notes:** Use `Beijing-inspired synthetic grid` and `simplified ex-post diagnostic over fixed accepted sets`.

---

## Ledger Coverage Scope

| Option | Description | Selected |
|--------|-------------|----------|
| Layered coverage | Main manuscript claims enter the full ledger; README, CLAUDE, cover/response, and figure-script risks enter blocker/package-consistency tracking unless submitted or reused. | yes |
| Put everything in the ledger | Every manuscript and package-facing risk sentence enters one claim ledger. | |
| Main manuscript first | Only `manuscript/main.tex` and `manuscript/sections/` are mandatory ledger scope. | |

**User's choice:** Layered coverage.
**Notes:** This keeps the main ledger executable while still tracking package-facing risk.

| Option | Description | Selected |
|--------|-------------|----------|
| Treat as package-consistency risks | `cover_letter.tex` and `response_to_reviewers.tex` are not full ledger scope now; Phase 5 decides whether to rewrite or clean them. | yes |
| Treat as final submission-package files | Add stricter package-facing ledger rows now. | |
| Treat as historical files | Mark them historical and outside required Phase 2/3 handling. | |

**User's choice:** Treat as package-consistency risks.
**Notes:** They remain scan targets, but not main manuscript claim-ledger rows unless they are submitted or reused.

| Option | Description | Selected |
|--------|-------------|----------|
| Script risks into blockers; figure claims to Phase 4 provenance | Comments, legacy input paths, TR Part A notes, and Pareto/Gamma naming risks are blocker/provenance risks; figure titles/captions/references are verified in Phase 4. | yes |
| Put all figure-script text in the ledger | Treat code comments and script labels like manuscript claims. | |
| Defer figure scripts | Wait until Phase 4 figure refresh. | |

**User's choice:** Script risks into blockers; figure claims to Phase 4 provenance.
**Notes:** This separates code/comment hygiene from formal figure and caption provenance.

| Option | Description | Selected |
|--------|-------------|----------|
| Submission or reuse trigger | Non-manuscript files upgrade to full ledger rows only when submitted or reused in submitted material. | yes |
| Numerical trigger | Any old number or evidence claim outside the manuscript gets a full ledger row. | |
| Never upgrade | Non-manuscript files always stay in blocker/package-consistency tracking. | |

**User's choice:** Submission or reuse trigger.
**Notes:** Package-facing material is controlled without overloading the manuscript claim ledger.

---

## Non-Numeric Claim Provenance

| Option | Description | Selected |
|--------|-------------|----------|
| Full schema with explicit N/A | Keep mandatory columns for all claim rows; use `not_applicable` for non-numeric formula, numerator, and denominator fields. | yes |
| Full schema only for numerical claims | Non-numeric claims may omit numerator/denominator columns. | |
| Split into two tables | Numerical claims and wording claims use separate ledgers. | |

**User's choice:** Full schema with explicit N/A.
**Notes:** Uniform schema supports downstream filtering and coverage checks.

| Option | Description | Selected |
|--------|-------------|----------|
| Two-source pattern | `source_path` points to the claim occurrence; `supporting_source_path` or notes point to the planning/evidence source that makes the wording safe. | yes |
| Occurrence path only | `source_path` is only the file containing the sentence. | |
| Supporting source only | `source_path` points only to the planning/evidence source. | |

**User's choice:** Two-source pattern.
**Notes:** This preserves both traceability to the sentence and justification for safe wording.

| Option | Description | Selected |
|--------|-------------|----------|
| Distinguish manual text, generated evidence, and scans | Manual wording uses `not_applicable_manual_text`; generated claims use actual script/command; blockers record scan command. | yes |
| All non-numeric claims use not_applicable | Simpler but loses scan/generation provenance. | |
| All non-numeric claims use scan command | Uniform scan provenance even when a formal script supports the claim. | |

**User's choice:** Distinguish manual text, generated evidence, and scans.
**Notes:** `script_path` and `generation_command` should describe how the row was found or supported.

| Option | Description | Selected |
|--------|-------------|----------|
| Fixed enum | Use a controlled `evidence_role` vocabulary such as positioning, mechanism_scope, primary_behavioral, diagnostic families, limitation, and package_consistency. | yes |
| Free text | Planner writes roles as needed. | |
| Coarse categories | Only primary, diagnostic, limitation, and package. | |

**User's choice:** Fixed enum.
**Notes:** A fixed enum makes Phase 3/4/5 scans and filters much less brittle.

---

## Allowed Sentence Precision

| Option | Description | Selected |
|--------|-------------|----------|
| Directly usable sentence with Phase 3 polish allowed | Phase 2 writes complete safe sentences; Phase 3 may polish style without changing evidence boundaries. | yes |
| Safe wording template only | Phase 2 records components and lets Phase 3 draft. | |
| Boundary rule only | Phase 2 says what is allowed/prohibited without replacement prose. | |

**User's choice:** Directly usable sentence with Phase 3 polish allowed.
**Notes:** This makes the ledger an execution handoff, not just a risk catalog.

| Option | Description | Selected |
|--------|-------------|----------|
| Structured Phase 4 placeholders | Use placeholders such as `[PHASE4_VERIFIED_VALUE]`, `[PHASE4_VERIFIED_CI]`, and `[PHASE4_VERIFIED_TABLE]`. | yes |
| Fully non-numeric wording | Use only directional wording before Phase 4. | |
| Keep old numbers with blocker status | Preserve current numerical sentences and rely on status fields. | |

**User's choice:** Structured Phase 4 placeholders.
**Notes:** The sentence can be complete without locking unverified final values.

| Option | Description | Selected |
|--------|-------------|----------|
| Safe replacement plus action | Unsafe claims get a replacement sentence plus `replace_non_numeric`, `downgrade_to_diagnostic`, `delete`, or similar action. | yes |
| Prohibited sentence only | Do not provide a safe replacement. | |
| Leave blank and mark blocker | Let Phase 3 draft replacements. | |

**User's choice:** Safe replacement plus action.
**Notes:** Unsafe claims should be immediately actionable for Phase 3.

| Option | Description | Selected |
|--------|-------------|----------|
| Exact sentence or prohibited pattern | Store exact current sentence for concrete hits or a prohibited pattern for generic risks. | yes |
| Keywords only | Store short scan terms. | |
| Explanation only | Describe the problem without a sentence or pattern. | |

**User's choice:** Exact sentence or prohibited pattern.
**Notes:** This supports later prohibited-wording scans.

---

## Blocker Table Granularity

| Option | Description | Selected |
|--------|-------------|----------|
| Category rules plus hit list | Include category-level rules and concrete hit rows with location, risk, status, owner phase, and action. | yes |
| Category rules only | Clear principles but less executable. | |
| Hit list only | Strong execution list but weaker reusable rules. | |

**User's choice:** Category rules plus hit list.
**Notes:** The blocker file should work both as a rulebook and as an execution queue.

| Option | Description | Selected |
|--------|-------------|----------|
| Full execution fields | Include `issue_id`, `location`, `matched_text_or_pattern`, `risk_family`, `status`, `evidence_role`, `owner_phase`, `required_action`, `allowed_replacement`, and `verification_check`. | yes |
| Minimal fields | Include only `location`, `risk`, and `action`. | |
| Planner decides by risk class | Field set varies by risk family. | |

**User's choice:** Full execution fields.
**Notes:** The table should support routing, verification, and readiness closeout.

| Option | Description | Selected |
|--------|-------------|----------|
| Gate-based routing | Use the four status values and route owner phase to Phase 3, 4, 5, or future/v2 by gate. | yes |
| Everything goes to Phase 3 | Let later phases re-route. | |
| No owner phase | Record the issue only. | |

**User's choice:** Gate-based routing.
**Notes:** Wording goes to Phase 3, numerical provenance to Phase 4, package/readiness checks to Phase 5, future evidence/model gaps to v2.

| Option | Description | Selected |
|--------|-------------|----------|
| Fixed risk-family scan | Scan Part A/TR-A, policy-first, old values, dominance/outperform, Gamma/Pareto, Beijing validation, MILP/exact/near-optimal, legacy paths, and readiness wording. | yes |
| Only old values and obvious Part A/policy | Faster but less complete. | |
| Planner chooses scan terms | Flexible but less enforceable. | |

**User's choice:** Fixed risk-family scan.
**Notes:** Phase 2 should require a minimum scan family list so later plans do not miss semantic blockers.

## Agent Discretion

No user decisions were delegated to agent discretion.

## Deferred Ideas

None.
