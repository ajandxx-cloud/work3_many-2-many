# Phase 9 TR-E Manuscript Structure

**Purpose:** Source-of-truth manuscript architecture for restructuring the
current draft into a Transportation Research Part E evidence-chain manuscript.

## Current Manuscript Diagnosis

The current manuscript is organized around a method-and-policy story: the master
file targets Transportation Research Part A, then proceeds from introduction and
literature to separate model, algorithm, experiments, policy, and conclusion
sections. That order keeps useful technical material, but it lets old numerical
claims, diagnostic results, and policy-style language appear before the rebuilt
claim gate has approved them.

Primary diagnosis:

- The dominant story is still "the method wins" rather than evidence-chain
  reconstruction.
- `manuscript/main.tex` currently targets Transportation Research Part A and
  must be updated later if the paper is finalized for Transportation Research
  Part E.
- The current experiment section mixes behavioral comparisons, matched-coverage
  diagnostics, MILP/ALNS diagnostics, Beijing-inspired synthetic results,
  sensitivity, equity, gamma/welfare, and weight sensitivity.
- The current policy section should become `Managerial Insights and Boundary
  Conditions`, with limitations stated before applied implications.
- The current Beijing/city language must remain `Beijing-inspired synthetic
  scenario` unless later case-study evidence supports stronger wording.

## TR-E Evidence-Chain Architecture

The target manuscript structure should make the evidence chain visible before
the reader reaches any result or managerial implication:

1. **Introduction** - evidence gap, research questions, contribution order, and
   claim discipline.
2. **Literature and Positioning** - prior DARP, meeting-point, ridepooling,
   passenger-choice, and rolling-horizon work, with no broad first/only claims.
3. **Framework and Solution Approach** - choice-aware service-design framework,
   passenger response, route-then-sample operation, rolling-horizon ALNS, and
   clearly labeled diagnostics.
4. **Experimental Design and Evidence Families** - service-design variants,
   response assumptions, metrics, paired design, and evidence-family roles.
5. **Formal Main Evidence** - claim-gated behavioral comparisons only.
6. **Robustness, Equity, and Diagnostic Evidence** - matched coverage, fixed
   accepted-set controls, utility sensitivity, equity summaries, and scoped
   algorithm diagnostics.
7. **Limitations and Boundary Conditions** - synthetic-data, calibration,
   case-study, algorithm-diagnostic, and claim-gate limits before implications.
8. **Managerial Insights and Boundary Conditions** - conditional insights, not
   universal city-policy prescriptions or parameter rules.
9. **Conclusion** - evidence-graded takeaways, unresolved limits, and future
   work.

## Old-to-New Section Map

| Current source | Current role | Target section role |
|---|---|---|
| `manuscript/main.tex` | Journal target, title, front matter, include order, appendix, bibliography | Update target-journal metadata from Transportation Research Part A to Transportation Research Part E during later manuscript-edit execution; revise include order to match the TR-E evidence-chain architecture. |
| `manuscript/sections/abstract.tex` | Old abstract, keywords, legacy numerical claims | Rebuild via `Introduction` framing plus claim-gated front matter; final wording waits for Phase 8 supported claims. |
| `manuscript/sections/intro.tex` | Motivation, broad gap, contribution list, organization | `Introduction`, with evidence-confounding problem first and conditional research questions before claims. |
| `manuscript/sections/literature.tex` | DARP, meeting points, passenger choice, dynamic scheduling, positioning | `Literature and Positioning`, with precise overlap language and no unverified first/only statements. |
| `manuscript/sections/model.tex` | Problem formulation, passenger choice, three-layer model | `Framework and Solution Approach`, especially framework, utility, response, feasibility, and model architecture material. |
| `manuscript/sections/algorithm.tex` | MILP diagnostic, rolling-horizon ALNS, complexity | `Framework and Solution Approach` for operational mechanism; diagnostic solver details may be scoped or moved to appendix/supplement. |
| `manuscript/sections/experiments.tex` | Mixed setup, main results, diagnostics, case, sensitivity, equity, welfare, weight sensitivity | Split across `Experimental Design and Evidence Families`, `Formal Main Evidence`, and `Robustness, Equity, and Diagnostic Evidence`. |
| `manuscript/sections/policy.tex` | R1-R5 policy recommendations, VOT interpretation, deployment map | `Limitations and Boundary Conditions` plus `Managerial Insights and Boundary Conditions`, using conditional insight templates. |
| `manuscript/sections/conclusion.tex` | Old result recap, contributions, policy implications, limitations | `Conclusion`, with Phase 8-supported claims only and unsupported/exploratory items moved to limitations or future work. |

## Phase 8 Blocking Inputs

Final manuscript claim wording is blocked until these Phase 8 artifacts exist
and have been read:

- `.planning/phases/08-evidence-synthesis-and-claim-gate/08_CLAIM_EVIDENCE_MATRIX.md`
- `.planning/phases/08-evidence-synthesis-and-claim-gate/08_SUPPORTED_CLAIMS.md`
- `.planning/phases/08-evidence-synthesis-and-claim-gate/08_UNSUPPORTED_OR_EXPLORATORY_CLAIMS.md`

Because those inputs are absent in this workspace, this Phase 9 artifact may
define structure, templates, and placeholders, but it must not lock final
claim wording or final numerical effect statements.

### Claim Placeholder Policy

The following manuscript components must remain placeholders until all three
Phase 8 files exist and are read:

- Abstract result and contribution wording.
- Introduction contribution wording and any result-preview sentence.
- Table captions, including any statement about direction, magnitude,
  confidence interval, robustness, or equity trade-off.
- Conclusion claims and final takeaways.
- Managerial insights, including R1-R5 rewrites and any applied guidance.

Allowed placeholder forms include `[SUPPORTED_CLAIM_FROM_08]`,
`[MAIN_EFFECT_SIZE_IF_SUPPORTED]`, `[ROBUSTNESS_STATUS_FROM_08]`, and
`[MANAGERIAL_INSIGHT_IF_SUPPORTED]`. Unsupported or unresolved Phase 8 claims
must be removed, downgraded, or moved to limitations/future work rather than
smuggled into manuscript prose.

## Evidence Family Placement Rules

| Evidence family | Manuscript placement | Claim boundary |
|---|---|---|
| Behavioral Main Comparison | `Formal Main Evidence` | May support main conditional service-design claims only after Phase 6 formal paired evidence and Phase 8 claim grading. Must report coverage, acceptance, rejection, and operating efficiency together. |
| Core Supplementary Controls | `Robustness, Equity, and Diagnostic Evidence` | Matched coverage and fixed accepted-set controls support interpretation. They do not replace unconstrained behavioral evidence or create standalone superiority claims. |
| Deterministic Diagnostics | Appendix/supplement or short scoped diagnostic text | deterministic diagnostics cannot support headline behavioral claims because they do not represent passenger response or natural served share. |
| Algorithm Diagnostics | Appendix/supplement by default; limited main-text summary only if Phase 8 approves | ALNS, greedy, no-rolling-horizon, and MILP/static diagnostics support algorithm credibility, not behavioral service-design superiority. |

Paper-facing method labels must use the Phase 2/6 conceptual vocabulary:
`DoorToDoor + Choice`, `SingleSidedPickup + Choice`,
`SingleSidedDropoff + Choice`, and
`BidirectionalMP + Choice + RollingHorizon/ALNS`. Legacy labels such as
`FullModel` belong only in provenance or code-mapping notes.

## Direct LaTeX Edit Boundary

This phase creates planning Markdown outputs first. Later direct edits to
`manuscript/sections/*.tex`, `manuscript/main.tex`, captions, tables, or
figures must either:

1. cite `.planning/phases/08-evidence-synthesis-and-claim-gate/08_SUPPORTED_CLAIMS.md`
   for the exact claim being written; or
2. remain placeholder/comment-only text that explicitly waits for Phase 8.

No direct LaTeX edit may introduce final effect sizes, superiority language,
real-Beijing claims, policy prescriptions, or `vkm_per_trip` vocabulary unless
the relevant upstream evidence and Phase 8 claim status authorize the exact
wording.
