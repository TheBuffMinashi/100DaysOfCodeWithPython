import random


names_string = input("Give me everybody's name, seperated by comma: ")
names = names_string.split(",")
# print(names)

random_number = random.randint(0, len(names) - 1)
print(random_number)
print(f"The person who have to pay is: {names[random_number]}")

