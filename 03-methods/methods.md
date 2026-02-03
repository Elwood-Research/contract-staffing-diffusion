# Methodology

## Data Sources
The primary data for this study were obtained from the Centers for Medicare \& Medicaid Services (CMS) Payroll-Based Journal (PBJ) system, covering the period from January 1, 2022, through December 31, 2024. The PBJ system provides daily, facility-level records of staffing hours for both direct employees and contract staff. These data were supplemented with the Minimum Data Set (MDS) resident census figures to calculate staffing intensity. Facility-level metadata, including ownership status, bed count, and chain affiliation, were extracted from the CMS Provider Information files. Geographic identifiers, including county FIPS codes and facility coordinates, were used to facilitate the spatial analysis components of the study.

## Analytic Sample and Selection Process
The study population consists of all CMS-certified nursing facilities in the United States. We applied a sequential exclusion process to arrive at the final analytic sample. Initially, all facilities reporting to the PBJ system during the study period were included. We then excluded facilities with incomplete reporting, defined as missing more than five days of data in any given calendar quarter. Facilities with aberrant staffing ratios, such as those reporting zero total nursing hours or resident census counts that fluctuated by more than 50\% within a month without corresponding changes in capacity, were also removed. Furthermore, we excluded specialized facilities (e.g., pediatric or psychiatric nursing homes) that do not representative the general long-term care market. Based on these criteria, the final longitudinal analytic sample is estimated to include approximately 14,800 facilities, representing over 95\% of all Medicare- and Medicaid-certified nursing homes in the United States.

## Variable Construction
The primary outcome of interest is the **Contract Staffing Ratio**, which measures the proportion of total nursing care provided by agency or contract personnel. To construct this variable, we first aggregated daily hours for Registered Nurses, Licensed Practical Nurses, and Certified Nursing Assistants. For each staff category, we distinguished between hours worked by direct-hire employees and those worked by contract staff. The Contract Staffing Ratio was calculated as the sum of all contract nursing hours divided by the total nursing hours (employee plus contract) across all three categories. This ratio provides a comprehensive measure of a facility's reliance on external labor markets. Covariates used in the analysis include facility size (total bed count), ownership type (for-profit, non-profit, or government), and chain affiliation status.

## Spatial Analysis Framework
We employed a spatial econometrics framework to examine the diffusion of contract staffing across the United States. 

### Spatial Weights and Autocorrelation
To define spatial relationships between facilities, we constructed a spatial weights matrix using Queen contiguity at the county level. This approach assumes that facilities within the same or neighboring counties share similar labor market conditions. To test the first hypothesis (H1), we calculated Global Moran’s I for the Contract Staffing Ratio in each calendar quarter. This statistic measures the degree of global spatial autocorrelation, where a positive and significant Moran’s I indicates that facilities with similar contract staffing levels are geographically clustered.

### Local Indicators of Spatial Association (LISA)
To identify specific geographic clusters and address the second hypothesis (H2), we utilized Local Indicators of Spatial Association (LISA). This method identifies four types of spatial associations: High-High (hotspots), Low-Low (coldspots), High-Low, and Low-High outliers. High-High clusters represent regions where facilities with high contract staffing ratios are surrounded by other high-use facilities, signifying potential regional hubs of agency labor reliance.

### Spatial Expansion Analysis
To test the fourth hypothesis (H4) regarding the growth of contract staffing over time, we performed a spatial expansion analysis. This involved measuring the temporal change in the number and geographic extent of High-High hotspots. We tracked the centroid movement and the area of these clusters across the 12-quarter study period to determine if high-contract staffing patterns were spreading into adjacent territories or intensifying within existing hubs.

## Statistical Modeling
### Proximity Hypothesis Testing
To evaluate the "Proximity Hypothesis" (H3), which posits that a facility's adoption of contract staffing is influenced by the behavior of its neighbors, we developed a distance-based regression model. The model predicts a facility's Contract Staffing Ratio based on the average contract use of all other facilities within a 50-mile radius. We employed a Spatial Lag Model (SLM) to account for spatial dependency, controlling for facility-level characteristics such as size, ownership, and chain status. A positive and significant coefficient for the spatial lag term would support the hypothesis that proximity to high-contract facilities increases the likelihood of a facility increasing its own reliance on contract labor.

### Regional Stratification
Recognizing that nursing home labor markets are often regional or state-based, we performed sub-analyses stratified by U.S. Census Region (Northeast, Midwest, South, and West) to test the fifth hypothesis (H5). This allows for the identification of regional variations in diffusion mechanisms and the influence of state-level policies or market characteristics on contract staffing trends.

## Outlier Handling and Data Cleaning
To ensure the robustness of our estimates, we applied a strict outlier exclusion rule for all continuous staffing variables. Any observation with a z-score greater than 4 or less than -4 (|z| > 4) for total nursing hours per resident day or individual staff category hours was excluded from the analysis. This threshold was chosen to remove extreme values that likely represent reporting errors while retaining the natural variation present in the national nursing home market.

## Software and Computation
All data processing and statistical analyses were conducted using Python (version 3.10+). We utilized several key libraries, including **Pandas** for data manipulation, **SciPy** and **Statsmodels** for traditional statistical modeling, and the **PySAL** (Python Spatial Analysis Library) ecosystem for spatial weight construction, Moran's I calculation, and LISA mapping. Visualizations and spatial plots were generated using **Matplotlib** and **Geopandas**.
