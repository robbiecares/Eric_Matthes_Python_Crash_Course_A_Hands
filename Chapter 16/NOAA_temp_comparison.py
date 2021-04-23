import csv
import matplotlib.pyplot as plt
from datetime import datetime


files = ['data/sitka_weather_2018_simple.csv','data/death_valley_2018_simple.csv','data/beverly_hills_weather.csv']

def extract_weather_data(filename):
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)

        # Identify column number of dates & temps
        DATE = header_row.index("DATE")
        TMAX = header_row.index("TMAX")
        TMIN = header_row.index("TMIN")
        NAME = header_row.index("NAME")

        # Get dates and temperatures from this file.
        dates, highs, lows = [], [], []

        for row in reader:
            station_name = row[NAME].split(', ',1)[0].title()
            current_date = datetime.strptime(row[DATE], '%Y-%m-%d')
            if 'beverly_hills' in filename and current_date.year != 2018:
                continue
            try:
                high = float(row[TMAX])
                low = float(row[TMIN])
            except ValueError:
                print(f'missing data for {current_date} in {filename}')
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

    return station_name, dates, highs, lows


def plot_data(station_name, dates, highs, lows):
    ax.plot(dates, highs, c='red', alpha=.05)
    ax.plot(dates, lows, c='blue', alpha=.05)
    plt.fill_between(dates, highs, lows, facecolor='blue', alpha=.1)


#temps = sitka_lows + dv_lows + sitka_highs + dv_highs
#temp_range = range(int(min(temps)),int(max(temps)))

plt.style.use('seaborn')
fig, ax = plt.subplots()

# Plot data
stations = []

for file in files:
    station_name, dates, highs, lows = extract_weather_data(file)
    plot_data(station_name, dates, highs, lows)
    stations.append(station_name)

# Format plot
plt.title(f'2018 Daily Temperatures\n {stations}', fontsize=20)
plt.xlabel('', fontsize=16)
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.show()