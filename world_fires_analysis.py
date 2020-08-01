import csv

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
