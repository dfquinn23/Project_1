import pandas as pd
from call_api import CallAPI

from pathlib import Path

# First:    The county_api_call.py and state_api_call.py are called first
# Second:   The csv_df files are called second
# Third:    The plot files are called next

# path to save df to
path_one = Path('./BEA/files/raw_data/state_raw.csv')

years = [year for year in range(2010,2023)]

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

# return dfs to results
results = state_api.create_data_frames()

# merge the list of results dataframes
state_merged_df = pd.concat(results, ignore_index=True)

# save df to csv
state_merged_df.to_csv(path_one)