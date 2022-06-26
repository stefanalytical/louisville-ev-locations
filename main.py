import pandas as pd

df = pd.read_csv ('clean_data/cleaned_louisville_evs.csv')

df['Zip_Total_Income'] = df.Population_Per_Zip * df.Income_Per_Zip

df = df.astype({"Zip_Total_Income": int})
df = df.astype({"Income_Per_Zip": int})

print(df)
