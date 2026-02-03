# Contract Staffing Diffusion in U.S. Nursing Homes (2022-2024)

## Overview
This study investigates the geographic diffusion of contract nursing staffing across United States nursing homes from 2022 to 2024. Using Payroll-Based Journal (PBJ) data, we analyze how the reliance on agency staff has spread spatially and identified regional hotspots of contract staffing adoption.

## Key Findings
- **Increasing Spatial Clustering**: Moran's I analysis shows that clustering of contract staffing usage significantly increased from 0.0501 in 2022Q1 to 0.1068 in 2024Q4.
- **Proximity Influence**: A facility's contract staffing ratio is strongly predicted by the usage levels of other facilities in the same county (Coefficient: 0.3963, p < 0.001).
- **Regional Hotspots**: The Northeast region (particularly Vermont and Pennsylvania) maintained the highest reliance on contract staffing throughout the study period.
- **Geographic Variation**: Top states for agency reliance in 2024 include Vermont (23.5%), North Dakota (15.5%), and Montana (13.7%).

## Methodology
The study utilizes facility-level PBJ data to measure the ratio of contract hours to total hours for Registered Nurses (RNs), Licensed Practical Nurses (LPNs), and Certified Nursing Assistants (CNAs). Spatial autocorrelation and proximity regression models were employed to test the diffusion hypotheses.

## Visualizations
The study includes advanced spatial mapping to visualize the diffusion:
- **Contract Ratio Map (2024)**: State-level choropleth map showing the intensity of agency labor reliance.
- **Spatial Hotspots Map**: Identifying regional clusters and "staffing corridors" where agency usage is most concentrated.

## Repository Structure
- `01-literature/`: Literature review and BibTeX references.
- `02-research-plan/`: Hypotheses and study design.
- `03-methods/`: Inclusion criteria and variable definitions.
- `04-analysis/`: Python scripts and aggregated outputs (tables/figures).
- `05-manuscript/`: Final research paper (LaTeX source and PDF).

## License
This research is published by Elwood Research.
