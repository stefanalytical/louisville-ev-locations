# [Louisville EV Charging Locations](https://github.com/stefanalytical/louisville_ev_locations.git)
**This is a project for Code Louisville Data Analytics Session 2 Fall 2022**

Disclaimer: Towards the end of the project I realized zip codes were not the best method to accurately map data. Going forward, I will use a combination of Federal Information Processing Systems (FIPS) codes and shapefiles in tandem with geopandas and will update this repository.

## About

As electric vehicles become more common place, the need for charging stations will grow substantially. In late 2017, Louisville Metro crowdsourced data to determine where Louisville Residents wanted EV charging stations most. In total, there were over 200 respondents that helped identify over 150 locations around the city for better EV charging infrastructure. These responses will allow the city to prioritize constructions internally and with third parties.




In Fall 2017, Louisville Metro used crowdsourcing to identify locations in Louisville with the highest demand for EV chargers. Over 200 respondents helped identify dozens of locations around the city where there is a demand for better EV charging infrastructure. Their responses will help determine where to prioritize the construction of new charging stations both internally and with partners.




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
## Features Used

Category 1: Python Programming Basics:
```bash
- Implement a “master loop” console application where the user can repeatedly enter commands/perform actions, including choosing to exit the program.
- Build a conversion tool that converts user input to another type and displays it (ex: converts cups to grams).	
```

Category 2: Utilize External Data:
```bash
- Read data from an external file, such as text, JSON, CSV, etc, and use that data in your application.
- Connect to an external/3rd party API and read data into your app
```

Category 3: Data Display:
```bash
- Visualize data in a graph, chart, or other visual representation of data.
- Display data in tabular form
```

Category 4: Best Practices:
```bash
- The program should utilize a virtual environment and document library dependencies in a requirements.txt file.
```

Stretch List:
```bash
- Use pandas, matplotlib, and/or numpy to perform a data analysis project. Ingest 2 or more pieces of data, analyze that data in some manner, and display a new result to a graph, chart, or other display.
```

## Usage

The data used in the analysis is updated to reflect the latest prices for each currency. The conversion tool can take the data from the API and allow you to manipulate it to compare the value of currencies around the world.

The chart that displays the 15 currencies of higher value than the USD gives a clear picture in terms of US buying power eslewhere. By using pandas and myplotlib, I was able to retrieve the JSON data and graph this visual. I was rather surprised that so many currencies were currently of higher value than the USD, with the Kuwaiti Dinar being the most expensive.
