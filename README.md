# Identifying Optimal Locations for New Home Construction

## Project Overview
Home builders face the critical decision of selecting the best locations for new construction projects to maximize profitability and meet market demand. This project aims to identify and evaluate the most suitable areas for building new homes by analyzing various factors such as demographic trends, market value growth, and environmental risks. This analysis will provide actionable insights to guide home builders in making informed decisions about where to build.

## Objectives
1. Determine the top locations for new home construction based on comprehensive data analysis.
2. Analyze the impact of key factors such as population growth, economic growth, market demand, and environmental risks on the suitability of a location.
3. Provide a comparative analysis of different regions to highlight their attributes (e.g., growth rates) for new home construction.
4. Offer actionable recommendations to home builders on the most promising areas for development.

## Key Questions
1. Which regions exhibit the highest demand for new homes?
2. What are the home value implications for land in different counties?
3. How do demographic trends (population growth, income levels) influence the attractiveness of a location for home building?
4. How do environmental factors (climate, natural disaster risks) impact the suitability of a location for building new homes?

## Data Sources
- **Demographic Data:** Population growth, income levels, employment rates (U.S. Census Bureau - [API](https://www.census.gov/data/developers.html)).
- **Economic Data:** Local economic indicators, market trends (Bureau of Economic Analysis - [API](https://www.bea.gov/resources/for-developers)).
- **Real Estate Data:** Property prices, sales volumes, rental yields (Zillow - [API](https://www.zillowgroup.com/developers/)).
- **Geospatial Data:** Land availability and proximity to amenities (Google Maps - [API](https://developers.google.com/maps)).
- **Environmental Data:** Natural disaster risks (FEMA - [API](https://www.fema.gov/about/openfema/api)).

## Hypotheses
1. Counties with higher population growth will have a higher demand for new homes.
2. Counties with higher economic growth will have a higher demand for new homes.
2. Areas with higher growth rates for home values will be more attractive for new construction.
4. Locations with lower environmental risks will be preferred for new home construction.

## Evaluation Metrics
- **Cost Analysis:** Average land and construction costs.
- **Demand Analysis:** Sales volume, rental yields, population growth rates.
- **Risk Analysis:** Environmental risks, economic stability.
- **Accessibility Analysis:** Proximity to infrastructure and amenities.

## Project Timeline
- **7/2:** Project proposal alignment
- **7/3:** Git set-up and project scope agreement
- **7/8:** Eric's feedback and approval
- **7/10:** Data exploration
- **7/11:** Analysis
- **7/15:** Plotting
- **7/17:** Prediction
- **7/18:** Clean-up
- **7/21:** Presentation deck
- **7/22:** Project Due

## File Content Summariers

## Dependencies
This project requires Python and the following Python libraries installed:

import pandas
import time
import requests
import os
from dotenv import os
from dotenv import load_dotenv
from pathlib import Path
import geopandas
import matplotlib.pyplot
import hvplot.pandas
import geoviews
from bokeh.io import seaborn
from prophet import Prophet
from prophet.plot import add_changepoints_to_plot, plot_cross_validation_metric
from prophet.diagnostics import cross_validation, performance_metrics
import numpy
import json
import seaborn
from datetime import datetime, timedelta
import requests





## Directory Structure (abbreviated), Installation, and Usage
```
Project_1/
├── 01_MergedData/
│   ├── Data/
│ 
├── BEA/
│   ├── files/
│   │   ├── data/
│   │   ├── maps/
│   │   └── raw_data/
│   ├── notebooks/
│   │   ├── BEA.ipynb
│   │   └── BEA_Plots.ipynb
│   └── scripts/
│       ├── api/
│       ├── bonus-sb/api
│       ├── cvs_df
│       └── plot
│ 
├── Census/
│   ├── 7-17-24 Work/
│   ├── Draft Work/
│   └── .ipynb files
│
├── Weather/
│   ├── disaster_time_series_analysis.ipynb
│   ├── enviro_risk.ipynb
│   └── fema-data-analysis-notebook.ipynb
│
├── Zillow/
│   ├── home_values.ipynb
│   ├── home_values_county.ipynb
│   └── 
│
└── README.md


```

## Project Structure
- **01_MergedData/**: Contains the datasets used for the integration.
- **BEA/**: US Bureau of Economic Analysis: Jupyter Notebooks and Python scripts with data exploration, analysis, and visualizations.
- **Census/**: The US Census Bureau: Jupyter Notebooks and Python scripts with data exploration, analysis, and visualizations.
- **Weather/**: The Federal Emergency Management Agency (FEMA): Jupyter Notebooks and Python scripts with data exploration, analysis, and visualizations.
- **Zillow/**: Housing Data: Jupyter Notebooks and Python scripts with data exploration, analysis, and visualizations.
- **Spotify/**: Music Data (not used in the project): Jupyter Notebooks
- **README.md**: Project overview.
- **Project 1 Concept.docx**: Initial project ideation.


## Contributors
- Matt Cannon
- David Kaplan
- Dan Quinn
- Roberto Reis
