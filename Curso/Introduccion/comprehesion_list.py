squares = [value ** 2 for value in range(1, 11)]
# Value toma el valor de 1 a 10, y se eleva al cuadrado y se guarda en la lista squares
#se usa el ciclo for para recorrer los valores de 1 a 10

celcius = [0, 10, 20, 30, 40, 50]
fahrenheit = [(temperaure * 9/5) + 32 for temperaure in celcius]
# se recorre la lista de celcius y se convierte a fahrenheit, se aplica la formula de conversión (temperaure * 9/5) + 32

evens = [value for value in range(1, 20) if value % 2 == 0]
# se recorre la lista de 1 a 20 y se guarda en la lista evens los valores que son pares 
# primero se debe definir el ciclo for y luego la condición if esto por que la condición se evalua despues de recorrer el ciclo for

# print(squares, end="\n\n")
# print(celcius, end="\n\n")
# print(fahrenheit, end="\n\n")
# print(evens, end="\n\n")

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12]
]

print(matrix, end="\n\n")

transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print(transposed, end="\n\n")
# comprehesion list anidado, se recorre la matriz y se transpone
# [acccion cliclo clave rango condiciones*]
# *en este caso no hay condiciones

# Tambien se puede hacer de la siguiente manera: 
transposed = []
for i in range(len(matrix[0])):
    transposed_row = []
    for row in matrix:
        #print(row, end="\n")
        #print(row[i], end="\n")
        transposed_row.append(row[i])
    #print("----------------", end="\n\n")
    transposed.append(transposed_row)
    
# Yo lo entiendo de la siguiente manera:
# Se obtiene la longitud de la primera fila de la matriz para transponer la matriz de 4x3 a 3x4
# Por cada columna se realiza una iteracion "i" es decir un total de 3 iteraciones que seran las filas de la matriz transpuesta
# por cada elemento en la matriz se van recorriendo las posiciones de cada coluna (0, 1, 2) y se van guardando en una lista transposed_row para crear la matriz transpuesta
# se puede apreciar mejor el proceso si se descomenta los print de los ciclos for

print(transposed, end="\n\n")
