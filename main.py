import pandas as pd
import re

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

# Convert data types for both DataFrames
df = df.astype({"Zip_Code": str})
df2 = df2.astype({"Population": int, "Age": float})
df2["AVG_Income"] = df2["AVG_Income"].replace("[$,]", "", regex=True).astype(float)

dataTypeSeries = df.dtypes
print(dataTypeSeries)

dataTypeSeries2 = df2.dtypes
print(dataTypeSeries2)

