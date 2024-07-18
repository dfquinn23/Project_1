import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# First:    The county_api_call.py and state_api_call.py are called first
# Second:   The csv_df files are called second
# Third:    The plot files are called next

# Path to the downloaded shapefile
# you can download 'shapefile_paths':
# https://www.census.gov/cgi-bin/geo/shapefiles/index.php
shapefile_path = './BEA/files/shapefiles/tl_2023_us_state.zip'

# path to save png
path_png = Path('./BEA/files/maps/state_pct_change.png')

# path to read csv data from
read_path = Path('./BEA/files/data/state_clean.csv')

# Read the shapefile into a GeoDataFrame
gdf = gpd.read_file(shapefile_path)

# load is csv
state_pct_change = pd.read_csv(read_path)
# merge csv with gdp for mapping 
state_merged = gdf.merge(state_pct_change, left_on='NAME', right_on='GeoName')
gdf.head()

# set up and plot
fig, ax = plt.subplots(1, 1, figsize=(15, 10))
state_merged.boundary.plot(ax=ax)
state_merged.plot(column='2022', ax=ax, legend=True,
            legend_kwds={'label': "Percent Change in Income",
                         'orientation': "horizontal"})
plt.title('Percent Change in Income by State')
plt.savefig(path_png)
plt.show()