import pandas as pd
from pathlib import Path

# First:    The county_api_call.py and state_api_call.py are called first
# Second:   The csv_df files are called second
# Third:    The plot files are called next

# path to read raw csv data from
read_path = Path('./BEA/files/raw_data/state_raw.csv')

# path to save cleaned data to 
save_path = Path('./BEA/files/data/state_clean.csv')

# csv to pandas df
state_raw_df = pd.read_csv(read_path)
# change Income column to integer from string
state_raw_df['Income'] = pd.to_numeric(state_raw_df['Income'])
print(state_raw_df.head(3))

# extract needed columns
pivot_state_merged_df = state_raw_df.pivot(index=['GeoFips','GeoName'], columns='Year', values='Income')
print(pivot_state_merged_df.head())
# calculate percentage change from 2019 - 2022
state_select_years = pivot_state_merged_df[[2010,2022]]
state_change = state_select_years.pct_change(axis='columns') * 100
state_change = state_change.reset_index()
state_change_clean = state_change.drop(index=0)

# save dataframe
state_change_clean.to_csv(save_path)
print(state_change_clean.head(3))