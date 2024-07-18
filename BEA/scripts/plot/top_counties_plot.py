import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

# First:    The county_api_call.py and state_api_call.py are called first
# Second:   The csv_df files are called second
# Third:    The plot files are called next

# path to save png
path_png_one = Path('./BEA/files/maps/top_counties.png')
path_png_two = Path('./BEA/files/maps/top_counties_seaborn.png')

# path to read csv data from
read_path = Path('./BEA/files/data/county_select_change.csv')

# load dataframe
county_df = pd.read_csv(read_path)

# counties should already be sorted, but just in case, sort then take the top 25
top_25_df = county_df.sort_values('2022', ascending=False).head(25)

print(top_25_df)
# Plot the data using matplotlib
plt.figure(figsize=(12, 8))
plt.barh(top_25_df['GeoName'], top_25_df['2022'], color='skyblue')
plt.xlabel('% Change in Income')
plt.ylabel('County')
plt.title('Top 25 Counties by % Change in Income from 2010 - 2022')
plt.gca().invert_yaxis()  # To have the highest income at the top
plt.savefig(path_png_one)
plt.show()

# seaborn plot
plt.figure(figsize=(12, 8))
sns.barplot(x=2022, y='GeoName', data=top_25_df, palette='viridis')
plt.xlabel('Income')
plt.ylabel('County')
plt.title('% Change in Income from 2010 - 2022')
plt.savefig(path_png_two)
plt.show()