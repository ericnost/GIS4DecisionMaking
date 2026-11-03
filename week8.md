---
layout: lectures
title: "Week 8: Spatial Statistics"
permalink: /lectures/week-08/
---

# Week 8
## Spatial Staistics

APIs, API demos, analysis assignment, spatial association and spatial statistics, tutorial preview: Survey123 

---
# Application 3 - Analysis
Do the thing!

**You can always switch projects if need be**

Write it up in ~200 words

Submit to the Courselink Dropbox

You may also post to the original RFP on the Discussion Board

**_You must include the RFP you are responding to in your bid._**

---
# GIS APIs
<div class="split-slide" markdown="1">
<div markdown="1">
GIS APIs as software: 

> “collections of library modules that resemble various functionalities of GIS software through programming”

Well, what is a library module? In this case, a bundle of software code.

Example: [`Geopandas`](https://geopandas.org/en/stable/docs.html) [code](https://github.com/geopandas/geopandas/blob/main/geopandas/tools/sjoin.py)
GIS functionalities: [projections](https://geopandas.org/en/stable/docs/user_guide/projections.html), [geocoding](https://geopandas.org/en/stable/docs/user_guide/geocoding.html), [overlay](https://geopandas.org/en/stable/docs/user_guide/set_operations.html), [spatial joins](https://geopandas.org/en/stable/docs/user_guide/mergingdata.html)
</div>
<div markdown="1">
![Louisiana climate sea level rise scenarios]({{ site.baseurl }}/assets/images/cc_scenarios.png)
</div>
</div>

---
# GIS APIs
GIS APIs as communication protocols
> "GIS APIs provide a communication protocol to handle client requests and return the processed response back from a server that provides GIS functionalities and/or datasets as a service"

Example: [Mapbox](https://docs.mapbox.com/api/navigation/directions/)
Functionalities: routing/navigation as a service

Advantages:
- interoperability (GIS without Windows)
- light-weight (no desktop GIS or plug-ins)

</div>
<div markdown="1">
![Louisiana climate sea level rise scenarios]({{ site.baseurl }}/assets/images/cc_scenarios.png)
</div>
</div>

---
# GIS APIs - Examples
<div class="split-slide" markdown="1">
<div markdown="1">
-	EJSCREEN ([ArcGIS for JS](https://developers.arcgis.com/javascript/latest/))
-	EJAM-API ([https://api.ejanalysis.com/](https://api.ejanalysis.com/))
- Google Maps Places API (New) - [Grocery stores in Guelph example](https://colab.research.google.com/drive/1larRMJEQ1uqJJzWrfTakeVpSJM4jhO4w?usp=sharing)
- Censusmapper.ca walkthrough
- eBird tutorial

</div>
<div markdown="1">
![Robust decision-making diagram](https://media.springernature.com/full/springer-static/image/chp%3A10.1007%2F978-3-030-05252-2_2/MediaObjects/427530_1_En_2_Fig1_HTML.png)

[Source](https://link.springer.com/chapter/10.1007/978-3-030-05252-2_2)
</div>
</div>

---
# Statistics and Decision-Making
ECCC study

"Trust in Numbers" - decision-makers seek legitimacy for their actions by pointing to statistics

_Spatial_ statistics are those that involve some notion of spatial association

So, calculating an odds ratio based on counts per dissemination may be _geographical_ in the sense that the measures pertain to space, the odds ratio isn't a _spatial statistic_

---
# First Law of Geography
<div class="split-slide" markdown="1">
<div markdown="1">
Everything is related, but near things are more related than distant ones

_Is it always true though?_
</div>

<div markdown="1">
![Wikipedia climate model diagram](https://thumb.wikimedia.org/wikipedia/commons/thumb/4/43/20250712_Climate_model_inputs_and_outputs.svg/1920px-20250712_Climate_model_inputs_and_outputs.svg.png?utm_source=en.wikipedia.org&utm_campaign=imageinfo&utm_content=thumbnail)

[Source](https://en.wikipedia.org/wiki/Climate_model)
</div>
</div>

---
# Spatial association
<div class="split-slide" markdown="1">
<div markdown="1">

> how events, measurements or places are related in space.

Clustered, dispersed, random?

How to assess:
> ...the distance between nearby observations ... whether the value of observations at nearby locations are similar [i.e. autocorrelated]...

</div>
<div markdown="1">
![Process model - ArcGIS workflow](https://bok-figures.s3.amazonaws.com/files/AM20_Fig1.png)
</div>
</div>

---
# Spatial autocorrelation
<div class="split-slide" markdown="1">
<div markdown="1">

> the dependence between the values of one attribute due to spatial proximity.

Specific measures to detect this: Global and Local Indicators of Spatial Association

</div>
<div markdown="1">
![Deterministic vs stochastic model](https://upload.wikimedia.org/wikipedia/commons/d/dc/Process-based-stochastic-modelling.png?utm_source=commons.wikimedia.org&utm_campaign=index&utm_content=original)

[Source](https://commons.wikimedia.org/wiki/File:Process-based-stochastic-modelling.png)
</div>
</div>

---
# Conceptualizing spatial relationships
<div class="split-slide" markdown="1">
<div markdown="1">
How are phenomena related in space?

- point-based: weighting based on distance
  -  "Inverse distance or inverse distance squared relationships involve nearer observations having a stronger influence and that influence decaying with increasing distance; this relationship is commonly applied to continuous data, such as temperatures or air pressures"
  - "Fixed radius relationships apply the same influence to all points within a fixed radius of neighborhood area"
  - "k nearest neighbors ensures that every observation has a specified number of neighbors, “k,”"
- polygon-based: spatial contiguity (Queen/Rook)

</div>
<div markdown="1">
![ArcGIS Moran's I report](https://raw.githubusercontent.com/HughSt/HughSt.github.io/master/_posts/Week-4-spatial-clustering_updatedMar19_files/figure-gfm/unnamed-chunk-14-1.png)

[Source](https://hughst.github.io/week-4/)
</div>
</div>

---
# Spatial autocorrelation patterns
<div class="split-slide" markdown="1">
<div markdown="1">

> > Often, you will run one of the pattern analysis tools, hoping that the z-score and p-value will indicate that you can reject the null hypothesis, because it would indicate that rather than a random pattern, your features (or the values associated with your features) exhibit statistically significant clustering or dispersion. Whenever you see spatial structure such as clustering in the landscape (or in your spatial data), you are seeing evidence of some underlying spatial processes at work, and as a geographer or GIS analyst, this is often what you are most interested in.

[Source](https://pro.arcgis.com/en/pro-app/3.4/tool-reference/spatial-statistics/what-is-a-z-score-what-is-a-p-value.htm)

- Z scores = standard deviations above/below a mean (score - mean / standard deviation)
- Standard deviation = square root of variance
- Variance = difference between each value and the mean, squared and averaged

Interpretation:
- Positive spatial autocorrelation (clustering)
- No spatial autocorrelation (random)
- Negative spatial autocorrelation (dispersion)

</div>
<div markdown="1">
![ArcGIS Moran's I report](https://upload.wikimedia.org/wikipedia/commons/f/fc/UnitedStates2022_Population_MoransI_Report.png)

[Source](https://en.wikipedia.org/wiki/Spatial_analysis#Spatial_dependence)
</div>
</div>

---
# Global vs Local
<div class="split-slide" markdown="1">
<div markdown="1">
> Global measures of spatial autocorrelation give one single statistic that summarizes whether the values (of the single variable) are similar to their neighbors across the entire study region. It, however, does not tell us where the similarity (or dissimilarity) occurs.

</div>
<div markdown="1">
![Louisiana Master Plan models]({{ site.baseurl }}/assets/images/lamp_models.png)
</div>
</div>

---
# Clusters vs Outliers
Large positive z score (e.g. z > +1.96) indicates that the observation and its neighbors have significantly similar values (spatial clusters consisting of _either high or low values_). 

Large negative z score (e.g., z < -1.96) indicates that the value at observation i is significantly different than its neighbors (i.e., spatial outliers).


---
# Applications
- Statistical: interpolation (Kriging, IDW)
-	Policy: public health, crime, environmental justice

ECCC study

---
# Tutorial preview: Public Participation GIS with Survey123 - Part 1
<div class="split-slide" markdown="1">
<div markdown="1">
You will create Squirrel Spotter!!! Decision-making is only as good as the information behind it, but typically that information lacks local perspective. Ordinary individuals can be invaluable sources of data on public issues, because scientists and officials often lack capacity to gather localized data or are uninterested in it. 

Imagine we need to know more about Guelph's squirrel population - where different kinds are when. Sure, we could hire a bunch of wildlife biologists to do surveys, but basic squirrel identification can be done by laypeople. Esri built the Survey123 tool to help collect such information.
</div>
<div markdown="1">

![EJ tutorial with spatial statistics]({{ site.baseurl }}/assets/images/spatialstats.png)

</div>
</div>

