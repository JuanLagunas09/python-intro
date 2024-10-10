import statistics
import csv

monthly_sales = {}

with open('month_sales.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        month = row['month'] # obtiene el valor de la columna month
        sales = int(row['sales']) # convierte el valor de la columna sales a entero
        monthly_sales[month] = sales # agrega el valor de la columna month y sales al diccionario monthly_sales

sales = list(monthly_sales.values()) # obtiene los valores de la lista sin las llaves
# print(sales)

# Media de datos
mean = statistics.mean(sales) # obtiene la media de los datos
print(f'Media: {mean}')

# Mediana de datos
median = statistics.median(sales) # obtiene la mediana de los datos
print(f'Mediana: {median}')

# Moda de datos
mode = statistics.mode(sales) # obtiene la moda de los datos
print(f'Moda: {mode}')

# Desviación estándar de datos
stdev = statistics.stdev(sales) # obtiene la desviación estándar de los datos
print(f'Desviación estándar: {stdev}')

# Varianza de datos
variance = statistics.variance(sales) # obtiene la varianza de los datos
print(f'Varianza: {variance}')

# Maximo de datos
max_sales = max(sales) # obtiene el valor máximo de los datos
print(f'Máximo: {max_sales}')

# Minimo de datos
min_sales = min(sales) # obtiene el valor mínimo de los datos
print(f'Mínimo: {min_sales}')

# Rango de datos
range_sales = max_sales - min_sales # obtiene el rango de los datos
print(f'Rango: {range_sales}')