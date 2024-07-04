# List of pizza toppings
topping = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]

# Corresponding prices for each topping
prices = [2, 6, 1, 3, 2, 7, 2]

# Count the number of pizzas that cost $2
num_two_dollar_slices = prices.count(2)
print(num_two_dollar_slices)

# Count the total number of different types of pizzas
num_pizzas = len(topping)
print(num_pizzas)

# Print the total number of different kinds of pizzas
print("We sell " + str(num_pizzas) + " different kinds of pizza!")

# Combine prices and toppings into a list of lists
pizza_and_prices = [[2, "pepperoni"], [6, "pineapple"], [1, "cheese"], [3, "sausage"], [2, "olives"], [7, "anchovies"], [2, "mushrooms"]]
print(pizza_and_prices)

# Sort pizzas by price
pizza_and_prices.sort()
print(pizza_and_prices)

# Identify the cheapest pizza
cheapest_pizza = pizza_and_prices[0]
print(cheapest_pizza)

# Identify the priciest pizza
priciest_pizza = pizza_and_prices[-1]
print(priciest_pizza)

# Remove the priciest pizza from the list
pizza_and_prices.pop()
print(pizza_and_prices)

# Add a new pizza with a price of $2.5 to the list
pizza_and_prices.insert(4, [2.5, "peppers"])
print(pizza_and_prices)

# Get the three cheapest pizzas
three_cheapest = pizza_and_prices[:3]
print(three_cheapest)
