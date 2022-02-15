# 1 
# For each of the following expressions, fill in the blank
# (indicated by __) with an appropriate Boolean comparator so that 
# the expression evaluates to True: 

# print(4 _ 2)
print(4 > 2)
# print(5 _ 10)
print(5 < 10)
# print("python" _ "C++")
print("python" != "C++")
# print(50 _ "50")
print(50 != "50")

# 2
# Add parentheses where necessary so that each of the following 
# expressions evaluates to True:

# print(False == not True)
print(False == (not True))
# print(True and False == True and False)
print((True and False) == (True and False))
# print(not True and "A" == "B")
print(not (True and "A" == "B"))

# 3 
# Write a conditional statement to print `business and accountancy` if 
# a string is equal to `business and accountancy`, 
# otherwise print `invalid entry`.

school = "business and accountancy"

if school == "business and accountancy":
    print(school)
else: 
    print("invalid entry")

# 4 
# Write a conditional statement to evaluate the price of an apple and 
# and orange. 
# If the price of apple is greater than orange, print 
# "apple price is higher than orange". 
# If the price of apple is greater than orange, print 
# "apple price is lower than orange". 
# Otherwise, print "apple and orange prices are equal".

apple_price = 0.74
orange_price = 0.74

if apple_price > orange_price:
    print("apple price is higher than orange")
elif apple_price < orange_price:
    print("apple price is lower than orange")
else:
    print("apple and orange prices are equal")

# 5
# Write a conditional statement to evaluate the following conditions 
# of a variable `height`:
# If height is greater or equal to 175, print "tall"
# If height is greater or equal to 165 and less than 175, print "average"
# If height is less than 165, print "short"
# Test the condition with 160, 170 and 180 to evaluate the conditional statements
height = 170

# Require the conditions to evaluate from highest to lowest value
if height >= 175:
    print("tall")
elif height >= 165:
    print("average")
else:
    print("short")

# Alternate solution using compound conditions.
# Notice the evaluation does not require highest to lowest value
if height >= 165 and height < 175:
    print("average")
elif height >= 175:
    print("tall")
else:
    print("short")


# 6 
# Write a conditional statement to evaluate the following conditions of 2 variables:
# gender = "male" and hair_length = "long":

    ## If gender = "female" and hair_length = "long", print "tie up your hair"
    ## If gender = "female" and hair_length = "short", print "style your hair"
    ## If gender = "male" and hair_length = "long", print "cut your hair"
    ## If gender = "male" and hair_length = "short", print "comb your hair"
gender = "male" 
hair_length = "long"

if gender == "female" and hair_length == "long":
    print("tie up your hair")
elif gender == "female" and hair_length == "short":
    print("style your hair")
elif gender == "male" and hair_length == "long":
    print("cut your hair")
else:
    print("comb your hair")



# 7
# Create a range of values 0 to 20 (inclusive of 20).
# Write a `for loop` to iterate over the values to evaluate each value 
# using the following conditions:

    ## If 1 == 0, print (f"{value} is first value")
    ## If 10 == 0, print (f"{value} is middle value")
    ## If 20 == 0, print (f"{value} is last value")

# When the program is executed, it should display the output:
    ## 1 is first value
    ## 10 is middle value
    ## 20 is last value

for value in range(21):
    if value - 10 == 0:
        print(f"{value} is middle value")
    elif value - 20 == 0:
        print(f"{value} is last value")
    elif value - 1 == 0:
        print(f"{value} is first value")


# 8 
# Create a for loop over range(80, 150).
# Print a pair of values using enumerate function and break
# the iteration when the index reach number 20.

for index, value in enumerate(range(80,150)):
    print(index, value)
    if index == 20:
        break

# 9 
# Create a function `height()` to ask a user to input height in metres.
# "Enter your height in metres : "
# The function does not take in any parameters.
# If a user input is string data type, the program should print:
# "Your input is invalid, please try again".
# If a user input is float or integer data type, the program will
# convert it to feet using 1 metre = 3.28084 feet, before printing 
# "Your height of ___ in metre is ____ in feet." 
# The function will loop endlessly, prompting the user to input height
# until the correct data type is entered.

    ## Enter your height in metres: two  
    ## Your input is invalid, please try again
    ## Enter your height in metres: TWO
    ## Your input is invalid, please try again
    ## Enter your height in metres: 2
    ## Your height of 2.0 in metre is 6.56168 in feet.

def height():
    while True:
        try:
            user_input = float(input("Enter your height in metres: "))
        except ValueError:
            print("Your input is invalid, please try again")
        else:
            print(f"Your height of {user_input} in metre is {user_input*3.28084} in feet.")
            break


# alternate solution #
def height():
    while True:
        try:
            user_input = float(input("Enter your height in metres: "))
            print(f"Your height of {user_input} in metre is {user_input*3.28084} in feet.")
            break
        except ValueError:
            print("Your input is invalid, please try again")

