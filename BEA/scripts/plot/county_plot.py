import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt

import hvplot.pandas
import geoviews as gv
from bokeh.io import output_notebook
from pathlib import Path

# First:    The county_api_call.py and state_api_call.py are called first
# Second:   The csv_df files are called second
# Third:    The plot files are called next

output_notebook()
gv.extension('bokeh')

# Path to save heatmap
path_heatmap = Path('./BEA/files/maps/county_heatmap.html')

# Path to the downloaded shapefile
# you can download 'shapefile_paths':
# https://www.census.gov/cgi-bin/geo/shapefiles/index.php
shapefile_path = './BEA/files/shapefiles/tl_2023_us_county.zip'

# Read the shapefile into a GeoDataFrame
gdf = gpd.read_file(shapefile_path)

# csv to pandas df
pct_change = pd.read_csv('./BEA/files/data/county_select_change.csv')

# ensure GeoFips and GEOID are integers and not strings
pct_change['GeoFips'] = pd.to_numeric(pct_change['GeoFips'])
gdf['GEOID'] = pd.to_numeric(gdf['GEOID'])

# merge gdf and pandas df for mapping by state
merged = gdf.merge(pct_change, left_on='GEOID', right_on='GeoFips')

# set up heatmap
heatmap = merged.hvplot.polygons(
    geo=True,
    tiles='CartoLight',
    color='percent_increase',
    hover_cols=['NAME', 'percent_increase'],
    line_color='black',
    line_width=0.1,
    title='Percentage Increase in Income by County 2010 - 2022'
)

# save heatmap
hvplot.save(heatmap, path_heatmap)
# Show the plot inline
heatmap