import csv
from datetime import datetime
from datetime import time
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

# Explore the structure of the data.
filename = 'data/MODIS_C6_Global_7d.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get dates and high temperatures from this file.
    dates, times, lats, lons, intensity = [], [], [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[5], '%Y-%m-%d')
            current_time = row[6]
            lat = float(row[0])
            lon = float(row[1])
            brightness = float(row[2])
        except ValueError:
            print(f'missing data for {current_date} @ {current_time}')

        dates.append(current_date)
        times.append(current_time)
        lats.append(lat)
        lons.append(lon)
        intensity.append(brightness)

# Map the fires.
data = [{
'type': 'scattergeo',
'lon': lons,
'lat': lats,
'text': brightness,
'marker': {
    'size': [brightness*.01 for brightness in intensity],
    'color': intensity,
    'colorscale': 'Magma',
    'reversescale': False,
    'colorbar': {'title': 'Intensity'},
    },
}]

my_layout = Layout(title=f'global fires - past 7 days')
fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename=f'global fires - past 7 days.html')