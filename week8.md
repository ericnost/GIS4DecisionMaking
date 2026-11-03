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
Do the thing

You can always switch

Write it up in ~200 words

**_You must include the RFP you are responding to in your bid._**

Submit to the Courselink Dropbox

You may also post to the original RFP on the Discussion Board

---
# APIs
<div class="split-slide" markdown="1">
<div markdown="1">
GIS API: 

> “collections of library modules that resemble various functionalities of GIS software through programming”

Well, what is a library module? In this case, a bundle of software code 

> "GIS APIs provide a communication protocol to handle client requests and return the processed response back from a server that provides GIS functionalities and/or datasets as a service"

Advantages:
- interoperability (GIS without Windows)
- light-weight (no desktop GIS or plug-ins)

[Source](https://gistbok.ucgis.org/bok-topics/2022-quarter-02/conceptual-models-error-and-uncertainty)
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
Everything related, near things more related than distant ones

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
>  “the dependence between the values of one attribute due to spatial proximity.”

Measures to detect this: Global and Local Indicators of Spatial Association

</div>
<div markdown="1">
![Deterministic vs stochastic model](https://upload.wikimedia.org/wikipedia/commons/d/dc/Process-based-stochastic-modelling.png?utm_source=commons.wikimedia.org&utm_campaign=index&utm_content=original)

[Source](https://commons.wikimedia.org/wiki/File:Process-based-stochastic-modelling.png)
</div>
</div>

---
# Conceptualizing spatial relationships
How are phenomena related in space?

- weighting based on distance (e.g., inverse distance or inverse distance squared; fixed radius; k nearest neighbors) for point data, 
  -  Inverse distance or inverse distance squared relationships involve nearer observations having a stronger influence and that influence decaying with increasing distance; this relationship is commonly applied to continuous data, such as temperatures or air pressures
  - Fixed radius relationships apply the same influence to all points within a fixed radius of neighborhood area
  - k nearest neighbors ensures that every observation has a specified number of neighbors, “k,” a relationship often applied when the density of observations varies widely across the study region”
- spatial contiguity (e.g., Rook’s case; Queen’s case) for polygon data

---
# Spatial autocorrelation patterns
<div class="split-slide" markdown="1">
<div markdown="1">

Positive spatial autocorrelation (clustering)
No spatial autocorrelation (random)
Negative spatial autocorrelation (dispersion)

</div>
<div markdown="1">
![Land loss in s. Louisiana 1932-2011](https://www.climate.gov/sites/default/files/2022-01/LandLossinSouthernLouisiana1932_vs_2011_ani_0.gif)

[Source](https://www.climate.gov/media/13990)
</div>
</div>

---
# Global vs Local
<div class="split-slide" markdown="1">
<div markdown="1">
> Global measures of spatial autocorrelation give one single statistic that summarizes whether the values (of the single variable) are similar to their neighbors across the entire study region. It, however, does not tell us where the similarity (or dissimilarity) occurs

</div>
<div markdown="1">
![Louisiana Master Plan models]({{ site.baseurl }}/assets/images/lamp_models.png)
</div>
</div>

---
# Clusters vs Outliers
Z scores = (see EJSCREEN tech doc)

Large positive z score (e.g. z > +1.96) indicates that the observation and its neighbors have significantly similar values (spatial clusters consisting of _either high or low values_). 

Large negative z score (e.g., z < -1.96) indicates that the value at observation i is significantly different than its neighbors (i.e., spatial outliers).


---
# Applications
-	“Recent applications include identifying disproportionate burdens of disease transmission in areas with certain sociodemographic characteristics (Chang et al., 2017), discovering local areas most prone to crime (Malleson & Andresen, 2015), and recognizing soil contamination hotspots of rare earth elements or heavy metals (Yuan et al., 2018; Wu & Johnston, 2019).”

ECCC study

---
# Tutorial preview: Public Participation GIS with Survey123 - Part 1
<div class="split-slide" markdown="1">
<div markdown="1">
You will create Squirrel Spotter!
</div>
<div markdown="1">

![EJ tutorial with spatial statistics]({{ site.baseurl }}/assets/images/spatialstats.png)

</div>
</div>

