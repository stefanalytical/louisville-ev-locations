import pandas as pd
import re
import os

# region - DF1 (CSV)
# Read in first .CSV file using Pandas
df = pd.read_csv('CSVs/louisville_evs.csv')

# Drop rows that are not needed in final merged DataFrame
df.drop(['OBJECTID', 'FID_EV_Charging_Suggestions', 'Comments', 'Location', 'Date', 'CreationDate', 'COUNDIST'], axis = 1, inplace = True)

# Rename columns
fixed_columns = {
    'NUMVOTES':'Num_Votes',
    'ZIPCODE':'Zip_Code',
}
df.rename(columns = fixed_columns, inplace = True)

# Drop rows with value zero and remove all rows with Null/NaN values
df = df[df.Num_Votes != 0]
df = df.dropna()

# Rename strings in 'Name' column
df['Name'] = df['Name'].replace(['RIVERVIEW PARK', 'KROGER', 'BECKLEY PARK', 'Beckley Creek Park, Egg Lawn', 'EV Charging Suggestion: St.Matthews/ Eline Library', '7th Street Road at Industry Road / Metro Government Archives'],
                                ['Riverview Park', 'Kroger', 'Beckley Park', 'Egg Lawn', 'Eline Library', '7th Street at Industry Road'])
# endregion

# region - DF2 (CSV)
# Read in second .CSV file
df2 = pd.read_csv ('CSVs/crime_data_2021.csv')

# Include only 2 columns relevant to final DataFrame and only include rows with specific string
df2 = df2[['CRIME_TYPE', 'ZIP_CODE']]
df2 = df2[df2["CRIME_TYPE"].str.contains("MOTOR VEHICLE THEFT")]

# Remove decimal and digit after from all zip codes
df2 = df2.astype(str).replace(r'\.0$', '', regex=True)

# Rename columns to match other DataFrames and to allow for joining
fixed_columns = {
    'CRIME_TYPE':'Crime_Type',
    'ZIP_CODE':'Zip_Code',
}
df2.rename(columns = fixed_columns, inplace = True)

# Create new column to count the number of vehicle thefts per zip code and drop 'Crime_Type' column
df2['Vehicle_Theft_Per_Zip'] = df2.groupby(['Zip_Code']).transform('count')
df2.drop(['Crime_Type'], axis = 1, inplace = True)
# endregion

# region - DF3 (Scraped)
# Scrape data from html table
url = 'https://localistica.com/usa/ky/louisville/zipcodes/highest-household-income-zipcodes/'
scraper = pd.read_html(url)

# Get first table                                                                                                           
df3 = scraper[0]

# Drop and rename columns
df3.drop([1,3], axis = 1, inplace = True)
fixed_columns = {
    0:'Zip_Code',
    2:'Zip_Population',
    4:'Zip_Age',
    5:'Zip_Income',
}
df3.rename(columns = fixed_columns, inplace = True)
# endregion

# region - DF4 (Scraped)
# Scrape data from html table
url2 = 'http://zipatlas.com/us/ky/louisville/zip-code-comparison/median-household-income.html'
scraper2 = pd.read_html(url2)

# Get table                                                                                                           
df4 = scraper2[11]
df4 = df4[[1, 6]].copy()

# Rename columns to allow merger of DataFrames
fixed_columns = {
    1:'Zip_Code',
    6:'Zip_Income_National_Rank',
}
df4.rename(columns = fixed_columns, inplace = True)

# Drop first row with incorrect headings
df3 = df3.drop(df3.index[0])
df4 = df4.drop(df4.index[0])

# Remove hashtag and comma to convert str to int
df4['Zip_Income_National_Rank'] = df4['Zip_Income_National_Rank'].map(lambda x: x.lstrip('#'))
df4['Zip_Income_National_Rank'] = df4['Zip_Income_National_Rank'].str.replace(',', '')
# endregion

# region - Convert and Merge
# Convert data types for all DataFrames
df = df.astype({"Zip_Code": str})
df3 = df3.astype({"Zip_Population": int, "Zip_Age": float})
df3['Zip_Income'] = df3['Zip_Income'].replace('[$,]', '', regex=True).astype(float)
df4 = df4.astype({'Zip_Income_National_Rank': int})

# Created a fourth DataFrame by merging df, df3, df4 based on the Zip_Code column
final_df = pd.merge(pd.merge(df, df3, on='Zip_Code'), df4, on='Zip_Code')
# endregion

# region - Create and Format Columns
# Create calculated column and convert data type and supress scientific notation
final_df['Zip_Total_Income'] = final_df.Zip_Population * final_df.Zip_Income
final_df = final_df.astype({'Zip_Total_Income': int})
final_df = final_df.astype({'Zip_Income': int})

# Merge df2 and final_df and drop duplicate rows
final_df = final_df.merge(df2, on = 'Zip_Code')
final_df = final_df.drop_duplicates()

# Sort rows by values in 'Num_Votes' in descending order
final_df = final_df.sort_values('Num_Votes', ascending=False)

# Create new calculated ratio column and set decimal places to 5
final_df['Theft_Vote_Ratio'] = final_df['Num_Votes'] / final_df['Vehicle_Theft_Per_Zip']
final_df['Theft_Vote_Ratio'] = final_df['Theft_Vote_Ratio'].round(decimals = 5)

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
    if (x < 15000):
        return 'Small'
    if (x >= 15000 and x < 30000):
        return 'Medium'
    if x >= 30000:
        return 'Large'

# Create new column and apply filters
final_df['Income_Group'] = final_df['Zip_Income'].apply(filter1)
final_df['Age_Group'] = final_df['Zip_Age'].apply(filter2)
final_df['Zip_Pop_Size'] = final_df['Zip_Population'].apply(filter3)

# Assign correct zip code to row
final_df.at[856,'Zip_Code'] = '40214'
final_df.at[17907,'Zip_Code'] = '40222'
final_df.at[3819,'Zip_Code'] = '40228'

# Added locations to fill in all zip codes in Louisville
final_df.loc[len(final_df.index)] = ['Fairdale', '1', '40118', '-85.758855', '38.105069', '35.2', '9724', '46033', '8334', '447624892', '82', '0.01224', 'Medium Income', 'Mid-Aged', 'Large']
final_df.loc[len(final_df.index)] = ['Strathmoor Village', '1', '40205', '-85.677800', '38.220800', '41.3', '23678', '67446', '1792', '1596986388', '34', '0.02941', 'High Income', 'Older', 'Medium']
final_df.loc[len(final_df.index)] = ['Portland Christian School', '1', '40242', '-85.595482', '38.281155', '38.8', '10930', '63429', '2468', '693278970', '26', '0.03844', 'High Income', 'Mid-Aged', 'Small']
final_df.loc[len(final_df.index)] = ['GE Appliance Park', '1', '40225', '-85.649548', '38.175394', '0', '0', '0', '0', '0', '42', '0.02381', 'Low Income', 'Younger', 'Small']

# Rearrange columns to make DataFrame more readable
final_df = final_df[['Name', 'Num_Votes', 'Zip_Code', 'Longitude', 'Latitude', 'Zip_Age', 
                    'Zip_Population', 'Zip_Income', 'Zip_Income_National_Rank', 'Zip_Total_Income', 
                    'Vehicle_Theft_Per_Zip', 'Theft_Vote_Ratio', 'Income_Group', 'Age_Group', 'Zip_Pop_Size'
                    ]]
# endregion

# region - Create Cleaned Folder
# Make sure the clean data folder exists
new_csv_folder = ('clean_data')
check_folder = os.path.isdir(new_csv_folder)
if not check_folder:
    os.makedirs(new_csv_folder)

# Export cleaned Pandas DataFrame to CSV file
final_df.to_csv(('clean_data/cleaned_louisville_evs.csv'), index=False)
# endregion
print(final_df)