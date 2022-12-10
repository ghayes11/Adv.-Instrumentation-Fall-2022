# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 23:59:45 2022
eco

@author: gunte
"""

import pandas as pd
import matplotlib.pyplot as plt

# Read the Data
data = pd.read_csv('C:/Users/gunte/.spyder-py3/Log-2022-11-29-Eco.csv')
df = pd.read_csv('C:/Users/gunte/.spyder-py3/Log-2022-11-29-Eco.csv') 

# Filter out any speed less than 1 
filt_speed = df[df['Speed'] > 1] 

# Plot the Map Points
plt.scatter(data['Longitude'], data['Latitude'])
plt.title('Eco Map Points')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.show()

# Plot the Speed
plt.plot(data['Time'],df['Speed'])
plt.title('Eco Speed')
plt.xlabel('Time (sec)')
plt.ylabel('Speed (MPH)')
plt.show()

# Calculate Acceleration
data['Acceleration'] = filt_speed['Speed'].diff()

# Plot the Acceleration
plt.plot(data['Time'], data['Acceleration'])
plt.title('Eco Acceleration')
plt.xlabel('Time (Sec)')
plt.ylabel('Acceleration')
plt.show()

#calculate the average speed
avg_speed = filt_speed["Speed"].mean()
print("Eco Average Speed with Filter (MPH):", avg_speed)
 
#calculate the highest speed
max_speed = filt_speed["Speed"].max()
print("Eco Highest Speed (MPH):", max_speed)

# Calculate the average speed 
avg_speed = df['Speed'].mean()
print("Eco Average Speed without Filter (MPH):", avg_speed) 

# Calculate the fastest acceleration over  
max_acc = df['Speed'].diff().max() 
print("Eco Maximum Acceleration:", max_acc)