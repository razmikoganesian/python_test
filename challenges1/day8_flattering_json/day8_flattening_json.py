import json
import os

INPUT_FILE = "nested_data.json"
OUTPUT_FILE = "flattened_data.json"

def flatten_json(data, parent_key="", sep="."):
    items = {}

    if isinstance(data, dict):
        pass
    elif isinstance(data, list):
        pass
    else:
        items[parent_key] = data

    return items
