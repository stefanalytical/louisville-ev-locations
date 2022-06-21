import pandas as pd

df = pd.read_csv (r'/Users/stefanvuleta/louisville_ev/louisville_ev.csv')

df.drop(['coun_dist'], axis = 1, inplace = True)
print(df)

col = "num_votes"
max_x = df.loc[df[col].idxmax()]
print("Maximum value of column ", col, " is:\n", max_x)

