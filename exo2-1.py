# Exercise 2.1 - Shopping List Manager
    # Create an empty shopping list
    # Add 5 items
    # Display the total number of items
    # Remove the 3rd item
    # Display the final lis

# Create an empty shopping list
myList = []

# Add 5 items
myList.extend(['milk', 'egg', 'water', 'meat', 'vegetable'])
print(myList)

# Display the total number of items
print(len(myList))

# Remove the 3rd item
myList.pop(2)
print(myList)


# This exercise teaches how to create and manage a list in Python. 
# It covers initializing an empty list, adding multiple items with extend, counting items using len, removing an item by index with pop, and displaying the final list. 
# It highlights the difference between append (adds a single element) and extend (adds multiple elements individually)