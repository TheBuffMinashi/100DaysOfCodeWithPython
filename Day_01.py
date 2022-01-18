# Step 1 - print out different messages using print function
print('Day 1 - Python Print Function')
print('The function is declared like this:')
print(" print('what to print') ")

# Step 2 - try out different printing formats 
# (\n)
print("Hello world!\nHello world!")

# (+) sign
print("Hello " + "Mina")
print("Hello" + " " + "Mina")

# Input function
# Writing comments
# e.g. This is a comment
name = input("What is your name? ")
print("Your name has " + str(len(name)) + " letters.")

# Exchange value of two variables
a = input("a: ")
b = input("b: ")

# Using a third variable (c) to exchange values
c = a
a = b
b = c

print("a: " + a)
print("b: " + b)
