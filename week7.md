---
layout: lectures
title: "Week 7: Scenarios"
permalink: /lectures/week-07/
---

# Week 7
## Scenarios

Scenarios, types of models, case studies: Louisiana climate adaptation / ecosystem services models, spatial statistics tutorial preview

---
# Application 2 - Proposal
Step 1: review the Discussion Board and select an RFP to respond to. 

Step 2: consider what data and analysis will be necessary. 

Step 3: write your bid in no more than 500 words -
- **Data**: An inventory of the datasets you intend to use, including the agency/source, spatial resolution, temporal currency, and a link, where available. 
- **Anticipated Methodology:** A brief narrative describing the intended analysis techniques (e.g., Multi-Criteria Evaluation, network routing) and a ModelBuilder diagram illustrating it
- **Project Timeline:** A simply but realistic Gantt chart outlining the steps from data acquisition and processing to analysis and final map production.

_You must include the RFP you are responding to in your bid._

Step 4: submit to the Courselink Dropbox

---
# Next few weeks

Scenarios - alternatives/futures, Louisiana coastal restoration case, InVEST software
Spatial statistics - spatial stats in policy, global and local indicators of spatial autocorrelation
Uncertainty - what motivates scenario analysis, different kinds, uncertainty vs error, Survey123

---
# Scenario planning
“Scenarios are alternative hypotheses of what might happen, using the same model with different assumptions, usually constructed around a central trend extrapolation or ‘business as usual’ scenario.”
What about “working with uncertainty rather than trying (in vain) to eliminate it….[the] goal is to increase the resilience of our approach to the future and the question they pose is not “what will happen?” but: “given that one cannot predict, what actions available today are likely to serve us best in the future?”….
“But instead of picking a most probable or desirable scenario to recommend or act upon, scenarios here are used as part of a very large space of time-varying possibilities that is analyzed to guide the next set of recommendations and actions.”

https://gistbok.ucgis.org/bok-topics/2022-quarter-02/conceptual-models-error-and-uncertainty


---
# Scenario planning
Strategies: “Using very large ensembles (sets) of plausible scenarios, Robust Adaptive Planning [RAP; also Robust Decision-Making (RDM)] strives to identify paths of action that can serve as many desirable alternative futures as possible, while keeping one’s options open as long as possible.” 
https://link.springer.com/chapter/10.1007/978-3-030-05252-2_2

---
# Models
Models help us get a handle on the future or alternatives

But they are not "crystal balls"

---
# Types of models

Static vs dynamic
Deterministic vs stochastic
Process

---
# Case: Models in Louisana coastal restoration
Context: land loss -> worse Katrina/Rita impacts

Coastal Master Plans in 2007, 2012, 2017, 2023, 2029

ICM model: biophysical, engineering, and social
What will the landscape look like?
What will it look like with a sediment diversion?
Who will be affected?

Calculations:
land loss/gain
flood depths

Scenarios: 
high/low environmental changes
with and without restoration projects

---
# LAMP paper
Who wins/loses in implementing the restoration projects?

Comparing 2050 flooding due to storm surge, levels with projects vs levels without projects

If projects are built, most places are expected to see less flooding than if projects aren't built. 

But:
1. some places will see _more_ flooding *with* projects than without
2. nearly all places will see more flooding in the future than they do now

---
# Case: Ecosystem services models

ES definition: the benefits nature provides to society
Examples: flood mitigation, carbon sequestration

Decision-making typically doesn't account for these. When we approve building a new subdivision, we might look at impacts to species and/or acres of forest loss, but this isn't measured in terms of affects on flooding or carbon sequestration, certainly not in $$$ terms

Current ecosystem service supply vs supply under decision X

Current conditions = land cover and other measurements
Ecosystem services = flood depths reduced, carbon sequestered, etc.
Monetary impact = flood damages avoided, carbon credits awarded, etc.

Decision X = e.g. build a road, log a forest, etc.
Impact = land cover change due to new road, forest loss
Ecosystem services = change in flood depths rerduced, carbon sequestered, etc.
Monetary impact = flood damages increased, carbon not credited, etc.

Part of environmental impact assessment (?)

---
# Case: Portugal land cover change and ES supply


---
# Scenarios in the decision-making problems we've already seen

MCE - different sets of results, different weights
LA - comparing different candidate sites in terms of how much demand they meet
MCLP - which of _p_ sites give us the most coverage? xyz sites vs zab sites etc.
LSCP - which sites give us complete coverage? xyz sites vs zab sites etc.
Routing - e.g. which is the shortest path if we build a bike lane vs no bike lane?

---
# Scenarios as means of testing some of our assumptions
What if? This weight instead of that? This site instead of that?

But we still have to make assumptions (aka choices)!
 - how do roads lead to different kinds of land cover/land use changes?
 - which scenarios should we compare or focus on? (see "robust decision-making")

---
# Formulating scenarios
"Natural" scenarios, analytical scenarios, and futures

Natural scenarios = company X proposes to develop a mine here, how will that change ecosystem services relative to the status quo?
Analytical scenarios = these XYZ restoration projects that each individually build the most land per dollar spent, vs the status quo
Futures = stories about different paths society/environments can take

Chloe Madison Workshops...

---
# Tutorial preview: Assessing Environmental Justice with Spatial Statistics
<div class="split-slide" markdown="1">
<div markdown="1">
You will calculate two kinds of spatial statistics to re-create a recent Environment and Climate Change Canada study.
</div>
<div markdown="1">

![EJ tutorial with spatial statistics]({{ site.baseurl }}/assets/images/spatialstats.png)

</div>
</div>

