import json
import os

current_path = os.path.dirname(__file__)
json_path = os.path.join(current_path, "files", "products_json.json")

new_product = {
        "name": "product",
        "price": 100,
        "quantity": 40,
        "brand": "brand",
        "category": "category",
        "entry_date": "2021-01-01"
    }

with open(json_path, mode="r") as file_json:
    products = json.load(file_json) # Lectura del archivo

products.append(new_product) # Agrega un nuevo producto a la lista

with open(json_path, mode="w") as file: # Modo escritura
    json.dump(products, file, indent=4) # Añade la lista modificada con una identacion de 4 espacios
    
print(type(products)) # Devuelve una lista
for element in products:
    # print(element)
    print(f"Pructo: {element['name']} cuesta {element['price']}")