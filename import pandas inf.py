import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data=pd.read_csv("Inflation.csv")

plt.title("Inflation Over Time")
data["date"] = data["date"].astype("datetime64")
data = data.set_index(data["date"])
plt.plot(data.inflation, marker="o")
plt.show()