import pandas as pd
from pathlib import Path

# path to read raw csv data from
bea_path = Path('./BEA/files/data/county_select_change.csv')
census_path = Path('./Census/7-17-24 Work/7-18-CSVs/2010_2022_pop_totals_CAGR.csv')
weather_path = Path('./Weather/ranked_disasters_by_year_county.csv')
zillow_path = Path('./Zillow/home_value_CAGR.csv')

# path to save cleaned data to 
save_path = Path('./01_MergedData/data/top_counties.csv')

# csv to pandas df
bea_df = pd.read_csv(bea_path)
census_df = pd.read_csv(census_path)
weather_df = pd.read_csv(weather_path)
zillow_df = pd.read_csv(zillow_path)

census_df = census_df[['GeoFips', 'Total Growth Rate']]
census_df['Total Growth Rate'] = census_df['Total Growth Rate'] * 100
census_df = census_df.sort_values('Total Growth Rate', ascending=False)
census_df = census_df[:300]


bea_df = bea_df.sort_values('2022', ascending=False)[:300]
zillow_df = zillow_df.sort_values('CAGR', ascending=False)[:300]


weather_df = weather_df.rename(columns={'county_fips':'GeoFips'})

zillow_df = zillow_df.rename(columns={'County_State':'GeoName'})
bea_df['GeoName'] = bea_df['GeoName'].apply(lambda x: x.replace('*', '') if '*' in x else x)


zillow_df['GeoName'] = zillow_df['GeoName'].apply(lambda x: x.replace(' County', '') if ' County' in x else x)


print(census_df.columns)

county_zillow = pd.merge(bea_df, zillow_df, on='GeoName').dropna()

print(census_df.head())

merged_df = pd.merge(county_zillow, census_df, on='GeoFips')


print(merged_df.head(25))

merged_df.to_csv(save_path)