import random


names_string = input("Give me everybody's name, seperated by comma: ")
names = names_string.split(",")
# print(names)

person_who_pay = random.choice(names)
print(f"The person who have to pay is: {person_who_pay}")
