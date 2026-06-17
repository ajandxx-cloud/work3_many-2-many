# Phase 3: TR-E Manuscript Repositioning - Discussion Log

> **Audit trail only.** Do not use as input to planning, research, or execution agents.
> Decisions are captured in `03-CONTEXT.md`; this log preserves the alternatives considered.

**Date:** 2026-06-17T20:48:36.4109432+08:00
**Phase:** 3-TR-E Manuscript Repositioning
**Areas discussed:** Title/abstract/introduction frame, experiments evidence layering, managerial and operational implications, boundary wording for Gamma/Beijing/MILP/equity

---

## Title, Abstract, And Introduction Contribution Frame

### Manuscript Primary Identity

| Option | Description | Selected |
|--------|-------------|----------|
| Service-design evidence first | Frame as TR-E logistics/operations evidence for DRT meeting-point service design. | Yes |
| Simulation framework first | Emphasize passenger-response-aware simulation framework. | |
| Operations-management problem first | Emphasize operator-facing consolidation and fleet-operation problem. | |
| Hybrid | Framework title, service-design abstract/introduction. | |

**User's choice:** Service-design evidence first.
**Notes:** This locks the paper's primary identity as operational service-design evidence rather than policy validation or method supremacy.

### Core Title/Abstract Noun Phrase

| Option | Description | Selected |
|--------|-------------|----------|
| Passenger-response-aware bidirectional meeting-point consolidation | Strongest mechanism-plus-service phrase. | |
| Passenger-response-aware simulation framework | More method-forward. | |
| Bidirectional meeting-point DRT service design | More operational and TR-E-facing. | Yes |
| Minimal safe revision of existing title | Smallest change from current title. | |

**User's choice:** Bidirectional meeting-point DRT service design.
**Notes:** Passenger response remains important, but as a mechanism in subtitle, abstract, and contribution wording.

### Old Numbers In Abstract And Introduction

| Option | Description | Selected |
|--------|-------------|----------|
| All non-numeric conditional wording | Remove old final values and use conditional prose. | Yes |
| Use Phase 4 placeholders | Preserve value slots with placeholders. | |
| Non-numeric abstract, placeholders in introduction | Hybrid strategy. | |

**User's choice:** All non-numeric conditional wording.
**Notes:** Phase 3 should not lock final values or use placeholders in abstract/introduction by default.

### Introduction Contribution Structure

| Option | Description | Selected |
|--------|-------------|----------|
| Three contribution paragraphs | Service design, passenger-response-aware simulation, evidence/trade-offs. | Yes |
| Concise bullet contribution list | Keep current scannable list style. | |
| Short paragraph plus bullets | Hybrid paragraph and list. | |

**User's choice:** Three contribution paragraphs.
**Notes:** Replaces the current engineering-style contribution list.

---

## Experiments Evidence-Layering Structure

### Main Text Versus Diagnostics

| Option | Description | Selected |
|--------|-------------|----------|
| Primary evidence first, diagnostics after | Main behavioral results followed by diagnostic sections. | |
| Main evidence plus nearby diagnostic evidence by topic | Keep diagnostics close to relevant main results. | |
| Core experiments in main text, diagnostics in appendix/supplement | Keep main text focused and demote diagnostics. | Yes |

**User's choice:** Core experiments in main text, diagnostics in appendix/supplement.
**Notes:** This intentionally separates headline evidence from diagnostic evidence.

### Diagnostic Trace In Main Text

| Option | Description | Selected |
|--------|-------------|----------|
| Diagnostic roadmap paragraph only | One paragraph naming diagnostic roles; no values. | Yes |
| Short diagnostic summary subsection | Main-text subsection summarizing diagnostics. | |
| Appendix pointers after each main result | Cross-reference diagnostics near related results. | |

**User's choice:** Diagnostic roadmap paragraph only.
**Notes:** The main text should not include diagnostic numerical values.

### Main Experimental Metrics

| Option | Description | Selected |
|--------|-------------|----------|
| Routing intensity plus served share plus rejection decomposition | Emphasize vkm metrics, served share, choice rejection, and feasibility rejection. | Yes |
| Routing intensity plus served share plus passenger-type heterogeneity | Keep passenger-type results as a core finding. | |
| Routing intensity plus operating conditions | Emphasize service-design conditions. | |

**User's choice:** Routing intensity plus served share plus rejection decomposition.
**Notes:** Passenger type, Gamma, MILP, matched coverage, and robustness should not be main-text headline results.

### Old Tables In Experiments

| Option | Description | Selected |
|--------|-------------|----------|
| Keep table positions with non-numeric placeholders | Preserve structure for Phase 4 fill-in. | |
| Delete/comment old diagnostic tables and keep only core main table | Remove old diagnostic/3-seed tables from main text. | Yes |
| Leave table environments untouched and revise surrounding prose | Minimal structural change. | |

**User's choice:** Delete/comment old diagnostic tables and keep only core main table.
**Notes:** Diagnostic tables may move to appendix/supplement or be decided in Phase 4.

---

## Managerial And Operational Implications Section

### Section Shape

| Option | Description | Selected |
|--------|-------------|----------|
| Managerial and Operational Implications with 4-5 operational themes | Retain useful structure but remove policy-recommendation framing. | Yes |
| Shorter Operational Design Implications prose section | More compact journal prose. | |
| Compress most implications into conclusion/limitations | Minimal separate discussion. | |

**User's choice:** Managerial and Operational Implications with 4-5 operational themes.
**Notes:** The current R1-R5 recommendation framing should be downgraded.

### Theme Organization

| Option | Description | Selected |
|--------|-------------|----------|
| By service-design decisions | Walking tolerance, fleet deployment, consolidation trade-off, passenger-segment monitoring, validation limits. | Yes |
| By evidence role | Main evidence, robustness, equity/type, diagnostics, limitations. | |
| By operator questions | When to deploy, whom it burdens, what to monitor, what not to claim. | |

**User's choice:** By service-design decisions.
**Notes:** This preserves a TR-E operations/service-design orientation.

### Chinese/Suburban Context

| Option | Description | Selected |
|--------|-------------|----------|
| Weakly retain as tested synthetic Chinese-suburban-inspired conditions | Keep context but qualify evidence scope. | Yes |
| Mostly remove Chinese city context | Safer but less connected to scenario motivation. | |
| Keep Chinese context as motivation, not evidence scope | Hybrid strategy. | |

**User's choice:** Weakly retain as tested synthetic Chinese-suburban-inspired conditions.
**Notes:** The section must not become real-world Chinese city validation or deployment guidance.

### Prescriptive Recommendation Sentences

| Option | Description | Selected |
|--------|-------------|----------|
| Convert to design considerations | Keep operator-facing usefulness with bounded wording. | Yes |
| Keep only evidence explanation, no should sentences | Most conservative. | |
| Retain limited should sentences with strong qualifiers | More advisory but higher risk. | |

**User's choice:** Convert to design considerations.
**Notes:** Downgrade policy-prescriptive language.

---

## Boundary Wording For Gamma, Beijing, MILP, And Equity

### Gamma/Pareto

| Option | Description | Selected |
|--------|-------------|----------|
| Appendix/supplement post-hoc sensitivity accounting | Main text only states Gamma does not affect routing, offers, or acceptance. | Yes |
| Keep a short main-text section with mandatory post-hoc qualifiers | More information, higher risk. | |
| Only discuss as limitation/future work | Most conservative. | |

**User's choice:** Appendix/supplement post-hoc sensitivity accounting.
**Notes:** Avoid endogenous-control or policy-control readings.

### Beijing-Inspired Scenario

| Option | Description | Selected |
|--------|-------------|----------|
| Robustness/sensitivity setting in appendix/supplement or weak main text | Synthetic grid only, not real-world validation. | Yes |
| Keep a main-text section with synthetic qualifiers | More prominent but riskier. | |
| Only describe in experimental design | Minimal result emphasis. | |

**User's choice:** Robustness/sensitivity setting in appendix/supplement or weak main text.
**Notes:** Use `Beijing-inspired synthetic grid` or `semi-realistic synthetic grid`.

### MILP/ALNS Gap

| Option | Description | Selected |
|--------|-------------|----------|
| Algorithm diagnostic appendix | Main text states simplified ex-post diagnostic over fixed accepted sets. | Yes |
| Keep MILP formulation in algorithm section but remove experiments gap table | Retain formulation without result table. | |
| Keep main-text diagnostic gap subsection | Most complete, highest risk. | |

**User's choice:** Algorithm diagnostic appendix.
**Notes:** Do not present gap values or tables as ALNS near-optimality evidence.

### Equity / Passenger-Type Heterogeneity

| Option | Description | Selected |
|--------|-------------|----------|
| Passenger-segment monitoring implication | Use validated simulated type diagnostics only as monitoring implications. | Yes |
| Short main-text heterogeneity finding | Richer but higher evidence-risk. | |
| Limitation only | Most conservative. | |

**User's choice:** Passenger-segment monitoring implication.
**Notes:** User asked whether the experiment considered this; local evidence confirms simulated passenger types and validated `equity_type_outcomes`, but these are simulation-range constructs and not real population equity validation.

---

## Agent Discretion

- Exact prose, section sequencing, and LaTeX mechanics are left to downstream planning and implementation.
- The appendix/supplement mechanics for moved diagnostics may be decided downstream, provided main-text diagnostic demotion is preserved.

## Deferred Ideas

None.
