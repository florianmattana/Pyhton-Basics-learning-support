# Ask for the user's age
    # Check if the person is:
    #   - A minor (< 18)
    #   - An adult (18-65)
    #   - A senior (> 65)
    # Display an appropriate message

age = int(input(" What's your age ?"))

if age < 18 :
    print("You are minor")
elif age >= 19 and age <= 65 :
    print("You are an adult")
else :
    print("You are a bit old")




# this exercise demonstrates how to take user input, use conditional statements (if, elif, else), and compare numeric values in Python. It teaches how to classify a value into multiple categories and display the appropriate message.
# Key insights:
    # You can chain comparisons like 18 <= age <= 65 for readability.
    # Conditional statements are evaluated in order; the first true condition executes.
    # else handles any remaining cases not covered by previous conditions.elif 18 <= age <= 65: can also work