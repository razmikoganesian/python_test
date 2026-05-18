# API
import os
import csv
from datetime import datetime
import requests


FILENAME = "weather.logs.csv"
API_key = "get you own key"


if not os.path.exists(FILENAME):
    with open(FILENAME, 'w', encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Date", "City", "Temperature", "Condition"])

def log_weather():
    city = input("Enter your city name:  ").strip()
    date = datetime.now().strftime("%Y-%m-%d")


    with open(FILENAME, 'r', encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row["Date"] == date and row["City"].lower() == city.lower():
                print("Entry for this city and date exists")
                return
    
    try:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_key}&units=metric"
        response = requests.get(url)
        data = response.json()

        if response.status_code != 200:
            print(f"Api error")
            return
        
        temperature = data['main']['temp']
        condition = data['weather'][0]['main']

        with open(FILENAME, 'a', encoding="utf-8", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([date, city, temperature, condition])
            print(f"Logged: {temperature} {condition} of {city} on {date}")


    except Exception as e:
        print("Failed to make a API request")

def view_logs():
    with open(FILENAME, 'r', encoding="utf-8", newline="") as f:
        reader = list(csv.reader(f))
        if len(reader) <= 1:
            print("No data for display")
            return
        for row in reader[1:]:
            print(f"- {row[0]} : {row[1]} : {row[2]} C degree: {row[3]}")
        



def main():
    while True:
        print("Real time weather logger")
        print("1. Add weather log")
        print("2. View weather logs")

        choise = input("Choose an option:  ").strip()

        match choise:
            case "1" : log_weather()
            case "2" : view_logs()
            case _: print("Invalid choice")

if __name__  == "__main__":
    main()







