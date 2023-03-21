import csv
from datetime import datetime

infile = open("sitka_weather_2018_simple.csv", "r")

csvfile = csv.reader(infile)

header_row = next(csvfile)  # eliminates the first line

print(type(header_row))

for index, column_header in enumerate(header_row):
    print(index, column_header)

highs = []  # y axis
lows = []
dates = []  # x axis

for row in csvfile:
    highs.append(int(row[5]))
    lows.append(int(row[6]))
    date = datetime.strptime(row[2], "%Y-%m-%d")
    dates.append(date)

print(highs)
print(lows)
print(dates)
