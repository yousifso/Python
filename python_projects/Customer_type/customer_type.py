# Import necessary libraries
import codecademylib
from matplotlib import pyplot as plt
import pandas as pd

# Load the orders data from the CSV file
orders = pd.read_csv('orders.csv')

# Group the data by customer ID and sum the prices for each customer
customer_amount = orders.groupby('customer_id').price.sum().reset_index()

# Print the first few rows of the grouped data
print(customer_amount.head())

# Plot a histogram to visualize the distribution of total spending by customers
plt.hist(customer_amount.price.values, range=(0, 200), bins=40)
plt.xlabel('Total Spent')
plt.ylabel('Number of Customers')
plt.title('Customer Expenditure Over 6 Months')
plt.show()
