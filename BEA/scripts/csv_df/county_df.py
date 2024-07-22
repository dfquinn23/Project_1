import pandas as pd
from pathlib import Path

# First:    The county_api_call.py and state_api_call.py are called first
# Second:   The csv_df files are called second
# Third:    The plot files are called next

# path to read raw csv data from
read_path = Path('./BEA/files/raw_data/county_raw.csv')

# path to save cleaned data to 
save_path_one = Path('./BEA/files/data/county_clean.csv')
save_path_two = Path('./BEA/files/data/county_select_change.csv')

# csv to pandas df
county_raw_df = pd.read_csv(read_path)

# change Income column to integer from string
county_raw_df['Income'] = pd.to_numeric(county_raw_df['Income'])
print(county_raw_df.head(3))

# create a pivot plot
pivot_merged_df = county_raw_df.pivot(index=['GeoFips','GeoName'], columns='Year', values='Income')
print(pivot_merged_df.head(3))

# calculate percent change
pct_change_df = pivot_merged_df.pct_change(axis='columns') * 100
pct_change_df = pct_change_df.reset_index()

# save dataframe
pct_change_df.to_csv(save_path_one, index=False)
print(pct_change_df.head(3))

# select years 2019 - 2022 to calculate percent difference between years
selected_pct_change = pivot_merged_df[[2010,2022]]
percent_change = selected_pct_change.pct_change(axis='columns')
percent_change.reset_index()

percent_change = percent_change.drop(columns=[2010])
percent_change[2022] = percent_change[2022].astype(str)


percent_change[2022] = percent_change[2022].replace('inf', 0)
percent_change[2022] = percent_change[2022].replace('nan', 0)

percent_change[2022] = pd.to_numeric(percent_change[2022])


percent_change = percent_change.sort_values(2022, ascending=False)
percent_change = percent_change.rename(columns={2022:'Income Change'})

# save dataframe
percent_change.to_csv(save_path_two)
print(percent_change[:50])