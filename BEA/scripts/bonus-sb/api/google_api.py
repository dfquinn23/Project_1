import pandas as pd
import requests
import time

from dotenv import load_dotenv
import os

from pathlib import Path

import json

# First:    The county_api_call.py and state_api_call.py are called first
# Second:   The csv_df files are called second
# Third:    The plot files are called next

# path to save cleaned data to 
save_path = Path('./BEA/files/data/starbucks_county.csv')

# path to read csv data from
read_path = Path('./BEA/files/data/county_select_change.csv')

# Sample GeoFip DataFrame
geo_df = pd.read_csv(read_path)

counties = geo_df['GeoName']

# Your Google Maps API key
load_dotenv()
API_KEY = os.environ.get('API_KEY_MAPS')

def get_starbucks_count(county, api_key):
    url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
    query = f"Starbucks in {county}"
    params = {
        'query': query,
        'key': api_key
    }
    response = requests.get(url, params=params)
    data = response.json()

    # Count the number of Starbucks locations
    count = len(data['results'])

    print(json.dumps(data['results'], indent=4))

    
    # If there are more pages of results, iterate through them
    while 'next_page_token' in data:
        time.sleep(2)  # Required delay before making the next request
        params['pagetoken'] = data['next_page_token']
        response = requests.get(url, params=params)
        data = response.json()
        count += len(data['results'])
    
    return count

# Add a new column for Starbucks count
geo_df['StarbucksCount'] = geo_df['GeoName'].apply(lambda name: get_starbucks_count(name, API_KEY))

geo_df.to_csv(save_path)
print(geo_df)