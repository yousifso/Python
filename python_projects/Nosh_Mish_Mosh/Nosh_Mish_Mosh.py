# Import necessary libraries
import noshmishmosh
import numpy as np

# Get all visitors and paying visitors data
all_visitors = noshmishmosh.customer_visits
paying_visitors = noshmishmosh.purchasing_customers

# Calculate the total number of visitors and paying visitors
total_visitor_count = len(all_visitors)
paying_visitor_count = len(paying_visitors)

# Calculate the baseline conversion rate and print it
baseline_percent = 100 * paying_visitor_count / total_visitor_count
print(baseline_percent)

# Analyze the payment history to find the average payment
payment_history = noshmishmosh.money_spent
average_payment = np.mean(payment_history)
print(average_payment)

# Calculate the number of new customers needed to reach $1240 in additional revenue
new_customers_needed = np.ceil(1240 / average_payment)
print(new_customers_needed)

# Calculate the percentage point increase and print it
percentage_point_increase = 100 * new_customers_needed / total_visitor_count
print(percentage_point_increase)

# Calculate the lift and print it
lift = 100 * percentage_point_increase / baseline_percent
print(lift)

# Define the sample size for the A/B test
ab_sample_size = 490

