import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import geopandas as gpd
from scipy import stats

# Set paths
DATA_DIR = '/data'
STUDY_DIR = '/study'
OUTPUT_FIGURES = os.path.join(STUDY_DIR, '04-analysis/outputs/figures')
GEOJSON_PATH = os.path.join(STUDY_DIR, '04-analysis/us-states.json')

os.makedirs(OUTPUT_FIGURES, exist_ok=True)

state_name_to_abbr = {
    'Alabama': 'AL', 'Alaska': 'AK', 'Arizona': 'AZ', 'Arkansas': 'AR', 'California': 'CA',
    'Colorado': 'CO', 'Connecticut': 'CT', 'Delaware': 'DE', 'Florida': 'FL', 'Georgia': 'GA',
    'Hawaii': 'HI', 'Idaho': 'ID', 'Illinois': 'IL', 'Indiana': 'IN', 'Iowa': 'IA',
    'Kansas': 'KS', 'Kentucky': 'KY', 'Louisiana': 'LA', 'Maine': 'ME', 'Maryland': 'MD',
    'Massachusetts': 'MA', 'Michigan': 'MI', 'Minnesota': 'MN', 'Mississippi': 'MS', 'Missouri': 'MO',
    'Montana': 'MT', 'Nebraska': 'NE', 'Nevada': 'NV', 'New Hampshire': 'NH', 'New Jersey': 'NJ',
    'New Mexico': 'NM', 'New York': 'NY', 'North Carolina': 'NC', 'North Dakota': 'ND', 'Ohio': 'OH',
    'Oklahoma': 'OK', 'Oregon': 'OR', 'Pennsylvania': 'PA', 'Rhode Island': 'RI', 'South Carolina': 'SC',
    'South Dakota': 'SD', 'Tennessee': 'TN', 'Texas': 'TX', 'Utah': 'UT', 'Vermont': 'VT',
    'Virginia': 'VA', 'Washington': 'WA', 'West Virginia': 'WV', 'Wisconsin': 'WI', 'Wyoming': 'WY',
    'District of Columbia': 'DC'
}

def load_and_process(quarter):
    file_path = os.path.join(DATA_DIR, f'PBJ_dailynursestaffing_CY{quarter}.csv')
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return None
    
    print(f"Loading {file_path}...")
    cols = ['PROVNUM', 'STATE', 'MDScensus', 
            'Hrs_RN', 'Hrs_LPN', 'Hrs_CNA', 
            'Hrs_RN_ctr', 'Hrs_LPN_ctr', 'Hrs_CNA_ctr']
    
    df = pd.read_csv(file_path, usecols=cols, encoding='latin1', low_memory=False)
    
    # Filter valid MDScensus
    df = df[df['MDScensus'] > 0]
    
    # Aggregate to facility-quarterly averages
    df_fac = df.groupby(['PROVNUM', 'STATE']).mean().reset_index()
    
    # Calculate Contract Ratio
    df_fac['Total_Hrs'] = df_fac['Hrs_RN'] + df_fac['Hrs_LPN'] + df_fac['Hrs_CNA']
    df_fac['Contract_Hrs'] = df_fac['Hrs_RN_ctr'] + df_fac['Hrs_LPN_ctr'] + df_fac['Hrs_CNA_ctr']
    
    # Handle division by zero
    df_fac['Contract_Ratio'] = np.where(df_fac['Total_Hrs'] > 0, df_fac['Contract_Hrs'] / df_fac['Total_Hrs'], 0)
    
    # Screen outliers: |z| > 4 for Contract Ratio
    z_scores = stats.zscore(df_fac['Contract_Ratio'])
    df_fac = df_fac[np.abs(z_scores) <= 4]
    
    return df_fac

# 1. Load Data
df_2024 = load_and_process('2024Q4')
df_2022 = load_and_process('2022Q1')

# Calculate Average by State
state_avg_2024 = df_2024.groupby('STATE')['Contract_Ratio'].mean().reset_index()
state_avg_2022 = df_2022.groupby('STATE')['Contract_Ratio'].mean().reset_index() if df_2022 is not None else None

# 2. Load GeoJSON
usa = gpd.read_file(GEOJSON_PATH)

# Add STATE abbreviation to GeoJSON
usa['STATE_ABBR'] = usa['name'].map(state_name_to_abbr)

# 3. Merge
usa_2024 = usa.merge(state_avg_2024, left_on='STATE_ABBR', right_on='STATE', how='left')

# 4. Generate 2024 Map
fig, ax = plt.subplots(1, 1, figsize=(15, 10))
# Exclude Alaska and Hawaii for the main continental map to make it more readable, 
# or use a projection that includes them properly. 
# For now, let's keep it simple but filter to Continental US for better visualization if needed.
# continental_usa = usa_2024[~usa_2024['STATE_ABBR'].isin(['AK', 'HI'])]

usa_2024.plot(column='Contract_Ratio', ax=ax, legend=True,
              legend_kwds={'label': "Average Contract Staffing Ratio",
                           'orientation': "horizontal"},
              cmap='YlOrRd', missing_kwds={'color': 'lightgrey'})

ax.set_title('Geographic Distribution of Contract Staffing Intensity (2024Q4)', fontsize=16)
ax.axis('off')

plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_FIGURES, 'contract_ratio_map_2024.png'), dpi=300)
print("Saved 2024 map.")

# 5. Generate Change Map or 2022 Map if available
if state_avg_2022 is not None:
    merged_all = state_avg_2024.merge(state_avg_2022, on='STATE', suffixes=('_2024', '_2022'))
    merged_all['Change'] = (merged_all['Contract_Ratio_2024'] - merged_all['Contract_Ratio_2022'])
    
    usa_change = usa.merge(merged_all, left_on='STATE_ABBR', right_on='STATE', how='left')
    
    # Use TwoSlopeNorm to center the colormap at 0
    from matplotlib.colors import TwoSlopeNorm
    
    # Calculate min, max and check if they cross zero
    vmin = usa_change['Change'].min()
    vmax = usa_change['Change'].max()
    
    if vmin < 0 < vmax:
        norm = TwoSlopeNorm(vmin=vmin, vcenter=0, vmax=vmax)
    else:
        norm = None
    
    fig, ax = plt.subplots(1, 1, figsize=(15, 10))
    usa_change.plot(column='Change', ax=ax, legend=True,
                   legend_kwds={'label': "Change in Average Contract Staffing Ratio (2022Q1 to 2024Q4)",
                                'orientation': "horizontal"},
                   cmap='PuOr', norm=norm, missing_kwds={'color': 'lightgrey'})
    
    ax.set_title('Change in Contract Staffing Intensity (2022Q1 to 2024Q4)', fontsize=16)
    ax.axis('off')
    
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_FIGURES, 'spatial_hotspots_map.png'), dpi=300)
    print("Saved change map.")
else:
    # If 2022 is not available, just save another version of 2024 as requested for 'spatial_hotspots_map.png'
    # or identify actual hotspots (High-High)
    plt.savefig(os.path.join(OUTPUT_FIGURES, 'spatial_hotspots_map.png'), dpi=300)

print("Map generation complete.")
