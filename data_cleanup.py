import pandas as pd
import re
import os

df = pd.read_csv ('louisville_evs.csv')
df.drop(['OBJECTID', 'FID_EV_Charging_Suggestions', 'Comments', 'Location', 'Date', 'CreationDate', 'COUNDIST'], axis = 1, inplace = True)
df = df.dropna()
fixed_columns = {
    'NUMVOTES':'Num_Votes',
    'ZIPCODE':'Zip_Code',
}
df.rename(columns = fixed_columns, inplace = True)
df = df[df.Num_Votes != 0]

# Scrape data from html table
url = 'https://localistica.com/usa/ky/louisville/zipcodes/highest-household-income-zipcodes/'
scraper = pd.read_html(url)

# Get first table                                                                                                           
df2 = scraper[0]

# Drop and rename columns
df2.drop([1, 3], axis = 1, inplace = True)
fixed_columns = {
    0:'Zip_Code',
    2:'Population_Per_Zip',
    4:'Age_Per_Zip',
    5:'Income_Per_Zip',
}

df2.rename(columns = fixed_columns, inplace = True)

# Drop first row with incorrect headings
df2 = df2.drop(df2.index[0])

# Convert data types for both DataFrames
df = df.astype({"Zip_Code": str})
df2 = df2.astype({"Population_Per_Zip": int, "Age_Per_Zip": float})
df2["Income_Per_Zip"] = df2["Income_Per_Zip"].replace("[$,]", "", regex=True).astype(float)

#dataTypeSeries = df.dtypes
#print(dataTypeSeries)
#dataTypeSeries2 = df2.dtypes
#print(dataTypeSeries2)

df3 = pd.merge(df, df2, on='Zip_Code')
print(df3)

# Make sure the clean data folder exists
new_csv_folder = ('clean_data/new_csv')
check_folder = os.path.isdir(new_csv_folder)
if not check_folder:
    os.makedirs(new_csv_folder)

# Export cleaned Pandas DataFrame to CSV file
df3.to_csv(('clean_data/new_csv/new_louisville_evs.csv'), index=False)
