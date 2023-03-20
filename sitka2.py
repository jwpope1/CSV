# We are adding dates to x axis for the month of July 2108

import csv
from datetime import datetime

infile = open("sitka_weather_07-2018_simple.csv", "r")
csvfile = csv.reader(infile)

header_row = next(csvfile)

print(type(header_row))

for index, column_header in enumerate(header_row):
    print(index, column_header)

highs = []  # our y axis
dates = []  # our x axis

somedate = datetime.strptime("2018-07-01", "%Y-%m-%d")

for row in csvfile:
    highs.append(row[5])
    thedate = datetime.strptime(row[2], "%Y-%m-%d")
    dates.append(thedate)

print(highs)

import matplotlib.pyplot as plt

fig = plt.figure()

plt.plot(dates, highs, c="red")
plt.title("Daily Temperatire July 2018", fontsize=16)
plt.xlabel("", fontsize=16)
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis="both", which="major", labelsize=8)

fig.autofmt_xdate()
plt.show()
