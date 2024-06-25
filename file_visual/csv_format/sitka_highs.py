

import csv
import matplotlib.pyplot as plt
from datetime import datetime

# we open the csv file and assign the file object to f
filename = 'file_visual/csv_format/data/sitka_weather_07-2018_simple.csv'
with open(filename) as f:
    # create a reader object associate with the file we open before
    reader = csv.reader(f)
    # 'next()' get a reader object and return the next line of the file
    header_row = next(reader)

    # get TMAX in 5th row in the csv file
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        try: 
            high = int(row[5])
            low = int(row[6])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:     
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
# param alpha set the transprancy of the line, decreasing from 0 to 1
ax.plot(dates, highs, c = 'red', alpha = 0.5)
ax.plot(dates, lows, c = 'blue', alpha = 0.5)
# fill the area between the high and low
ax.fill_between(dates, highs, lows, facecolor = 'blue', alpha = 0.1)
# set the config of the figure
ax.set_title("Title", fontsize = 24)
ax.set_xlabel('', fontsize = 14)
# use 'autofmt_xdate()' to draw inclined date to avoid overlapping
fig.autofmt_xdate() 
ax.set_ylabel("Temperature(F)", fontsize = 14)
ax.tick_params(axis = 'both', which = 'major', labelsize = 14)

plt.show()


