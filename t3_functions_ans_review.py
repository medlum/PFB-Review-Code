# 1. Import math library and use the sqrt() function from 
# the math library to find out the square root value of 450.
import math
print(math.sqrt(450))

# 2. Import floor() from the math library to round down the
# value of 423.89 to an integer. 
from math import floor
print(floor(423.89))

# 3. Which Python function allows you to list all the functions 
# available in math library?
print(dir(math))

# 4. Write a function called `convertUSD_SGD` that takes a 
# parameter USD. When a value of 100 is supplied to USD parameter,
# the function will convert number to SGD by multiplying the 
# number by 1.075 and return the converted value.

def convertUSD_SGD(USD):
    return USD * 1.075

print(convertUSD_SGD(100))

# 5. 
# Create a global variable `counter` and assign it with a value of 0. 
# Write a function called `addNumber` with a parameter `x`. 
# When a value of 10 is supplied to `x` parameter, 10 will be added 
# to the counter variable. 
# Execute the function twice and the value of counter variable
# in the second execution should return 20 as follow:

    # print(addNumber(10)) => 10
    # print(addNumber(10)) => 20

counter = 0
def addNumber(x):
    global counter
    counter = counter + x
    return counter

print(addNumber(10))
print(addNumber(10))