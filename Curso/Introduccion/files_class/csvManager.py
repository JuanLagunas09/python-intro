import csv
import os

current_path = os.path.dirname(__file__)
path_csv = os.path.join(current_path, "files", "products.csv")

""" with open(path_csv, mode="r") as file:
    csv_reader = csv.DictReader(file) # Convierte las lineas en directorios { key : value}
    for row in csv_reader:
        print(row) """
        
""" with open(path_csv, mode="r") as file:
    csv_reader = csv.DictReader(file) # Convierte las lineas en directorios { key : value}
    for row in csv_reader:
        print(f"Producto: {row['name']} cuesta ${row['price']}") """
        
new_product = {
    'name' : 'product 1',
    'price': 30,
    'quantity': 100,
    'brand': 'marca 1',
    'category': 'Accessories',
    'entry_date': '2021-01-01'
}

""" with open(path_csv, mode="a", newline='') as file:
    file.write('\n')
    csv_writer = csv.DictWriter(file, fieldnames=new_product.keys()) # Crea las llaves del direcorio
    csv_writer.writerow(new_product) # Match keys y creacion del nuevo registro """
    
path_csv_copy = os.path.join(current_path, "files", "prducts_copy.csv") # Crea una copia del archivo original, no tiene que estar creada la copia
    
with open(path_csv, mode='r') as file:
    csv_reader = csv.DictReader(file) # Convierte las lineas en directorios { key : value}
    fields_names= csv_reader.fieldnames + ['total_value'] # Obtiene el valord de los encabezados y agrega un nuevo encabezado
    
    with open(path_csv_copy, mode='w', newline='') as file_copy:
        csv_writer = csv.DictWriter(file_copy, fieldnames=fields_names) # Crea las un directorio con las nuevas llaves
        csv_writer.writeheader() # crear solo los encabezados
        
        for row in csv_reader: # for sobre el archivo original
            row['total_value'] = float(row['price']) * int(row['quantity']) # calcula los valores de la nueva columna
            csv_writer.writerow(row) # Llena el nuevo archivo con la copia de las filas originales + total_value
        
    
    