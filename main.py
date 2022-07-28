import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('clean_data/cleaned_louisville_evs.csv')

table = pd.pivot_table(df, index=['Zip_Pop_Size', 'Income_Group', 'Age_Group'], 
                       values=['Num_Votes'], aggfunc={'Num_Votes': 'sum',})

print(table)

x = [157,69,152]
x2 = [207,132,39]
x3 = [127,148,103]

df.groupby(['Income_Group']).sum().plot(kind='pie', y='Num_Votes')
plt.title("Percentage Of Votes For EV Charging Stations\n" + "Based On Louisville Income Groups", bbox={'facecolor':'0.8', 'pad':5})
plt.legend(bbox_to_anchor=(1.32, .95), loc='upper right', borderaxespad=0)
plt.ylabel("")
plt.pie(x, autopct='%.1f%%')

df.groupby(['Age_Group']).sum().plot(kind='pie', y='Num_Votes')
plt.title("Percentage Of Votes For EV Charging Stations\n" + "Based On Louisville Age Groups", bbox={'facecolor':'0.8', 'pad':5})
plt.legend(bbox_to_anchor=(1.32, .95), loc='upper right', borderaxespad=0)
plt.ylabel("")
plt.pie(x2, autopct='%.1f%%')

df.groupby(['Zip_Pop_Size']).sum().plot(kind='pie', y='Num_Votes')
plt.title("Percentage Of Votes For EV Charging Stations\n" + "Based On Louisville Zip Code Size", bbox={'facecolor':'0.8', 'pad':5})
plt.legend(bbox_to_anchor=(1.32, .95), loc='upper right', borderaxespad=0)
plt.ylabel("")
plt.pie(x3, autopct='%.1f%%')

plt.show()