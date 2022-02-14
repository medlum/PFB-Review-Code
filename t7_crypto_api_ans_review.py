### Write a program to retrieve cryptocurriences exchange rate from https://www.alphavantage.co ###

# The required API endpoints and query parameters are:

# function=CURRENCY_EXCHANGE_RATE
# from_currency=BTC 
# to_currency=USD
# apikey=yourAPIkey 
# where BTC refers to BitCoin and USD refers to United States Dollar.

# The data from the API call should return similar results:
"""
{
    "Realtime Currency Exchange Rate": {
        "1. From_Currency Code": "BTC",
        "2. From_Currency Name": "Bitcoin",
        "3. To_Currency Code": "USD",
        "4. To_Currency Name": "United States Dollar",
        "5. Exchange Rate": "51800.01000000",
        "6. Last Refreshed": "2021-09-06 01:19:02",
        "7. Time Zone": "UTC",
        "8. Bid Price": "51800.00000000",
        "9. Ask Price": "51800.01000000"
    }
}
"""

### Write the values from the following keys to a csv file ###
# "From_Currency Name"
# "To_Currency Name"
# "Exchange Rate"
# "Last Refreshed"
# "Bid Price"
# "Ask Price"

# The csv should include the keys as its headers.
# Therefore, the CSV output should be similar to the following:
"""
From_Currency Name,To_Currency Name,Exchange Rate,Last Refreshed,Bid Price,Ask Price
Bitcoin,United States Dollar,46858.12000000,2022-01-03 04:35:01,46858.11000000,46858.12000000
"""

import requests, csv
from pathlib import Path 
url = "https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=BTC&to_currency=USD&apikey=F2UE00AWKLCI7DKV"
response = requests.get(url)
print(response)
data = response.json()
print(data)

fp = Path.home()/"python4biz"/"crypto.csv"
fp.touch()
print(fp.exists())

with fp.open(mode="w", encoding="UTF-8", newline="") as file:
    writer = csv.writer(file)
    headers = ["From_Currency Name", "To_Currency Name", "Exchange Rate", "Last Refreshed", "Bid Price","Ask Price"]
    writer.writerow(headers)
    for item in data.values():
        writer.writerow([item["2. From_Currency Name"],
        item["4. To_Currency Name"],
        item["5. Exchange Rate"], 
        item["6. Last Refreshed"], 
        item["8. Bid Price"], 
        item["9. Ask Price"]])

