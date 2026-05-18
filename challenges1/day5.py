import csv
from collections import defaultdict
import matplotlib.pyplot as plt


FILENAME = "weather.logs.csv"

def visualize_weather():
    date = []
    temps = []
    conditions = defaultdict(int)

    with open(FILENAME, "r", encoding="utf-8") as f:
        dict_reader = csv.DictReader(f)
        for row in dict_reader:
            try:
                date.append(row['Date'])
                temps.append(float(row["Temperature"]))
                conditions[row["Condition"]] += 1
            except (ValueError, KeyError):
                continue
    if not date:
        print("No dates")
        return
    
    plt.figure(figsize=(10,7))
    plt.bar(conditions.keys(), conditions.values(), color='skyblue')
    plt.xlabel('Condition')
    plt.ylabel('Days')



    plt.figure(figsize=(7,5))
    plt.plot(date,temps,marker='o')
    plt.title('Temperature over time')
    plt.xlabel('Date')
    plt.ylabel('Temperature')
    plt.grid(True)
    plt.tight_layout()

    plt.show()
        


visualize_weather()