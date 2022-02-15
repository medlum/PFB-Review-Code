### Exercise 1 ###
# 1. Create a tuple literal named `sgp_township` that 
# holds the strings "queensway", "jurong", and "clementi", in that order.
sgp_township = ("queensway", "jurong","clementi")
# 2. Using index notation and print(), display "clementi" in `sgp_township`.

print(sgp_township[1])

# 3. In a single line of code, unpack the values in `sgp_township`
# into three new strings named `town1`, `town2`, and `town3`. 
# Print each value on a separate line.
town1, town2, town3  = sgp_township
print(town1, town2, town3, sep="\n")


# ### Exercise 2 ###
# 1. Using tuple() and a string literal, create a tuple called `my_devices`
# that contains 3 elements: "laptop", "cellphone", "camera".
my_devices = ("laptop", "cellphone", "camera")

# 2. Check whether the "smartwatch" is in `my_devices` using the `in` keyword and
# print.
print("smartwatch" in my_devices)

# 3. Create a new tuple called `two_devices` containing all items in `my_devices`
# except "camera" using slice notation.
two_devices = my_devices[:-1]

