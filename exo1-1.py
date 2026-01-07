# Exercise 1.1 - Basic Calculator
# Create a program that:

# Asks the user for two numbers
# Displays their sum, difference, product, and quotient
# Shows results with clear messages

input1 = float(input("Give the first number: "))
input2 = float(input("Give the second number: "))

total = input1 + input2
difference =  input1 - input2
product = input1 * input2
quotient = input1 / input2

print("Here is the sum : ", total)
print("Here is the difference :", difference)
print("Here is the product :",product)
print("Here is the quotient :",quotient)


#===========================================

# input() returns a string, so numeric input must be converted using int() or float()
# Basic arithmetic operations in Python:
# + → addition
# - → subtraction
# * → multiplication
# / → division
# Use clear print() messages to display results
# This exercise demonstrates user input handling, type conversion, and basic arithmetic operations in Python.