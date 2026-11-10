---
layout: lectures
title: "Week 9: Uncertainty and Bias"
permalink: /lectures/week-09/
---

# Week 9
## Uncertainty and Bias

Uncertainties, Error, Bias, Applications 4 - Public Comment, Tutorial Preview: Survey123 map

---
# Uncertainty in everyday life

_What uncertainties do you encounter everday in your decision-making?_

_What kind of uncertainties are those?_

_Do they matter? Why?_

_What about everyday spatial decision-making?_

---
# Uncertainty in decision-making
1. Maps often obtain their authority by obscuring uncertainties, appearing more confident than they should be...

> “Oftentimes a ‘‘one map solution’’ (Monmonier 1991) is presented to map users, with little information provided about the potential limitations and uncertainties inherent in such displays for various tasks” [Source](https://utppublishing.com/doi/10.3138/carto.48.3.1531)

Example: [EJSCREEN](https://pedp-ejscreen.azurewebsites.net/)

2. A shift in perspective is needed: from "More data = better decisions" -> "How much data is enough?" (_fitness for use_ / "just good enough")

---
# Uncertainty and error
“**Uncertainty** as the _unknown_ difference between reality and measured data.” Hunter and Goodchild (1993) in [Kubler et al. 2019](https://www.tandfonline.com/doi/full/10.1080/24694452.2019.1644992)

Example = +/- 1m sea level rise (SLR) by 2050

**Error** = amount we are wrong. We know and can measure the difference between reality and the data.

Example = -.25m difference (in a model that estimates SLR 1990-2020)

[US NOAA Sea Level Rise Viewer](https://coast.noaa.gov/slr/#/layer/slr/2/-10024568.233817915/3497661.245251188/11.802/satellite/none/0.8/2050/interHigh/noAccretion/NOS_Minor)

---
# Types of uncertainty
_About the phenomena itself_

Example: climate change. What we don’t know about the past, present, and future is immense. Or, sea level rise (SLR). We don’t know its magnitude.

_About the data representing it_

Data error leads to uncertainties

SLR: our elevation data may be inaccurate, imprecise, incomplete, etc.

---
# Accuracy, precision
<div class="split-slide" markdown="1">
<div markdown="1">
**Accuracy**

> the converse of error, i.e. it is defined as the extent to which an estimated value approaches the true value

**precision** = "the degree of dispersion of observations around a mean." (bullseye analogy)
</div>
<div markdown="1">
![Esri accuracy and precision](https://www.esri.com/arcgis-blog/app/uploads/2017/10/AccuracyvsPrecision.png)
</div>
</div>

---
# Vagueness, ambiguity
<div class="split-slide" markdown="1">
<div markdown="1">
**Vagueness**

> general term for a class of common situations whereby objects with sharp boundaries need to be identified on surfaces and for phenomena that are in reality continuous, that have uncertain boundaries, or whose shifting boundaries cannot be precisely determined

Example: how many trees make a forest?

![Forest map vagueness example](https://www.researchgate.net/profile/Brandon-Bennett-3/publication/235970322/figure/fig2/AS:299815146672128@1448492909042/Possible-forest-demarcations-for-a-given-tree-distribution-Inner-contours-are-based-on-a.png)

[Source](https://www.researchgate.net/publication/235970322_Spatial_Vagueness)
</div>
<div markdown="1">
**Ambiguity** = "meanings that can be interpreted in more than one way." Semantics!

![Ambuiguity cartoon](https://geos270.github.io/Module6/docs/content/images/ambiguity.png)

Example: what even is a forest? (what kinds of trees?)
</div>
</div>

---
# Rumsfeldian philosophy 101
<div class="split-slide" markdown="1">
<div markdown="1">
> … as we know, there are **known knowns**; there are things we know we know. We also know there are **known unknowns**; that is to say we know there are some things we do not know. But there are also **unknown unknowns**—the ones we don't know we don't know”. 

> There are _degrees of uncertainty_, ranging from **tractable statistical uncertainties** to **scenario uncertainties**, to **ignorance** (the known unknowns and unknown unknowns).

_epistemic uncertainty_ = "tractable statistical uncertainties [that can be ]'cured' with more information" - collect more data

_aleatory uncertainty_ = "random, truly unpredictable events."

> _uncertainties related to dimensions external to the data_ are the flipside of the assumptions we must make in order to develop stories, models, and forecasts, and to make decisions that go beyond the data.
</div>
<div markdown="1">
![Donald Rumsfeld](https://en.wikipedia.org/wiki/Donald_Rumsfeld#/media/File:Rumsfeld1_(cropped)(b).jpg)
</div>
</div>

---
# Known -> unknown

> Even though we cannot have knowledge of the future and in many cases also of the past, we can reduce our ignorance through inferring unknown facts from known facts.


**Projection** = "trend extrapolation … and works best for short time horizons and simple problems, e.g. as in estimating student enrollments and related space needs for the next five years."
**Forecasting** = "more general and complex, and can include projections as well as more sophisticated techniques. Forecasts and projections always have some greater or lesser degree of uncertainty, since they can at best be rational attempts to guess – not to know – what the future holds in the particular area of interest."
**Prediction** = "implies much higher levels of accuracy and precision (barring human or technical errors)."

[Source](https://gistbok.ucgis.org/bok-topics/2022-quarter-02/conceptual-models-error-and-uncertainty)


---
# Fuzzy data
<div class="split-slide" markdown="1">
<div markdown="1">
> Fuzzy sets allow an element to partially belong to a set with the aid of a membership function ranging from zero to one. 
</div>
<div markdown="1">
![Protestant vs Catholic fuzzy map](https://www.tandfonline.com/cms/asset/0a859eed-6590-4200-bad3-43d22d16cd8d/tgis_a_2229894_f0003_c.jpg)

[Source](https://www.tandfonline.com/doi/full/10.1080/13658816.2023.2229894)
</div>
</div>

---
# The role of data quality

**data quality** = "the degree to which our data match the reality they intend to represent" aka how much error is there?
**metadata** = "the documentation of data quality and other dataset characteristics"
**data evaluation** = "the process of assessing whether a dataset is suitable _for a particular use_, using tools such as metadata."

> the goal is not to find the “perfect” dataset (...this does not exist), but to determine how well each dataset meets the needs of a particular application, a concept known as **fitness for use**. Each dataset may be excellent for the purposes for which it was originally created but unsuitable for other purposes...

---
# Uncertainty and subjectivity, risk and use
> Any GIS application can thus tolerate some degree of uncertainty, but how much is acceptable depends on the project. **The key is that the data are “good enough” to produce analytical results that correspond closely to results in the real world.** In practice, this means results can be “correct” even if the data is not. 

“**Uncertainty depends on someone’s knowledge, interests, and motivations, and on the context within which an uncertainty may arise**. One user may consider a particular database good enough, while for another its errors and related uncertainties may make it practically useless. By contrast, a GPS navigation system with a location error will equally affect every driver who follows it.”

A lot of this has to do with risk: typically, the higher the risk, the more certain we will want to be about the data.
This is _subjective_: different people themselves have different ideas about risk.

[Source](https://gistbok.ucgis.org/bok-topics/2022-quarter-02/conceptual-models-error-and-uncertainty)

---
# Metadata
**Access**: "how it can be acquired and whether it can be used legally."
**Content**: "What the dataset claims to include, and conversely, what it not include." 
**Structure**: "How the dataset is organized, specifying its file format, attribute datatypes, coordinate system, and so on."
**Semantics**: "What the terms and measurements in the data mean."

Example: [NPRI dataset](https://open.canada.ca/data/en/dataset/06022cc0-a31e-4b4c-850d-d4dccda5f3ac)

---
# Measures of data quality
**Attribute Accuracy**: "The degree to which attribute values match real-world values." Example: land use/cover classification accuracy.
**Positional Accuracy**: "The degree to which data locations and shapes match their true counterparts."
**Completeness**: "The extent to which all of the features and attributes are included in the data."
**Currency**: "How up-to-date the data are relative to the present state of the world"
**Provenance**: "it is simply ethical for data producers to be honest about their sources and methods."

Example: [AAFC Land Use](https://open.canada.ca/data/en/dataset/fa84a70f-03ad-4946-b0f8-a3b481dd5248)

---
# Representing uncertainty on maps
![Maceachren uncertainty topology]({{ site.baseurl }}/assets/images/uncertainty.png)

---
# Representing uncertainty on maps
![Uncertainty methods]({{ site.baseurl }}/assets/images/uncertainty_methods.png)

---
# Case: representing uncertainty on maps
<div class="split-slide" markdown="1">
<div markdown="1">
“How does the visualization of uncertainty lead to different map-based decision outcomes?" - [Kubler et al.](https://www.tandfonline.com/doi/full/10.1080/24694452.2019.1644992)

“We find that participants decided to buy different houses, depending on whether uncertainty is shown on the map display and on the type of uncertainty visualization (i.e., varying color value, focus, or texture).”

“…our participants seem to have underestimated hazard risks with the visualization of uncertainty, because they most often selected houses in the red danger zone in trials showing uncertainty with a color value...[an] explanation for this result could be that the depicted uncertainty at hazard zone boundaries might have suggested to participants not to **trust** the official hazard zone classification at all…”

Keyword: _trust_
</div>
<div markdown="1">
![Annals AAG uncertainty hazard map](https://www.tandfonline.com/cms/asset/e6d9da1a-4e42-49df-99f7-c030e50958d6/raag_a_1644992_f0003_c.jpg)
</div>
</div>

---
# Decision-Making is Always a Subjective Excerise, Like it or Not
<div class="split-slide" markdown="1">
<div markdown="1">
The value of data: decision-making is not just about the facts

> “The sirens now feel different…They come with a different flood of emotions.” The noise outside her window was a tangible reminder of the human lives hidden in the maze of anonymous data that had come to dominate her days.

[Source](https://www.washingtonpost.com/local/johns-hopkins-tracker/2020/06/29/daea7eea-a03f-11ea-9590-1858a893bd59_story.html)
</div>
<div markdown="1">
![Daniel Huffman emotional valence maps]({{ site.baseurl }}/assets/images/huffman.png)

[Source](https://twitter.com/pinakographos/status/1326289958806708225) - Daniel Huffman
</div>
</div>

---
# Bias
**Bias** is another source of error, often associated with completeness

Statistical definition of bias = "systematic error" -> over/underestimating true values

As with uncertainty, whether bias is a problem depends on use

Examples of bias: [Strava in urban planning](https://www.strava.com/maps/global-heatmap?sport=All&style=dark&terrain=false&labels=true&poi=true&cPhotos=true&3d=false&gColor=blue&gOpacity=100), [Indigenous census counts](https://www.cbc.ca/news/canada/toronto/toronto-urban-indigenous-census-1.6192449)

---
# From Bias to Public Participation
_Can pulic participation rectify biases?_

(stay tuned...)

---
# Application 4 - Public Comment
You've successfully created a request for proposals (RFP) for a spatial decision-making context, switched roles to make a bid on that RFP, and then conducted the necessary analysis. Now it is time to switch roles one last time, from that of a GIS analyst consulting for a government, business, or not-for-profit, to a member of the public. 

**Step 1: identify a project.** You are welcome to switch projects and provide a public comment on someone else's analysis, but that depends on them posting it to the Discussion Board, which I am not requiring any one do. Most likely, you will stick with the project you completed the proposal and analysis for.

**Step 2: identify a stakeholder group** with an alternative perspective on the issue. *One way to think about this is, what are the assumptions going into your analysis and how could they be different?* Some examples: if you are doing an MCE that weights three different parameters (e.g. slope, land cover, and distance to wetlands), perhaps one needs to be weighted more than the others were in the original analysis (for instance, an environmental NGO might say distance to wetlands is more important than land cover type). Or perhaps there is some other variable that is needed instead of or in addition to these. If you are doing some kind of location-allocation, maybe different demographics need to be considered as demand points, such as low-income residents rather than the general population. 

**Step 3: conduct the alternative analysis**, producing a high quality static map.

**Step 4: write up a public comment.** I will share an example public comment I wrote on ECCC's *draft* environmental racism/justice strategy. Yours will not be as long! But you should likewise, _in no more than 500 words_, describe who you are/what stakeholder group, what that group's interests are, what fault you find with the existing analysis, the alternative approach you took, and a summary of what you found different.

Tentative Criteria:
1. **logic** - does the scenario make sense? Is it a likely stakeholder position?
2. **significance** - is the alternative analysis meaningful? Does it show something different, and something that the stakeholder would want to point out?
3. **cartography** - does the static map reflect cartographic conventions regarding projections, classification, symbology, and design? Think 2480 here.
4. **summary** - are key differences in the map

_You must include the original RFP **AND** analysis in your submission, but these do not count for the word count_

---
# Tutorial preview: Public Participation GIS with Survey123 - Part 2
<div class="split-slide" markdown="1">
<div markdown="1">
You will now make a map of squirrel observations using your and your classmates' Survey123 results.

Step 1: actually observe squirrels. Make 5-10 entries in your survey (which may amount to more than 5-10 squirrels depending on how many you see at a time). Note: this is not a wildlife biology class. I encourage you to get outside, touch grass, and actually find some squirrels, but if you are pressed for time, you can enter fictitious results. 

**Complete Step 1 _sometime prior to Sunday afternoon (the 15th)_ so that your classmates can compile all our findings into a single database for mapping purposes**

Step 2: In ArcGIS Pro, connect to this AGOL hosted feature layer representing the compliation of all our squirrel sightings.

Step 3: Design a bivariate map to represent the data. It should follow the cartographic principles we learned in 2480. 

Step 4: Take a screenshot of your map that includes your login information in ArcGIS Pro AND export your map as a high quality .png image file.

Step 5: Consider the iNaturalist [map of squirrel observations in Guelph](https://www.inaturalist.org/observations?place_id=140509&subview=map&taxon_id=45933), which you have effectively recreated (kind of). Think about the uncertainties and biases in these data. Where are there more observations than others? Why? 

Step 6: Submit both map images to the Courselink Quiz, inserting them as images rather than attaching them as files. _Write no more than 100 words_ with your reflections on how the iNaturalist equivalent of Squirrel Spotter may provide a better view of squirrel distributions than expert-led surveys, but one that is still skewed.

</div>
<div markdown="1">

![Survey123 image]({{ site.baseurl }}/assets/images/squirrels.png)

</div>
</div>

