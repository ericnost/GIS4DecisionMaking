---
layout: lectures
title: "Week 3: Location-Allocation"
permalink: /lectures/week-03/
---

# Week 3
## Location-Allocation

Location modeling problems, data management check-in, RFP/Application 1 brainstorm, 2SFCA tutorial preview

---
# Service and catchment areas
<div class="split-slide" markdown="1">
<div markdown="1">
- **Catchment area**: conceptual territory being served or accessed
- **Service area**: the technical implementation of CA, what the model deems to be "the geographical area where the intended service of a facility is effectively received"
- SA **model parameters**: predetermined ranges such as travel distance/time or nearest facility
  - Euclidean distance e.g. cell tower coverage. Tools: buffer
  - Relative distance, including network distance e.g. travel time for fire truck. Tools: Service Area, Viewshed
- Sometimes the SA is "fixed" (e.g. fire trucks have a 5 minute service area) and sometimes we need to determine it (e.g. who are the store's customers?)
- Used in retailing, communication, banking, transportation, health care, emergency response
- CA/SA sometimes used interchangeably
</div>
<div markdown="1">

![Service areas](https://bok-figures.s3.amazonaws.com/files/AM43_Fig1.png)
[Source](https://gistbok-ltb.ucgis.org/current/concept/AM-05-043)

</div>
</div>

---
# Who does my public transit system serve?
![Bus stop service areas](https://www.esri.com/arcgis-blog/app/uploads/2016/06/A2ServiceAreas1.png)

[Source](https://www.esri.com/arcgis-blog/products/network-analyst/transportation/who-does-my-public-transit-system-serve)

---
# Location modeling
Use of linear programming/optimization algorithms to selection locations that achieve policy/profit goals like providing services, while minimizing costs

"Minimize/maximize x subject to y"

---
# LSCP (location set covering problem)
Definition: location model constructed to **find the minimum number of facilities for providing full service coverage** to a region. "Minimize x (number of facilities) subject to meeting each demand"
- For applications where facilities have a fixed service range
- **Which facilities/locations do we need to cover _all_ demand?**

Put another way:
- Goal: Minimize the number of facilities.
- Rule ("subject to"): Cover 100% of demand points within a maximum time or distance limit (e.g. placing fire stations so every home is within a 5-minute drive).

---
# LSCP examples
<div class="split-slide" markdown="1">
<div markdown="1">
> "Solving the problem gives the optimal solution: XA = 1, XB = 1, XC = 1, XD = 0. That is, to cover all demand in Figure 3, at least three facilities are required, and these facilities need to be sited at A, B, and C." 

Say what?
</div>
<div markdown="1">

![Service areas](https://bok-figures.s3.amazonaws.com/files/AM43_Fig3.png)
[Source](https://gistbok-ltb.ucgis.org/current/concept/AM-05-043)

</div>
</div>

---
# LSCP examples
Let's learn some computer programming while we're at it...
- [allagash](https://apulverizer.github.io/allagash/examples/LSCP.html)
- [allagash in ArcGIS](https://apulverizer.github.io/allagash/examples/Using%20ArcGIS.html)
- [ArcGIS tool - "Maximize Coverage, Minimize Facilities"](https://pro.arcgis.com/en/pro-app/3.6/help/analysis/networks/location-allocation-analysis-layer.htm)

---
# What we just saw
Python package: an interconnected set of modules and functions that help users solve (general) problems, such as organizing (spatial) data

Pro: we don't have to re-invent the wheel ourselves. Packages are infrastructure to make our lives easier

Con: inherently some "black-boxing" going on

```
import geopandas as gpd
import pandas as pd

# Use pandas to organize this data in tabular form (a la Excel)
data = {
    'city': ['Montreal', 'Toronto', 'Vancouver'],
    'longitude': [-73.5673, -79.3832, -123.1216],
    'latitude': [45.5017, 43.6532, 49.2827]
}
df = pd.DataFrame(data)

# Convert it to spatial data (a la ArcGIS) with geopandas
gdf = gpd.GeoDataFrame(
    df, 
    geometry=gpd.points_from_xy(df['longitude'], df['latitude']), 
    crs='EPSG:4326' # WGS 84 coordinate reference system
)
```

Jupyter Notebook: Tool for executing code, recording output, and contextualizing. Enables reproducibility. Platforms include Google Colab and ArcGIS Pro.


---
# MCLP (maximal covering location problem)
Definition: location model constructed to **find the _best_ locations of a number of facilities for achieving the maximal service coverage**. "Maximize coverage of demand subject to limited facilities"
-	When resources are insufficient for full coverage of a region
-	**Which of p facilities/locations cover the most demand?**

Put another way:
- Goal: Maximize the amount of demand covered.
- Rule: You have a fixed budget or a set number of facilities (p), and you place them to reach as many people as possible within a time or distance limit (e.g., placing a limited number of ambulance hubs).

---
# MCLP examples
<div class="split-slide" markdown="1">
<div markdown="1">
- [allagash MCLP](https://apulverizer.github.io/allagash/examples/MCLP.html)
- [ArcGIS Maximize Coverage](https://pro.arcgis.com/en/pro-app/3.6/help/analysis/networks/location-allocation-analysis-layer.htm)
</div>
<div markdown="1">

![Service areas](https://bok-figures.s3.amazonaws.com/files/AM43_Fig3.png)
[Source](https://gistbok-ltb.ucgis.org/current/concept/AM-05-043)
> Solving the problem yields the optimal solution, xA = 0, xB = 1 , xC = 0 , xD = 1  with a total coverage of 7 (y1=0 , y2=1 , y3=1 , y4=1 , y5=1 , y6=1 , y7=1 , y8=1 , y9=0).

</div>
</div>

---
# MCLP examples
![MCLP species]({{ site.baseurl }}/assets/images/MCLP.png)
[Source](https://www.researchgate.net/publication/286121362_Application_of_the_Maximal_Covering_Location_Problem_to_Habitat_Reserve_Site_Selection_A_Review)

---
# And now for something (not so completely) different
> Coverage problems are suitable for applications where facilities have a predefined service range [like 5-minutes, 5km, etc.] so that the service area can be stipulated a priori. _For applications where service areas need to be delineated based on nearest facilities_, **service areas need to be determined along with the siting decisions in the modeling framework**.

---
# Location-allocation
Definition: location model constructed to **find the _best_ locations of a number of facilities so that the _total demand weighted travel is minimal_**

Who goes where?

> **Location**: The most suitable location(s) considering the demand distribution. Suitability is commonly the outcome of minimizing transportation costs, often using distance as a proxy.
i.e. the best location for the grocery store

> **Allocation**: The most suitable allocation of flows from points of distribution to points of demand. As for location, suitability is commonly the outcome of minimizing transportation costs.
i.e. whom the grocery store serves

[Source](https://transportgeography.org/contents/methods/location-allocation-models/)

---
# Location-allocation
Challenges
- LA often involves representing places like neighbourhoods as points (centroids)
- BUT, coverage of points does not necessarily guarantee coverage of the associated areas/polygons
- Same issue with previous coverage problems (MCLP/LSCP) too...

![Spider diagram for Location-Allocation](https://desktop.arcgis.com/en/arcmap/latest/extensions/business-analyst/GUID-6D82E6EC-4AD1-4A55-B01A-8EEA364A23DA-web.png)

[Source](https://desktop.arcgis.com/en/arcmap/latest/extensions/business-analyst/GUID-6D82E6EC-4AD1-4A55-B01A-8EEA364A23DA-web.png)
---
# LA: P-Median Problem
- Place p facilities while minimizing distance of all demands 

Another way to put it:
- Goal: Minimize the total travel distance or cost between demand points and their closest facility.
- Rule: We have p facilities to place (e.g. choose where to put 3 warehouses to minimize the total delivery miles for all customers).
- Heuristic: a feasible solution to a problem

In ArcGIS Pro: [Minimize Impedance](https://pro.arcgis.com/en/pro-app/3.6/help/analysis/networks/location-allocation-analysis-layer.htm)

---
# P-Median with a twist
Back to the grocery store location-allocation.

Our goal was to find the candidate store site that minimized the travel distance for the most people (total demand weighted travel). P-median ("Minimize Impedance") assumes short trips are all consumers demand. Each demand point (you!) simply gets "assigned" to the nearest store. 

**In the real world, we may want to incorporate consumer preferences**. Hence we used the "Maximize Market Share" tool, which relies on a ["gravity model"](https://pro.arcgis.com/en/pro-app/3.6/tool-reference/business-analyst/understanding-huff-model.htm) that measures the _probability_ of demand rather than a more falliable determination of demand. It accounts for relative attraction AND distance (weight/distance), although we didn't _actually_ have the info to weight different supermarkets differently.

---
# Aside: how do we model how people think about distance?
We are assessing "impedance" and it is a function of cost: time or distance and ... perception. We can further model the attractiveness of a site based on how attraction "decays" with distance.

Options:
* **Linear** - 5, 10, 20 minutes - the relative proportions remain the same
* **Power** - e.g. x^2 = 25, 100, 400 - the cost increases non-linearly
* **Exponential** - e.g. 2^5 = 32, 1024, 1048576 - even more exaggerated increases in cost, especially further away 

(Typically we then invert these costs so they become "weights", 32 becomes 1/32, which is a larger/higher weight number than 1/1024)

How do we choose? As usual, we make some assumptions. But we may have consumer data that tells us how far consumers really do travel to get to our stores, so we can calibrate.

In general, more "essential" trips like to the grocery store are less elastic than trips to e.g. buy a car. Meaning the grocery store case may require an exponential approach, whereas a car dealership case might be modeled more linearly.

---
# Modeling how people think about distance
![Retail distance decay curve](https://i0.wp.com/transportgeography.org/wp-content/uploads/distance_decay_curves_retail.png?resize=1024%2C750&ssl=1)
[Source](https://transportgeography.org/contents/methods/market-area-analysis/retail-distance-decay-curve-conventional/)

---
# Classic warehouse location problem
- Specific kind of LA problem in which the number of facilities (e.g. warehouses) is not fixed in advanced but is determined by the model
In other words:
-	Goal: Minimize total fixed costs associated with building facilities plus travel costs.
-	Rule: Unlike the p-median problem, **we do not know the number of facilities ahead of time.** We weigh the high upfront cost of opening a new warehouse against any savings on shipping costs.

---
# Spatial data management
Geodatabases and GeoPackages

Similarities
- **Core Functionality**: Both act as spatial database containers capable of storing vector geometry, raster datasets, and non-spatial attributes within a single relational structure.
- **ArcGIS Pro Integration**: ArcGIS Pro provides support for viewing, managing, and editing data in both proprietary Geodatabases and open SQLite-based GeoPackage files.

---
# Spatial data management
Differences

| Aspect | Geodatabase | GeoPackage |
| :--- | :--- | :--- |
| **Standardization** | Proprietary architecture built and maintained specifically for the Esri ArcGIS software ecosystem. | Open, non-proprietary standard developed by the Open Geospatial Consortium (OGC) to maximize interoperability. |
| **Platforms** | Optimized for, but not exclusive to, ArcGIS Pro. | Universal cross-platform compatibility. |
| **Structure** | Integrates with database management systems like PostgreSQL (Enterprise) or uses folder structures (File GDB). | Single-file SQLite database. |
| **Users** | Supports multiple simultaneous users across an organization (Enterprise). | Typically restricted to single-user editing. |
| **Use** | Designed for complex schema constraints, topologies, and relationship classes. | Ideal as a lightweight, portable storage container. |

---
# Application 1: RFP

---
# Tutorial preview: 2SFCA
<div class="split-slide" markdown="1">
<div markdown="1">
2SFCA = two-step floating catchment area

In this tutorial, we will assess access to medical clinics. Access here is a function of supply and demand. You could have a big clinic with lots of doctors, but if you also have a large population to serve, there may not be much access. 

The problem involves two components (steps): 1. clinic service areas; 2. population demand areas. 

We calculate how many people are "servicable" per clinic then look at it from the "consumer" or patient perspective. Do I live in a neighbourhood where nearby i.e. within 10 minute drive clinics have a lot of other people to serve too?
</div>
<div markdown="1">

![Two-step floating catchment area method tutorial result]({{ site.baseurl }}/assets/images/2SFCA.png)

</div>
</div>


