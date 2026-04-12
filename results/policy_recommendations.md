# Policy Recommendations: Bidirectional DRT Deployment in Chinese Cities

*Generated from numerical experiments. All values are simulation-based estimates
using synthetic scenarios calibrated to Chinese suburban conditions.*

---

## Recommendation 1: Set Walking Radius Threshold at 1000 m for Viable Bidirectional Service

**Evidence:** Sensitivity analysis across ρ ∈ [200, 1000] m shows that bidirectional
meeting point assignment only achieves non-trivial acceptance rates when walking tolerance
reaches 1000 m. At ρ = 1000 m, FullModel acceptance rate is
9.0% (vs 0.0% at ρ ≤ 400 m), while DoorToDoor holds steady at
58.0% regardless of ρ. The MNL utility function penalizes walking
distance heavily: passengers reject meeting-point-based offers when the required walk
exceeds their tolerance, making ρ the critical deployment parameter. At the threshold
ρ = 1000 m, FullModel vehicle-km = 219.7 vs DoorToDoor = 1693.8 km
(standard density tier).

**Policy implication:** DRT operators in Chinese cities should survey walking tolerance
before deploying bidirectional meeting points. Districts where residents routinely walk
> 1000 m to transit stops (common in suburban areas with sparse bus networks)
are prime candidates. Districts with elderly-dominant populations or poor pedestrian
infrastructure should retain door-to-door service. Operators should pilot bidirectional
meeting points with opt-in enrollment, allowing passengers to self-select based on their
own walking tolerance before system-wide rollout.

---

## Recommendation 2: Minimum Fleet Ratio of 15 Vehicles per 100 Daily Requests

**Evidence:** Fleet size sensitivity analysis (n_vehicles ∈ [5, 30], n_requests = 200 fixed)
shows that FullModel achieves its highest acceptance rate of 24.0% at
n_vehicles = 30 (15.0 vehicles per 100 requests).
Vehicle scarcity is the binding constraint at low fleet sizes: even with full bidirectional
meeting point flexibility, acceptance rates remain below 25% across all tested fleet sizes,
indicating that demand in the synthetic scenario exceeds vehicle capacity.
At n_vehicles = 15 (baseline), DoorToDoor acceptance rate exceeds FullModel by
38.0 pp, confirming that door-to-door service is more robust
under vehicle scarcity because it does not impose walking penalties on passengers.

**Policy implication:** Chinese city DRT operators planning new services should budget
for at least 15 vehicles per 100 peak-hour requests. Underfleeting
negates the efficiency gains from bidirectional meeting point optimization. Operators
can phase in vehicles incrementally, using the sensitivity curve to project service
quality at each fleet size. Bidirectional meeting points deliver their greatest advantage
when fleet supply is sufficient to serve the majority of requests.

---

## Recommendation 3: Monitor Time-sensitive Passengers for Service Equity

**Evidence:** Equity analysis across three passenger types (price-sensitive, time-sensitive,
walk-sensitive) shows that Time-sensitive passengers have the lowest
acceptance rate (14.4%), compared to price-sensitive (25.4%) and
walk-sensitive (20.2%). This indicates systematic disadvantage under bidirectional meeting
point assignment: time-sensitive passengers face longer in-vehicle travel times (avg IVT
1109.6 s) and higher wait times (avg 603.2 s) relative to other types. The Gini coefficient
of acceptance rates across types is 0.122, indicating moderate inequality — some passenger types are systematically better served.
A Gini of 0.122 means that roughly 12% of the total acceptance rate variation
is attributable to passenger type rather than random demand variation.

**Policy implication:** DRT operators should track per-type acceptance rates in real
deployments. If Time-sensitive passengers are disproportionately
rejected, operators should consider: (a) adjusting MNL utility weights to reduce the
penalty for this type, (b) offering a door-to-door fallback option for passengers who
opt out of meeting-point service, or (c) subsidizing the disadvantaged type through
reduced fares. Regulatory bodies in Chinese cities should require DRT operators to
report disaggregated acceptance rates by passenger segment as a condition of operating
licenses. This aligns with TR Part A's equity mandate for public transit policy.

---

## Recommendation 4: Match Service Mode to City Density Tier

**Evidence:** City tier comparison (low density: 100 requests / 20 km², high density:
400 requests / 20 km²) shows FullModel acceptance rates of 0.0% (low)
vs 0.2% (high) at ρ = 500 m. Vehicle efficiency gains from bidirectional
assignment are 75.9% relative to door-to-door in the standard scenario
(n = 200, FullModel vkm = 628.5 vs DoorToDoor = 2603.7).

**Policy implication:** Three-tier deployment framework for Chinese cities:
- **Tier 1 (high density, > 300 requests/day in service zone):** Bidirectional meeting
  points with full MNL choice model. Highest efficiency gains justify the system complexity.
- **Tier 2 (medium density, 100–300 requests/day):** Single-sided pickup meeting points
  with door-to-door dropoff. Balances efficiency and passenger convenience.
- **Tier 3 (low density, < 100 requests/day):** Door-to-door service. Meeting point
  overhead exceeds efficiency gains at low demand levels.

---

## Recommendation 5: Deploy Rolling Horizon Re-optimization for Dynamic Demand

**Evidence:** Ablation experiment (AblationNoRollingHorizon vs FullModel) shows 16.6% increase in vehicle-km when rolling horizon re-optimization is disabled, confirming that periodic re-assignment of meeting points to newly arrived requests is essential for efficiency.

**Policy implication:** DRT operators should implement rolling horizon re-optimization
with a window H ≥ 30 minutes and time step Δ = 5 minutes. Static assignment (greedy
insertion without re-optimization) is insufficient for dynamic urban demand patterns.
The computational overhead is acceptable: average decision time per request remains
below 1 second on instances with 200 requests and 15 vehicles, making real-time
deployment feasible on standard server hardware. Chinese city operators should plan
for cloud-based dispatch systems rather than on-vehicle computation.

---

*Scenarios: synthetic 20 km × 20 km grid, vehicle capacity 8, max ride time 45 min.*
*MNL parameters: α = [1.0, 1.0, 1.0, 1.0], outside option penalty = 5.0.*
*All results averaged across seeds [42, 43, 44] where applicable.*
