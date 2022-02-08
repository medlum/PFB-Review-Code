##########################################################################################
# Weather Readings 

# Write a program to retrieve 24 hour weather readings across Singapore 
# based on the your computer's current system date. 
# The weather temperature data can be found at https://data.gov.sg/dataset/weather-forecast

### datetime library ###
# You can make use of a built-in library: datetime to obtain the current time from your computer system:

import datetime as dt
current_time = dt.date.today()

# After assigning the current time to `current_time`, you can include a f-string format and 
# insert the current_time in the placeholder.
# For example: url = f'your_api_url/endpoint/?date={current_time}'
# For more information, refer to datetime documentation  https://docs.python.org/3.7/library/datetime.html

### API Connection ###
# The response code should return 200 after calling the API.
# The data from the response object should be retrieved by .json().
# The response code, keys and data structure should look like the followings:
"""
<Response [200]>

dict_keys(['area_metadata', 'items', 'api_info'])

{'area_metadata': [{'name': 'Ang Mo Kio', 'label_location': {'latitude': 1.375, 'longitude': 103.839}}, 
{'name': 'Bedok', 'label_location': {'latitude': 1.321, 'longitude': 103.924}}, 
{'name': 'Bishan', 'label_location': {'latitude': 1.350772, 'longitude': 103.839}}, 
{'name': 'Boon Lay', 'label_location': {'latitude': 1.304, 'longitude': 103.701}},
{'name': 'Bukit Batok', 'label_location': {'latitude': 1.353, 'longitude': 103.754}},.......
"""

### Retrieve key/value pairs in `forecast` ###
# Retrieve the values in the `forecasts` key nested in the `items` key.
# The values in the `forecasts` key consists of 2 key/value pairs : `area` and `forecast` 
# Iterate with `for loop` to print the values of `area` and `forecast`.
# The output of the values should return similar results:
"""
Estate: Ang Mo Kio, 24 hour Forecast: Light Rain
Estate: Bedok, 24 hour Forecast: Light Rain
Estate: Bishan, 24 hour Forecast: Light Rain
Estate: Boon Lay, 24 hour Forecast: Light Rain
Estate: Bukit Batok, 24 hour Forecast: Light Rain
Estate: Bukit Merah, 24 hour Forecast: Light Rain
...
...
"""

import datetime as dt
import requests
current_time = dt.date.today()
url = f"https://api.data.gov.sg/v1/environment/2-hour-weather-forecast?date={current_time}"
response = requests.get(url)
print(response)
data = response.json()
print(data.keys())
print(data)

for item in data["items"]:
    for estate in item["forecasts"]:
        print(f'Estate: {estate["area"]}, 24 hour Forecast: {estate["forecast"]}')
