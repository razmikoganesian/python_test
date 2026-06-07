import json
import csv
import os

from contourpy.util import data
from numpy import rec

INPUT_FILE = "api_data.json"
OUPUT_FILE = "converted_api_data.csv"


def load_json_data(filename):
    if not os.path.exists(filename):
        print("There is no JSON file")
        return []
    
    with open(filename, 'r', encoding="utf-8") as f:
        try:
            return json.load(f)
        except:
            print("Invalid JSON format")

def convert_json_to_csv(data, output_file):
    if not data:
        print("No data to convert")
        return
    
    fielnames = list(data[0].keys())

    with open(output_file, 'w', newline='', encoding="utf-8") as f:
        writer = csv.DictWriter(f,fieldnames=fielnames)
        writer.writeheader()
        for record in data:
            writer.writerow(record)
    
    print(f"Converted {len(data)} rocerds to {output_file}")

def main():
    print('Converting json to csv')
    data = load_json_data(INPUT_FILE)
    convert_json_to_csv(data, OUPUT_FILE)

if __name__ == "__main__":
    main()