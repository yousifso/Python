# Import necessary libraries
import codecademylib
import numpy as np
from matplotlib import pyplot as plt

# List of survey responses
survey_responses = ['Ceballos', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos',
                    'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 
                    'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 
                    'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 
                    'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Ceballos', 
                    'Ceballos', 'Ceballos', 'Ceballos', 'Ceballos', 'Ceballos',
                    'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 
                    'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 
                    'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 
                    'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Ceballos',
                    'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 
                    'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 
                    'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 
                    'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Ceballos']

# Count the number of responses for Ceballos
total_ceballos = sum([1 for response in survey_responses if response == 'Ceballos'])
print(total_ceballos)

# Calculate the total number of survey responses
survey_length = float(len(survey_responses))

# Calculate the percentage of responses for Ceballos
percentage_ceballos = total_ceballos / survey_length
print(percentage_ceballos)

# Simulate 10,000 possible survey outcomes using a binomial distribution
possible_surveys = np.random.binomial(survey_length, .54, size=10000) / survey_length

# Plot a histogram of the possible survey outcomes
plt.hist(possible_surveys, range=(0, 1), bins=20)
plt.show()

# Calculate the percentage of surveys where Ceballos received less than 50% of the vote
ceballos_loss_surveys = np.mean(possible_surveys < 0.50)
print(ceballos_loss_surveys)

# Simulate a larger survey with 7,000 responses using a binomial distribution
large_survey_length = float(7000)
large_survey = np.random.binomial(large_survey_length, .54, size=1000) / large_survey_length

# Calculate the percentage of larger surveys where Ceballos received less than 50% of the vote
ceballos_loss_new = np.mean(large_survey < 0.50)
print(ceballos_loss_new)

