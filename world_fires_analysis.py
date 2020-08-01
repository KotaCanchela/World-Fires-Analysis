import csv
from datetime import datetime
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

# Initial data load.
filename = "world_fires_1_day.csv"
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    # Get index number and value for each item in the header_row list
    for index, column_header in enumerate(header_row):
        print(index, column_header)
    # Create empty list for latitude, longitude, brightness, date, and day/night occurrence.
    lats, lons, brightness, acq_date, daynight = [], [], [], [], []
    # Pull the data to append to all of the lists
    for row in reader:
        current_date = datetime.strptime(row[5], "%Y-%m-%d")
        try:
            lat = row[0]
            lon = row[1]
            bright = row[2]
            dnight = row[12]
        except ValueError:
            print(f"Missing data for {current_date}.")
        else:
            if dnight == "D":
                daynight.append("Day fire")
                lats.append(lat)
                lons.append(lon)
                brightness.append(bright)
            elif dnight == "N":
                daynight.append("Night fire")
                lats.append(lat)
                lons.append(lon)
                brightness.append(bright)


print(lats[:10])
print(lons[:10])
print(brightness[:10])
print(daynight[:10])
brightness = list(map(float, brightness))

data = [
    {
        "type": "scattergeo",
        "lon": lons,
        "lat": lats,
        "text": daynight,
        "marker": {
            "size": [0.03 * bright for bright in brightness],
            "color": brightness,
            "colorscale": "thermal",
            "reversescale": True,
            "colorbar": {"title": "Brightness of world fires"},
        },
    }
]


my_layout = Layout(title="World Fires data in one 24 hour timespan")


fig = {"data": data, "layout": my_layout}
offline.plot(fig, filename="global_fires.html")

