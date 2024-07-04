import codecademylib3_seaborn
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load and preview data
data = pd.read_csv("country_data.csv")
print(data.head(5))

# Life expectancy analysis
life_expectancy = data["Life Expectancy"]
print(life_expectancy)
life_expectancy_quartiles = np.quantile(life_expectancy, [0.25, 0.5, 0.75])
print(life_expectancy_quartiles)
plt.hist(life_expectancy)
plt.title('Life Expectancy Distribution')
plt.xlabel('Life Expectancy')
plt.ylabel('Frequency')
plt.show()

# GDP analysis
gdp = data["GDP"]
print(gdp)
median_gdp = np.quantile(gdp, 0.5)

# Split data into low and high GDP groups
low_gdp = data[data["GDP"] <= median_gdp]
high_gdp = data[data["GDP"] > median_gdp]

# Life expectancy analysis for high GDP group
high_gdp_quartiles = np.quantile(high_gdp["Life Expectancy"], [0.25, 0.5, 0.75])

# Compare life expectancy distributions
plt.hist(high_gdp["Life Expectancy"], alpha=0.5, label="High GDP")
plt.hist(low_gdp["Life Expectancy"], alpha=0.5, label="Low GDP")
plt.legend()
plt.title('Life Expectancy by GDP Group')
plt.xlabel('Life Expectancy')
plt.ylabel('Frequency')
plt.show()

