# 1
# Write the list `cbp_modules` to a text file in your home directory. 
# Name the text file as modules.txt. 
# Each module should be on a separate line in the text file.
 
    # cbp_modules = 
    # ["Programming for Business",
    # "Statistical Application for Business",
    # "Economics",
    # "Making a Business"]

from pathlib import Path
fp = Path.home()/"modules.txt"
fp.touch()
print(fp.exists())

cbp_modules = ["Programming for Business", "Statistical Application for Business", "Economics", "Making a Business"]

with fp.open(mode="w", encoding="UTF-8") as file:
    for module in cbp_modules:
        file.write(module + "\n")

# 2
# Read `modules.txt` created from the last exercise and 
# store each module back as a list. 
# `\n` should not be included in the list.
# Name the list as `modules_list`.  

from pathlib import Path
fp = Path.home()/"modules.txt"

with fp.open(mode="r", encoding="UTF-8") as file:
    modules_list = []
    for line in file.readlines():
        modules_list.append(line.replace("\n", ""))

print(modules_list)

# 3
# Read `modules.txt` created from the last exercise. 
# Store the module(s) that start with the letter `P` as a list.
# Name the list as `p_module`.
# `\n` should not be included in the list.

from pathlib import Path
fp = Path.home()/"modules.txt"

p_module = []

with fp.open(mode="r", encoding="UTF-8") as file:
    for line in file.readlines():
        if line.lower().startswith("p"):
            p_module.append(line.replace("\n", ""))

print(p_module)