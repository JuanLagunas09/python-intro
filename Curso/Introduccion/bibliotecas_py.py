import os # Trabaja conrutas y archivos
import math # Trabaja valores y operaciones matematicas exactas como PI
import random

# OBTIENE LA RUTA ACTUAL
""" pwd = os.getcwd()
print("\n",pwd) """

#LISTAR ARCHIVO TXT
""" txt_files = [file for file in os.listdir('./poo') if file.endswith('.py')] # Genera una lista de los arhivos .py en la carpeta poo
print(txt_files) """

""" os.rename('bucles.py', 'ciclos.py') # Cambia el nombre del archivo
print("rename") """

# Perimetro y area de un circulo
""" radius = 5
area = math.pi * radius**2
perimeter = 2 * math.pi * radius

print(area)
print(perimeter) """

# Generar numero entero aleatorio
""" random_number = random.randint(1,10)
print(random_number) """

# Elegir color aleatorio
""" colors=['red', 'blue', 'green']
random_color = random.choice(colors)
print(random_color) """

# Barajar cartas
cards = ['as', 'rey', 'reina', 'jota', '10']
random.shuffle(cards) # Desordenar lista
print(cards)