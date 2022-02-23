import random

# Generate random integer between two numbers, (a and b included)
coin = random.randint(1, 2)
print(coin)

if coin == 1:
    print("It's heads")
elif coin == 2:
    print("It's tails")
