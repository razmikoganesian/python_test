import json
import os


INPUT_FILE = "nested_data.json"
OUTPUT_FILE = "flattened_data.json"

def flatten_json(data, parent_key="", sep="."):
    items = {}

    if isinstance(data, dict):
        for key, value in data.items():
            full_key = f"{parent_key}{sep}{key}" if parent_key else key
            print(full_key)
            items.update(flatten_json(value, full_key, sep=sep))

    elif isinstance(data, list):
        for index, item in enumerate(data):
            full_key = f"{parent_key}{sep}{index}" if parent_key else str(index)
            items.update(flatten_json(item, full_key, sep=sep))

    else:
        items[parent_key] = data

    return items

def main():
    if not os.path.exists(INPUT_FILE):
        print("No input file")
        return
    
    try:
        with open(INPUT_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)

        separater = input("Enter your separater like # or .").strip() or '.'

        data1 = flatten_json(data, sep=separater )
        with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
            json.dump(data1, f, indent=2)

        print(f"Flatteened json saved to {OUTPUT_FILE}")
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()