# Exercise 1.2 - Temperature Converter
    # Ask for a temperature in Celsius
    # Convert it to Fahrenheit (formula: F = C × 9/5 + 32)
    # Convert it to Kelvin (formula: K = C + 273.15)
    # Display formatted results

celsius = float(input("What is the Celsius temp : "))

fahrenheit = (celsius * (9/5)) + 32
print(celsius, "celsius is", fahrenheit, "Fahrenheit !")

kelvin = celsius + 273.15
print(celsius, "celsius is", kelvin, "Kelvin !")

#or

print(f"{celsius} Celsius is {fahrenheit} Fahrenheit!")
print(f"{celsius} Celsius is {kelvin} Kelvin!")


# Takeaway of the exercise

# This exercise teaches how to take user input, perform arithmetic operations, and convert temperatures from Celsius to Fahrenheit and Kelvin. 
# It also demonstrates how to display results clearly using both basic print statements and formatted string literals (f-strings) in Python