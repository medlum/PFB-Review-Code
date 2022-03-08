#1. Create 1st variable `num_1` and assign with a value of 5 billion using 
# an underscore '_' to separate every 3 zeros.
num_1 = 5_000_000_000

#2. Create 2nd variable `num_2` and assign 100.50 to the variable.
num_2 = 100.50

#3. Create 3rd variable `num_3` and assign "200.50" to the variable
num_3 = "200.50"

#4. Check the data type of `num_1`, `num_2`, `num_3`.
# `num_3` should be string data type.
print(type(num_1))
print(type(num_2))
print(type(num_3))

#5. 
# Add `num_2` and `num_3` with an addition operation. 
# The result should return 301.00.
# Convert the string to a float before addition.
print(num_2 + float(num_3))

#6. Create 4th variable `num_4` and assign 50 to the variable.
num_4 = 50

#7. What is the value of an integer division of `num_2` by `num_4`?
print(num_2 // num_4)

#8. What is the  remainder of `num_2` by `num_4`?
print(num_2 % num_4)

#9. What is  the value of 4 raised to the power of 5?
print(4 ** 5)

#10. Multiply `num_2` with `num_4` before adding the value to `num_3` in a single 
# arithmetic expression.
print(num_2 * num_4 + float(num_3))

#11. Add `num_2` and `num_4` before multiplying the value by `num_3` in a single 
# arithemtic expression.
print((num_2 + num_4) * float(num_3))

#12. Round 2.02454 to 2 decimal places.
print(round(2.02454, 2))

#13. Round 1000.40 to an integer.
print(round(1000.40))

#14. What is the value of 4 raised to the power of 5 using the pow() function?
print(pow(4, 5))