# Inclusion and Exclusion Criteria

## Inclusion Criteria
To be included in the analytic sample, a facility-day must meet the following criteria:
1. **Certification**: Facility must be Medicare-certified.
2. **Staffing Reporting**: Facility must have reported non-zero total nursing hours (RN, LPN, or CNA) for the given WorkDate.
3. **Census Reporting**: Facility must have a reported resident census (`MDScensus`) greater than zero.
4. **Geographic Location**: Facility must be located in one of the 48 contiguous U.S. states or the District of Columbia (excluding HI, AK, and territories for spatial consistency).

## Exclusion Criteria
Observations will be excluded if they meet any of the following:
1. **Outliers**:
   - Total Nursing HPRD > 24 hours (implausible staffing level).
   - Total Nursing HPRD < 1 hour (extreme low staffing).
   - Contract Ratio > 1.0 (reporting error where contract > total).
2. **Statistical Outliers**: Following the study protocol, continuous variables (HPRD, Contract Ratio) will be screened, and observations with |z| > 4 will be removed.
3. **Missing Geographic Data**: Facilities with missing or invalid County FIPS codes that cannot be mapped.
4. **Extreme Low Volume**: Categorical levels with <5% membership (e.g., specific rare ownership types) may be excluded or collapsed.

## Sample Flow (STROBE)
The final analysis will include a STROBE flow diagram detailing:
- Total facilities/days available in 2022-2024.
- Count of observations excluded due to zero hours/census.
- Count of observations excluded due to outlier thresholds.
- Final analytic sample size (Facilities and facility-days).
