import pandas as pd #imports
import matplotlib.pyplot as pltpornhub
import numpy as np

data=pd.read_csv("Crime_Data.csv")#sets csv file as variable

plt.title("Crime Count Over Time") #Plot Title
data["date"] = data["date"].astype("datetime64")#sets type do a datetime object
data = data.set_index(data["date"])#sets index to date
plt.plot(data.crime_count, marker="o")#plots 
#plt.legend("blue","black")
plt.show()