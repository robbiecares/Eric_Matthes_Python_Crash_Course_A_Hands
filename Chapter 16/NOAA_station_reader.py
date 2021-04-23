import csv
import matplotlib.pyplot as plt
from datetime import datetime


filename = 'data/beverly_hills_weather.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get dates and high temperatures from this file.
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[5], '%Y-%m-%d')
        try:
            high = float(row[8])
            low = float(row[10])
        except ValueError:
            print(f'missing data for {current_date}')
        dates.append(current_date)
        highs.append(high)
        lows.append(low)

# Plot the high temperatures.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=.05)
ax.plot(dates, lows, c='blue', alpha=.05)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=.1)

# Format plot.
title = "Daily high and low temperatures - 2018\nDeath Valley, CA"
plt.title(title, fontsize=20)
fig.autofmt_xdate
plt.ylabel("Temperature (C)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.show()