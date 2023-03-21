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

plt.subplot(2, 1, 1)  # means 2 rows, 1 column, first graph
plt.plot(dates, highs, c="red")
plt.title("Lows")

plt.suptitle("Highs and Lows of Sitka, Alaska")

plt.show()
