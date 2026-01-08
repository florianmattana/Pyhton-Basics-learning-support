#Create a function that computes a factorial
#compare against math.factorial()

import math

def facto (number) :
    result = 1
    for i in range(1, number + 1):
        result *= i
    return result

n = 5

print(f"My factorial function : {facto(n)}")
print(f"Math module factorial: {math.factorial(n)}")
