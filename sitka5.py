import csv
import matplotlib as plt
from datetime import datetime

death_infile = open("death_valley_2018_simple.csv", "r")
sitka_infile = open("sitka_weather_2018_simple.csv", "r")

death_csvfile = csv.reader(death_infile, delimiter=",")
sitka_csvfile = csv.reader(sitka_infile, delimiter=",")

death_header_row = next(death_csvfile)  # eliminates the first line
sitka_header_row = next(sitka_csvfile)

# print(type(header_row))

# for index, column_header in enumerate(header_row):
#    print(index, column_header)

death_highs = []  # y axis
death_lows = []
death_dates = []  # x axis
sitka_highs = []  # y axis
sitka_lows = []
sitka_dates = []  # x axis


# Automatic Indexes: We hard coded the indexes corresponding to the TMIN and TMAX
# columns. Use the header row to determine the indexes for these values, so your program can work
# for Sitka or Death Valley. Use the station name to automatically generate an appropriate title
# for your graph as well.
for index, column_header in enumerate(death_header_row):
    if column_header == "TMAX":
        death_max_index = index
    elif column_header == "TMIN":
        death_min_index = index
    elif column_header == "DATE":
        death_date_index = index
    elif column_header == "NAME":
        death_name_index = index

for index, column_header in enumerate(sitka_header_row):
    if column_header == "TMAX":
        sitka_max_index = index
    elif column_header == "TMIN":
        sitka_min_index = index
    elif column_header == "DATE":
        sitka_date_index = index
    elif column_header == "NAME":
        sitka_name_index = index


for row in csvfile:
    highs.append(int(row[5]))  #
    lows.append(int(row[6]))


# create 2 subplot graphs in one visualization so you can see both graphs to compare side by side.


# Matplotlib's pyplot API has a convenience function called subplots() which acts as a
# utility wrapper and helps in creating common layouts of subplots, including the
# enclosing figure object, in a single call
