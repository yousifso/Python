# Import the numpy library
import numpy as np

# Define an array for cupcake ingredients
cupcakes = np.array([2, 0.75, 2, 1, 0.5])

# Load recipes from a CSV file
recipes = np.genfromtxt('recipes.csv', delimiter=',')

# Print the loaded recipes
print(recipes)

# Extract the column for the number of eggs used in each recipe
eggs = recipes[:, 2]

# Print the eggs column
print(eggs)

# Create a boolean array where the number of eggs is equal to 1
one_egge = (eggs == 1)

# Print the boolean array
print(one_egge)

# Extract the ingredients for the cookies recipe
cookies = recipes[2, :]

# Print the ingredients for cookies
print(cookies)

# Calculate the ingredients for a double batch of cupcakes
double_batch = (cupcakes * 2)

# Print the ingredients for the double batch of cupcakes
print(double_batch)

# Calculate the total grocery list by adding cookies ingredients to double batch of cupcakes
grocery_list = (cookies + double_batch)

# Print the grocery list
print(grocery_list)

