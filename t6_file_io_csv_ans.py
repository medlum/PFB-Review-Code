# 1.
# Write a program that writes  numbers`list to a csv file in your home directory.
# Name the csv file as `numbers.csv`.

# numbers = [[2, 4, 6, 8, 10], [12, 14, 16, 18, 20], [22, 24, 26, 28, 30]]

from pathlib import Path
import csv

fp = Path.home()/"numbers.csv"
fp.touch()
print(fp.exists())

numbers = [[2, 4, 6, 8, 10], [12, 14, 16, 18, 20], [22, 24, 26, 28, 30]]

with fp.open(mode="w", encoding="UTF-8" , newline="") as file:
    writer = csv.writer(file)
    for list_num in numbers:
        writer.writerow(list_num)

# 2.
# Write a program to read `numbers.csv` file created from the last exercise.
# The program will read and print each line from the csv file as follows: 

    # ['2', '4', '6', '8', '10']
    # ['12', '14', '16', '18', '20']
    # ['22', '24', '26', '28', '30']

fp = Path.home()/"numbers.csv"
with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    for line in reader:
        print(line)

# 3.
# Write a program to write `weather` list to a csv file in your home directory.
# Include three headers : Day, Temperature, Wind Speed in the csv file.
# Name the csv file as `weather.csv` 

# weather = [["Monday", 28.7, 10], ["Tuesday", 30.2, 15],  ["Wednesday", 32, 9], ["Thursday", 26, 19],  ["Friday", 28, 14]]


fp = Path.home()/"weather.csv"
fp.touch()
print(fp.exists())

weather = [["Monday", 28.7, 10], ["Tuesday", 30.2, 15],  ["Wednesday", 32, 9], ["Thursday", 26, 19],  ["Friday", 28, 14]]
header = ["Day", "Temperature", "Wind Speed"]

with fp.open(mode = "w", encoding="UTF-8", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(header)
    for line in weather:
        writer.writerow(line)

# 4.
# Write a program to read `weather.csv` file created from the last 
# exercise. The program will read the file into a list of dictionaries.
# Name the list as `weather_list`

    # weather_list =
    # [{'day': 'Monday', 'temp': '28.7', 'windspeed': '10'},
    #  {'day': 'Tuesday', 'temp': '30.2', 'windspeed': '15'}, 
    #  {'day': 'Wednesday', 'temp': '32', 'windspeed': '9'}, 
    #  {'day': 'Thursday', 'temp': '26', 'windspeed': '19'}, 
    #  {'day': 'Friday', 'temp': '28', 'windspeed': '14'}]

fp = Path.home()/"weather.csv"

with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    #reader  = csv.DictReader(file)
    weather_list = []
    reader = csv.reader(file)

    next(reader)
    for day, temp, windspeed in reader:
        empty_dict = dict()
        empty_dict["day"] = day
        empty_dict["temp"] = temp
        empty_dict["windspeed"] = windspeed
        weather_list.append(empty_dict)
        
print(weather_list)