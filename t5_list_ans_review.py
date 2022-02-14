### Exercise 1 ###
# Create a list named `apparel` with two elements, "shoes" and "shirt".
apparel = ["shoes","shirt"]

# Append the string "tie" to apparel using .append().
apparel.append("tie")

# Add the strings "sunnies" and "pants" to apparel using .extend().
apparel.extend(["sunnies", "pants"])

# Print the first two items in the apparel list using print() and slice notation.
print(apparel[0:2])

# Print the last item in apparel using print() and index notation.
print(apparel[-1])

### Exercise 2 ###
# Create a list called sports_list from the string "running, cycling, swimming" 
# with the string .split() method.
sports_list = "running, cycling, swimming".split(",")

# Verify that sports has three items using len().
print(len(sports_list))

# Create a new list called sports_length using a list comprehension 
# that contains the length of each string in sports_list.
sports_length = [len(length) for length in sports_list]
