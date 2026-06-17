# Claim Ledger

## Purpose

This ledger is the occurrence-level execution artifact for Phase 3 manuscript
edits and Phase 4 numerical provenance. It maps each current or planned
manuscript claim occurrence to a stable claim ID, evidence role, source path,
generation command, metric formula, denominator, allowed replacement sentence,
and prohibited sentence.

This file is not a manuscript rewrite, not a result table, and not a place to
inject final numbers before Phase 4.

## Scope

Full ledger scope is limited to:

- `manuscript/main.tex`
- every current `manuscript/sections/*.tex` file

Package-facing files such as `README.md`, `CLAUDE.md`,
`manuscript/cover_letter.tex`, `manuscript/response_to_reviewers.tex`, and
figure-script comments are routed to `05_BLOCKERS_AND_SAFE_CLAIMS.md` unless
their wording is reused in the manuscript.

Each claim-bearing sentence, clause, bullet, caption-like manuscript reference,
or planned safe replacement receives one row. Related rows share a
`claim_family_id` without merging occurrence-level traceability.

## Ledger Rules

- Use one row per manuscript claim occurrence.
- Use stable IDs such as `C-001` and family IDs such as
  `F-routing-intensity`, `F-coverage-tradeoff`, `F-policy-framing`,
  `F-gamma`, `F-beijing`, `F-milp`, and `F-diagnostic-evidence`.
- Use normalized forward-slash manuscript paths and line ranges in
  `manuscript_location`.
- Use `source_path` under `results/formal/phase06/` for formal numerical
  claims.
- Use `not_applicable_manual_text` for `script_path` and
  `generation_command` on manual positioning, scope, and limitation rows.
- Use `not_applicable` for `metric_formula`, `numerator`, and `denominator`
  on non-numeric rows.
- Keep old or risky numerical values as `current_sentence`, `reported_value`,
  notes, or `prohibited_sentence`; do not place them in final allowed
  replacement text.
- Diagnostic evidence must carry a diagnostic qualifier in `allowed_sentence`.
- Phase 3 may use `allowed_sentence` text as a safe drafting handoff, but may
  not change its evidence boundary.

## Evidence Role Enum

| evidence_role | Meaning | Allowed use | Prohibited use |
|----------------|---------|-------------|----------------|
| `positioning` | TR-E logistics/operations framing and journal-fit text. | Non-numeric manuscript positioning and contribution framing. | Policy-first framing, TR Part A validation, or deployable decision-tool claims. |
| `mechanism_scope` | Scope of the passenger-response-aware simulation mechanism. | Describe binary-logit passenger response as service-design evaluation within the simulation. | Endogenous routing-control, empirically calibrated behavior, or co-optimization claims. |
| `primary_behavioral` | Formal main behavioral evidence. | Conditional efficiency, served-share, acceptance, rejection, and denominator claims after Phase 4 verification. | Universal dominance, real-world validation, or final numbers before Phase 4. |
| `diagnostic_matched_coverage` | Matched-coverage coverage-confounding control. | Diagnostic discussion of served-share matching and coverage confounding. | Primary headline estimate or equal-service dominance proof. |
| `diagnostic_fixed_accepted_set` | Fixed-accepted-set routing decomposition control. | Diagnostic decomposition over fixed accepted sets. | Complete online behavioral benchmark or dynamic routing optimum. |
| `robustness_sensitivity` | Formal robustness and sensitivity diagnostics. | Conditional service-design boundary and sensitivity statements. | Unbounded generalization beyond tested synthetic service designs. |
| `equity_type_heterogeneity` | Passenger-type and burden heterogeneity evidence. | Limited monitoring and heterogeneity implications after Phase 4 checks. | Real population equity conclusions or welfare dominance. |
| `algorithm_diagnostic` | Simplified ex-post algorithm and MILP diagnostics. | Algorithm-scope explanation, fixed-set MILP diagnostics, and limitations. | ALNS near-optimality proof or complete exact dynamic benchmark. |
| `limitation` | Evidence, model, and reproducibility boundaries. | Explicitly state what the current package does not prove. | Convert future/v2 gaps into current manuscript claims. |
| `package_consistency` | Submission/package consistency risk when manuscript text reuses package-facing wording. | Track manuscript-reused package wording in this ledger only when needed. | Full package risk tracking; those risks belong in `05_BLOCKERS_AND_SAFE_CLAIMS.md`. |

## Action Enum

| action | Meaning |
|--------|---------|
| `retain_with_verification` | Retain the claim only after Phase 4 verifies source, denominator, and wording. |
| `replace_non_numeric` | Replace current wording with safe non-numeric TR-E wording in Phase 3. |
| `delete` | Remove the claim because it is unsupported or out of scope. |
| `downgrade_to_diagnostic` | Keep only with explicit diagnostic qualifier and non-headline placement. |
| `move_to_limitation` | Move or recast the claim as a limitation or future-work boundary. |
| `phase4_verify_number` | Preserve the occurrence for Phase 4 numerical provenance before any final value is injected. |

## Phase 4 Placeholder Rules

Use placeholders for all unverified numerical content in `allowed_sentence`.
Phase 2 and Phase 3 must not lock final percentages, improvement values,
confidence intervals, significance language, table numbers, or figure numbers.

Required placeholders:

- `[PHASE4_VERIFIED_VALUE]`
- `[PHASE4_VERIFIED_CI]`
- `[PHASE4_VERIFIED_TABLE]`
- `[PHASE4_VERIFIED_FIGURE]`

## Metric Formula Reference

| metric | metric_formula | numerator | denominator | Source |
|--------|----------------|-----------|-------------|--------|
| `served_share` | `served_share = n_served / n_requests` | `n_served` | `n_requests` | `experiments/formal_validation.py`; `experiments/metrics.py` |
| `vkm_per_original_request` | `vkm_per_original_request = vehicle_km / n_requests` | `vehicle_km` | `n_requests` | `experiments/formal_validation.py`; `experiments/metrics.py` |
| `vkm_per_served_trip` | `vkm_per_served_trip = vehicle_km / n_served` | `vehicle_km` | `n_served` | `experiments/formal_validation.py`; `experiments/metrics.py` |
| `behavioral_acceptance_rate` | `behavioral_acceptance_rate = 1.0 - choice_rejection_rate` | `1.0 - choice_rejection_rate` | `not_applicable` | `experiments/formal_validation.py`; `experiments/metrics.py` |
| `choice_rejection_rate` | `choice_rejection_rate = choice_rejected / n_requests` | `choice_rejected` | `n_requests` | `experiments/metrics.py` |
| `feasibility_rejection_rate` | `feasibility_rejection_rate = feasibility_rejected / n_requests` | `feasibility_rejected` | `n_requests` | `experiments/metrics.py` |
| `rejection_partition` | `rejection_partition = served_share + choice_rejection_rate + feasibility_rejection_rate` | `served_share + choice_rejection_rate + feasibility_rejection_rate` | `1.0` | `experiments/formal_validation.py` |
| `non_numeric_claim` | `not_applicable` | `not_applicable` | `not_applicable` | Manual positioning, mechanism scope, or limitation text. |

## Manuscript Coverage Inventory

| reviewed_path | reviewed_line_range | claim_ids_or_no_claim_note |
|---------------|---------------------|----------------------------|
| `to_be_populated_task_2` | `to_be_populated_task_2` | `to_be_populated_task_2` |

## Claim Ledger

| claim_id | claim_family_id | manuscript_location | current_sentence | claim_type | comparison | metric | reported_value | source_path | supporting_source_path | script_path | generation_command | metric_formula | numerator | denominator | evidence_role | phase4_status | action | allowed_sentence | prohibited_sentence | notes |
|----------|-----------------|---------------------|------------------|------------|------------|--------|----------------|-------------|------------------------|-------------|--------------------|----------------|-----------|-------------|---------------|---------------|--------|------------------|---------------------|-------|
