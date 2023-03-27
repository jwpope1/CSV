import csv
import matplotlib.pyplot as plt
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


for row in death_csvfile:
    death_title = row[death_name_index]
    try:
        high = int(row[death_max_index])
        low = int(row[death_min_index])
        currentdate = datetime.strptime(row[death_date_index], "%Y-%m-%d")
    except ValueError:
        print(f"There is data missing for {currentdate}. Please look into fixing this.")
    else:
        death_highs.append(high)
        death_lows.append(low)
        death_dates.append(currentdate)

for row in sitka_csvfile:
    sitka_title = row[sitka_name_index]
    try:
        high = int(row[sitka_max_index])
        low = int(row[sitka_min_index])
        currentdate = datetime.strptime(row[sitka_date_index], "%Y-%m-%d")
    except ValueError:
        print(f"There is data missing for {currentdate}. Please look into fixing this.")
    else:
        sitka_highs.append(high)
        sitka_lows.append(low)
        sitka_dates.append(currentdate)

# create 2 subplot graphs in one visualization so you can see both graphs to compare side by side.
plt.subplot(2, 1, 2)
plt.plot(death_dates, death_highs, c="red")
plt.plot(death_dates, death_lows, c="red")
plt.fill_between(death_dates, death_highs, death_lows, facecolor="green", alpha=0.1)
plt.title(death_title, fontsize=14)

plt.subplot(2, 1, 1)
plt.plot(sitka_dates, sitka_highs, c="red")
plt.plot(sitka_dates, sitka_lows, c="red")
plt.fill_between(sitka_dates, sitka_highs, sitka_lows, facecolor="green", alpha=0.1)
plt.title(sitka_title, fontsize=14)

# Matplotlib's pyplot API has a convenience function called subplots() which acts as a
# utility wrapper and helps in creating common layouts of subplots, including the
# enclosing figure object, in a single call

maintitle = "Comparison of " + death_title + " and " + sitka_title
plt.suptitle(maintitle, fontsize=18)

plt.show()
