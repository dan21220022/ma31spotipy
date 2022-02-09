import json


def load_json(json_path):
    with open(json_path) as json_file:
        data = json.load(json_file)
        return data
    return None


def get_field_val(data: json, *args):
    json_data = data
    for arg in args:
        json_data = json_data[arg]
    return json_data
