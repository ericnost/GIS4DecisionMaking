---
layout: lectures
title: "Week 2: Multi-Criteria Evaluation"
permalink: /lectures/week-02/
---

# Week 2
## Multi-Criteria Evaluation

Rationale, methods, workflow, preview of RFP assignment, location-allocation demo

---
# Multi-Criteria Evaluation (MCE)
## We're supporting implementation of conservation practices on farmland. 
## Find the best spots: cornfields with the worst soils, near wetlands

---
# MCE aka MCDA (Multi-Criteria Decision Analysis)
_Discussion: What are your rankings? What was your thought process? How did you compare different factors?_

---
## Definitions
> A "systematic way of comparing pros and cons of choice alternatives, often using weighted criteria to generate a measure of a relative strength of each alternative vis-à-vis other alternatives (systematic pro-con list with a calculated result)" 

^ _NOT INHERENTLY SPATIAL!!!_

> "a collection of formal approaches which seek to take explicit account of [key factors] in helping individuals or groups explore decisions that matter" [Source](https://doi.org/10.1111/j.1749-8198.2011.00431.x) 

> “Multiple-criteria decision analysis aids decision makers in analysing potential actions or alternatives based on multiple incommensurable factors ⁄ criteria, using decision rules to aggregate those criteria to rate or rank the alternatives.” [Source](https://doi.org/10.1111/j.1749-8198.2011.00431.x)

**Tradeoffs**: route selection example

---
## Why MCE?

> "**Different people facing the same problem may apply different values and motivations and reach different conclusions**. As decisions increase in complexity and importance, so does the need to _formalise_ them using available information, and to _document the rationale_" [Source](https://doi.org/10.1111/j.1749-8198.2011.00431.x) 

> “MCDA researchers and practitioners do not view it simply as a quantitative optimisation problem that identifies the best potential ‘solutions’. Instead, the focus is on **eliciting and making transparent the values and subjectivity that are applied to the more objective measurements**, and _understanding their implications_.” [Source](https://doi.org/10.1111/j.1749-8198.2011.00431.x) 

General applications
- the most trendy neighborhoods
- the top-10 cities to visit
- the best universities for undergraduate studies

---
## MCE problem types
- Choice (making a single selection or recommendation)
- Ranking (establishing a preference order for some or all of the alternatives)
- Sorting (separating alternatives in classes or groups)
- Portfolio (selecting a subset of alternatives)

[Source](https://doi.org/10.1111/j.1749-8198.2011.00431.x) 


---
## MCE methods
**Non-compensatory** (hard cut-offs) 
- Conjunctive: “Accept alternatives if they meet a cut-off value on every criterion.” Keyword: AND
- Risk-averse: a failure to meet the required standard on just one criterion eliminates the entire option

**Compensatory** (more subtle)	
- Poor performance on one criterion can be offset or balanced by strong performance on another.
- Each factor gets a relative weight based on its importance

---
## MCE methods
- **Constraints**: Boolean (true/false -> 0/1) limits that completely exclude certain areas (like protected water bodies).
- **Factors**: Continuous variables that show a degree of suitability (like distance to roads or slope steepness).
  - Weighting: Each factor is multiplied by a specific weight representing its importance.
  - Summation: The weighted factors are added together and multiplied by any Boolean constraints to produce a final suitability map (often scaled from 0 to 255 or 0 to 1)

e.g. Weighted Linear Combination (WLC)

---
## MCE methods
Well, how do we determine how to weight?
- Analytic Hierarchy Process (AHP)
>The decision-maker determines the relative importance of each pair of criteria on a predefined scale, and percentage weights are automatically calculated.
- [Tool](https://spicelogic.com/ahp-calculator)

---
# MCE examples
<div class="split-slide" markdown="1">
<div markdown="1">

Wind turbine siting
- Slope
- Wind speed
- Existing land use
- Proximity to roads

</div>
<div markdown="1">

![Wind turbine suitability]({{ site.baseurl }}/assets/images/wind.png)
[Source](https://www.sciencedirect.com/science/article/abs/pii/S0960148115000592)

</div>
</div>

---
## MCE issues
Is a single correct decision ever possible?
> One of the most important and difficult-to-accept properties of MCE is **its fundamental nature as a normative or optimization model rather than a descriptive or explanatory approach**. In contrast to other statistical analysis techniques, where results emerge from the data, in MCE **it is the analyst or decision-maker who determines the model parameters and thus the results.**

---
## MCE issues
But how do we understand decision-makers?
> MCE models and methods integrate elements from rational decision-making and bounded/procedural rationality theories (Simon, 1957), **which assume a rational decision-maker who understands the decision problem, identifies all options, knows their outcomes, and can rank them by evaluating trade-offs.** These assumptions are mirrored in MCE concepts like preferences, trade-offs, objectives, and decision rules. Malczewski and Jankowski (2020) suggested that theoretical bases for MCE can be expanded by integrating behavioral concepts like bounded rationality, prospect theory, and regret theory. These theories, which blend normative methods with empirical research, aim to enhance the understanding of decision-making by showing that **people evaluate gains and losses differently.** For instance, prospect theory reveals that individuals typically require a higher gain to compensate for a potential loss, challenging traditional utility theory.

---
## MCE issues
Bad data
> The nature of available input data presents another practical issue with MCE. The techniques mostly require numeric data yet many real-world phenomena are difficult to quantify and measure with known accuracy

---
## MCE workflow - suitability modeling
<div class="split-slide" markdown="1">
<div markdown="1">
Finding the optimal site or region for a given phenomenon is known as suitability modeling. Examples:
- New bus stops
- A new storefront location
- Optimal habitat areas for an endangered species

Source: ESRI

[What is the Suitability Modeler](https://pro.arcgis.com/en/pro-app/3.7/help/analysis/spatial-analyst/suitability-modeler/what-is-the-suitability-modeler.htm)

[The general suitability modelling worfklow](https://pro.arcgis.com/en/pro-app/3.7/help/analysis/spatial-analyst/suitability-modeler/the-general-suitability-modeling-workflow.htm)

</div>
<div markdown="1">

![Suitability scales]({{ site.baseurl }}/assets/images/suitabilityscale.png)

</div>
</div>

---
## MCE workflow - suitability modeling
## GOAL -> CRITERIA -> DERIVE DATA -> TRANSFORM DATA -> SCORE/WEIGHT CRITERIA -> LOCATE


---
## MCE workflow - goal/criteria

<div class="split-slide" markdown="1">

<div markdown="1">
**Goal** - specify how many locations need to be identified and the type of location that needs to be identified, such as a site or region. 

**Criteria** - Each criterion should identify a model variable that can represent the condition. The criterion should also define the variable values that are favorable to the phenomenon. 
</div>

<div markdown="1">

![Variable values]({{ site.baseurl }}/assets/images/variablevalues.png)

</div>

</div>

Source: ESRI

---
## MCE workflow - data

![Data types]({{ site.baseurl }}/assets/images/datatypes.png)

Source: ESRI

---
## MCE workflow - deriving data/data prep
<div class="split-slide" markdown="1">

<div markdown="1">
Examples:
- Density calculations
- Interpolation
- Reclassification
- Data type conversion (e.g. polygon to raster)
- Distance calculations (e.g. accumulation)
</div>

<div markdown="1">

![Derived data]({{ site.baseurl }}/assets/images/deriveddata.png)

</div>

</div>

Source: ESRI


---
## MCE workflow - transforming data

![Transforming data]({{ site.baseurl }}/assets/images/transformeddata.png)

Source: ESRI

---
## MCE workflow - transforming data

![Transforming data types]({{ site.baseurl }}/assets/images/transformeddatatypes.png)

Source: ESRI

---
## MCE workflow - scoring
<div class="split-slide" markdown="1">

<div markdown="1">
![Scoring options]({{ site.baseurl }}/assets/images/scoring.png)
</div>
<div markdown="1">
![Scoring options]({{ site.baseurl }}/assets/images/howtoscore.png)
</div>
</div>
Source: ESRI

---
## MCE workflow - weighting
![Weighting process]({{ site.baseurl }}/assets/images/weighting.png)

Source: ESRI

---
## MCE workflow - locating
<div class="split-slide" markdown="1">

<div markdown="1">
- Shape
- Size (min, max, total)
- Number
- Inter-region distance
- What’s “best”? (average, highest sum, etc.)
</div>
<div markdown="1">
![Locate options]({{ site.baseurl }}/assets/images/locate.png)
</div>
</div>
Source: ESRI

---
## MCE in the real-world
Example: [finding social-impact grocery store sites in Denver, CO using Felt GIS](https://40056855.fs1.hubspotusercontent-na1.net/hubfs/40056855/Webinars/2026%20webinar%20felt%20ai.mp4?__hstc=204114447.df3feb36ec7f37aab18426abae234ab2.1790007492496.1790007492496.1790007492496.1&__hssc=204114447.4.1790007492496&__hsfp=04ef42812f9b1b780e77a1fe02c5e4b1&submissionGuid=2929d1ec-0502-4a50-adb1-6611983dfb1f) ~5 minute mark / ~13 minute mark
<iframe width="800" height="500" 
        src="https://40056855.fs1.hubspotusercontent-na1.net/hubfs/40056855/Webinars/2026%20webinar%20felt%20ai.mp4?__hstc=204114447.df3feb36ec7f37aab18426abae234ab2.1790007492496.1790007492496.1790007492496.1&__hssc=204114447.4.1790007492496&__hsfp=04ef42812f9b1b780e77a1fe02c5e4b1&submissionGuid=2929d1ec-0502-4a50-adb1-6611983dfb1f" 
        frameborder="0" 
        allow="accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
        allowfullscreen>
</iframe>

---
# Requests for Proposals (RFP)
## How GIS happens in the working world
A Request for Proposal (RFP) is a formal document issued by a client (e.g., a municipality or private developer) seeking bids from consultants. 

Generally speaking, it consists of three components:
- **Objective:** Defines the problem that needs solving.
- **Scope of Work:** Outlines the required deliverables (maps, databases, web apps).
- **Evaluation Criteria:** How the proposal will be judged.

---
## RFP examples
From international orgs like the UN to cities:
- [IUCN](https://hrms.iucn.org/iresy/index.cfm?event=vac.offline.download&offline_vacancy_id=6810)
- [UNESCO](https://articles.unesco.org/sites/default/files/medias/fichiers/2025/03/RFP_GIS%20Mapping%20and%20Condition%20Assessment.pdf)
- [Santa Clara, CA, USA](https://media.governmentnavigator.com/media/bid/1721945976_2024-07-25_24-25-02.pdf)
- [Missoula, MT, USA](https://www.ci.missoula.mt.us/DocumentCenter/View/80743/RFP_GIS-Boundary-Alignment?bidId=)
- [Clarington](https://clarington.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/56fc03bc-99ce-4b6a-8496-5d51bf0a0271)
- [Orangeville](https://orangeville.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/06568e6f-8483-428f-886e-19280151e595)
- [Inuvialuit](https://irc.inuvialuit.com/wp-content/uploads/2024/12/241106_Lands-GIS-RFQ-2.pdf)

---
## Application 1: RFP
**Background**

Your goal is to envision yourself as a client in need of GIS and to solicit help from experts.

- What kind of client? e.g. city, private business, NGO
- What kind of problem are you trying to solve? What data and analytical techniques might address the problem?
- What kind of info, in what format, do you need at the end of the day?

---
## Application 1: RFP
**Considerations**

The scope of work should be equal to or greater than a Tutorial, but not a PhD dissertation.

---
## Application 1: RFP
**Prompt**

In three paragraphs (approximately 300 words), write the following:
1. **background** - e.g. "The City of X is a mid-sized municipality in ..."
2. **objective** - e.g. "Business X solicits bids to help it determine optimal locations for two new warehouses in the Y region." Any important factors (e.g. the importance of wetlands in the analysis), constraints (e.g. fire stations cannot be built on private property), and assumptions (e.g. people will drive no more than 15 minutes to get to the store) go here.
3. **scope of work** - e.g. "The successful applicant will provide Y product." 

---
## Application 1: RFP
**Submission**

(Anonymous) posting to the Courselink Discussion Board

---
## Application 1: RFP
**Assessment**

You will be assessed on:
- **clarity and specificity**: Is it obvious what the problem is and what the contractor is generally expected to do? Is there enough detail for someone to know more or less what to do?
- **feasability**: Do the data exist publicly? Could this be done within the confines of the course? Would _you_ want to do it?
- **logic and realism**: Does the scenario you've crafted make sense? A scenario in which a business asks for help determining where to put a fire station isn't logical.
- **novelty**: Does the scenario help you/classmates explore new aspects of techniques we're learning? (e.g. using a different kind of location-allocation approach instead of Maximize Market Share)

---
# Tutorial preview: Location-Allocation

<div class="split-slide" markdown="1">

<div markdown="1">

This map displays the most suitable of four hypothetical grocery stores, with lines illustrating how much demand would be allocated to it, assuming:

* Existing stores would compete with the new one
* Consumers travel no more than 10 minutes for groceries
* Consumers have no other preferences (e.g. between smaller and larger shops)

</div>

<div markdown="1">

![Location-Allocation]({{ site.baseurl }}/assets/images/la.png)

</div>

</div>