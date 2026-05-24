import requests
import os
import csv
from datetime import datetime
import matplotlib.pyplot as plt

API_URL = "https://api.coingecko.com/api/v3/coins/markets"
PARAMETERS = {
    "vs_currency": "usd",
    "order": "market_cap_desc",
    "per_page": 10,
    "page": 1,
    "sparkline": False,
}
CSV_FILE = "crypto_prices.csv"


def fetch_crypto_data():
    response = requests.get(API_URL, params=PARAMETERS)
    return response.json()


def save_to_csv(data):
    file_exist = os.path.exists(CSV_FILE)

    with open(CSV_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        if not file_exist:
            writer.writerow(["timestamp", "coin", "price"])

        timestamp = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
        for coin in data:
            writer.writerow([timestamp, coin["id"], coin["current_price"]])

    print(" Data saved to CSV")


def plot_graph(coin_id):
    times = []
    prices = []

    with open(CSV_FILE, newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["coin"] == coin_id:
                times.append(row["timestamp"])
                prices.append(float(row["price"]))

    if not times:
        print(f"No data found for  {coin_id}")

    plt.figure(figsize=(10, 5))
    plt.plot(times, prices, marker="o")
    plt.tight_layout()
    plt.grid()
    plt.show()


def main():
    print("Fetching live crypto data....")
    crypto_data = fetch_crypto_data()
    save_to_csv(crypto_data)

    print("-" * 30)
    for coin in crypto_data:
        print(f"{coin['id']} - ${coin['current_price']}")
    print("-" * 30)

    choise = input("Enter the coinnane to get graph:  ").strip().lower()

    if choise:
        plot_graph(choise)


if __name__ == "__main__":
    main()
