import random
import my_module

# Random integer
random_integer = random.randint(1, 10)
print(f"Random integer: {random_integer}")

# Test the module that we built
print(f"Pi from my module: {my_module.pi}")

# Random float
random_float = random.random()
print(f"Random float: {random_float}")

love_score = random.randint(1, 100)
print(f"Your love score is {love_score}")

# Python lists
states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut",
                     "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia",
                     "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky",
                     "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois",
                     "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida",
                     "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon",
                     "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota",
                     "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah",
                     "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

print(len(states_of_america))
