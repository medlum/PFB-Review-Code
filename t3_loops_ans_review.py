# 1
# Write a function `loop` that use a `while loop` to multiply 1,2,3,4,5 by 2. 
# Use the f-strings (formatted strings)to print each line inside the while loop.
# The output should display:

    ## Double of loop 1 is 2
    ## Double of loop 2 is 4
    ## Double of loop 3 is 6
    ## Double of loop 4 is 8
    ## Double of loop 5 is 10

def loop():
    num = 1
    while num < 6:
        print(f"Double of loop {num} is {num * 2}")
        num += 1
loop()

# 2
# Prompt a user to enter user id with a message:
# `Enter your user id : ` and assign the input to a variable `user_input`
# Check if the user input is equal to `ba_admin` 
# You can assign `ba_admin` to a variable `user_id`
# If the user input values did not match "ba_admin", the program will 
# keep looping to prompt user with a message - "Incorrect id, enter again: "
# When the user input match "ba_admin",  it will print - "Log in successful!"  
# When the program is executed, it should look like:

    ## Enter your user id : andy
    ## Incorrect id, enter again : benny
    ## Incorrect id, enter again : ba_adim
    ## Incorrect id, enter again : ba_admin
    ## Log in successful!

user_id = "ba_admin"
user_input = input("Enter your user id : ")

while user_id != user_input:
    user_input = input("Incorrect id, enter again : ")

print("Log in successful!")

# 3
# Write a `for loop` to print each character of a 
# strings "expresso" in a new line.
# Include a count index using `enumerate` function.
# The output should look like:

    ## (0, 'e')
    ## (1, 'x')
    ## (2, 'p')
    ## (3, 'r')
    ## (4, 'e')
    ## (5, 's')
    ## (6, 's')
    ## (7, 'o')

for letter in enumerate("expresso"):
    print(letter)

# 4
# Check the documentation of `enumerate` function to find out 
# how to change the start index (default to 0) and rewrite the 
# `for loop` to start index at 1.
# Output should display:

    ## (1, 'e')
    ## (2, 'x')
    ## (3, 'p')
    ## (4, 'r')
    ## (5, 'e')
    ## (6, 's')
    ## (7, 's')
    ## (8, 'o')

for letter in enumerate("expresso", start = 1):
    print(letter)
