import pandas as pd
import requests
import geopandas as gpd

df = pd.read_csv ('louisville_evs.csv')
df.drop(['OBJECTID', 'FID_EV_Charging_Suggestions', 'Comments', 'Location', 'Date', 'CreationDate', 'COUNDIST'], axis = 1, inplace = True)
df = df.dropna()
fixed_columns = {
    'NUMVOTES':'Num_Votes',
    'ZIPCODE':'Zip_Code',
}
df.rename(columns = fixed_columns, inplace = True)
df = df[df.Num_Votes != 0]
print(df)

# Scrape data from html table
url = 'https://localistica.com/usa/ky/louisville/zipcodes/highest-household-income-zipcodes/'
scraper = pd.read_html(url)

# Get first table                                                                                                           
df2 = scraper[0]

# Drop and rename columns
df2.drop([1, 3], axis = 1, inplace = True)
fixed_columns = {
    0:'Zip_Code',
    2:'Population',
    4:'Age',
    5:'AVG_Income',
}

df2.rename(columns = fixed_columns, inplace = True)

# Drop first row with incorrect headings
df2 = df2.drop(df2.index[0])
print(df2)

# Read GeoJSON File into a GeoPandas DF
df3 = gpd.read_file('https://services1.arcgis.com/79kfd2K6fskCAkyg/arcgis/rest/services/OpenDataMetroLib/FeatureServer/1/query?outFields=*&where=1%3D1&f=geojson')

# Drop columns that are not relevant. County column will be dropped later so data can be filtered by Jefferson County only.
df3.drop(['OBJECTID', 'AOI_WEB', 'FCC', 'GlobalID'], axis = 1, inplace = True)

# Drop all rows that don't contain Jefferson County.
df3 = df3[df3['COUNTY'] == 'JEFFERSON']

fixed_columns = {
    'NAME':'Areas_of_Interest',
    'COUNTY':'County',
    'Shape__Area':'Shape_Area',
    'Shape__Length':'Shape_Length',
    'geometry':'Geometry',
}

df3.rename(columns = fixed_columns, inplace = True)

# Drop County column after data was filtered to only include areas of interest in Jefferson County.
df3.drop(['County'], axis = 1, inplace = True)

print(df3)
print(df3.columns)
