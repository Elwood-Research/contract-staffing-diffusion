import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import os

# State to FIPS mapping
state_to_fips = {
    'AL': '01', 'AK': '02', 'AZ': '04', 'AR': '05', 'CA': '06', 'CO': '08', 'CT': '09', 'DE': '10',
    'DC': '11', 'FL': '12', 'GA': '13', 'HI': '15', 'ID': '16', 'IL': '17', 'IN': '18', 'IA': '19',
    'KS': '20', 'KY': '21', 'LA': '22', 'ME': '23', 'MD': '24', 'MA': '25', 'MI': '26', 'MN': '27',
    'MS': '28', 'MO': '29', 'MT': '30', 'NE': '31', 'NV': '32', 'NH': '33', 'NJ': '34', 'NM': '35',
    'NY': '36', 'NC': '37', 'ND': '38', 'OH': '39', 'OK': '40', 'OR': '41', 'PA': '42', 'RI': '44',
    'SC': '45', 'SD': '46', 'TN': '47', 'TX': '48', 'UT': '49', 'VT': '50', 'VA': '51', 'WA': '53',
    'WV': '54', 'WI': '55', 'WY': '56', 'PR': '72', 'VI': '78'
}

# Paths
data_path = '/data/PBJ_dailynursestaffing_CY2024Q4.csv'
geojson_path = '/study/04-analysis/us-counties.json'
output_dir = '/study/04-analysis/outputs/figures'
output_path = f'{output_dir}/county_contract_map_2024.png'

# Ensure output dir exists
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

print("Loading data...")
# Read in chunks or usecols to save memory
df = pd.read_csv(data_path, usecols=['STATE', 'COUNTY_FIPS', 'Hrs_RN', 'Hrs_RN_ctr', 'Hrs_LPN', 'Hrs_LPN_ctr', 'Hrs_CNA', 'Hrs_CNA_ctr'], encoding='latin1', low_memory=False)

# Convert staffing hours to numeric, coerce errors to 0
for col in ['Hrs_RN', 'Hrs_RN_ctr', 'Hrs_LPN', 'Hrs_LPN_ctr', 'Hrs_CNA', 'Hrs_CNA_ctr']:
    df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0)

# Calculate total hours and contract hours
df['Total_Nursing_Hrs'] = df['Hrs_RN'] + df['Hrs_LPN'] + df['Hrs_CNA']
df['Total_Contract_Hrs'] = df['Hrs_RN_ctr'] + df['Hrs_LPN_ctr'] + df['Hrs_CNA_ctr']

# Aggregate by county
print("Aggregating by county...")
# Ensure COUNTY_FIPS is numeric
df['COUNTY_FIPS'] = pd.to_numeric(df['COUNTY_FIPS'], errors='coerce')
df = df.dropna(subset=['COUNTY_FIPS'])

county_agg = df.groupby(['STATE', 'COUNTY_FIPS']).agg({
    'Total_Nursing_Hrs': 'sum',
    'Total_Contract_Hrs': 'sum'
}).reset_index()

# Calculate ratio
county_agg['Contract_Ratio'] = county_agg['Total_Contract_Hrs'] / county_agg['Total_Nursing_Hrs']
county_agg['Contract_Ratio'] = county_agg['Contract_Ratio'].fillna(0)

# Create 5-digit FIPS
county_agg['state_fips'] = county_agg['STATE'].map(state_to_fips)
# Handle cases where COUNTY_FIPS might be float or int
county_agg = county_agg.dropna(subset=['state_fips', 'COUNTY_FIPS'])
county_agg['county_fips_3'] = county_agg['COUNTY_FIPS'].astype(int).astype(str).str.zfill(3)
county_agg['GEOID'] = county_agg['state_fips'] + county_agg['county_fips_3']

# Load GeoJSON
print("Loading GeoJSON...")
counties = gpd.read_file(geojson_path)

# Merge
# Note: GeoJSON id is the 5-digit FIPS based on previous inspect
merged = counties.merge(county_agg, left_on='id', right_on='GEOID', how='left')

print("Columns in merged:", merged.columns.tolist())

# Handle missing data (counties with no nursing homes)
merged['Contract_Ratio'] = merged['Contract_Ratio'].fillna(0)

# Use 'state_fips' which comes from county_agg
merged = merged[~merged['state_fips'].isin(['72', '78'])]

# Plot
print("Plotting map...")
fig, ax = plt.subplots(1, 1, figsize=(20, 12))
# Filter out non-continental for better zoom using state_fips
continental = merged[~merged['state_fips'].isin(['02', '15'])]
continental = continental.to_crs("EPSG:5070") # Albers Equal Area Conic for USA

continental.plot(column='Contract_Ratio', ax=ax, legend=True,
            legend_kwds={'label': "Contract Staffing Ratio", 'orientation': "horizontal", 'shrink': 0.5, 'pad': 0.05},
            cmap='OrRd', edgecolor='black', linewidth=0.1)

ax.set_title('County-Level Distribution of Contract Staffing Intensity (2024Q4)', fontsize=20)
ax.set_axis_off()

# Save
print(f"Saving to {output_path}...")
plt.savefig(output_path, dpi=300, bbox_inches='tight')
print("Done!")
