import csv
from datetime import datetime

infile = open("death_valley_2018_simple.csv", "r")

csvfile = csv.reader(infile)

header_row = next(csvfile)  # eliminates the first line

print(type(header_row))

for index, column_header in enumerate(header_row):
    print(index, column_header)

highs = []  # y axis
lows = []
dates = []  # x axis


# Automatic Indexes: We hard coded the indexes corresponding to the TMIN and TMAX
# columns. Use the header row to determine the indexes for these values, so your program can work
# for Sitka or Death Valley. Use the station name to automatically generate an appropriate title
# for your graph as well.


# create 2 subplot graphs in one visualization so you can see both graphs to compare side by side.


# Matplotlib's pyplot API has a convenience function called subplots() which acts as a
# utility wrapper and helps in creating common layouts of subplots, including the
# enclosing figure object, in a single call
