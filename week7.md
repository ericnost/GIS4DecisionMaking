---
layout: lectures
title: "Week 7: Scenarios"
permalink: /lectures/week-07/
---

# Week 7
## Scenarios

Scenario planning, types of models, case studies: Louisiana climate adaptation / ecosystem services models, spatial statistics tutorial preview

---
# Application 2 - Proposal
_Step 1_: review the Discussion Board and select an RFP to respond to. 

_Step 2_: consider what data and analysis will be necessary. 

_Step 3_: write your bid in no more than 500 words:
- **Data**: An inventory of the datasets you intend to use, including the agency/source, spatial resolution, temporal currency, and a link, where available. 
- **Anticipated Methodology:** A brief narrative describing the intended analysis techniques (e.g., Multi-Criteria Evaluation, network routing) and a ModelBuilder diagram illustrating it
- **Project Timeline:** A simply but realistic Gantt chart outlining the steps from data acquisition and processing to analysis and final map production.

**_You must include the RFP you are responding to in your bid._**

_Step 4_: submit to the Courselink Dropbox

---
# Next few weeks

**Scenarios** - alternatives/futures, Louisiana coastal restoration case, InVEST software

**Spatial statistics** - spatial stats in policy, global and local indicators of spatial association

**Uncertainty** - what motivates scenario analysis, different kinds of uncertainty, uncertainty vs error, Survey123

---
# Scenario planning
<div class="split-slide" markdown="1">
<div markdown="1">
> “**Scenarios are alternative hypotheses of what might happen, using the same model with different assumptions**, usually constructed around a central trend extrapolation or ‘business as usual’ scenario.”

What about “working with uncertainty rather than trying (in vain) to eliminate it….[the] goal is to increase the resilience of our approach to the future and _the question they pose is not “what will happen?” but: “given that one cannot predict, what actions available today are likely to serve us best in the future?”_

[Source](https://gistbok.ucgis.org/bok-topics/2022-quarter-02/conceptual-models-error-and-uncertainty)
</div>
<div markdown="1">
![Louisiana climate sea level rise scenarios]({{ site.baseurl }}/assets/images/cc_scenarios.png)
</div>
</div>

---
# Scenario planning
<div class="split-slide" markdown="1">
<div markdown="1">
Strategies: “Using very large ensembles (sets) of plausible scenarios, **Robust Adaptive Planning [RAP; also Robust Decision-Making (RDM)]** _strives to identify paths of action that can serve as many desirable alternative futures as possible, while keeping one’s options open as long as possible._” 

"HOPE FOR THE BEST, PLAN FOR THE WORST"

Which set of actions works best under the most scenarios?
</div>
<div markdown="1">
![Robust decision-making diagram](https://media.springernature.com/full/springer-static/image/chp%3A10.1007%2F978-3-030-05252-2_2/MediaObjects/427530_1_En_2_Fig1_HTML.png)

[Source](https://link.springer.com/chapter/10.1007/978-3-030-05252-2_2)
</div>
</div>

---
# Models
<div class="split-slide" markdown="1">
<div markdown="1">
Models help us get a handle on the future or alternatives...._but they are not "crystal balls"_
</div>

<div markdown="1">
![Wikipedia climate model diagram](https://thumb.wikimedia.org/wikipedia/commons/thumb/4/43/20250712_Climate_model_inputs_and_outputs.svg/1920px-20250712_Climate_model_inputs_and_outputs.svg.png?utm_source=en.wikipedia.org&utm_campaign=imageinfo&utm_content=thumbnail)

[Source](https://en.wikipedia.org/wiki/Climate_model)
</div>
</div>

---
# Types of models
<div class="split-slide" markdown="1">
<div markdown="1">
- **Data** vs **process**
  - model of reality, e.g. raster vs "1) an expression of how the world is believed to work, or 2) a workflow of spatial operations to achieve certain analytical goals"
</div>
<div markdown="1">
![Process model - ArcGIS workflow](https://bok-figures.s3.amazonaws.com/files/AM20_Fig1.png)
</div>
</div>

---
# Types of models
<div class="split-slide" markdown="1">
<div markdown="1">
- **Static** vs **dynamic**
  - single point in time vs time x, y, z
  - output of time x becomes input for time y, output of time y becomes input for time z, etc.
- **Deterministic** vs **stochastic**
  - guaranteed outcome vs some element of randomness
</div>
<div markdown="1">
![Deterministic vs stochastic model](https://upload.wikimedia.org/wikipedia/commons/d/dc/Process-based-stochastic-modelling.png?utm_source=commons.wikimedia.org&utm_campaign=index&utm_content=original)

[Source](https://commons.wikimedia.org/wiki/File:Process-based-stochastic-modelling.png)
</div>
</div>

---
# Model validation

**Validation**: does your model accurately reflect the processes it is meant to reflect?

_Challenge_: models that offer predictions of future conditions can't be tested...until the future happens

3 approaches:
- to see if it can predict the future, see if the model can predict the past (assumes stationarity)
- to see if it can predict here, see if the model works elsewhere (aka transfer learning; assumes homogeneity)
- internal cross-validation: develop the model using some of the data, check it against the rest of the data

---
# Case: Models in Louisana coastal restoration
<div class="split-slide" markdown="1">
<div markdown="1">
**Context**: land loss due to sea level rise, subsidence, river management, natural resource exploitation -> worse Katrina/Rita impacts

Coastal Master Plans in 2007, 2012, 2017, [2023](https://coastal.la.gov/wp-content/uploads/2023/06/230531_CPRA_MP_Final-for-web_spreads.pdf), 2029
</div>
<div markdown="1">
![Land loss in s. Louisiana 1932-2011](https://www.climate.gov/sites/default/files/2022-01/LandLossinSouthernLouisiana1932_vs_2011_ani_0.gif)

[Source](https://www.climate.gov/media/13990)
</div>
</div>

---
# Case: Models in Louisana coastal restoration
<div class="split-slide" markdown="1">
<div markdown="1">
**ICM model**: biophysical, engineering, and social
- What will the landscape look like?
- What will it look like with a sediment diversion?
- Who will be affected?

The ICM is comprised of many dynamic process models.
</div>
<div markdown="1">
![Louisiana Master Plan models]({{ site.baseurl }}/assets/images/lamp_models.png)
</div>
</div>

---
# Case: Models in Louisana coastal restoration
![Louisiana Master Plan scenarios]({{ site.baseurl }}/assets/images/lamp_scenarios.png)


---
# Case: Models in Louisana coastal restoration
**Calculations**:
- land loss/gain
- flood depths

[Master Plan Data Viewer](https://mpdv.coastal.la.gov/?_gl=1*1br6lwy*_ga*MTAwMDI3NjA3Ni4xNzg5Mzk3MDY5*_ga_QXZEQ3TW20*czE3OTMxMTMwNDUkbzIkZzEkdDE3OTMxMTMwNjckajM4JGwwJGgw#map=7.83/29.283/-91.51&view=land-change)

---
# LAMP paper
<div class="split-slide" markdown="1">
<div markdown="1">

Who wins/loses in implementing the restoration projects?

Comparing 2050 flooding due to storm surge, levels with projects vs levels without projects

If projects are built, most places are expected to see less flooding than if projects aren't built. 

But:
1. some places will see _more_ flooding *with* projects than without
2. nearly all places will see more flooding in the future than they do now
</div>
<div markdown="1">
![LAMP land loss scenarios]({{ site.baseurl }}/assets/images/lamp_ll.png)
![LAMP paper test 1]({{ site.baseurl }}/assets/images/lamp_test1.png)
</div>
</div>

---
# Case: Ecosystem services (ES) models

**ES: the benefits nature provides to society**

Examples: flood mitigation, carbon sequestration

Decision-making typically doesn't account for these. When we approve building a new subdivision, we might look at impacts to species and/or acres of forest loss, but this isn't measured in terms of affects on flooding or carbon sequestration, certainly not in $$$ terms

---
# Case: Ecosystem services (ES) models
**Current ecosystem service supply vs supply under decision X**

1. _Current conditions_ = land cover and other measurements
2. _Ecosystem services_ = flood depths reduced, carbon sequestered, etc.
3. _Monetary impact_ = flood damages avoided, carbon credits awarded, etc.
4. Decision X = e.g. build a road, log a forest, etc.
5. _Impact_ = land cover change due to new road, forest loss
6. _Ecosystem services_ = flood depths reduced, carbon sequestered, etc.
7. _Monetary impact_ = flood damages avoided/increased, carbon credits (not) awarded, etc.
8. _Changes_ in ES and their monetary value

Part of environmental impact assessment (?)

---
# Case: Portugal land cover change and ES supply
<div class="split-slide" markdown="1">
<div markdown="1">
> Land cover change scenarios hold far-reaching implications for ecosystem services (ES), highlighting the need for understanding the trade-offs and synergies underlying the provision of multiple ES. **The insufficient knowledge of the mechanisms governing the relationships among multiple ES, along with the lack of information on trade-offs among ES under different scenarios, restricts the ability to provide effective information for decision-makers**. To fill this gap, we assessed the interplay among six ES: climate regulation, habitat creating and maintaining species diversity, cultivated crops, regulation of the chemical condition of freshwaters by living processes (water quality), water yield, and control of erosion rates, within three river basins in northwest Portugal. **We employed the InVEST to map the state of these ES in 2018, along with three projected land cover scenarios for 2050: business-as-usual, farmland return, and afforestation.**
</div>
<div markdown="1">
![Ecosystem services scenarios Portugal case study]({{ site.baseurl }}/assets/images/es_scenarios.png)
[Source](https://doi.org/10.1007/s00267-023-01916-8)
</div>
</div>

---
# Scenarios in the decision-making problems we've already seen

- **MCE** - different sets of results, different weights
- **LA** - comparing different candidate sites in terms of how much demand they meet
- **MCLP** - which of _p_ sites give us the most coverage? xyz sites vs zab sites etc.
- **LSCP** - which sites give us complete coverage? xyz sites vs zab sites etc.
- **Routing** - e.g. which is the shortest path if we build a bike lane vs no bike lane?

---
# Scenarios as means of testing some of our assumptions
What if? This weight instead of that? This site instead of that?

But we still have to make assumptions (aka choices)!
 - how do roads lead to different kinds of land cover/land use changes?
 - which scenarios should we compare or focus on? (see "robust decision-making")

---
# Formulating scenarios
<div class="split-slide" markdown="1">
<div markdown="1">
"Natural" scenarios, analytical scenarios, and futures

- Natural scenarios = company X proposes to develop a mine here, how will that change ecosystem services relative to the status quo?
- Analytical scenarios = these XYZ restoration projects that each individually build the most land per dollar spent, vs the status quo
- Futures = stories about different paths society/environments can take

[Example](https://wsc.limnology.wisc.edu/yahara2070-ecosystem-benefits/index.html): Yahara River watershed flooding in Madison, WI USA

[Scenarios/pathways](https://ecologyandsociety.org/vol21/iss2/art12/figure2.html)
</div>
<div markdown="1">
![Yahara flood scenarios](https://wsc.limnology.wisc.edu/yahara2070-ecosystem-benefits/flood_files/flood.jpg)
</div>
</div>

---
# Tutorial preview: Assessing Environmental Justice with Spatial Statistics
<div class="split-slide" markdown="1">
<div markdown="1">
You will calculate two kinds of spatial statistics to re-create [a recent Environment and Climate Change Canada study](https://www.canada.ca/en/environment-climate-change/services/strategic-policy-branch/environmental-justice/national-strategy.html).
</div>
<div markdown="1">

![EJ tutorial with spatial statistics]({{ site.baseurl }}/assets/images/spatialstats.png)

</div>
</div>

