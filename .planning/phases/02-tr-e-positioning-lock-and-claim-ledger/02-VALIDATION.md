# Phase 2 Planning Validation

**Phase:** 02 - TR-E Positioning Lock and Claim Ledger
**Purpose:** Validate that Phase 2 plans fully specify the planning artifacts needed before manuscript prose, numerical values, tables, or figures are edited.
**Scope:** Planning artifact validation only. This file does not validate executed manuscript edits and does not authorize changes outside `.planning/`.

## Validation Targets

| Target | Required artifact | Primary requirement |
|--------|-------------------|---------------------|
| Positioning lock | `.planning/milestones/tr_e_claim_ready/02_TR_E_POSITIONING_LOCK.md` | CLAI-01 |
| Claim ledger | `.planning/milestones/tr_e_claim_ready/03_CLAIM_LEDGER.md` | CLAI-02, CLAI-03, CLAI-04 |
| Blockers and safe claims | `.planning/milestones/tr_e_claim_ready/05_BLOCKERS_AND_SAFE_CLAIMS.md` | PLAN-04, CLAI-04 |

## Planning Gates

| Gate ID | Gate | Required checks | Automated command pattern | Pass condition |
|---------|------|-----------------|---------------------------|----------------|
| V-02-01 | Positioning lock schema | Required sections, allowed TR-E framing, prohibited framing, journal-fit rationale, safe core sentence, and readiness label boundary. | `rg -n "Allowed TR-E Framing|Prohibited Framing|Core Contribution Lock|Journal-Fit Rationale|Evidence Role Boundaries|Readiness Label Boundary" .planning/milestones/tr_e_claim_ready/02_TR_E_POSITIONING_LOCK.md` | All required sections and safe labels are present. |
| V-02-02 | Evidence-role separation | Primary behavioral evidence, matched-coverage diagnostics, fixed-accepted-set diagnostics, robustness/sensitivity, equity/type heterogeneity, algorithm diagnostics, and limitations are distinct. | `rg -n "primary_behavioral|diagnostic_matched_coverage|diagnostic_fixed_accepted_set|robustness_sensitivity|equity_type_heterogeneity|algorithm_diagnostic|limitation" .planning/milestones/tr_e_claim_ready/02_TR_E_POSITIONING_LOCK.md .planning/milestones/tr_e_claim_ready/03_CLAIM_LEDGER.md .planning/milestones/tr_e_claim_ready/05_BLOCKERS_AND_SAFE_CLAIMS.md` | Diagnostic and limitation roles are never promoted to `primary_behavioral`. |
| V-02-03 | Claim ledger mandatory schema | Ledger includes `source_path`, `script_path`, `generation_command`, `metric_formula`, `numerator`, `denominator`, `evidence_role`, `allowed_sentence`, and `prohibited_sentence`. | `$content = Get-Content -Raw ".planning\milestones\tr_e_claim_ready\03_CLAIM_LEDGER.md"; $required = @("source_path","script_path","generation_command","metric_formula","numerator","denominator","evidence_role","allowed_sentence","prohibited_sentence"); $missing = $required | Where-Object { $content -notmatch "\|\s*$($_)\s*\|" }; if ($missing) { throw "Missing ledger columns: $($missing -join ', ')" }` | No mandatory columns are missing. |
| V-02-04 | Full manuscript coverage inventory | Ledger has one coverage inventory row for `manuscript/main.tex` and every current `manuscript/sections/*.tex`, with reviewed line ranges and claim IDs or an explicit no-claim note. | `$ledger = Get-Content -Raw ".planning\milestones\tr_e_claim_ready\03_CLAIM_LEDGER.md"; $targets = @("manuscript/main.tex") + (Get-ChildItem manuscript\sections\*.tex | Sort-Object Name | ForEach-Object { "manuscript/sections/$($_.Name)" }); $missing = $targets | Where-Object { $ledger -notmatch [regex]::Escape($_) }; if ($missing) { throw "Coverage inventory missing target files: $($missing -join '; ')" }; rg -n "reviewed_path|reviewed_line_range|claim_ids_or_no_claim_note|no_claims_after_review" .planning\milestones\tr_e_claim_ready\03_CLAIM_LEDGER.md` | Every target manuscript file is represented; no target file is omitted because regex scans returned no hits. |
| V-02-05 | Formal evidence provenance | Formal claim rows cite `results/formal/phase06/` and use script, command, formula, numerator, and denominator fields. | `rg -n "results/formal/phase06/|experiments/formal_statistics.py|experiments/formal_validation.py|served_share = n_served / n_requests|vkm_per_served_trip = vehicle_km / n_served" .planning/milestones/tr_e_claim_ready/03_CLAIM_LEDGER.md` | Formal evidence is canonical and denominator fields are explicit. |
| V-02-06 | Blockers and safe-claims schema | Required statuses, risk families, owner phases, and verification checks are present. | `rg -n "safe_with_qualifier|downgrade_required|blocker|old_numbers|part_a_tr_a|policy_first|dominance_outperform|gamma_pareto|beijing_validation|milp_exactness|legacy_result_paths|premature_readiness|diagnostic_promotion|package_consistency" .planning/milestones/tr_e_claim_ready/05_BLOCKERS_AND_SAFE_CLAIMS.md` | Status and risk-family routing are explicit. |
| V-02-07 | Prohibited wording controls | Old numbers, policy-first framing, dominance, real-world Beijing validation, endogenous Gamma/Pareto, MILP exactness, legacy paths, and premature readiness are scan-backed blockers or downgraded risks. | `rg -n "18\.3%|29\.1%|35\.0%|0\.1216|TR-E submission-ready|post-hoc welfare or sensitivity accounting|Beijing-inspired synthetic grid|simplified ex-post diagnostic over fixed accepted sets" .planning/milestones/tr_e_claim_ready/05_BLOCKERS_AND_SAFE_CLAIMS.md` | Unsafe wording families have owner-phase routing and allowed replacements. |
| V-02-08 | Phase 4 numeric deferral | Allowed sentences use non-numeric wording or Phase 4 placeholders for unverified values. | `rg -n "\[PHASE4_VERIFIED_VALUE\]|\[PHASE4_VERIFIED_CI\]|\[PHASE4_VERIFIED_TABLE\]|\[PHASE4_VERIFIED_FIGURE\]|phase4_verify_number" .planning/milestones/tr_e_claim_ready/03_CLAIM_LEDGER.md .planning/milestones/tr_e_claim_ready/05_BLOCKERS_AND_SAFE_CLAIMS.md` | Final percentages, CIs, significance language, table numbers, and figure numbers remain deferred to Phase 4. |
| V-02-09 | Phase 2 scope boundary | Execution of Phase 2 plans does not edit manuscript, results, source, experiment, analysis, README, CLAUDE, or dependency files. | `git diff --name-only -- manuscript results src experiments analysis README.md CLAUDE.md pyproject.toml` | Command prints no paths after Phase 2 execution. |

## Nyquist Coverage Rules

- `02_TR_E_POSITIONING_LOCK.md` must be validated for allowed framing, prohibited framing, evidence-role boundaries, and readiness-label boundaries before Phase 3 prose edits.
- `03_CLAIM_LEDGER.md` must validate both schema and coverage. Regex hits are seed data only; every target manuscript file must have reviewed line ranges and claim IDs or `no_claims_after_review`.
- `05_BLOCKERS_AND_SAFE_CLAIMS.md` must validate both rule families and concrete scan-backed rows so Phase 3, Phase 4, and Phase 5 can route work without reinterpretation.
- Phase 2 must not inject final numerical values. Any allowed sentence with unverified numerical content must use Phase 4 placeholders.
- Formal claims must trace to `results/formal/phase06/`; root legacy CSVs, smoke outputs, archive outputs, and ad hoc outputs are non-canonical by default.

## Failure Routing

| Failure | Route |
|---------|-------|
| Missing positioning-lock sections or unsafe framing | Revise `02-01-PLAN.md` or rerun plan checking before executing Phase 3. |
| Missing ledger schema columns | Revise `02-02-PLAN.md`; execution cannot proceed to Phase 3/4 handoff. |
| Missing target manuscript file in coverage inventory | Revise `02-02-PLAN.md`; this is a coverage blocker, not a discretionary omission. |
| Diagnostic evidence promoted as headline evidence | Revise `02-01-PLAN.md`, `02-02-PLAN.md`, or `02-03-PLAN.md` depending on artifact location. |
| Old numbers or prohibited wording lack owner-phase routing | Revise `02-03-PLAN.md`; do not shift this to manuscript execution. |
| Phase 2 execution modifies non-planning files | Stop execution and restore scope before proceeding. |

## Completion Standard

Phase 2 planning is valid when the three PLAN files instruct executors to create the three target artifacts, the research open questions are explicitly resolved, this validation file exists, and the claim-ledger plan requires full manuscript coverage inventory for `manuscript/main.tex` plus all `manuscript/sections/*.tex`.
