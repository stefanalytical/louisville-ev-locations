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

# Rename certain values in 'Name' column to match rest of data
df['Name'] = df['Name'].replace(['RIVERVIEW PARK', 'KROGER', 'BECKLEY PARK', 'Beckley Creek Park, Egg Lawn', 'EV Charging Suggestion: St.Matthews/ Eline Library'],
                                ['Riverview Park', 'Kroger', 'Beckley Park', 'Egg Lawn', 'Eline Library'])

# Scrape data from html table
url = 'https://localistica.com/usa/ky/louisville/zipcodes/highest-household-income-zipcodes/'
scraper = pd.read_html(url)

# Get first table                                                                                                           
df2 = scraper[0]

# Drop and rename columns
df2.drop([1], axis = 1, inplace = True)
fixed_columns = {
    0:'Zip_Code',
    2:'Zip_Population',
    3:'Zip_Growth_Percent',
    4:'Zip_Age',
    5:'Zip_Income',
}
df2.rename(columns = fixed_columns, inplace = True)

# Scrape data from html table
url2 = 'http://zipatlas.com/us/ky/louisville/zip-code-comparison/median-household-income.html'
scraper2 = pd.read_html(url2)

# Get table                                                                                                           
df3 = scraper2[11]
df3 = df3[[1, 6]].copy()

# Rename columns to allow merger of DataFrames
fixed_columns = {
    1:'Zip_Code',
    6:'Zip_National_Rank',
}
df3.rename(columns = fixed_columns, inplace = True)

# Drop first row with incorrect headings
df2 = df2.drop(df2.index[0])
df3 = df3.drop(df3.index[0])

# Remove hashtag and comma to convert str to int
df3['Zip_National_Rank'] = df3['Zip_National_Rank'].map(lambda x: x.lstrip('#'))
df3['Zip_National_Rank'] = df3['Zip_National_Rank'].str.replace(',', '')

# Convert data types for all DataFrames
df = df.astype({"Zip_Code": str})
df2 = df2.astype({"Zip_Population": int, "Zip_Age": float})
df2["Zip_Income"] = df2["Zip_Income"].replace("[$,]", "", regex=True).astype(float)
df2["Zip_Growth_Percent"] = df2["Zip_Growth_Percent"].str.rstrip("%").astype("float") / 100
df3 = df3.astype({"Zip_National_Rank": int})

# Created a fourth DataFrame by merging df, df2, df3 based on the Zip_Code column
final_df = pd.merge(pd.merge(df, df2, on='Zip_Code'), df3, on='Zip_Code')

# Create calculated column and convert data type and supress scientific notation
final_df['Zip_Total_Income'] = final_df.Zip_Population * final_df.Zip_Income
final_df = final_df.astype({"Zip_Total_Income": int})
final_df = final_df.astype({"Zip_Income": int})

# Define function filter to categorize int data to str
def filter1(x):
    if x <= 20000:
        return 'Low Income'
    if (x > 20000 and x <= 50000):
        return 'Medium Income'
    if x > 50000:
        return 'High Income'

def filter2(x):
    if x <= 35:
        return 'Younger'
    if (x > 35 and x <= 40):
        return 'Mid-Aged'
    if x > 40:
        return 'Older'

def filter3(x):
    if x < 1000:
        return 'Tiny'
    if (x >= 1000 and x < 15000):
        return 'Small'
    if (x >= 15000 and x < 30000):
        return 'Medium'
    if x >= 30000:
        return 'Large'

# Create new column and apply filters
final_df['Income_Group'] = final_df['Zip_Income'].apply(filter1)
final_df['Age_Group'] = final_df['Zip_Age'].apply(filter2)
final_df['Zip_Population_Size'] = final_df['Zip_Population'].apply(filter3)

print(final_df)

# Make sure the clean data folder exists
new_csv_folder = ('clean_data')
check_folder = os.path.isdir(new_csv_folder)
if not check_folder:
    os.makedirs(new_csv_folder)

# Export cleaned Pandas DataFrame to CSV file
final_df.to_csv(('clean_data/cleaned_louisville_evs.csv'), index=False)