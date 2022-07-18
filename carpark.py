from textwrap import indent
import requests
import json
datetime = "2022-07-01T08:00:00"
url = f"https://api.data.gov.sg/v1/transport/carpark-availability?date_time={datetime}"
response = requests.get(url)
data = response.json()
#print(data["items"])
for i in data["items"]:
    for y in i["carpark_data"]:
        print(y)
#print(json.dumps(data["items"], indent=4))

