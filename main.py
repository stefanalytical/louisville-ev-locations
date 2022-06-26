import pandas as pd

# Read in cleaned .csv file
df = pd.read_csv ('clean_data/cleaned_louisville_evs.csv')

# Create calculated column to find total income per zip code
df['Zip_Total_Income'] = df.Population_Per_Zip * df.Income_Per_Zip

# Convert data type to integer to supress scientific notation
df = df.astype({"Zip_Total_Income": int})
df = df.astype({"Income_Per_Zip": int})

# Define function filter to categorize int data to str
def filter(x):
    if x <= 20000:
        return 'Low Income'
    if (x > 20000 and x <= 50000):
        return 'Medium Income'
    if x > 50000:
        return 'High Income'

# Create new column and apply filter to 'Income_Per_Zip' column 
df['Income_Group'] = df['Income_Per_Zip'].apply(filter)

# Define function filter to categorize int data to str
def filter(x):
    if x <= 35:
        return 'Younger'
    if (x > 35 and x <= 40):
        return 'Mid-Aged'
    if x > 40:
        return 'Older'

# Create new column and apply filter to 'Age_Per_Zip' column 
df['Age_Group'] = df['Age_Per_Zip'].apply(filter)

# Define function filter to categorize int data to str
def filter(x):
    if x <= 35:
        return 'Younger'
    if (x > 35 and x <= 40):
        return 'Mid-Aged'
    if x > 40:
        return 'Older'

# Create new column and apply filter to 'Age_Per_Zip' column 
df['Age_Group'] = df['Age_Per_Zip'].apply(filter)

print(df)

#df22 = df['Age_Group'].dtypes
#print(df22)

# Export final cleaned Pandas DataFrame to CSV file that will overwrite previous file
df.to_csv(('clean_data/cleaned_louisville_evs.csv'), index=False)

