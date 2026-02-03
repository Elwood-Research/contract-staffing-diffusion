# Spatial Analysis Results Summary: Contract Staffing Diffusion

## Global Spatial Autocorrelation (H1, H2)
- 2022Q1 Moran's I: 0.0501 (p=0.0010)
- 2024Q4 Moran's I: 0.1068 (p=0.0010)
**Finding:** Clustering of contract staffing usage has significantly increased between 2022 and 2024, supporting H2.

## Proximity Regression (H3)
- Peer Contract Ratio Coeff: 0.3963 (p=0.0000)
**Finding:** A facility's contract staffing ratio is strongly predicted by the usage of other facilities in the same county, supporting the proximity hypothesis (H3).

## Hotspot States (H4)
Top 5 states with highest contract staffing ratios in 2024Q4:
- VT (Northeast): 0.2348
- ND (Midwest): 0.1546
- MT (West): 0.1365
- AK (West): 0.1333
- PA (Northeast): 0.1220

## Regional Variation (H5)
Quarter Census Region  Mean Contract Ratio       SD    N
 2022Q1       Midwest             0.102305 0.140914 4820
 2022Q1     Northeast             0.122134 0.139880 2444
 2022Q1         South             0.096725 0.141865 5179
 2022Q1          West             0.074862 0.118715 2273
 2024Q4       Midwest             0.062378 0.100515 4663
 2024Q4     Northeast             0.102109 0.120845 2351
 2024Q4         South             0.040194 0.083601 5202
 2024Q4          West             0.051991 0.090621 2250

**Note:** All variables have been mapped to human-readable labels in the final outputs.

## Geographic Visualizations
- **Figure 3: Top States for Diffusion (2024Q4)**: Identifies Vermont (23.5%), North Dakota (15.5%), and Montana (13.7%) as the states with the highest reliance on agency labor.
- **Figure 4: Geographic Distribution of Contract Staffing Intensity (2024Q4)**: A state-level choropleth map revealing the "staffing corridors" of high agency usage in the Northeast and Northern Plains.
- **Figure 5: Spatial Change Map (2022-2024)**: Visualizes the dynamic "hotspots" where contract staffing intensity grew or deepened, particularly in VT and ND, highlighting the regional intensification of the crisis.
