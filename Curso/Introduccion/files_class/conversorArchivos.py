import os
import csv
import json

current_path = os.path.dirname(__file__)
path_csv = os.path.join(current_path, "files", "products.csv")
path_json = os.path.join(current_path, "files", "products_json.json")

path_json_to_csv = os.path.join(current_path, "files", "products_json_to_csv.csv")
path_csv_to_json = os.path.join(current_path, "files", "products_csv_to_json.json")

# JSON TO CSV
with open(path_json, mode='r') as file_json:
    products_json = json.load(file_json)
    products_json_fields = products_json[0].keys()
    
    with open(path_json_to_csv, mode='w', newline='') as file_convert:
        csv_writer = csv.DictWriter(file_convert, fieldnames=products_json_fields)
        csv_writer.writeheader()

        for element in products_json:
            csv_writer.writerow(element)

# CSV TO JSON
with open(path_csv, mode='r') as file_csv:
    products_csv = csv.DictReader(file_csv)
    with open(path_csv_to_json, mode="w") as file_convert_csv:
        products_to_json = []
        for element in products_csv:
            products_to_json.append(element)
        json.dump(products_to_json, file_convert_csv, indent=4)
    