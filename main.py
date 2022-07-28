import pandas as pd # Allows us to read in cleaned CSV file
import matplotlib.pyplot as plt # Allows us to plot 3 pie charts

# Read in CSV file using Pandas
df = pd.read_csv('clean_data/cleaned_louisville_evs.csv')

# Pandas pivot table drilling down the number of votes received per each group
table = pd.pivot_table(df, index=['Zip_Pop_Size', 'Income_Group', 'Age_Group'], 
                       values=['Num_Votes'], aggfunc={'Num_Votes': 'sum',})
print(table)

# First pie chart showing percentage of votes based on income groups
x = [157,69,152] # Number of votes for each subgroup
df.groupby(['Income_Group']).sum().plot(kind='pie', y='Num_Votes') # Sum the number of votes for each subgroup
plt.title("Percentage Of Votes For EV Charging Stations\n" + "Based On Louisville Income Groups", bbox={'facecolor':'0.8', 'pad':5}) # Add a title
plt.legend(bbox_to_anchor=(1.32, .95), loc='upper right', borderaxespad=0) # Moves the legend and prevents from overlapping
plt.ylabel("") # Removes the y label
plt.pie(x, autopct='%.1f%%') # Displays the percentage in each slice

# Second pie chart showing percentage of votes based on age groups
x2 = [207,132,39] # Number of votes for each subgroup
df.groupby(['Age_Group']).sum().plot(kind='pie', y='Num_Votes') # Sum the number of votes for each subgroup
plt.title("Percentage Of Votes For EV Charging Stations\n" + "Based On Louisville Age Groups", bbox={'facecolor':'0.8', 'pad':5}) # Add a title
plt.legend(bbox_to_anchor=(1.32, .95), loc='upper right', borderaxespad=0) # Moves the legend and prevents from overlapping
plt.ylabel("") # Removes the y label
plt.pie(x2, autopct='%.1f%%') # Displays the percentage in each slice

# Third pie chart showing percentage of votes based on zip code size
x3 = [127,148,103] # Number of votes for each subgroup
df.groupby(['Zip_Pop_Size']).sum().plot(kind='pie', y='Num_Votes') # Sum the number of votes for each subgroup
plt.title("Percentage Of Votes For EV Charging Stations\n" + "Based On Louisville Zip Code Size", bbox={'facecolor':'0.8', 'pad':5}) # Add a title
plt.legend(bbox_to_anchor=(1.32, .95), loc='upper right', borderaxespad=0) # Moves the legend and prevents from overlapping
plt.ylabel("") # Removes the y label
plt.pie(x3, autopct='%.1f%%') # Displays the percentage in each slice
plt.show()