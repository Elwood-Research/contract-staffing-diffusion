# Variable Definitions and Mapping

## Facility Identifiers & Geographic Data
| PBJ Variable | Human-Readable Label | Type | Description |
|--------------|---------------------|------|-------------|
| `PROVNUM` | Facility Provider Number | String | 6-digit Medicare provider ID |
| `PROVNAME` | Facility Name | String | Name of the nursing home |
| `STATE` | State | String | 2-letter state postal code |
| `COUNTY_FIPS` | County FIPS Code | String | 3-digit county identifier |
| `WorkDate` | Work Date | Date | The specific day of reported staffing |
| `CY_Qtr` | Calendar Quarter | String | Format: YYYYQX |

## Nursing Staff Hours
| PBJ Variable | Human-Readable Label | Type | Definition |
|--------------|---------------------|------|------------|
| `Hrs_RN_emp` | RN Employee Hours | Numeric | Direct-hire RN hours |
| `Hrs_RN_ctr` | RN Contract Hours | Numeric | Agency/Contract RN hours |
| `Hrs_LPN_emp` | LPN Employee Hours | Numeric | Direct-hire LPN hours |
| `Hrs_LPN_ctr` | LPN Contract Hours | Numeric | Agency/Contract LPN hours |
| `Hrs_CNA_emp` | CNA Employee Hours | Numeric | Direct-hire CNA hours |
| `Hrs_CNA_ctr` | CNA Contract Hours | Numeric | Agency/Contract CNA hours |
| `MDScensus` | Daily Resident Census | Integer | Number of residents on WorkDate |

## Calculated Analysis Variables
- **Total Nursing Hours**: `Hrs_RN_emp + Hrs_RN_ctr + Hrs_LPN_emp + Hrs_LPN_ctr + Hrs_CNA_emp + Hrs_CNA_ctr`
- **Total Contract Hours**: `Hrs_RN_ctr + Hrs_LPN_ctr + Hrs_CNA_ctr`
- **Contract Ratio (Primary Outcome)**: `Total Contract Hours / Total Nursing Hours`
- **Nursing Hours Per Resident Day (HPRD)**: `Total Nursing Hours / MDScensus`

## Facility Covariates (Merged)
- **Facility Size**: Bed Count (from Provider Info)
- **Ownership**: For-Profit, Non-Profit, Government (from Provider Info)
- **Chain Status**: Multi-facility organization membership (from Provider Info)
- **Urban/Rural**: RUCA code or Metro/Non-metro status (from Provider Info)
