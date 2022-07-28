# [Louisville EV Charging Locations](https://github.com/stefanalytical/louisville_ev_locations.git)
_**This is a project for Code Louisville Data Analytics Session 2 Fall 2022**_

**Disclaimer**: Towards the end of the project I realized zip codes were not the best method to accurately map data. Going forward, I will use a combination of Federal Information Processing Systems (FIPS) codes and shapefiles in tandem with geopandas and will update this repository.

## About

As electric vehicles become more common place, the need for charging stations will grow substantially. In late 2017, Louisville Metro crowdsourced data to determine where Louisville Residents wanted EV charging stations most. In total, there were over 200 respondents that helped identify over 150 locations around the city for better EV charging infrastructure. These responses will allow the city to prioritize constructions internally and with third parties.

## Project Goals

In the simplest form, this project ingests, analyzes, and displays data. My goal was to merge CSV files and to scrape websites to create a new set of data that will give deeper meaning to the residents' votes. This allows one to better understand and visualize the desire for these new locations and to possibly find correlations between various variables. Ultimately, I wanted these questions answered:

1. Did any zip codes receive substantially more than others?
2. Did the zip code size, age group, or income group in a zip code affect the number of votes received?
3. Did the correlation of specific variables in a zip code affect the number of votes?
4. What were the top 10 zip codes in terms of votes received and did the vehicle theft to votes ratio play a role?
5. When this data was visualized, what would it look like?

## Installation

This project was created using Python 3.10. A virtual environment is required to run the program.

First, clone the repository: [https://github.com/stefanalytical/real-time-currency-converter.git](https://github.com/stefanalytical/real-time-currency-converter.git)

Once the virtual environment is activated, please install the packages found in the requirements.txt folder.

```bash
pip install -r requirements.txt
```
Run the file
```bash
python Conversion.py
```

Relevant packages that were used:
```bash
pip install requests
pip install tk
pip install pandas
pip install myplotlib
pip install re
```
## Project Requirements

Category 1: Loading Data:
```bash
- Read TWO data files (CSV).
- Scrape TWO pieces of data from anywhere on the internet and utilize it in your project.	
```

Category 2: Clean and Operate the Data While Combining Them:
```bash
- Clean your data and perform a pandas merge with your two data sets, then calculate some new values based on the new data set.
```

Category 3: Visualize/Present Your Data:
```bash
- Make a Tableau dashboard to display your data.
- Make at least 1 Pandas pivot table and 1 matplotlib/seaborn plot.
```
Category 4: Best Practices:
```bash
- Utilize a virtual environment and include instructions in your README on how the user should set one up.
- List dependencies in a requirement.txt file.
```

Interpretation of Your Data:
```bash
- Annotate your .py files with well-written comments and a clear README.md
```

## Usage

The data used in the analysis is updated to reflect the latest prices for each currency. The conversion tool can take the data from the API and allow you to manipulate it to compare the value of currencies around the world.

The chart that displays the 15 currencies of higher value than the USD gives a clear picture in terms of US buying power eslewhere. By using pandas and myplotlib, I was able to retrieve the JSON data and graph this visual. I was rather surprised that so many currencies were currently of higher value than the USD, with the Kuwaiti Dinar being the most expensive.