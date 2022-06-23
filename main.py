import pandas as pd

df = pd.read_csv ('louisville_evs.csv')
print(df)

df.drop(['OBJECTID', 'FID_EV_Charging_Suggestions', 'Comments', 'Location', 'Date', 'CreationDate', 'COUNDIST'], axis = 1, inplace = True)
df = df.dropna()

fixed_columns = {
    'NUMVOTES':'Num_Votes',
    'ZIPCODE':'Zip_Code',
}

df.rename(columns = fixed_columns, inplace = True)

df = df[df.Num_Votes != 0]
print(df)
