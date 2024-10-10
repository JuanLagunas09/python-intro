print("Hola", "Mundo") # Concatenación
print("Hola" + " " + "Mundo") # Concatenación
print("Hola","Mundo", sep="-") # Sep define el separador de los argumentos
print("Hola", end=" ") # end define el final de la impresión
print("Mundo") # Concatenación

variable = "Hola Mundo"
numero = 5
print(f"{variable} {numero}") # f-string imprime el valor de la variable dentro de {}

valor_pi = 3.1416
print("valor_pi: {:.2f}".format(valor_pi)) # :.2f imprime el valor de la variable

print('Hola soy \'Juan\'') # \ sirve para escapar caracteres imprime comillas simples \'
print("La ruta de archivo es: C:\\Users\\Usuario\\Desktop\\archivo.txt") # \\ imprime una diagonal invertida \