import json

def save_to_json(data, filename):
    with open(filename, 'w') as json_file:
        json.dump(data, json_file, indent=4)

def load_from_json(filename):
    with open(filename, 'r') as json_file:
        data = json.load(json_file)
    return data
