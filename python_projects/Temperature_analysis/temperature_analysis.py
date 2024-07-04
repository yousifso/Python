import codecademylib3_seaborn
import pandas as pd
import numpy as np
from weather_data import london_data

# Load and preview data
print(london_data.head())
print(london_data.iloc[100:200])
print(len(london_data))

# Temperature analysis
temp = london_data["TemperatureC"]
average_temp = np.mean(temp)
temperature_var = np.var(temp)
temperature_standard_deviation = np.std(temp)

# Monthly temperature analysis for June and July
june = london_data.loc[london_data["month"] == 6]["TemperatureC"]
july = london_data.loc[london_data["month"] == 7]["TemperatureC"]
june_mean = np.mean(june)
july_mean = np.mean(july)
june_standard_deviation = np.std(june)
july_standard_deviation = np.std(july)

print(f"June Mean Temperature: {june_mean}")
print(f"July Mean Temperature: {july_mean}")
print(f"June Temperature Standard Deviation: {june_standard_deviation}")
print(f"July Temperature Standard Deviation: {july_standard_deviation}")

# Monthly temperature analysis for all months
for i in range(1, 13):
    month = london_data.loc[london_data["month"] == i]["TemperatureC"]
    print(f"The mean temperature in month {i} is {np.mean(month)}")
    print(f"The standard deviation of temperature in month {i} is {np.std(month)}\n")

# Pressure analysis
pres = london_data["PressurehPa"]
average_pressure = np.mean(pres)
variance_pressure = np.var(pres)
pressure_standard_deviation = np.std(pres)

print(f"Average Pressure: {average_pressure}")
print(f"Variance in Pressure: {variance_pressure}")
print(f"Pressure Standard Deviation: {pressure_standard_deviation}")

# Hourly pressure analysis
for i in range(1, 13):
    hour = london_data.loc[london_data["hour"] == i]["PressurehPa"]
    print(f"The mean pressure at {i} is {np.mean(hour)}")
    print(f"The standard deviation of pressure at {i} is {np.std(hour)}\n")

