# Phase 6: Formal Synthetic Experiments - Discussion Log

> **Audit trail only.** Do not use as input to planning, research, or execution agents.
> Decisions are captured in CONTEXT.md; this log preserves the alternatives considered.

**Date:** 2026-06-15T23:15:28+08:00
**Phase:** 6-Formal Synthetic Experiments
**Areas discussed:** Main Evidence Experiment Matrix, Supplementary Experiment Layering, Failure Timeout and Rerun Rules, Statistical Reporting and Paper Table Scope

---

## Main Evidence Experiment Matrix

### Formal seed priority

| Option | Description | Selected |
|--------|-------------|----------|
| 20 seeds minimum | Prioritize paired completion; extend to 30 only if runtime permits. | Yes |
| Direct 30 seeds | Stronger statistics but higher runtime and failure pressure. | |
| Two-stage 20 to 30 | Lock 20 first, then use 21-30 as a predeclared expansion batch. | |

**User's choice:** 20 seeds minimum.
**Notes:** Formal success is anchored on complete 20 paired seeds.

### Main methods

| Option | Description | Selected |
|--------|-------------|----------|
| Four behavioral methods only | Keep the main evidence family clean. | Yes |
| Four behavioral methods plus no-RH diagnostic | Adds rolling-horizon contribution context but risks mixing evidence families. | |
| Four behavioral methods plus greedy/ALNS/MILP diagnostics | Most complete but too broad for main evidence. | |

**User's choice:** Four behavioral methods only.
**Notes:** Diagnostics remain outside the main table.

### Request scales

| Option | Description | Selected |
|--------|-------------|----------|
| Existing 100/200/300/500 scales | Align with `experiments/config.py` and show scale trends. | Yes |
| Only 200/500 | More focused and runtime-stable but narrower. | |
| Pilot 20 plus 100/200/300/500 | Adds continuity but risks treating pilot scale as formal evidence. | |

**User's choice:** Existing 100/200/300/500 scales.
**Notes:** Scale 20 remains Phase 5 readiness evidence only.

### 30-seed extension rule

| Option | Description | Selected |
|--------|-------------|----------|
| Complete 30 required to upgrade | Use 30 only if seeds 21-30 all complete under the same rules. | Yes |
| 20 always main, 21-30 appendix | Conservative but may waste extra statistical value. | |
| Report however many complete | Informative but weakens paired-design credibility. | |

**User's choice:** Complete 30 required to upgrade.
**Notes:** Incomplete extension leaves main evidence at 20 paired seeds.

---

## Supplementary Experiment Layering

### Package structure

| Option | Description | Selected |
|--------|-------------|----------|
| Main evidence plus independent supplementary packages | Separate package gates and reports prevent evidence mixing. | Yes |
| One comprehensive supplementary matrix | Easier central management but much larger failure surface. | |
| Reviewer-critical packages only | More stable but narrower evidence coverage. | |

**User's choice:** Main evidence plus independent supplementary packages.
**Notes:** Main evidence supports core efficiency; supplementary packages support robustness or diagnostics.

### Package completion scope

| Option | Description | Selected |
|--------|-------------|----------|
| Complete all roadmap supplementary packages | Run matched coverage, fixed accepted-set, utility sensitivity, density, fleet/demand, rolling-horizon, equity, and ALNS/MILP. | Yes |
| Reviewer-critical packages only | Prioritize matched coverage, utility sensitivity, fixed accepted-set, and ALNS/MILP. | |
| Layered hard gates | Require only selected critical packages; attempt others if feasible. | |

**User's choice:** Complete all roadmap supplementary packages.
**Notes:** Packages stay independent; package issues do not automatically contaminate main evidence.

### Paper placement

| Option | Description | Selected |
|--------|-------------|----------|
| Main-text summary plus appendix detail | Keep the story focused while preserving complete detail. | Yes |
| Full main-text presentation | Very complete but risks overwhelming the paper. | |
| Appendix only | Clean main text but may look like hidden robustness evidence. | |

**User's choice:** Main-text summary plus appendix detail.
**Notes:** Full tables, failure rows, diagnostic plots, and parameters go to appendix/supplement outputs.

### Conflict handling

| Option | Description | Selected |
|--------|-------------|----------|
| Downgrade or qualify claim | Preserve evidence but narrow the claim. | |
| Appendix-only effect | Keep main claim unchanged; risky for reviewer trust. | |
| Critical conflicts block Phase 6 | Explain, rerun/correct, or downgrade before Phase 8. | Yes |

**User's choice:** Critical conflicts block Phase 6.
**Notes:** A critical supplementary conflict cannot be hidden in the appendix.

---

## Failure Timeout and Rerun Rules

### Main-run failure handling

| Option | Description | Selected |
|--------|-------------|----------|
| Keep failure row and rerun same seed | Transparent and preserves paired design. | Yes |
| Keep failure row only | Transparent but leaves main matrix incomplete. | |
| Replacement seed | Fills sample count but weakens predeclared paired design. | |

**User's choice:** Keep failure row and rerun same seed.
**Notes:** No silent deletion and no replacement seeds.

### Main-evidence blocker rule

| Option | Description | Selected |
|--------|-------------|----------|
| Any unclosed main-matrix failure blocks | Complete matrix required for main evidence passage. | Yes |
| Allow small failure count with CI | Looser but weakens paired comparison. | |
| Pass by scale | Useful for exploratory reporting, not headline evidence. | |

**User's choice:** Any unclosed main-matrix failure blocks.
**Notes:** Applies to four methods across 100/200/300/500 by 20 paired seeds.

### Supplementary failure handling

| Option | Description | Selected |
|--------|-------------|----------|
| Independent package gates | Failed packages cannot support their robustness claim; critical failures can block. | Yes |
| Any supplementary failure blocks Phase 6 | Strict but overweights non-critical diagnostics. | |
| Supplementary failures never block | Easier but inconsistent with critical-conflict rule. | |

**User's choice:** Independent package gates.
**Notes:** Non-critical failures are limitations; critical failures can block Phase 6.

### Rerun ledger detail

| Option | Description | Selected |
|--------|-------------|----------|
| Run-level plus reason-level ledger | Preserve run/config/seed/scale/method/status/error/reason/fix/rerun result. | Yes |
| Final CSV plus simple note | Lighter but weak for review traceability. | |
| Full logs without ledger | Rich raw logs but hard for claim gate and synthesis. | |

**User's choice:** Run-level plus reason-level ledger.
**Notes:** Ledger summary belongs in `06_FORMAL_SYNTHETIC_RESULTS.md`.

---

## Statistical Reporting and Paper Table Scope

### Main comparison

| Option | Description | Selected |
|--------|-------------|----------|
| Paired differences first | Compare methods within the same seed and scale. | Yes |
| Absolute means first | More intuitive but uses paired design less directly. | |
| Rank/win-rate first | Easy to read but too reductive for main evidence. | |

**User's choice:** Paired differences first.
**Notes:** Report means, confidence intervals, direction, and matrix completeness.

### Core metrics

| Option | Description | Selected |
|--------|-------------|----------|
| Efficiency plus coverage quartet | Report total vkm, vkm per served trip, vkm per original request, and served share together. | Yes |
| Efficiency triplet | Omits total vehicle-km. | |
| Main-text short table plus appendix full metrics | Saves space but risks coverage confounding. | |

**User's choice:** Efficiency plus coverage quartet.
**Notes:** Coverage cannot be hidden in the appendix.

### Uncertainty summary

| Option | Description | Selected |
|--------|-------------|----------|
| Paired bootstrap CI first | 95% CI on paired seed differences; optional tests in appendix. | Yes |
| Paired t-test first | Familiar but more assumption-sensitive with 20 seeds. | |
| Means and standard deviations only | Too weak for formal evidence. | |

**User's choice:** Paired bootstrap CI first.
**Notes:** P-values should not drive the main story.

### Claim-gate eligibility

| Option | Description | Selected |
|--------|-------------|----------|
| Complete main matrix plus no critical supplementary conflict | Only complete, reproducible evidence reaches Phase 8. | Yes |
| Main matrix complete only | Faster but defers conflicts too late. | |
| Directionally consistent only | Too weak for reviewer-resistant evidence. | |

**User's choice:** Complete main matrix plus no critical supplementary conflict.
**Notes:** Quartet metrics and paired confidence intervals must be reproducible.

---

## the agent's Discretion

- Exact formal seed IDs and extension seed IDs.
- Exact helper/module names and formal output directory names.
- Bootstrap implementation details, timeout thresholds, ledger file format, and plot filenames.
- Exact wording of package gate summaries, as long as it preserves the locked evidence boundaries.

## Deferred Ideas

None. Discussion stayed within Phase 6 scope.
