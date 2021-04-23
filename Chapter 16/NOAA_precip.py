import csv
import matplotlib.pyplot as plt
from datetime import datetime


filename = 'data/death_valley_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get dates and high temperatures from this file.
    dates, prcp_amount = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        prcp = float(row[3])
        dates.append(current_date)
        prcp_amount.append(prcp)

# Plot the high temperatures.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, prcp_amount, c='green')

# Format plot.
plt.title("Daily Precipitation\nSitka, AK - 2018", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate
plt.ylabel("Rainfall (inches)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.show()