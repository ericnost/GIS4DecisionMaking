---
layout: lectures
title: "Week 6: Enterprise GIS"
permalink: /lectures/week-06/
---

# Week 6
## Enterprise GIS

WebGIS as spatial data infrastructure, Enterprise GIS, project management, scenario analysis tutorial preview

---
# Application 2 - Proposal
Step 1: review the Discussion Board and select an RFP to respond to. 

Step 2: consider what data and analysis will be necessary. 

Step 3: write your bid in no more than 500 words -
- **Data**: An inventory of the datasets you intend to use, including the agency/source, spatial resolution, temporal currency, and a link, where available. 
- **Anticipated Methodology:** A brief narrative describing the intended analysis techniques (e.g., Multi-Criteria Evaluation, network routing) and a ModelBuilder diagram illustrating it
- **Project Timeline:** A simply but realistic Gantt chart outlining the steps from data acquisition and processing to analysis and final map production.

_You must include the RFP you are responding to in your bid._

Step 4: submit to the Courselink Dropbox

---
## There's both too little and too much data in the world. 

## Much (thouh increasingly less) of it is produced and held by governments, for the public interest

## How do we find what we need?

---
# Spatial Data Infrastructure
> As multiple government agencies are sharing their data on one platform, SDI reduces data redundancy and the extra efforts in collecting duplicated geospatial data. From a cost/benefit perspective, SDI allows geospatial data to be collected once and reused multiple times in different applications.

Components:
- **Geoportals** e.g. Data.gov, ArcGIS hubs, Open Government Canada, Ontario Data Catalogue, Ontario GeoHub, Geo.ca, Guelph Open Data
- **Metadata**: data about the data that tells us about currency, resolution, provenance, accuracy, etc.
- **Search**: spatial and/or text

> Historically, the majority of local government GIS programs employed cost recovery, where data is sold to cover development and maintenance costs. Many local governments found that the effort of cost recovery was outweighed by the benefits of open data. In 2010, all 10 counties in the Metro-Denver, Colorado region charged for their geospatial data.  As of 2019, all but Gilpin County have open data sites.

---
# WebGIS
- **API: Application Programming Interface**. "A set of specifications for functions, objects, data structures and communications protocols that facilitate reuse of code and enable programming at a high level of abstraction. Web GIS makes extensive use of APIs."
- **Cloud**: "Someone else's computer."
- **SaaS**: "Software as a Service." (Software applications subscribed to and accessed online through the cloud)

Takeaway: _"GIS functionality is delivered to an organization without said organization having any awareness of, or responsibility for, the underlying infrastructure and software components."_

---
# WebGIS implementation
Implementation: [hosted services](https://www.esri.com/arcgis-blog/products/developers/developers/arcgis-hosted-services-use-cases-for-each-type-of-data-service)

**Map tile services** (think weather maps)

![Map tile layer](https://www.esri.com/arcgis-blog/app/uploads/2025/09/arcgis-map-tile-raster-layers.jpg)

**Vector tile services** (think Google Maps) 

![Vector tile layer](https://www.esri.com/arcgis-blog/app/uploads/2025/09/interactive-vector-tile-layer.gif)

**Feature services** (e.g. your City of Guelph tree map!) 

![Feature service layer](https://www.esri.com/arcgis-blog/app/uploads/2025/09/feature-service-age-income-in-LA.gif)

# WebGIS in municipal operations
<div class="split-slide" markdown="1">
<div markdown="1">
![City of Denver GIS](https://bok-figures.s3.amazonaws.com/files/DA05_Fig1.png)
</div>

<div markdown="1">

> This architecture diagram highlights the variety of GIS integrations from an enterprise geospatial database to the City and County of Denver’s Enterprise Applications. 

[City of Denver Real Estate search](https://property.spatialest.com/co/denver#/map/search/)
</div>
</div>

---
# Enterprise GIS
> **GIS infrastructure, processes and tools at scale within the context of an organization.**
> ...the **people**, **processes** and **technology** by which geospatial data, maps, apps, and tools are integrated into and deployed within the context of an organization. 

_Technology_ - functions Enterprise GIS serves within an organization
-	Centralized storage of geospatial data
- Securing sharing and dissemination of geospatial data, maps, apps and tools (e.g. AGOL groups)
- Web GIS.
- System integration (e.g. with other enterprise tools like CAD)

---
# Enterprise GIS
_Process_ not just product
> planning, management, and iterative improvement steps that are undertaken in the context of an organization to identify the functional requirements of an organization, translate business needs into geospatial information products, build a well-performing technical infrastructure to deliver and disseminate those products, and integrate it into an organization’s business processes and culture

---
# Types of organizations (_People_)
See [Table 1](https://gistbok-ltb.ucgis.org/current/concept/KE-03-033)

---
# Ways GIS is embedded in organizations (_People_)
- **Senior Executive Office:** Special management position or office inside the senior executive management office of an organization (e.g., Mayor or City Manager’s Office)
    - Maybe some smaller NGOs or businesses
- **User Department:** Placement inside a line department or office in the organization that is a principal user of GIS and which has been assigned a role for organization-wide GIS coordination and management.
    - e.g. placed in the Ministry of Transport or Natural Resources because historically they were the first to use GIS
- **Organization’s Information Technology Department:** Placement inside the unit and given responsibility for the information technology management and support for the organization.
    - Grand River Conservation Authority
    - City of Guelph
-	**Independent Public Entity:** Approach for GIS in public-sector agencies in which GIS management is assigned to an existing or newly created autonomous organization, not directly managed by or in the line of authority of the organization(s) that it serves.
-	**Outsourced to External Contractor:** All or some GIS management and coordination functions are assigned to an external group (e.g., private company, public agency, or non-profit organization) with terms established through a formal contract.
    - RFPs!

[Table 3](https://gistbok-ltb.ucgis.org/current/concept/KE-03-033)

---
# Ways GIS is embedded in organizations (_People_)
<div class="split-slide" markdown="1">
<div markdown="1">
Example: "a GIS office is placed inside a City’s Information Technology Department. This office would have responsibility for managing the GIS program and supporting users in all City departments and coordinating with external organizations for sharing of data and access to the GIS."
</div>

<div markdown="1">
![chart](https://bok-figures.s3.amazonaws.com/files/FCXX-Fig2.png)
</div>
</div>
---
# Stakeholders (_People_)

- **GIS managers:** Individuals or bodies with a formal or informal role in planning, managing, overseeing, or coordinating GIS programs and projects.  
- **GIS/IT technical staff:** Individuals with technical skills and roles in GIS program development and operations.
- **Direct GIS users:** Individuals or groups that directly access GIS software and applications to support their organization’s needs. 
- **Indirect GIS users:** Individuals and groups that have access to products generated from a GIS (e.g., map) but do not access GIS software or data directly.
- **Organization management:** Mid-level or senior managers in organizations that have a role in overseeing GIS operations, approving resources for GIS, or which have other decision-making responsibilities that impact GIS programs and products. 
- **External partners:** Outside organizations, with which the organization running the GIS program collaborates, normally through a formal agreement.
- **Product/service providers:** Includes any parties, most frequently private companies, which provide GIS programs with an array of products (e.g., GIS software and hardware) and services. 

[Section 2.2](https://gistbok-ltb.ucgis.org/current/concept/KE-03-033)

---
# Project management
All GIS, including GIS for Decision-Making, takes place in context

Often that context is an organization 
- Internal: colleagues, supervisors, support staff
- External: clients, stakeholders, users

What does working in this sort of context look like? To be successful, project management

_What does project management look like for you?_

---
# Project management

![Project management flow chart](https://bok-figures.s3.amazonaws.com/files/FC33-Fig4.jpg)

---
# Project management
- **Initiating**
> Identifying stakeholders and soliciting their input, or identifying key project personnel such as the project manager or the sponsors.
> Rationale....the merits of such work, including needs assessments, business cases, or alignment of the project with the organization.
- **Planning**
> Project plan: elements to address any criteria that could have an impact on its success, including its scope, schedule, budget, quality, risk, and procurement needs [see next slide].
- **Controlling**
> Meetings, status reporting, and progress tracking
- **Executing**
> In a well-executed project, the work will move along as planned and should be relatively stress-free (?!)
- **Closing**
> Providing the deliverables and having the customer or stakeholder accept them. 
- **Ongoing improvement**

---
# GIS project management structure

![Project management structure](https://bok-figures.s3.amazonaws.com/files/KE12_Fig1.jpg)

---
# GIS project management structure

- **Scope, Time, and Cost**
> The scope refers to all work that will be done to complete the project and what processes will be followed to accomplish this work. The most common planning and management approach is to break the project down into hierarchical tasks that are sequenced and individually assigned durations and resources (including personnel). -> Gantt
-	**Quality** - "the degree to which project deliverables meet requirements”
-	**Risk** – four ways to avoid risk
    -	_Avoidance_: adjusting a project plan (tasks, timing, resources, etc.) to protect objectives from negative impacts.
    -	_Transference_: the consequences or responsibility of a risk are shifted to a third party.
    -	_Mitigation_: reduction in the probability and/or impacts of an adverse risk event to an acceptable level.
    -	_Acceptance_: the risk event or threat is understood but not addressed by changes to the project plan or by the addition of resources to respond to the risk.
-	**Stakeholders/communication**
-	**Procurement**
> If an organization lacks all of the resources (e.g. skilled staff, equipment, software) necessary for completing projects, they may turn to procuring these resources.

---
# Gantt Charts
<div class="split-slide" markdown="1">
<div markdown="1">

![Gantt Chart](https://courses.ems.psu.edu/geog583/sites/geog583/files/images/Lesson_7/Lesson7_Image_gant.png)
</div>

<div markdown="1">

[Source](https://courses.ems.psu.edu/geog583/node/436)

[Gantt Charts in Excel](https://support.microsoft.com/en-us/excel/present-your-data-in-a-gantt-chart-in-excel)

</div>

</div>

---
# Beyond Gantt Charts
Just as there are many different kinds of organizations, there are many different project management approaches! We’ll review some general principles, but they may not always apply.

Software development PM:
- Waterfall, Agile/Scrum, Lean, Kanban, oh my! See [here](https://www.kpi.com/en/blog/2019/07/31/overview-of-leading-project-management-philosophies-and-methodologies/)

Project management and collaboration tools
- ArcGIS Enterprise, other Esri utilities
- Slack, Github, Trello, etc.

---
# Other project management tools
<div class="split-slide" markdown="1">
<div markdown="1">
**Map series**– “[you often] need to create a series of easily referenced and reproduced maps that are at the exact same scale, have minimal overlap, and maintain consistent collar material throughout."

[Source](https://saylordotorg.github.io/text_essentials-of-geographic-information-systems/s14-02-gis-project-management-tools-a.html)

[Esri](https://doc.esri.com/en/arcgis-pro/latest/help/layouts/map-series.html)
</div>

<div>
<iframe id="kmsembed-1_l6i1lilv" width=800 height=500 src="https://mediaspace.esri.com/embed/secure/iframe/entryId/1_l6i1lilv/uiConfId/49806163" class="kmsembed" allowfullscreen webkitallowfullscreen mozAllowFullScreen allow="autoplay *; fullscreen *; encrypted-media *" referrerPolicy="no-referrer-when-downgrade" sandbox="allow-downloads allow-forms allow-same-origin allow-scripts allow-top-navigation allow-pointer-lock allow-popups allow-modals allow-orientation-lock allow-popups-to-escape-sandbox allow-presentation allow-top-navigation-by-user-activation" frameborder="0" title="Thematic map series in ArcGIS Pro"></iframe>
</div>
</div>

---
# Failure
> Murphy’s Law of Project Management states that no major project is completed on time, within budget, and with the same staff that started it—do not expect yours to be the first. It has been estimated that only 16 percent of fully implemented information technology projects are completed on time and within budget

[Source](https://saylordotorg.github.io/text_essentials-of-geographic-information-systems/s14-01-project-management-basics.html)

Why does it happen? Poor planning, lack of support, poor PM, lack of involvement of client
> More than one GIS project has been completed and delivered to the client, only to discover that the final product was neither what the client envisioned nor what the client wanted.

---
# Exericse: Plan your bid
_Turn to a partner and start thinking through some of the details together_

1. what project have you chosen?
2. briefly write out:
  - what kinds of data do you need?
  - what kinds of analysis will you do?
  - what kinds of products will you deliver?
3. guesstimate how much time each step will take (data collection, analysis, map design)

---
# Tutorial preview: Scenario analysis with GIS beyond ArcGIS
<div class="split-slide" markdown="1">
<div markdown="1">
By the end of this lab, you will be able to apply well-known conservation tools – namely, the InVEST suite of models – to map land use/land cover scenarios and perform ecosystem services valuation. This is a chance for you to further explore GIS beyond ArcGIS.
</div>
<div markdown="1">

![Scenarios/Invest tutorial result]({{ site.baseurl }}/assets/images/invest.png)

</div>
</div>

