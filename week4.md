---
layout: lectures
title: "Week 4: Modelling Accessibility"
permalink: /lectures/week-04/
---

# Week 4
## Modelling Accessibility

Access concepts, 2SFCA, Model Builder and toolboxes, Routing tutorial preview

---
# Access
<div class="split-slide" markdown="1">
<div markdown="1">
> Modeling movement opportunity
> An attribute that reflects how easy it is to reach destinations that enable participation in different activities ([Source](https://www.sciencedirect.com/science/article/pii/S2214367X25001693))
- Supply and demand 
- Last week we focused on assigning service areas and siting facilities. Goals included maximizing access/coverage, minimizing facilities, minimizing travel time, etc. Now we want to measure existing access.
</div>
<div markdown="1">
![Copenhagen 15 minute city map](https://ars.els-cdn.com/content/image/1-s2.0-S2214367X25001693-gr4_lrg.jpg)
[Source](https://www.sciencedirect.com/science/article/pii/S2214367X25001693)
</div>
</div>

---
# Networks
- Unless you’re a bird (you're not), movement happens along a network
> **network**: A collection of nodes, and links between nodes, that describe discrete movement opportunities in space. 
> **isochrone**: A line of equal time travel used to map how far one can travel in a given amount of time from a particular focal location. 
- compare with service area
- [Mapbox example](https://docs.mapbox.com/playground/isochrone/)
- [Commute time map](https://commutetimemap.com/map?places=43.549381%253B-80.224560%253B2%253B900%253B%25234143f4)
- [Google Maps isochrones](https://maps.google.com)
---
# Measuring accessibility
> Calculation of the distance, time, or cost distance between two (or more) locations
> Accessibility is influenced both by the location of an individual to the locations of potential destinations (and the distances between). 
Thus, measures of accessibility are **a joint function of the distance (geographical distance, travel time, or cost distance) required to reach destinations and the number (and/or variety) of potential destinations available**
> The level of accessibility from a given place reflects the distribution of destinations around it, the ease with which those destinations can be reached by various modes, and the amount and character of the activity found there. Accessibility depends on the individual’s needs, abilities and opportunities; the characteristics of the land use and transport systems; and time restrictions [Source](https://www.sciencedirect.com/science/article/pii/S2214367X25001693)
- opportunity measures, gravity-based measures, utility-based measures, and space-time measures

---
# Opportunity measures
<div class="split-slide" markdown="1">
<div markdown="1">
> Count the number of potential destinations that can be reached within a given distance measurement for an individual.
> Opportunity measures are straightforwardly calculated in a GIS using geographical buffers, network based isochrones, or accumulated cost surfaces...
</div>
<div markdown="1">
![Puerto Alegre isochrones](https://ipeagit.github.io/r5r/articles/isochrones_files/figure-html/unnamed-chunk-8-1.png)
[Source](https://ipeagit.github.io/r5r/articles/isochrones.html)
</div>
</div>

---
# Other measures
- **Gravity** - destinations are weighted by their relative distance from the individual, for example destinations that are closer are given a higher weight than destinations further away. 
- **Utility** - desirability of the full complement of destinations
- **Space-time** – accessibility as a function of both space and time
- Distance to the nearest **destination of interest**
- **Perceived vs objective**

> **Individual-based** accessibility measures are possible when individual data are present, for example from geolocated cell phone records. In contrast, accessibility measures can also be calculated for specific **places** (e.g., bus stops, police stations, census blocs). 

---
# Constraints
Limit the set of potentially accessible locations
- **Capability** constraints e.g. disability
- **Coupling** constraints e.g. face to face
- **Authority** constraints e.g. times things are open

---
# Aggregation of accessibility measures
<div class="split-slide" markdown="1">
<div markdown="1">
> Often it is useful to summarize the accessibility of regions (e.g., census blocs or counties) to generalize (and map) a measure of accessibility across the population. 

Where to start? Four kinds of methods:
- Take the centroid of a neighborhood
- Population-weighted centroid when we have an idea of how pop is distributed
- Sampling
- Critical locations
</div>
<div markdown="1">
![Copenhagen population grid](https://ars.els-cdn.com/content/image/1-s2.0-S2214367X25001693-gr3_lrg.jpg)
[Source](https://www.sciencedirect.com/science/article/pii/S2214367X25001693)

![Beijing population distribution](https://www.tandfonline.com/cms/asset/04e73ece-086b-435d-9aa1-6fb7e526d79f/tjde_a_2479864_f0003_oc.jpg)
[Source](https://www.tandfonline.com/doi/full/10.1080/17538947.2025.2479864#d1e1784)
</div>
</div>

---
# Solutions
Demand
> Origin driven solutions attempt to improve the movement opportunities of individuals (or regions), for example by improving public transit options.

Supply
> Destination driven solutions attempt to improve the provision of destinations, for example by adding or changing locations.

---
# The 15-minute city
<div class="split-slide" markdown="1">
<div markdown="1">
> ...an urban planning framework intended to set up communities in such a way that they would have access to all their needs within a 15-minute walk or bike ride from their homes 

</div>
<div markdown="1">
![Calgary neighbourhood 15 minute 1km map](https://images.squarespace-cdn.com/content/v1/588e65d737c5818a6a061678/bcd16ac3-78b3-48ae-921c-8cfcd8d60d7f/6.We+Live+in+a+15-Minute+Neighbourhood%21.JPG)
[Source](https://www.hsca.ca/blog/2022/4/1/we-live-in-a-15-minute-neighbourhood)
</div>
</div>

---
# The 15-minute city
_How would you do it?_

---
# The 15-minute city
<div class="split-slide" markdown="1">
<div markdown="1">
[Ottawa Example](https://ottawacitizen.com/news/local-news/maps-illustrate-challenge-with-creating-15-minute-neighbourhoods-in-built-up-areas)
[Ottawa 15-minute City Planning](https://ehq-production-canada.s3.ca-central-1.amazonaws.com/792ae0ee2ee9af625a4061e96c2c6269918e5a88/original/1625496759/85e7468e61481a3be9541fb09b7b9007_15_min_Neighbourhood_March_30_presentation_for_web_ua.pdf)
</div>
<div markdown="1">
![Ottawa 15 minute city map](https://smartcdn.gprod.postmedia.digital/ottawacitizen/wp-content/uploads/2021/08/15_minute_neighbourhoods_riverside_south_86951372-w.jpg?quality=90&strip=all&w=1128&h=846&type=webp&sig=j6Tsw0Pdg6TvpdbAUR9d7w)
[Source](https://ottawacitizen.com/news/local-news/maps-illustrate-challenge-with-creating-15-minute-neighbourhoods-in-built-up-areas)
</div>
</div>

---
# The 15-minute city
> Hundreds of people poured into a special public meeting in Essex County in southwestern Ontario earlier this month where many believed officials would be discussing 15-minute cities — even though County of Essex officials stressed that wasn't the case. 
The meeting was cut short because of the size of the crowd — and left officials surprised by the response.
Not only is the 15-minute-city concept not a part of County of Essex's plans — the concerns being raised by some residents are in line with what some experts describe as conspiracy theory thinking rather than rooted in what the concept is actually about.
[Source](https://www.cbc.ca/news/canada/windsor/15-minute-city-conspiracy-theory-essex-county-council-1.6808005)

---
# Two-Step Floating Catchment Area (2SFCA) model

<div class="split-slide" markdown="1">
<div markdown="1">
A spatial analysis method to measure population accessibility to service providers, such as healthcare facilities or parks, by comparing local supply and demand.

The two steps:
1 - calculate provider to population ratio (supply to demand ratio)
2 - sum these ratios within each population’s demand area

Not actually a standard tool in any GIS software! But others have built it as a toolbox we can download and use. [See here](https://www.arcgis.com/home/group.html?id=2bf20ef893594b6381a48fc142059ee2#overview).

</div>
<div markdown="1">
![Beijing emergency shelter 2SFCA](https://www.tandfonline.com/cms/asset/93a993e1-5d56-462d-bb2d-3c6e4786925c/tjde_a_2479864_f0005_oc.jpg)
[Source](https://www.tandfonline.com/doi/full/10.1080/17538947.2025.2479864#d1e1784)
</div>
</div>

---
# Model Builder and Toolboxes
When we have frequent workflows we might not want to recreate them click by click every time. A model can help. E.g. buffer and intersect X data. And it can also be generalized in many cases to different data e.g. Y, Z data.
- Create a model that accepts variable input e.g. amount to buffer
- Save as toolbox
- Share (export or publish to web)
  - [Publishing web tools](https://www.esri.com/arcgis-blog/products/arcgis-pro/sharing-collaboration/publishing-web-tools-just-got-easier-in-arcgis-pro)

---
# Tutorial preview: Routing
<div class="split-slide" markdown="1">
<div markdown="1">
Imagine Amazon is now delivering by bike, from their new “warehouse” (the Hutt building, because why not?) 

Identify the optimal route for delivering these 6 packages based on Guelph's road/bike lane network, where bike lanes are weighted better (less impedance) than streets. The bikes _can_ go on open roads, but it’s more “costly” (not necessarily in terms of time/speed, but risk/safety)
</div>
<div markdown="1">

![Routing tutorial result]({{ site.baseurl }}/assets/images/routing.png)

</div>
</div>


