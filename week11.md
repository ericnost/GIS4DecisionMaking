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
<div class="split-slide" markdown="1">
<div markdown="1">

_Bivariate = bivariable = two measures_

**Does not necessarily mean the [[Bivariate Colors](https://doc.esri.com/en/arcgis-pro/latest/help/mapping/layer-properties/bivariate-colors.html)] option in ArcGIS Pro**, especially when we're talking about mixed data types.

["Vary [unique values] symbology by attribute"](https://doc.esri.com/en/arcgis-pro/latest/help/mapping/layer-properties/attribute-driven-symbology.html) is the way to go when we have quantitative/ratio data like # of squirrels alongside qualitative/categorical data like squirrel type.

</div>
<div markdown="1">
![Example bivariate colour scheme](https://doc.esri.com/en/arcgis-pro/latest/help/mapping/layer-properties/images/Sym_BivariateColors_ex-A97E1.png)

</div>
</div>

---
# Indices
A better way to bivariate (or trivariate, quadvariate?, etc.) map!

_Indices = two or measures of the same data type (e.g. ratio) combined (averaged, weighted, etc.) into one_

Suitability is an index (my bad)

**Indices, indices everywhere!** They rule our world...Why? Because they make accounting for multiple factors easier for decision-makers, especially over time.

---
# Indices - ECCC example
<div class="split-slide" markdown="1">
<div markdown="1">
You want to understand the intersection of environmental risk and social marginalization.

You know the former is complex, but you reduce it to a simple count of industrial hazards nearby (_not_ an index)

You know the latter is complex, and would be really challenging to reduce - to pick just one element (e.g. poverty). It would also be really challenging to look at poverty, race, Indigeneity, education, unemployment, etc. separately. So, you combine them.

But you still have to compare two pieces of information at once - hazards and marginalization. A bivariate map could work, but often requires mapping 9+ classes. **So you combine these too!**
</div>

<div markdown="1">
![ECCC EEPCI](https://www.canada.ca/content/canadasite/en/environment-climate-change/services/strategic-policy-branch/environmental-justice/national-strategy/_jcr_content/par/mwsadaptiveimage_444602579/image.img.png/1792691758565.png)
</div>

</div>

---
# Indices - more examples
- **inflation** = percent changes in the Consumer Price Index which is a weighted "market basket"
- **stock market** (e.g. S&P 500, Nasdaq, DJIA, S&P/TSX)
- [**small-town vitality**](https://www.guelphtoday.com/local-news/how-local-data-is-helping-canadas-main-streets-fight-back-13045985)
- **habitat suitability** ([Louisiana example](https://coastal.la.gov/wp-content/uploads/2023/08/C10_2023HSIModel_Feb2023_v3.pdf))
- **NDVI** ([greenness](https://www.esri.com/arcgis-blog/products/arcgis-pro/imagery/automate-agriculture-monitoring-with-satellite-imagery-and-raster-analytics))
- **Canadian Index of Multiple Deprivation**
- [Canadian indexes of **social resilience and vulnerability to natural hazards**](https://open.canada.ca/openmap/en.html#11345e77-f6ab-4a10-9c53-06a874135b07)

---
# Indices - baselines
<div class="split-slide" markdown="1">
<div markdown="1">
Often the goal is tracking change over time in complex systems. So we set a baseline for our index.

Example: inflation
</div>

<div markdown="1">
![Inflation indexed to 100 example](https://static.haver.com/251114_ML_1_f60a936f4b.jpg)

[Source](https://www.haver.com/)
</div>
</div>

---
# Mapping indices
<div class="split-slide" markdown="1">
<div markdown="1">
Field calculations! e.g. NDVI ... `(NIR - Red) / (NIR + Red)`

Suitability modeler

Examples: [climate change performance index](https://ccpi.org/)
</div>

<div markdown="1">

![NDVI map](https://geoawesome.com/wp-content/uploads/2022/03/NDVI-image-Drone-Remote-Sensing-Geoawesomeness.png)

[Source](https://geoawesome.com/eo-hub/understanding-aerial-data-normalized-difference-vegetation-index-ndvi/)
</div>
</div>
---
# Indices - key limitations
They are, by definition, made-up numbers. Sometimes we adjust them to a 100 point scale to make them feel more familiar, but they are still made-up!

What does an EEPCI of 16 mean? The 16 itself isn't important (but it does mean all underyling quartile values were high)

**Complexity** - indices of indices (e.g. ECCC's EEPCI)

**Transparency** - how do we know what these values mean concretely? 

**Averaging** - by averaging different measures, we wash out counter trends in single variables

---
# Dashboards
<div class="split-slide" markdown="1">
<div markdown="1">
Dashboards are a kind of interactive report that gives CEOs, councillors, the public, etc. high level insights into trends, performance (KPIs), etc.

Basic examples: 
- [Bank of Canada inflation dashboard](https://www.bankofcanada.ca/rates/indicators/inflation-dashboard/cpi-inflation/)
- [City of Toronto](https://www.toronto.ca/city-government/data-research-maps/toronto-dashboard/)

</div>
<div markdown="1">
![Wikimedia dashboard example](https://upload.wikimedia.org/wikipedia/commons/b/b7/Infruid%27s_Self-Service_BI_Tool_Dashboard.jpg)
![Car dashboard](https://upload.wikimedia.org/wikipedia/commons/8/8a/Bentley_Continental_GTC_011.JPG)
</div>

---
# Dashboards - map-based examples

These often enable filtering data based on location, hence tailoring insights to place

- [JHU Covid-19](https://coronavirus.jhu.edu/map.html)
- [City of Guelph Collision Dashboard](https://experience.arcgis.com/experience/7112203aa8f0418aa94551003e070d3a/page/Collision-Dashboard)
- [AR controlled substance monitoring](https://www.arcgis.com/apps/dashboards/4b314711d252496d941048cd4867ab85#)
- [Clean water in PR](https://www.arcgis.com/apps/dashboards/c758a461e4174023b73fe988a0fc3d0e#)
- [Species Protection Index](https://mol.org/dashboard/indicators?layer=species-protection-index)
- [Agricultural Productivity in Lebanon](https://www.esri.com/arcgis-blog/products/arcgis-pro/imagery/automate-agriculture-monitoring-with-satellite-imagery-and-raster-analytics)

---
# GIS reports
People still live in the material world and like to be able to print things. You can't really print an interactive dashboard. 

[EJScreen report example](https://pedp-ejscreen.azurewebsites.net/)

---
# Tutorial preview: Dashboards
<div class="split-slide" markdown="1">
<div markdown="1">

In part 1, this/last week you re-created the index calculations for ECCC's EEPCI. In part 2, you will create a dashboard to present the results.

</div>
<div markdown="1">

<iframe src="https://uofguelph.maps.arcgis.com/apps/dashboards/4f1fb27308a340f8bfeab2cb4952da91" width="100%" height="800px"></iframe>


</div>
</div>