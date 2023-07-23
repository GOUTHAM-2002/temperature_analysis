import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')


df = pd.read_csv("weatherHistory.csv")
mean_temp=np.mean(df['Temperature (C)'])
median_temp=np.median(df['Temperature (C)'])
std_temp=np.std(df['Temperature (C)'])
max_temp=np.max(df['Temperature (C)'])
min_temp=np.min(df['Temperature (C)'])
print("The obtained mean is " , mean_temp)
print("The obtained median is " , median_temp)
print("The obtained standard deviation is ", std_temp)
print("The maximum temperature is " , max_temp , "This was recorded on " , df['Formatted Date'][np.argmax(df['Temperature (C)'])])
print("the min temperature is " , min_temp, "This was recorded on ", df['Formatted Date'][np.argmin(df['Temperature (C)'])])
plt.figure(figsize=(10, 6))
plt.plot(df['Formatted Date'], df['Temperature (C)'], label='Temperature')
plt.xlabel('Date')
plt.ylabel('Temperature')
plt.title('Temperature vs Date')
plt.ioff()  # Turn off interactive mode
plt.show()
