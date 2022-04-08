from collections import defaultdict
from curses.textpad import rectangle
from http.client import NOT_IMPLEMENTED
from plotnine import ggplot, aes, geom_point
import csv
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('ggplot')
rows = []
data = []
headers = [
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
  
with open("./place_5.csv", 'r') as file:
  color_freq = defaultdict(int)
  for k in headers:
    color_freq[k] = 0
  csvreader = csv.reader(file)
  header = next(csvreader)
  for row in csvreader:
    date = row[0]
    color = row[2]
    color_freq[color] += 1
    d = [date]
    for color in color_freq: 
      d.append(color_freq[color])
    data.append(d)

headers.insert(0, 'Time')
df = pd.DataFrame(data, columns = headers)
# data looks like this : 👇🏻
print(df)
g = ggplot(df, aes(x="Time")) + geom_point()
# print(g) -> this breaks