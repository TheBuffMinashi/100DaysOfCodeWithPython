# Day 2 - Data Types

# Calculate sum of the digits in a two digits number
two_digit_number = input("Type a two digit number: ")
first_digit  = int(two_digit_number[0])
second_digit = int(two_digit_number[1])
print(first_digit + second_digit)

# Make long numbers more readable (no difference in print)
long_number = 123456
long_number_modified = 123_567
print(long_number)
print(long_number_modified)

# f-Strings
score = 19.5
print(f"Your score is {score}")
