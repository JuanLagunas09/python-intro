import os

# Obtener la ruta del directorio actual del script
current_dir = os.path.dirname(__file__)

# Construir la ruta completa del archivo
file_path = os.path.join(current_dir, "files", "caperucita.txt")

# Abrir y leer el archivo linea por linea
""" with open(file_path, "r") as file:
    for line in file:
        print(line.strip()) """

# Leer todas las lineas en una lista
""" with open(file_path, "r") as file:
    lines = file.readlines()
    print(lines) """

# Añadir texto "a" (append)
""" with open(file_path, "a") as file:
    file.write("\n\nBy:ChatGPT") """
    
# Sobreescribir "w"
""" with open(file_path, "w") as file:
    file.write("\n\nBy:ChatGPT") """
    
# Contar lineas del archivo
counter_lines = 0
lines = []
with open(file_path, "r") as file:
    for line in file:
        if line.strip() != '':
            lines.append(line.strip())
        counter_lines += 1
    
# print(lines)
print("Filas con contenido - ", len(lines))
print("Lineas totales - ", counter_lines)
