import pandas as pd

df = pd.read_csv (r'/Users/stefanvuleta/louisville_ev/louisville_evs.csv')
print(df)

df.drop(['OBJECTID', 'FID_EV_Charging_Suggestions', 'Comments', 'Location', 'Date', 'CreationDate', 'COUNDIST'], axis = 1, inplace = True)

print(df.columns)

fixed_columns = {
    'NUMVOTES':'Num_Votes',
    'ZIPCODE':'Zip_Code',

}

df.rename(columns = fixed_columns, inplace = True)
print(df)