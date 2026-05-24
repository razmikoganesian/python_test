import requests
import os
import csv
from datetime import datetime
import schedule
import time
 
API_URL = "https://api.coingecko.com/api/v3/coins/markets"
PARAMETERS = {"vs_currency": 'usd',
              "order": "market_cap_desc",
              'per_page': 10,
              'page': 1,
              'sparkline': False}
CSV_FILE = 'crypto_prices.csv'

def fetch_crypto_data():
    response = requests.get(API_URL, params=PARAMETERS)
    return  response.json()


def save_to_csv(data):
    file_exist =  os.path.exists(CSV_FILE)

    with open(CSV_FILE, 'a', newline="" ) as f:
        writer = csv.writer(f)
        if not file_exist:
            writer.writerow(["timestamp", "coin", "price" ])
        
        timestamp = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
        for coin in data:
            writer.writerow([timestamp, coin["id"], coin["current_price"] ])

    print(" Data saved to CSV")

def job():
    print("Fetching data hourly..")
    crypto_data = fetch_crypto_data()
    save_to_csv(crypto_data)

schedule.every().day.at("10:30").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)