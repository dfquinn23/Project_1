import pandas as pd
import time
import requests
from dotenv import load_dotenv
import os

load_dotenv()
beakey = os.environ.get('API_KEY_BEA')

class CallAPI:
        """This Class that hols call_data,  calls the BEA API using the call_data dictionary that is passed in
        call_data is a dicitonary with the fields:
                "method"
                "data_set"
                "tablename"
                "geo"
                "lc"
                "years" (an array of years)
        after pulling the data, it returns the results of the data as a pandas dataframe
        """
        def __init__(self, call_data):
                # This is an instance attribute
                self.method = call_data['method']
                self.data_set = call_data['data_set']
                self.tablename = call_data['tablename']
                self.geo = call_data['geo']
                self.lc = call_data['lc']
                self.years = call_data['years']
    

        def call_api(self, year):
                """This function calls the BEA API using the call_data dictionary that is passed in
                call_data is a dicitonary with the fields:
                        "method"
                        "data_set"
                        "tablename"
                        "geo"
                        "lc"
                        "year"
                after pulling the data, it returns the results of the data as a pandas dataframe
                """
                time.sleep(5)
                print(year)
                params = f'TableName={self.tablename}&GeoFips={self.geo}&LineCode={self.lc}&Year={year}'
                result = requests.get(
                                        f'https://apps.bea.gov/api/data?&UserID={beakey}' +
                                        f'&method={self.method}&datasetname={self.data_set}' +
                                        f'&{params}&ResultFormat=JSON').json()
                df = pd.DataFrame(result["BEAAPI"]['Results']['Data'])
                df = df.sort_values('DataValue', ascending=False)
                df = df[['GeoName','DataValue','TimePeriod', 'GeoFips']]
                # LEAVING GeoName as is so county and state can be changed outside here
                df = df.rename(columns={'DataValue':'Income','TimePeriod':'Year'})
                return df
        def create_data_frames(self):
                self.results = [self.call_api(year) for year in self.years]
                return self.results

        def get_results(self):
                return self.results
                