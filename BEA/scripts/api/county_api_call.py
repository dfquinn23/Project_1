import pandas as pd
from call_api import CallAPI
import os
from pathlib import Path


years = [year for year in range(2010,2023)]
path_one = Path('./BEA/files/data/county_pct_change.csv')
path_two = Path('./BEA/files/data/county_change_19_22.csv')

call_data = {
    "method" : "GetData",
    "data_set" : "Regional",
    "tablename":'CAINC4',
    "geo":'COUNTY',
    "lc":'30',
    "years": years
}

# create API class
county_api = CallAPI(call_data)

# store results of dataframes
results = county_api.create_data_frames()


for result in results:
    print(result.head(1))

# merge the results
county_merged_df = pd.concat(results, ignore_index=True)

# change Income column to integer from string
county_merged_df['Income'] = pd.to_numeric(county_merged_df['Income'])
print(county_merged_df.head(3))

# create a pivot plot
pivot_merged_df = county_merged_df.pivot(index=['GeoFips','GeoName'], columns='Year', values='Income')
print(pivot_merged_df.head(3))

# calculate percent change
pct_change_df = pivot_merged_df.pct_change(axis='columns') * 100
pct_change_df = pct_change_df.reset_index()

# save dataframe
pct_change_df.to_csv(path_one, index=False)
print(pct_change_df.head(3))

# select years 2019 - 2022 to calculate percent difference between years
selected_years_19_22 = pivot_merged_df[['2019','2022']]
change_19_22 = selected_years_19_22.pct_change(axis='columns')
change_19_22.reset_index()

# save dataframe
change_19_22.to_csv(path_two)
print(change_19_22.head(3))