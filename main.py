import pandas as pd

df = pd.read_csv('clean_data/cleaned_louisville_evs.csv')

table = pd.pivot_table(df, index=['Zip_Pop_Size', 'Income_Group'], 
                       values=['Num_Votes'], aggfunc={'Num_Votes': 'count',})

table2 = pd.pivot_table(df, index=['Vehicle_Theft_Likeliness', 'Income_Group'], 
                       values=['Num_Votes'], aggfunc={'Num_Votes': 'count',})

print(table)
print(table2)