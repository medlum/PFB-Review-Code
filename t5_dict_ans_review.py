# 1. Create a dictionary named `fruits_order` with the following key/value pairs
# "apple" : 200, "orange": 150, "papaya": 50, "pineapple" : 45.

fruits_order = {"apple" : 200,
                "orange": 150,
                "papaya": 50,
                "pineapple" : 45
                 }
# 2. Insert a new key/pair "durian": 300 to `fruits_order`. 
fruits_order["durian"] = 300 

# 3. Access the value of "papaya" using [] and .get() method.

print(fruits_order["papaya"])
print(fruits_order.get("papaya"))

# 4. Write a if statement to check if "durian" exists as a key of the dictionary
# and set the value to 100 if it exists.

if "durian" in fruits_order.keys():
    fruits_order["durian"] = 100

# 5. Write a `for loop` to display the key/value pairs using f-strings to print.
# It should display the followings:
    # apple order: 200
    # orange order: 150
    # papaya order: 50
    # pineapple order: 45
    # durian order: 100

for fruit in fruits_order:
    print(f"{fruit} order: {fruits_order[fruit]}")

# 6. Write a `for loop` with a if statement to check for value less than 100 among
# the key/value pairs. If the value is less than 100, print the key using f-string.
# It should display the followings:
    # urgent order: papaya
    # urgent order: pineapple

for fruit in fruits_order:
    if fruits_order[fruit] < 100:
        print(f"urgent order: {fruit}")

# 7. Create an empty list named `total_quantity` and write a `for loop` to append
# the values of `fruits_order` to `total_quantity`, using dictionary's .values() method.
# Sum the values in `total_quantity` using sum() and print. The sum should be 545.

empty_list = []
for order in fruits_order.values():
    empty_list.append(order)

print(sum(empty_list))

