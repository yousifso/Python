# Define mass, acceleration, and distance for the train
train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1

# Function to convert Fahrenheit to Celsius
def f_to_c(f_temp):
  c_temp = (f_temp - 32) * 5/9
  return c_temp

# Convert 100 Fahrenheit to Celsius
f100_in_celsius = f_to_c(100)

# Function to convert Celsius to Fahrenheit
def c_to_f(c_temp):
  f_temp = c_temp * (9/5) + 32
  return f_temp

# Convert 0 Celsius to Fahrenheit
c0_in_fahrenheit = c_to_f(0)

# Function to calculate force using mass and acceleration
def get_force(mass, acceleration):
  return mass * acceleration

# Calculate the force of the train
train_force = get_force(train_mass, train_acceleration)
print("The GE train supplies " + str(train_force) + " Newtons of force.")

# Function to calculate energy using mass and the speed of light
def get_energy(mass, c = 3*10**8):
  return mass * c

# Calculate the energy of the bomb
bomb_energy = get_energy(500)
print("A 1kg bomb supplies " + str(bomb_energy) + " Joules ")

# Function to calculate work done using force and distance
def get_work(mass, acceleration, distance):
 force = get_force(mass, acceleration)
 return force * distance

# Calculate the work done by the train
train_work = get_work(train_mass, train_acceleration, train_distance)
print("The GE train does " + str(train_work) + " Joules of work over " + str(train_distance) + " meters.")

