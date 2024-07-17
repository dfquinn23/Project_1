import pandas as pd
from call_api import CallAPI

from pathlib import Path

years = [year for year in range(2010,2023)]

path_one = Path('./BEA/files/data/state_change_19_22.csv')

# call data to pass into the api
call_data = {
    "method" : "GetData",
    "data_set" : "Regional",
    "tablename":'SAINC1',
    "geo":'STATE',
    "lc":'3',
    "years": years
}

# create CallAPI object
state_api = CallAPI(call_data)

# save to results
results = state_api.create_data_frames()

# merge the list of results dataframes
state_merged_df = pd.concat(results, ignore_index=True)

# change Income column to integer from string
state_merged_df['Income'] = pd.to_numeric(state_merged_df['Income'])
print(state_merged_df.head(3))

# extract needed columns
pivot_state_merged_df = state_merged_df.pivot(index=['GeoFips','GeoName'], columns='Year', values='Income')
print(pivot_state_merged_df.head(3))

# calculate percentage change from 2019 - 2022
state_selected_years_19_22 = pivot_state_merged_df[['2019','2022']]
state_change_19_22 = state_selected_years_19_22.pct_change(axis='columns') * 100
state_change_19_22 = state_change_19_22.reset_index()
state_change_19_22_drop = state_change_19_22.drop(index=0)

# save dataframe
state_change_19_22_drop.to_csv(path_one)
print(state_change_19_22_drop.head(3))