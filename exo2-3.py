# Exercise 2.3 - GPS Coordinates
    # Create 3 tuples representing coordinates (latitude, longitude, altitude)
    # Store them in a list
    # Loop through the list and display each position

position_1 = (48.866669, 2.33333, 34)
position_2 = (54.676669, 2.34554, 1234)
position_3 = (76.236669, 1.34545, 343)

position_list = []
position_list.append(position_1)
position_list.append(position_2)
position_list.append(position_3) 

# or position_list = [position_1, position_2, position_3] if you dont want to practise append method

for i in position_list:
    print(i)
