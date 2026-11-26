---
layout: lectures
title: "Week 11: Indices and Dashboards"
permalink: /lectures/week-11/
---

# Week 11
## Indices and Dashboards

Bivariate maps, indices, tutorial preview: dashboards

---
# Bivariate maps
_Bivariate = bivariable = two measures_

**Does not necessarily mean the Bivariate symbology option in ArcGIS Pro**, especially when we're talking about point data.

"Vary [unique values] symbology by attribute" is the way to go when we have quantitative/ratio data like # of squirrels alongside qualitative/categorical data like squirrel type.

[Example bivariate map]

---
# Indices
A better way to bivariate (or trivariate, quadvariate?, etc.) map!

_Indices = two or measures of the same data type (e.g. ratio) combined (averaged, weighted, etc.) into one_

Suitability is an index (my bad)

**Indices, indices everywhere!** They rule our world...Why? Because they make accounting for multiple factors easier for decision-makers, especially over time.

---
# Indices - ECCC example
You want to understand the intersection of environmental risk and social marginalization.

You know the former is complex, but you reduce it to a simple count of industrial hazards nearby (not an index)

You know the latter is complex, and would be really challenging to reduce - to pick just one element (e.g. poverty). It would also be really challenging to look at poverty, race, Indigeneity, education, unemployment, etc. separately. So, you combine them.

But you still have to compare two pieces of information at once - hazards and marginalization. A bivariate map could work, but often requires mapping 9+ classes. So you combine these too!

[ECCC tables/maps]

---
# Indices - more examples
- inflation
- stock market
- [small-town vitality](https://www.guelphtoday.com/local-news/how-local-data-is-helping-canadas-main-streets-fight-back-13045985)
- habitat suitability
- NDVI
- Canadian Index of Multiple Deprivation

---
# Indices - baselines
Often the goal is tracking change over time in complex systems. So we set a baseline for our index.

Example: inflation

---
# Mapping indices
Field calculations! e.g. NDVI

Suitability modeler

Examples: climate change indices

---
# Indices - key limitations
They are, by definition, made-up numbers. Sometimes we adjust them to a 100 point scale to make them feel more familiar, but they are still made-up!

What does an EEPCI of 16 mean? The 16 itself isn't important (but it does mean all underyling quartile values were high)

Transparency - how do we know what these values mean?

Averaging - by averaging different measures, we wash out counter trends in single variables

---
# Dashboards

Definition - car analogy. Decision-makers are car drivers?

They are a kind of interactive report that gives CEOs, councillors, the public, etc. high level insights into trends, performance, etc.

---
# Dashboards - examples

JHU Covid-19
City of Toronto
climate?

---
# GIS Reports

EJScreen

---
# Tutorial preview: Dashboards
<div class="split-slide" markdown="1">
<div markdown="1">

In part 1, this/last week you re-created the index calculations for ECCC's EEPCI. In part 2, you will create a dashboard to present the results.

</div>
<div markdown="1">

![ECCC EEPCI dashboard]({{ site.baseurl }}/assets/images/dashboards.png)

</div>
</div>