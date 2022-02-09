import json


def load_json(json_path):
    with open(json_path) as json_file:
        data = json.load(json_file)
        return data
    return None


def get_field_val(class_field, field, data: json):
    return data[class_field][field]
