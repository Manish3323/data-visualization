from collections import defaultdict
import matplotlib.pyplot as plt
from matplotlib import animation
import pandas as pd
import csv
font = {
    'weight': 'normal',
    'size'  :  20,
    'color': 'black'
}
rows = []
color_data = []
user_data = []
headers = [
  "Time",
  "#FF4500",
  "#51E9F4",
  "#000000",
  "#3690EA",
  "#2450A4",
  "#FFFFFF",
  "#7EED56",
  "#D4D7D9",
  "#FF3881",
  "#FFA800",
  "#BE0039",
  "#FFD635",
  "#FF99AA",
  "#00CC78",
  "#493AC1",
  "#6D482F",
  "#898D90",
  "#00A368",
  "#B44AC0",
  "#6A5CFF",
  "#9C6926",
  "#811E9F",
  "#009EAA",
  "#00756F"
  ]

with open("../../place_1.csv", 'r') as file:
  color_freq = defaultdict(int)
  for k in headers[1:]:
    color_freq[k] = 0
  csvreader = csv.reader(file)
  next(csvreader) #ignore first line
  for row in csvreader:
    date = row[0]
    color = row[2]
    color_freq[color] += 1
    d = [date]
    for color in color_freq: 
      d.append(color_freq[color])
    color_data.append(d)

color_df = pd.DataFrame(color_data, columns = headers)


# this plots the number of times a color got used till that moment.
time = color_df['Time'].unique()

fig, ax = plt.subplots(figsize=(10, 5))
def update_barchart(i):
  _time = time[10000 * i]
  data_temp = color_df.loc[color_df['Time'] == _time, :]
  ax.clear()
  ax.set_xlabel(f'Count {_time}')
  for color_key in headers[1:]:
    ax.barh(color_key, data_temp[color_key], color = color_key)
    ax.set_facecolor('grey')

anim = animation.FuncAnimation(fig, update_barchart, frames = round(len(time) / 10000))
plt.show()
# anim.save('anim.gif')