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

```
One GeoDataFrame of communities, one of grocery stores.
Want to merge to get each grocery's community.
chicago.head()
Out[15]: 
                                            geometry        community
0  MULTIPOLYGON (((1181573.249800048 1886828.0393...          DOUGLAS
1  MULTIPOLYGON (((1186289.355600054 1876750.7332...          OAKLAND
2  MULTIPOLYGON (((1176344.998000037 1871187.5456...      FULLER PARK
3  MULTIPOLYGON (((1182322.042900046 1876674.7304...  GRAND BOULEVARD
4  MULTIPOLYGON (((1186289.355600054 1876750.7332...          KENWOOD

groceries.head()
Out[16]: 
   OBJECTID  ...                                           geometry
0        16  ...  MULTIPOINT ((1168268.671671558 1933554.3504257...
1        18  ...  MULTIPOINT ((1162302.617919334 1832900.2240279...
2        22  ...  MULTIPOINT ((1173317.042329894 1895425.4259547...
3        23  ...  MULTIPOINT ((1168996.475130927 1898801.4056401...
4        27  ...  MULTIPOINT ((1176991.988724414 1847262.4228848...

[5 rows x 8 columns]

Execute spatial join
groceries_with_community = groceries.sjoin(chicago, how="inner", predicate='intersects')

groceries_with_community.head()
Out[18]: 
   OBJECTID     Ycoord  ...  index_right       community
0        16  41.973266  ...           30          UPTOWN
1        18  41.696367  ...           73     MORGAN PARK
2        22  41.868634  ...           28  NEAR WEST SIDE
3        23  41.877590  ...           28  NEAR WEST SIDE
4        27  41.737696  ...           39         CHATHAM

[5 rows x 10 columns]
```

</div>
</div>

---
# GIS APIs
<div class="split-slide" markdown="1">
<div markdown="1">
GIS APIs as communication protocols
> "GIS APIs provide a communication protocol to handle client requests and return the processed response back from a server that provides GIS functionalities and/or datasets as a service"

Example: [Mapbox](https://docs.mapbox.com/api/navigation/directions/) routing/navigation as a service

Advantages:
- **interoperability** (GIS without Windows)
- **light-weight** (no desktop GIS or plug-ins)

</div>
<div markdown="1">
![Mapbox optimization API](https://cdn.prod.website-files.com/6050a76fa6a633d5d54ae714/6580c0514d17595923cca058_img_4.webp)
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

```
def find_grid(api_key, sw_lat, sw_lng, ne_lat, ne_lng, place_type):
    url = "https://places.googleapis.com/v1/places:searchNearby"

    # Notice we added 'places.id' to the mask for deduplication
    headers = {
        "Content-Type": "application/json",
        "X-Goog-Api-Key": api_key,
        "X-Goog-FieldMask": "places.id,places.displayName,places.formattedAddress,places.location"
    }

    # For a medium-sized city like Guelph, a 2km grid step with a 1500m radius covers everything
    grid_points = generate_grid(sw_lat, ne_lat, sw_lng, ne_lng, grid_size=(5, 5))
    print(f"Generated {len(grid_points)} grid points to scan. Beginning search...\n")

    all_store_data = []

    for i, (lat, lng) in enumerate(grid_points):
        print(f"Scanning point {i+1}/{len(grid_points)}: {lat:.4f}, {lng:.4f}...")

        k = {"supermarkets": ["supermarket"],
             "clinics": ["doctor", "medical_clinic"]
             }
        payload = {
            "includedTypes": k[place_type],
            "maxResultCount": 20,
            "locationRestriction": {
                "circle": {
                    "center": {"latitude": lat, "longitude": lng},
                    "radius": 5000 # 5 km radius ensures overlapping circles
                }
            }
        }

        response = requests.post(url, headers=headers, json=payload)
```

</div>
</div>

---
# Statistics and Decision-Making
<div class="split-slide" markdown="1">
<div markdown="1">
[ECCC study example](https://www.canada.ca/en/environment-climate-change/corporate/transparency/consultations/environmental-justice-draft-national-strategy.html)

"Trust in Numbers" - decision-makers seek legitimacy for their actions by pointing to statistics

_Spatial_ statistics are those that involve some notion of spatial association

So, calculating an odds ratio based on counts per dissemination may be _geographical_ in the sense that the measures pertain to space, the odds ratio isn't a _spatial statistic_

Spatial stats are also different from visual analysis ("eyeballing" trends)

</div>
<div markdown="1">
![Carto hotspots vs eyeballing trends](https://carto.com/cdn.prod.website-files.com/63483ad423421bd16e7a7ae7/63a19cebe8ffc88e11062317_hotspots.webp)

[Source](https://carto.com/blog/spatial-hotspot-tools/)
</div>
</div>

---
# First Law of Geography
<div class="split-slide" markdown="1">
<div markdown="1">
Everything is related, but near things are more related than distant ones

_Is it always true though?_
</div>

<div markdown="1">
![Tobler laws](https://media.springernature.com/m685/springer-static/image/art%3A10.1134%2FS1875372825700015/MediaObjects/13541_2025_1294_Fig1_HTML.png)

[Source](https://link.springer.com/article/10.1134/S1875372825700015)
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
![Esri clustered dispersed spectrum](https://doc.esri.com/en/arcgis-pro/latest/tool-reference/spatial-statistics/images/moransi_stat-7B209.gif)

[Source](https://doc.esri.com/en/arcgis-pro/latest/tool-reference/spatial-statistics/spatial-autocorrelation.html?tabs=dialog)
</div>
</div>

---
# Spatial autocorrelation
<div class="split-slide" markdown="1">
<div markdown="1">

> the dependence between the values of one attribute due to spatial proximity.

> the footprint of the process generating the variable of interest [soil pH, house prices, etc.]

[Source](https://blasbenito.github.io/spatialRF_talk/talk.html#7)

Specific measures to detect this: **Global and Local Indicators of Spatial Association**

</div>
<div markdown="1">
![Quantifying autocorrelation](https://blasbenito.github.io/spatialRF_talk/talk_files/figure-html/unnamed-chunk-2-1.png)

[Source](https://blasbenito.github.io/spatialRF_talk/talk.html)
</div>
</div>

---
# Conceptualizing spatial relationships
<div class="split-slide" markdown="1">
<div markdown="1">
How are phenomena related in space?

- point-based: weighting based on distance
  -  "**Inverse distance** or inverse distance squared relationships involve nearer observations having a stronger influence and that influence decaying with increasing distance; this relationship is commonly applied to continuous data, such as temperatures or air pressures"
  - "**Fixed radius** relationships apply the same influence to all points within a fixed radius of neighborhood area"
  - "**k nearest neighbors** ensures that every observation has a specified number of neighbors, “k,”"
- polygon-based: **spatial contiguity** (Queen/Rook)

</div>
<div markdown="1">

![NY Leukemia spatial relationships](https://raw.githubusercontent.com/HughSt/HughSt.github.io/master/_posts/Week-4-spatial-clustering_updatedMar19_files/figure-gfm/unnamed-chunk-14-1.png)

[Source](https://hughst.github.io/week-4/)

</div>
</div>

---
# Global Moran's I
> For each feature value, it subtracts the mean, creating a deviation from the mean. Deviation values for all neighboring features (features within the specified distance band, for example) are multiplied together to create a cross-product. The numerator for the Global Moran's I statistic includes these summed cross-products. Suppose features A and B are neighbors, and the mean for all feature values is 10. The range of possible cross-product results are as follows:

| Feature values |  | Deviations |     | Cross-products |
| -------------- | ---------- | -------------- | --- |
| A=50           | B=40       | 40             | 30  | 1200           |
| A=8            | B=6        | \-2            | \-4 | 8              |
| A=20           | B=2        | 10             | \-8 | \-80           |

> When values for neighboring features are either both larger than the mean or both smaller than the mean, the cross-product will be positive. When one value is smaller than the mean and the other is larger than the mean, the cross-product will be negative. In all cases, the larger the deviation from the mean, the larger the cross-product result. If the values in the dataset tend to cluster spatially (high values cluster near other high values; low values cluster near other low values), the Moran's Index will be positive. When high values repel other high values, and tend to be near low values, the index will be negative. If positive cross-product values balance negative cross-product values, the index will be near zero. The numerator is normalized by the variance so that index values fall between -1.0 and +1.0

[Source](https://pro.arcgis.com/en/pro-app/3.4/tool-reference/spatial-statistics/h-how-spatial-autocorrelation-moran-s-i-spatial-st.htm)

---
# Spatial autocorrelation patterns
<div class="split-slide" markdown="1">
<div markdown="1">

> Often, you will run one of the pattern analysis tools, hoping that the z-score and p-value will indicate that you can reject the null hypothesis, because it would indicate that rather than a random pattern, your features (or the values associated with your features) exhibit statistically significant clustering or dispersion. Whenever you see spatial structure such as clustering in the landscape (or in your spatial data), you are seeing evidence of some underlying spatial processes at work, and as a geographer or GIS analyst, this is often what you are most interested in.

[Source](https://pro.arcgis.com/en/pro-app/3.4/tool-reference/spatial-statistics/what-is-a-z-score-what-is-a-p-value.htm)

- **Z scores** = standard deviations above/below a mean (score - mean / standard deviation)
- **Standard deviation** = square root of variance
- **Variance** = difference between each value and the mean, squared and averaged

Interpretation:
- Positive spatial autocorrelation (**clustering**)
- No spatial autocorrelation (**random**)
- Negative spatial autocorrelation (**dispersion**)

|---|---|---|---|---|
| The p-value is not statistically significant. | You cannot reject the null hypothesis. It is quite possible that the spatial   distribution of feature values is the result of random spatial processes. The   observed spatial pattern of feature values could very well be one of many,   many possible versions of complete spatial randomness (CSR). |  |  |  |
| The   p-value is statistically significant, and the z-score is positive. | You may reject the null hypothesis. The spatial   distribution of high values and/or low values in the dataset is more   spatially clustered than would be expected if underlying spatial processes   were random. |  |  |  |
| The   p-value is statistically significant, and the z-score is negative. | You may reject the null hypothesis. The spatial   distribution of high values and low values in the dataset is more spatially   dispersed than would be expected if underlying spatial processes were random.   A dispersed spatial pattern often reflects some type of competitive process—a   feature with a high value repels other features with high values; similarly,   a feature with a low value repels other features with low values. |  |  |  |
|  |  |  |  |  |

[Source](https://pro.arcgis.com/en/pro-app/3.4/tool-reference/spatial-statistics/h-how-spatial-autocorrelation-moran-s-i-spatial-st.htm)

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

[Example of rent costs in MTL](https://mikaelbrunila.com/posts/understanding-morans-i/)

</div>
<div markdown="1">
![LISA rent clusters in MTL](https://mikaelbrunila.com/_astro/final_map-1.Dd6y0aVV_Z1abeSM.webp)

[Source](https://mikaelbrunila.com/posts/understanding-morans-i/)
</div>
</div>

---
# Clusters vs Outliers in LISA
> Large positive z score (e.g. z > +1.96) indicates that the observation and its neighbors have significantly similar values (spatial clusters consisting of _either high or low values_). 

> Large negative z score (e.g., z < -1.96) indicates that the value at observation i is significantly different than its neighbors (i.e., spatial outliers).

---
# Other local spatial statistics
<div class="split-slide" markdown="1">
<div markdown="1">
Getis-Ord Gi* = hot and cold spots (high-high, low-low)

![Iowa health clusters map]({{ site.baseurl }}/assets/images/iamap.png)

Compare with Local Moran's I (high-high, high-low, low-low, low-high)

</div>
<div markdown="1">

![Carto LSS comparisons](https://carto.com/cdn.prod.website-files.com/63483ad423421bd16e7a7ae7/63a19d0d7c2c7da014f812ab_method_comparison.webp)

[Source](https://carto.com/blog/spatial-hotspot-tools/)

See: [https://clausa.app.carto.com/map/4d4699b7-b2ed-42e4-9c0e-b68b8972be64?lat=37.760333&lng=-122.436317&zoom=12](https://clausa.app.carto.com/map/4d4699b7-b2ed-42e4-9c0e-b68b8972be64?lat=37.760333&lng=-122.436317&zoom=12)

</div>
</div>

---
# Applications
<div class="split-slide" markdown="1">
<div markdown="1">

- Statistical: interpolation (Kriging, IDW)
-	Policy: public health, crime, environmental justice (ECCC study)

![Optimized hot spot Houston west nile](https://www.researchgate.net/profile/Martin-Reyna/publication/316940945/figure/fig1/AS:525697027448835@1502347346860/Optimized-hotspot-analysis-results-showing-residential-locations-of-persons-who-had-West.png)

[Source](https://www.researchgate.net/publication/316940945_West_Nile_Virus_Outbreak_in_Houston_and_Harris_County_Texas_USA_2014)

</div>
<div markdown="1">

![Chicago violent crime liquor store hotspots](https://desktop.arcgis.com/en/analytics/case-studies/GUID-A999AB19-A86E-4C03-B71B-5209BE8162F8-web.png)

[Source](https://desktop.arcgis.com/en/analytics/case-studies/broken-bottles-3-pro-workflow.htm)

</div>
</div>

---
# Tutorial preview: Public Participation GIS with Survey123 - Part 1
<div class="split-slide" markdown="1">
<div markdown="1">
You will create **Squirrel Spotter**!!! Decision-making is only as good as the information behind it, but typically that information lacks local perspective. Ordinary individuals can be invaluable sources of data on public issues, because scientists and officials often lack capacity to gather localized data or are uninterested in it. 

Imagine we need to know more about Guelph's squirrel population - where different kinds are when. Sure, we could hire a bunch of wildlife biologists to do surveys, but basic squirrel identification can be done by laypeople. Esri built the Survey123 tool to help collect such information.
</div>
<div markdown="1">

![Survey123 image]({{ site.baseurl }}/assets/images/survey123.png)

</div>
</div>

