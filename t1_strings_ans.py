# 1. Create 2 string variables `firstname`, `lastname` with 
# your own name first and last name.
firstname = "andy"
lastname = "oh"

# 2. Combine the `firstname`, `lastname` variabls as `fullname`
# with `+` and put a whitespsace with a quotation " " 
# between the  firstname and lastname.
fullname = firstname + " " + lastname

# 3. Print the length of "fullname".
print(len(lastname))

# 4. Print the word "financial" from "financial_management" 
# with the slice notation [].
title = "financial_management"
print(title[0:10])

# 5. Print each word in the "sentence" variable on a separate line using `\n`.
sentence = "statistics economics programming"
print("statistics \neconomics \nprogramming")

# 6. Check if the 2 variables below are equal. It should return 
# a boolean: True or False.
module_1 = "marketing"
module_2 = "accounting"
print(module_1 == module_2)

# 7.
# Check the length of `country` variable.
# Remove any unwanted whitespace and and assign 
# to a new variable named `country_strip`.
# Check the length of `country_strip`.

country = ("      this is our country: Singapore  ")
print(len(country))
country_new = country.strip()
print(len(country_new))

# 8. Use formatted strings  f"{}" to print the address variables below:

block = "50"
unit = "20-22"
street = "clementi road" 
postal_code = "573679"

print(f"{block} {unit} {street} {postal_code}")

# 9. Use `.replace()` to replace `Rihana` to `BTS` in `favourite_artist` variable.
favourite_artist = "Rihana is my favourite artist"
favourite_artist.replace("Rihana", "BTS")
print(favourite_artist)
