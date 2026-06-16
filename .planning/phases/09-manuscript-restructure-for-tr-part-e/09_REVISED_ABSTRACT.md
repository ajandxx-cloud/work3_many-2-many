# Phase 9 Revised Abstract, Keywords, and Highlights Plan

**Purpose:** Claim-gated front-matter plan for a Transportation Research Part E
submission package. This file is a planning artifact, not final manuscript text.

## Current Abstract Risks

The current abstract states legacy numerical outcomes and policy implications
before the Phase 8 claim gate exists. It describes the old efficiency result,
matched-coverage diagnostic, equity values, and five policy implications as if
they were ready for final front matter. Under the rebuild contract, those items
must be treated as placeholders until formal evidence and the supported-claims
file approve the exact wording.

Specific risks:

- Unsupported numerical values could enter the revised abstract before Phase 8.
- Old language can imply unconditional superiority instead of conditional
  evidence under fair comparison.
- The Beijing-inspired synthetic scenario can be overread as real Beijing
  evidence.
- Algorithm diagnostics can be mistaken for behavioral service-design evidence.
- Elsevier front matter still needs abstract length, highlights, keywords,
  anonymization, and final AI-declaration checks.

## Revised Abstract Skeleton

The final abstract should be no longer than 250 words, factual, standalone, and
free of references or unexplained abbreviations.

### Problem

Meeting-point demand-responsive transit may reduce operating distance, but
evidence can be confounded by passenger response, coverage differences,
inconsistent baselines, and mixed diagnostic/result reporting.

### Approach

We provide an evidence-chain framework: a choice-aware dynamic service-design
simulation framework for bidirectional pickup/dropoff meeting points, paired
with fair comparison families, explicit metric denominators, coverage controls,
and a claim-evidence gate.

### Claim-gated evidence

`[SUPPORTED_CLAIM_FROM_08]` should summarize the strongest approved formal
finding. If Phase 8 approves a quantitative result, use
`[MAIN_EFFECT_SIZE_IF_SUPPORTED]` with the exact comparison condition,
metric denominator, `n_pairs`, and uncertainty summary. If Phase 8 does not
approve a headline numerical claim, this block should state only the supported
directional or exploratory evidence grade.

### Boundary conditions

Close with conditional design guidance and boundaries:
`[BOUNDARY_CONDITIONS_FROM_08]`, including synthetic scenario status,
passenger-choice calibration limits, coverage/rejection context, and any
managerial insight that Phase 8 explicitly supports.

## Claim Placeholders

| Placeholder | Replace only after reading | Required replacement discipline |
|---|---|---|
| `[SUPPORTED_CLAIM_FROM_08]` | `08_SUPPORTED_CLAIMS.md` | Use the exact supported claim or a weaker paraphrase. |
| `[MAIN_EFFECT_SIZE_IF_SUPPORTED]` | `08_CLAIM_EVIDENCE_MATRIX.md` | Include only approved metric, denominator, comparison, and uncertainty. |
| `[BOUNDARY_CONDITIONS_FROM_08]` | `08_SUPPORTED_CLAIMS.md` and `08_UNSUPPORTED_OR_EXPLORATORY_CLAIMS.md` | State limits before implications. |
| `[UNSUPPORTED_ITEMS_TO_REMOVE]` | `08_UNSUPPORTED_OR_EXPLORATORY_CLAIMS.md` | Delete, downgrade, or move to limitations/future work. |

## Forbidden Abstract Language

| Forbidden or risky wording | Replacement direction |
|---|---|
| "always wins" | "under the tested fair-comparison conditions..." |
| "universally improves" | "can improve... when [condition] is satisfied" |
| "first bidirectional meeting-point DRT paper" | "integrated choice-aware dynamic service-design simulation framework" |
| "real Beijing case" | "Beijing-inspired synthetic scenario" |
| "Pareto frontier" for gamma | "post-hoc welfare sensitivity" unless Phase 8 approves more |
| `vkm_per_trip` | `vkm_per_served_trip` or `vkm_per_original_request` |

## Candidate Title Direction

Use a conditional, descriptive title rather than a broad novelty or superiority
claim. Candidate direction:

> Choice-aware dynamic service-design evidence for bidirectional meeting points
> in demand-responsive transit

Title rules:

- Include `choice-aware`, `dynamic service-design`, and `bidirectional meeting
  points` as descriptive framing, not as proof of novelty.
- Avoid broad first/only language.
- Avoid result claims in the title unless Phase 8 approves the exact claim.
- Keep the logistics/service-design focus visible for Transportation Research
  Part E.

## Keyword Plan

Candidate keywords:

- demand-responsive transit
- meeting points
- passenger choice
- dynamic service design
- rolling-horizon dispatch
- fair comparison
- simulation evidence
- service equity

## Highlights Plan

Elsevier highlights should be 3 to 5 bullets, each no more than 85 characters.
Final result highlights require Phase 8 support.

- Evidence-chain framework for choice-aware DRT.
- Fair baselines separate service design from response.
- Claim-gated metrics report coverage and efficiency.
- [requires Phase 8 support] Conditional efficiency result.
- [requires Phase 8 support] Equity and boundary-condition insight.
