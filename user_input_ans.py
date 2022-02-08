# 1. Ask a user to enter: first name, last name, age and gender
# 2. Convert age variable from strings to integer 
# 3  Print a statement using f-strings to include the user input with last name in upper case.
# 4. Print the class of Age

firstname = input("Enter your first name : ")
lastname = input("Enter your last name : ")
age = int(input("Enter your age : "))
gender = input("Enter your gender (male or female) : ")

print(f"{firstname} {lastname.upper()} is {age} years old and is a {gender}. ")
print(type(age))