import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt

import hvplot.pandas
import geoviews as gv
from bokeh.io import output_notebook
from pathlib import Path

# path to save png
path_png = Path('./BEA/files/maps/state_pct_change_20192022.png')

# Path to the downloaded shapefile
# you can download 'shapefile_paths':
# https://www.census.gov/cgi-bin/geo/shapefiles/index.php
shapefile_path = './BEA/files/shapefiles/tl_2023_us_state.zip'

# Read the shapefile into a GeoDataFrame
gdf = gpd.read_file(shapefile_path)

# load is csv
state_pct_change = pd.read_csv('./BEA/files/data/state_change_19_22.csv')
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