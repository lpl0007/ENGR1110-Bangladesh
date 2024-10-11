import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

f = open("Bangladesh.csv", "r")
data = f.read()
data2 = data.split("\n")
graphData = {"Date": [], "Temperature (°C)": []}
num = 0
for i in data2:
  if num == 1:
    data3 = i.split(",")
    graphData["Date"].append(data3[2])
    graphData["Temperature (°C)"].append(float(data3[0]))
  else:
    if num == 12:
      num = 0
  num += 1

df = pd.DataFrame(graphData)
df.head()
df.plot(x = 'Date', title = "Bangladesh")
plt.show()