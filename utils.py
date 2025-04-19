import json
import os

def load_json(file_name: str):
    """Loads a JSON file and returns the content."""
    if os.path.exists(file_name):
        with open(file_name, 'r') as f:
            return json.load(f)
    else:
        return {}

def save_json(file_name: str, data: dict):
    """Saves data to a JSON file."""
    with open(file_name, 'w') as f:
        json.dump(data, f, indent=4)
