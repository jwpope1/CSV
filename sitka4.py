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

for row in csvfile:
    try:
        high = int(row[4])
        low = int(row[5])
        date = datetime.strptime(row[2], "%Y-%m-%d")
    except ValueError:
        print(f"Missing data for {date}")  # skips the data that has missing data
    else:
        highs.append(high)
        lows.append(low)
        dates.append(date)

import matplotlib.pyplot as plt

figure = plt.figure()

plt.plot(dates, highs, c="red", alpha=0.5)
plt.plot(dates, lows, c="blue", alpha=0.5)

plt.title("Daily and low high temperatures- 2018", fontsize=16)
plt.xlabel("", fontsize=12)
plt.ylabel("Temperature(F)", fontsize=16)
plt.tick_params(axis="both", which="major", labelsize=16)
plt.fill_between(dates, lows, highs, facecolor="turquoise", alpha=0.1)

figure.autofmt_xdate()

plt.show()
