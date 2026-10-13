---
layout: lectures
title: "Week 5: Network Analysis"
permalink: /lectures/week-05/
---

# Week 5
## Network Analysis

Network analysis concepts, WebGIS tutorial preview

---
## We’ve been doing distance/time minimization problems, relying on ArcGIS Online’s network to help us understand travel time along roads. 

## But what is that network? 

## How do we find the shortest route?

---
# Network Analysis
> an arrangement of elements (i.e., nodes, links) and information on their connections and interactions
> a system that is defined through a connected set of nodes which has a system of flow defined through the connections by means of its edges each of which have associated weights and possibly a direction of flow

Examples include roads, paths, railways, public transit lines, and streams

**Nodes**: points representing key features of the linear network, such as intersections, bends, etc.

**Edges or links**: the lines themselves

---
# Key concepts from graph theory
<div class="split-slide" markdown="1">
<div markdown="1">
- **Network types** - physical (e.g. tubes, roads) and logical (e.g. social network)
- **Topology** - arrangement of features 
- **Cost** - value of travel through the network along edges from node to node. Often measured as distance, but also time, speed limit, or even more abstract notions like risk
- **Walk** - a sequence of edges
- **Path** - a walk without repetition
- **Circuit** - a walk with no edge repetition
</div>
<div markdown="1">

![Network graph](https://bok-figures.s3.us-east-1.amazonaws.com/files/AM76_Fig3_combo.png)
![Network graph](https://bok-figures.s3.amazonaws.com/files/FC19_Fig3.png)

</div>
</div>


---
# Key concepts implementing graph theory in GIS
<div class="split-slide" markdown="1">
<div markdown="1">
- **Route** - sequence of edges from a starting node to an ending node
- **Link** - a network segment defined by two end points, e.g. intersections.
- **Link impedance** - the cost incurred by traversing a link, e.g. the time taken to drive along a road segment.
- **Junction** - an intersection, e.g. a road intersection, within the network, and is usually associated with link end-points.
- **Turn impedance** - the cost incurred by completing a turn through a junction point.
- **Restrictions** - include things like one-way streets or turning restrictions.
- **Flow** - direction of travel...could be bidirection (undirected) or directed (one way)
</div>
<div markdown="1">

![Junctions and edges](https://bok-figures.s3.amazonaws.com/files/FC19_Fig5a.png)
![Google Maps](https://bok-figures.s3.us-east-1.amazonaws.com/files/AM76_Fig1.png)

</div>
</div>

---
# Three steps in network analysis applications

1. Gathering data
- Network features are available from various public data sources, depending on the region and type of network data. Increasingly, OpenStreetMap (OSM) is an important data source, especially for road data.
2. Build the topology
- Largely involves GIS-based vector editing.
3. Attribute the network features
- Includes assigning link impedance, one-way streets, speed limits, restricted turns, etc.

Source: Dr. John Lindsay

---
# Shortest path problem
Dijkstra’s algorithm to find shortest path 

<iframe width="800" height="500" src="https://www.youtube.com/embed/wtdtkJgcYUM?si=JoMbL_DqUFPKhqj-" title="YouTube video player" frameborder="0" allow="accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

Vector representations based on graph theory (nodes, edges)

---
# Least-cost paths
<div class="split-slide" markdown="1">
<div markdown="1">
Raster representations

Examples
> Connect the wildlife habitat patches with corridors to allow the species to move between the patches. The cost surface units are preference per foot for movement through the features at each location.

> Locate a new pipeline to connect petroleum fields to a refinery. The cost surface units are based on the environmental impact the pipeline will have on each location.

> Determine the fastest way to reach an injured hiker in a remote area. The cost surface units are minutes per meter.
</div>
<div markdown="1">
[**Distance analysis**](https://pro.arcgis.com/en/pro-app/3.6/tool-reference/spatial-analyst/distance-analysis.htm)
1. Calculate straight-line distance
2. Calculate and apply a cost surface, creating an accumulative distance raster
3. Connect regions
</div>
</div>

---
# Calculate straight-line distance
![Straight-line distance](https://pro.arcgis.com/en/pro-app/3.6/tool-reference/spatial-analyst/GUID-5EE1C9E4-42E8-4531-B575-5EACB10BC425-web.jpg)
>The straight-line distance from each non-source cell to the closest ranger station (purple points). Rivers are displayed (blue lines)

[Source](https://pro.arcgis.com/en/pro-app/3.6/tool-reference/spatial-analyst/calculate-straight-line-distance.htm)

---
# Calculate and apply a cost surface -> accumulative distance raster
[**Cost surface**](https://pro.arcgis.com/en/pro-app/3.6/tool-reference/spatial-analyst/adjust-the-encountered-distance-using-a-cost-surface.htm)
> A cost surface represents the cost or preference of the mover to travel through each location. Cost is calculated per map unit, with each cell identifying how costly it is to move through that cell. Example cost units for cost surfaces include: Fire fighters: time to reach fires; Military troops: level of security; Bobcat: energy expended 
![Cost surface](https://pro.arcgis.com/en/pro-app/3.6/tool-reference/spatial-analyst/GUID-E9F28CA0-980F-4478-822C-99AC28C3F646-web.jpg)

**Accumulative distance**
> Calculated by summing the total cost required to travel from a starting source cell to every other cell in the analysis
![Accumulative distance](https://pro.arcgis.com/en/pro-app/3.6/tool-reference/spatial-analyst/GUID-6DED7D71-F3A4-4456-AC1F-987D8C3CE60E-web.png)

[Source](https://pro.arcgis.com/en/pro-app/3.6/tool-reference/spatial-analyst/adjust-the-encountered-distance-using-source-characteristics.htm)

---
# Connect regions
<div class="split-slide" markdown="1">
<div markdown="1">
![Optimal network connection](https://pro.arcgis.com/en/pro-app/3.6/tool-reference/spatial-analyst/GUID-711C8F58-2A61-4319-AD16-0105CA852ACC-web.jpg)
</div>
<div markdown="1">
![Optimal path and accumulative distance surface](https://pro.arcgis.com/en/pro-app/3.6/tool-reference/spatial-analyst/GUID-EE1D41B5-BA8D-47C0-87D9-8D783583E4BC-web.png)

[Source](https://pro.arcgis.com/en/pro-app/3.6/tool-reference/spatial-analyst/connect-regions-with-the-optimal-network.htm)
</div>
</div>

---
# Tutorial preview: WebGIS
<div class="split-slide" markdown="1">
<div markdown="1">
In this tutorial, you will use WebGIS alongside automation tools in ArcGIS Pro to streamline a validation workflow for re-zoning applications, rather than relying on locally or personally-saved layers.

You will explore proposed re-zoning locations and check if they are occurring within designated heritage districts.

This automated check acts as a way of raising potential concerns for additional scrutiny (e.g., flagging a proposal that attempts to rezone a residential property in a heritage zone to commercial).
</div>
<div markdown="1">

![WebGIS tutorial result]({{ site.baseurl }}/assets/images/webgis.png)
![WebGIS tutorial ModelBuilder]({{ site.baseurl }}/assets/images/mb.png)

</div>
</div>

