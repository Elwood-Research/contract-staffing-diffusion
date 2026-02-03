# Research Plan: Contract Staffing Diffusion

## Study Design
This is a longitudinal spatial analysis of nursing home staffing patterns using Payroll-Based Journal (PBJ) data from 2022 to 2024.

## Study Period
- January 1, 2022, to December 31, 2024 (CY2022Q1 - CY2024Q4).
- Analysis will be performed at the quarterly level to capture temporal trends.

## Data Sources
- **PBJ Daily Nurse Staffing**: Primary source for staffing hours (employee vs. contract) and resident census.
- **CMS Provider Information**: Supplementary source for facility characteristics (ownership, size, etc.).

## Methodology

### 1. Spatial Autocorrelation
- **County-level Moran's I**: Calculate global Moran's I for each quarter to measure overall spatial clustering of contract staffing ratios across U.S. counties.
- **Local Indicators of Spatial Association (LISA)**: Use LISA maps to identify specific "hotspots" (High-High clusters) and "coldspots" (Low-Low clusters).

### 2. Spatiotemporal Analysis
- Track the movement and growth of High-High clusters over the 12-quarter period.
- Calculate the "diffusion rate" by measuring the change in the number of high-contract facilities within various distance buffers (e.g., 10, 25, 50 miles).

### 3. Proximity Hypothesis Testing
- **Model**: A facility-level longitudinal model (e.g., Fixed Effects or GEE) predicting the `Contract Ratio`.
- **Primary Predictor**: Spatial lag of the contract ratio (average contract ratio of neighboring facilities within a defined distance).
- **Hypothesis**: Facilities closer to high-contract "hubs" will show faster increases in their own contract staffing ratios.

### 4. Regional Comparison
- Stratify Moran's I and hotspot analysis by U.S. Census Region to identify if diffusion mechanisms differ by regional market characteristics.

## Covariates
- **Facility Size**: Total number of beds.
- **Ownership Type**: For-profit, Non-profit, Government.
- **Chain Affiliation**: Member of a multi-facility chain (Yes/No).
- **Urban/Rural Status**: Based on Rural-Urban Commuting Area (RUCA) codes or Core Based Statistical Area (CBSA).
- **Resident Acuity**: Average case-mix or specific clinical indicators (if available).
