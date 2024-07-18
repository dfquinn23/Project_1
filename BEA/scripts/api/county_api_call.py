import pandas as pd
from call_api import CallAPI
from pathlib import Path

# First:    The county_api_call.py and state_api_call.py are called first
# Second:   The csv_df files are called second
# Third:    The plot files are called next

# path to save df to
path_one = Path('./BEA/files/raw_data/county_raw.csv')

# years that we want to hit the api for
years = [year for year in range(2010,2023)]

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

# save df
county_merged_df.to_csv(path_one)