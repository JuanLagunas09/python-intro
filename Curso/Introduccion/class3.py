# Python es un leguaje ordenado se ejecuta de arriba hacía abajo
greeting = "Hola"
name = "Juan"
last_name = "Perez"
edad = 25
greeting = "Buenos días" # Cambio de valor de la variable greeting
greeting_2 = "Buenas tardes"
char = "a"
strSimple = 'Hola'
strTriple = '''
Hola
Como estas hoy?
Eto es un string de tres lineas
Triple comilla simple para escribir comentarios largos indexados
'''
strIndexado = "0123456789"
strIndexado_2 = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"

print(greeting + " " + name + " tienes " + str(edad) + " años")
print(greeting_2 + " " + name + " tienes " + str(edad) + " años")
#print(type(greeting))
#print(type(char))
#print(type(edad))
#print(type(strSimple))
#print(type(strTriple))
#print(strTriple)

print(strIndexado[0:5]) # Imprime los primeros 5 caracteres de la cadena
print(strIndexado_2[0]) # Imprime el primer caracter de la cadena
print(strIndexado_2[-1]) # Imprime el último caracter de la cadena

print(name + " " + last_name) # Concatenación de cadenas
print((name + " ") * 5) # Repetición de cadenas 5 veces
print(len(name)) # Longitud de la cadena
print(name.upper()) # Convierte la cadena a mayúsculas
print(name.lower()) # Convierte la cadena a minúsculas
print(name.capitalize()) # Convierte la primera letra de la cadena a mayúscula
print(name.replace("J", "Hola")) # Reemplaza una letra por otra en la cadena
print(name.split("a")) # Divide la cadena en una lista de cadenas
print(name.find("a")) # Encuentra la posición de un caracter en la cadena
print(name.strip()) # Elimina los espacios en blanco al inicio y al final de la cadena