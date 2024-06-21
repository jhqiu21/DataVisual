import json
import plotly.express as px
import pandas as pd

filename = 'visual/json_format/data/eq_data_30_day_m1.json'

with open(filename) as f:
     all_eq_data = json.load(f)

readable_file = 'visual/json_format/data/readable_eq_data.json'
with open(readable_file, 'w') as f:
     # use parameter 'indent' to set tab
     json.dump(all_eq_data, f, indent = 4) 

all_eq_dicts = all_eq_data['features']
mags, titles, lons, lats = [], [], [], []
for eq_dict in all_eq_dicts:
     mag = eq_dict['properties']['mag']
     title = eq_dict['properties']['title']
     lon = eq_dict['geometry']['coordinates'][0]
     lat = eq_dict['geometry']['coordinates'][1]
     mags.append(mag)
     titles.append(title)
     lons.append(lon)
     lats.append(lat)

data = pd.DataFrame(
     data = zip(lons, lats, titles, mags),
     columns = ['lon', 'lat', 'location', 'mag']
)
data.head()

fig = px.scatter(
     data,
     x = 'lon',
     y = 'lat',
     range_x = [-200, 200],
     range_y = [-90, 90],
     width = 800,
     height = 800, 
     title = 'Title input',
     size = 'mag',
     size_max = 10,
     color = 'mag',
     hover_name = 'location'
)

fig.write_html('global_earthquakes.html')
fig.show()