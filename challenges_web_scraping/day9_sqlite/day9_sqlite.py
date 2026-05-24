import requests
from datetime import datetime
import sqlite3

DB_NAME = "crypto.db"
API_URL = "https://api.coingecko.com/api/v3/coins/markets"
PARAMETERS = {
    "vs_currency": "usd",
    "order": "market_cap_desc",
    "per_page": 10,
    "page": 1,
    "sparkline": False,
}


def fetch_crypto_data():
    response = requests.get(API_URL, params=PARAMETERS)
    return response.json()


def create_table():
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS crypto_prices (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp TEXT,
                coin TEXT,
                price REAL
            )
    """)

    connection.commit()
    connection.close()


def save_to_db(data):
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()
    timestamp = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
    for coin in data:
        cursor.execute(
            """
            INSERT INTO crypto_prices (timestamp, coin, price)
                       VALUES (?, ? ,?)

            """,
            (timestamp, coin["id"], coin["current_price"]),
        )

    connection.commit()
    connection.close()
    print("Price save to DB")


def search_coin(coin_name):
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()
    cursor.execute(
        """
    SELECT timestamp, price from crypto_prices
                   WHERE coin = ? 
                   ORDER BY timestamp DESC
                   LIMIT 1

    """,
        (coin_name,),
    )

    result = cursor.fetchone()
    connection.close()
    if result:
        print(f"💰 ${result[1]} - ⏰ {result[0]}")

    return result


def main():
    create_table()
    print("1. Fetch and store crypto data")
    print("2. Search latest price for  crypto coin")

    choise = input("Choose an options:  ").strip()

    if choise == "1":
        data = fetch_crypto_data()
        save_to_db(data)

    elif choise == "2":
        coin_name = input("Enter coin name:  ").strip().lower()
        result = search_coin(coin_name)

    else:
        print("Invalid option")


main()
