# Literature Gaps: Built Environment & Travel Behavior in Chinese Cities
# Target Journal: Transportation Research Part D: Transport and Environment

**Researched:** 2026-04-11
**Confidence:** MEDIUM (TR Part D volumes directly scanned 2023-2025; web search for China-specific papers limited by paywalls)

---

## 1. TR Part D Journal Profile

TR Part D publishes original research on "environmental impacts of transportation, policy responses, and their implications for design, planning, and management of transportation systems." The key filter for acceptance is the **environment-transport nexus** — papers must connect built environment or travel behavior to an environmental outcome (carbon emissions, air quality, energy use, modal shift toward sustainable modes). Pure travel behavior papers without an environmental angle are out of scope.

**What TR Part D accepts in this domain:**
- Built environment effects on mode choice, VKT, or carbon emissions
- Nonlinear/threshold effects of urban form on sustainable travel
- Equity dimensions of transport-environment interactions
- Methodological innovations applied to transport-environment questions
- Multi-city or cross-context comparisons with policy implications

---

## 2. What Is Currently Hot / Well-Covered (2022–2025)

Based on direct scanning of TR Part D Volumes 120–150 (2023–2026) and targeted searches:

### 2.1 Covered Topics (Saturated or Well-Represented)

**Metro/rail ridership and built environment (single-city)**
- Huang et al. (Vol. 130, 2024): "Causality between multi-scale built environment and rail transit ridership in Beijing and Tokyo" — multi-scale analysis, Beijing already done
- Zhu et al. (Vol. 128, 2024): "Exploring the long-term threshold effects of density and diversity on metro ridership" — threshold effects on metro already published
- Zhou et al. (Vol. 132, 2024): "Evaluating the impact of rail transit network expansion on travel behavior in Shenzhen, China"

**Nonlinear machine learning methods applied to built environment**
- Nachtigall et al. (Vol. 140, 2025): "Built environment and travel: Tackling non-linear residential self-selection with double machine learning" — double ML for self-selection now published
- Ding et al. (Vol. 128, 2024): "Revisiting residential self-selection and travel behavior connection using a double machine learning" — same method, China context
- Liu et al. (Vol. 128, 2024): "Nonlinear relationship between microenvironmental exposure and travel satisfaction explored with machine learning"

**Active school travel in China**
- Ma et al. (Vol. 134, 2024): "Active school travel in China: Unveiling multifaceted influences for sustainable mobility"

**Built environment and VKT / car ownership**
- Yin et al. (Vol. 144, 2025): "Revisiting built environment and vehicle kilometer traveled: Does car ownership matter?" — China context, car ownership mediation
- Berrill et al. (Vol. 128, 2024): "Comparing urban form influences on travel distance, car ownership, and mode choice" — multi-country including China

**EV ownership and built environment in China**
- Diao & Su (Vol. 146, 2025): "Electric vehicle ownership and the built environment: Evidence from China"
- Ma et al. (Vol. 146, 2025): "Electric or gasoline vehicle? Determinants of vehicle ownership in 247 Chinese cities"

**Transit equity and built environment in China**
- Zhang et al. (Vol. 136, 2024): "Does built environment improvement promote transport equity for internal migrants in Beijing?"
- Xu et al. (Vol. 126, 2024): "Distribution justice and regional equity of urban public transport services: Evidence from China"

**Commuting and wellbeing in China**
- Deng et al. (Vol. 126, 2024): "Commuting and its spillover effects on subjective well-being: Evidence from China"
- Zhao et al. (Vol. 136, 2024): "Across the city boundaries: Exploring the impact of neighborhood environment on intercity commuters' life satisfaction"

**Nonlinear built environment effects on freight emissions**
- Peng et al. (Vol. 134, 2024): "Nonlinear impacts of urban built environment on freight emissions"

**Bike-sharing and built environment**
- Song et al. (Vol. 132, 2024): "Unraveling the effects of micro-level street environment on dockless bikeshare in Ithaca"
- Li et al. (Vol. 134, 2024): "Public attention and attitudes towards bike-sharing in China: A text mining approach"

**Commuting CO2 and built environment**
- Yu et al. (Vol. 148, 2025): "Commuting CO2 emissions and built environment around residences and workplaces: Income disparities"

**Active travel and multi-scale built environment**
- Ge et al. (Vol. 146, 2025): "The impacts of multi-scale urban environments on commuters' active travel"
- Zhang et al. (Vol. 136, 2024): "Nonlinear associations between design, land-use features, and active travel"

**First/last-mile and transit**
- Yang et al. (Vol. 146, 2025): "Does the first/last-mile design matter for transit commuting compared to land use?"

---

## 3. Research Gaps — Specific Opportunities

### Gap 1: Built Environment Effects on Travel Carbon Emissions Across City Tiers (HIGH PRIORITY)

**What exists:** Most China studies focus on single cities (Beijing, Shanghai, Shenzhen, Wuhan). The commuting CO2 + built environment paper (Yu et al., Vol. 148) examines income disparities but appears to be single-city. Multi-city comparisons exist for ridership but not for travel carbon emissions linked to built environment.

**What's missing:** A systematic cross-city analysis linking built environment characteristics (density, mix, transit access) to per-capita travel carbon emissions across China's city tier system (Tier 1 vs. Tier 2 vs. Tier 3 cities). China's city tier system creates natural variation in urban form, transit investment, and car ownership that is analytically powerful but underexploited.

**Why it fits TR Part D:** Direct environment-transport nexus (carbon emissions). Cross-city scope enables policy-relevant generalizations. China's carbon peak/neutrality commitments make this timely.

**Data angle:** China Carbon Accounting Database (CEADs), National Bureau of Statistics city-level data, Gaode/Amap POI data (publicly accessible), OSM for built environment metrics.

**Methodological angle:** Spatial panel regression or multi-level modeling across 50–100 cities; SHAP values for nonlinear effects.

**Confidence:** MEDIUM — gap inferred from scanning TR Part D volumes; single-city dominance is clear, but a cross-city carbon paper may exist in other journals.

---

### Gap 2: Built Environment Effects on New Energy Vehicle (NEV) Travel Behavior (HIGH PRIORITY)

**What exists:** Diao & Su (Vol. 146, 2025) examine EV ownership and built environment in China. Ma et al. (Vol. 146, 2025) model EV vs. gasoline vehicle choice across 247 cities. These focus on ownership/adoption.

**What's missing:** How does the built environment shape the *travel behavior* of NEV owners — specifically VKT, charging trip generation, and mode substitution? NEV owners in compact, transit-rich neighborhoods may drive less and charge differently than those in sprawl. This is a genuinely new behavioral question that the EV adoption literature hasn't addressed.

**Why it fits TR Part D:** Directly relevant to transport decarbonization. China has the world's largest NEV fleet (20+ million as of 2023). The environmental implications of NEV travel patterns depend on whether compact urban form reduces VKT even for EV owners.

**Data angle:** China's NEV monitoring platform data (publicly reported aggregates), city-level NEV registration data from MIIT, combined with OSM/Gaode built environment metrics.

**Methodological angle:** Propensity score matching or instrumental variable approach to compare NEV vs. ICE vehicle travel behavior controlling for built environment; or cross-city panel analysis.

**Confidence:** MEDIUM — this specific angle (NEV travel behavior × built environment) not found in TR Part D scan; the EV-built environment literature focuses on adoption, not post-adoption travel.

---

### Gap 3: Dual-End Built Environment Effects on Commuting Carbon (MEDIUM-HIGH PRIORITY)

**What exists:** Yu et al. (Vol. 148, 2025) examine commuting CO2 and built environment around residences and workplaces with income disparities. Sun et al. (Vol. 128, 2024) examine transit allowance, land use, and transit commuting. Most studies use residential-end built environment only.

**What's missing:** A rigorous analysis of the *joint* and *interactive* effects of residential-end AND workplace-end built environment on commuting carbon emissions, with explicit attention to asymmetry (does workplace density matter more than residential density for carbon reduction?). The Yu et al. paper addresses income disparities but the interaction between the two ends and their relative importance for carbon reduction policy is unclear.

**Why it fits TR Part D:** Carbon emissions focus. Policy relevance: should planners prioritize densifying residential areas or employment centers? China's polycentric urban development makes this especially relevant.

**Data angle:** China's National Travel Survey data (if accessible), or city-level commuting data from census + built environment from OSM/Gaode. Alternatively, smart card data from metro systems (some cities publish aggregated OD data).

**Methodological angle:** Structural equation modeling or mediation analysis; or double machine learning to handle endogeneity at both ends simultaneously.

**Confidence:** MEDIUM — Yu et al. (2025) partially addresses this; the specific interactive/asymmetric angle may still be open.

---

### Gap 4: Built Environment and Ride-Hailing / Shared Mobility Carbon in Chinese Cities (MEDIUM PRIORITY)

**What exists:** Zhang et al. (Vol. 130, 2024): "Environmental impacts of ridesplitting considering modal substitution and associations with built environment" — but this is not China-specific. Wu et al. (Vol. 148, 2025): "Environmental implications and influencing mechanisms of urban ride-hailing services: A systematic perspective" — systematic review, not empirical China study.

**What's missing:** An empirical study of how built environment characteristics moderate the environmental impact of ride-hailing (Didi) in Chinese cities. Specifically: in what urban contexts does ride-hailing substitute for private car use (carbon-reducing) vs. substitute for transit/walking (carbon-increasing)? China's Didi platform is the world's largest ride-hailing service and has unique characteristics (high density, transit competition, e-bike competition).

**Why it fits TR Part D:** Environmental impact of emerging mobility. China context is underrepresented in ride-hailing-environment literature which is dominated by US/European cases.

**Data angle:** Didi publishes some aggregate city-level data; Gaode mobility data; city-level transit ridership statistics from Ministry of Transport (publicly available).

**Methodological angle:** Difference-in-differences exploiting Didi's city-by-city rollout; or cross-sectional analysis across cities with varying built environment characteristics.

**Confidence:** LOW-MEDIUM — gap inferred from absence in TR Part D scan; Didi data accessibility is uncertain.

---

### Gap 5: Built Environment, Extreme Heat, and Travel Behavior in Chinese Cities (EMERGING PRIORITY)

**What exists:** Batur et al. (Vol. 136, 2024): "Understanding how extreme heat impacts human activity-mobility and time use patterns" — US context. Chen et al. (Vol. 142, 2025): "Heat and mobility: Machine learning perspectives on bike-sharing resilience in Shanghai" — Shanghai bike-sharing only.

**What's missing:** A comprehensive study of how built environment characteristics (shade, green space, building density, transit access) moderate the effect of extreme heat on travel behavior and modal shift in Chinese cities. China's rapid urbanization has created urban heat islands that interact with travel behavior in ways not yet systematically studied. The environmental angle: heat-induced modal shift toward private cars increases emissions.

**Why it fits TR Part D:** Climate-transport-environment nexus. Aligns with TR Part D's growing interest in climate adaptation (Disasters and Resilience section). China's extreme heat events are intensifying.

**Data angle:** China Meteorological Administration temperature data (public), city-level transit ridership statistics (Ministry of Transport, public), OSM/Gaode for built environment, NDVI for green space.

**Methodological angle:** Panel regression with weather-city-time fixed effects; machine learning for nonlinear heat-built environment interactions.

**Confidence:** MEDIUM — the Shanghai bike-sharing paper exists but the broader multi-city, multi-mode, built environment moderation angle is open.

---

## 4. Methodological Innovations Being Published (2022–2025)

Based on TR Part D scan:

| Method | Papers | Notes |
|--------|--------|-------|
| Double machine learning (DML) | Ding et al. (2024), Nachtigall et al. (2025) | For handling residential self-selection/endogeneity |
| XGBoost + SHAP | Multiple papers 2023–2025 | Standard now; need to add something beyond basic SHAP |
| Geo-CNN weighted regression | Liu et al. (Vol. 132, 2024) | Spatial heterogeneity in emissions |
| Multi-scale buffer analysis | Huang et al. (2024), Ge et al. (2025) | Network vs. Euclidean buffers; 5/10/15-min scales |
| Accumulated Local Effects (ALE) | Wuhan older adults paper (2025) | Better than PDPs for correlated features |
| Explainable ML (SHAP + interaction effects) | Multiple 2024–2025 | Now expected, not novel alone |
| Spatial panel models | Standard across China papers | GWR, MGWR still publishable with right application |
| Causal ML / DML | Ding et al. (2024) | Growing; addresses long-standing self-selection critique |

**What's novel enough for 2025–2026:**
- Causal forest / heterogeneous treatment effects (who benefits most from compact development?)
- Double ML applied to China context (Ding et al. used it but more applications needed)
- Multi-city panel with city fixed effects + machine learning (hybrid approach)
- Counterfactual analysis using natural experiments (policy rollouts, metro openings)

---

## 5. Public Datasets Commonly Used for Chinese City Travel Behavior Research

| Dataset | Source | What It Contains | Accessibility |
|---------|--------|-----------------|---------------|
| China National Travel Survey | NBS / MOHURD | Household travel diaries, mode choice | Limited public access; some city-level aggregates |
| Metro smart card OD data | City transit authorities | Trip origins/destinations, timestamps | Some cities publish aggregates; raw data requires collaboration |
| Gaode (Amap) POI data | Alibaba/Amap API | Points of interest, land use proxy | API accessible; widely used in literature |
| OSM (OpenStreetMap) | Community | Road network, building footprints | Fully public |
| China Carbon Accounting Database (CEADs) | Tsinghua/PKU | City-level carbon emissions by sector | Public, widely cited |
| Ministry of Transport statistics | MOT China | City-level transit ridership, VKT | Annual yearbook, public |
| China Statistical Yearbook | NBS | City-level socioeconomic data | Public |
| Tencent Location Big Data | Tencent | Population mobility heatmaps | Some public releases; API for researchers |
| Didi Chuxing open data | Didi | Trip data for select cities/periods | Limited public releases (Chengdu, Xi'an datasets) |
| NDVI / Landsat | NASA/USGS | Green space, urban heat island | Fully public |
| China Meteorological Administration | CMA | Temperature, precipitation | Public |
| National Population Census | NBS | Commuting mode, residential density | Public (2010, 2020 census) |
| Baidu Maps POI | Baidu | POI data, similar to Gaode | API accessible |

**Most competitive combination for a TR Part D paper:** CEADs (carbon) + Gaode POI (built environment) + MOT transit statistics + NBS city data, analyzed across 50–100 cities. This avoids primary survey data while enabling large-scale analysis.

---

## 6. What Makes a Paper Competitive for TR Part D Acceptance

Based on journal scope and recent publication patterns:

**Must-haves:**
1. Clear environmental outcome variable (carbon emissions, modal shift to sustainable modes, VKT reduction) — not just travel behavior for its own sake
2. Policy implications that are actionable and generalizable beyond the study area
3. Methodological rigor — address endogeneity/self-selection explicitly (DML, IV, DiD, or at minimum propensity score matching)
4. China context must add value beyond confirming Western findings — exploit China-specific features (city tier system, rapid metro expansion, NEV penetration, hukou system, gated communities)

**Strong differentiators:**
- Multi-city scope (not single city) — enables generalization
- Nonlinear effects with policy-relevant thresholds (e.g., "density above X reduces carbon by Y%")
- Interaction effects between built environment and socioeconomic heterogeneity
- Natural experiment or quasi-experimental design
- Novel data combination (e.g., CEADs carbon + Gaode POI + MOT ridership)

**Common rejection reasons (inferred from scope):**
- Pure travel behavior without environmental outcome
- Single-city case study with no generalization
- Descriptive analysis without causal identification
- Replication of Western findings in China without theoretical contribution
- Methodological novelty without substantive contribution

---

## 7. Top 3–5 Recommended Research Gap Opportunities (Ranked)

### Rank 1: Cross-City Built Environment → Travel Carbon Emissions (China City Tiers)
**Angle:** How do built environment characteristics across China's city tier system explain variation in per-capita travel carbon emissions? Use 50–100 cities, CEADs carbon data, Gaode POI, MOT statistics. Apply spatial panel regression + SHAP for nonlinear effects. Identify carbon-reduction thresholds for density, transit access, and land use mix.
**Why competitive:** Multi-city scope, direct carbon outcome, policy-relevant thresholds, exploits China's unique city tier variation, no direct competitor in TR Part D.
**Risk:** CEADs transport sector carbon data quality at city level; may need to construct proxy from fuel consumption statistics.

### Rank 2: NEV Travel Behavior × Built Environment
**Angle:** Do NEV owners in compact, transit-rich neighborhoods drive less (lower VKT) than those in sprawl? Does compact urban form reduce the rebound effect of EV adoption? Use MIIT NEV registration data + city built environment + NBS data across cities.
**Why competitive:** Genuinely novel behavioral question, directly relevant to China's decarbonization strategy, no direct competitor found in TR Part D, timely given China's 20M+ NEV fleet.
**Risk:** NEV-level travel data may not be publicly available; may need to work with city-level aggregates.

### Rank 3: Dual-End Built Environment and Commuting Carbon (Residential + Workplace)
**Angle:** Jointly model residential-end and workplace-end built environment effects on commuting carbon, testing which end matters more for carbon reduction. Use DML or structural equation modeling to handle endogeneity at both ends.
**Why competitive:** Addresses a methodological gap in the literature (most studies use residential end only), direct policy implication (where to densify), builds on Yu et al. (2025) but adds the interactive/asymmetric angle.
**Risk:** Yu et al. (2025) may have partially addressed this; need to differentiate clearly.

### Rank 4: Extreme Heat × Built Environment → Modal Shift and Carbon (Multi-City China)
**Angle:** How does extreme heat interact with built environment to shift travel modes (toward private car, away from walking/cycling) and increase carbon emissions? Multi-city panel using CMA temperature data + MOT ridership + Gaode built environment.
**Why competitive:** Climate adaptation angle aligns with TR Part D's Disasters and Resilience section, multi-city scope, novel interaction effect, China's intensifying heat events make it timely.
**Risk:** Establishing causal mechanism (heat → modal shift → carbon) requires careful design.

### Rank 5: Built Environment and Ride-Hailing Environmental Impact in Chinese Cities
**Angle:** In what urban contexts does Didi ride-hailing substitute for private cars (carbon-reducing) vs. transit/walking (carbon-increasing)? Cross-city analysis using Didi open data + built environment + transit ridership.
**Why competitive:** Emerging mobility + environment nexus, China's Didi is world's largest ride-hailing platform, underrepresented in TR Part D.
**Risk:** Didi data availability is uncertain; may need to use indirect proxies.

---

## 8. Confidence Assessment

| Area | Confidence | Notes |
|------|------------|-------|
| TR Part D recent publications (2023–2025) | HIGH | Directly scanned Volumes 120–150 |
| China-specific papers in TR Part D | MEDIUM | Found ~15 relevant papers; paywall limits full text access |
| Research gaps | MEDIUM | Inferred from absence in TR Part D; gaps may be filled in other journals (TRB, Cities, JTLU) |
| Methodological trends | HIGH | Clear pattern from volume scanning |
| Public datasets | MEDIUM | Based on training knowledge + literature; accessibility may vary |
| TR Part D acceptance criteria | HIGH | Based on aims/scope + publication pattern analysis |

---

## 9. Key Papers Found in TR Part D (2023–2025) — China-Relevant

| Paper | Volume | Year | Topic | Relevance |
|-------|--------|------|-------|-----------|
| Huang et al. | 130 | 2024 | Multi-scale BE + rail ridership, Beijing/Tokyo | Direct competitor for metro ridership angle |
| Zhu et al. | 128 | 2024 | Threshold effects of density/diversity on metro ridership | Threshold methods for transit |
| Zhou et al. | 132 | 2024 | Rail transit expansion + travel behavior, Shenzhen | Transit expansion effects |
| Ding et al. | 128 | 2024 | Double ML for residential self-selection + travel behavior | Methodological benchmark |
| Sun et al. | 128 | 2024 | Transit allowance + land use + transit commuting | Land use-transit commuting |
| Zhang et al. | 136 | 2024 | BE improvement + transport equity, Beijing migrants | Equity angle |
| Xu et al. | 126 | 2024 | Transit equity, China | Equity + distribution |
| Deng et al. | 126 | 2024 | Commuting + wellbeing, China | Wellbeing angle |
| Peng et al. | 134 | 2024 | Nonlinear BE effects on freight emissions | Freight + nonlinear |
| Ma et al. | 134 | 2024 | Active school travel, China | School travel |
| Yin et al. | 144 | 2025 | BE + VKT + car ownership, China | VKT + car ownership |
| Diao & Su | 146 | 2025 | EV ownership + BE, China | EV adoption |
| Ma et al. | 146 | 2025 | EV vs. gasoline choice, 247 Chinese cities | EV choice |
| Ge et al. | 146 | 2025 | Multi-scale BE + active travel, commuters | Active travel |
| Yang et al. | 146 | 2025 | First/last-mile design vs. land use, transit | First/last mile |
| Yu et al. | 148 | 2025 | Commuting CO2 + BE + income disparities | Carbon + equity |
| Huang & Ma | 150 | 2026 | BE + cognitive dissonance + travel satisfaction | Psychological mediation |
| Li et al. | 150 | 2026 | Metro-connected micro-transit, Chongqing | First/last mile |
| Nachtigall et al. | 140 | 2025 | BE + travel, double ML for self-selection | Methodological |
| Zhang et al. | 136 | 2024 | Nonlinear BE + active travel | Nonlinear methods |

---

## 10. Open Questions / Gaps in This Research

- Whether a cross-city carbon + built environment paper already exists in TR Part D under different search terms (confidence: LOW that it exists, but cannot confirm)
- Exact accessibility of CEADs transport-sector carbon data at city level for 2020–2023
- Whether Didi open data is sufficient for a rigorous empirical study
- How TR Part D editors currently weight China-specific papers vs. global/Western papers (anecdotally, China papers are well-represented but must have strong environmental framing)
- Whether the "dual-end" commuting carbon angle is sufficiently differentiated from Yu et al. (2025) — needs careful reading of that paper

---

*Sources consulted: TR Part D journal volumes 120–150 (2023–2026) via ScienceDirect; WebSearch for China-specific transportation research; TR Part D aims and scope page; DOAJ for specific paper abstracts.*
