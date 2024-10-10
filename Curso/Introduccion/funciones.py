def voidFunction(message): # Definición de la función palabra reservada def
    print("Mensaje enviado: ", message)
    
voidFunction("Hola mundo")
voidFunction(2) # No hay restricción de tipos de datos

def typedSuma(a: int, b: int) -> int: 
# Restricción de tipos de datos
# -> int: indica que el tipo de dato que va a retornar la función
    return a + b

print("el resultado es: ", typedSuma(2, 3)) 


def fullName(nombre: str, apellido = "Sin dato") -> str: 
# apellido = "Sin dato": valor por defecto
# Restricción de tipos de datos nombre: str, apellido es str porque se le asigna un valor por defecto de tipo str
# -> str: indica que el tipo de dato que va a retornar la función
    return nombre + " " + apellido

print(fullName("Juan", "Perez"))
print(fullName("Juan")) # La función toma el valor por defecto
print(fullName(apellido = "Perez", nombre = "Juan")) # Se puede cambiar el orden de los argumentos
# print(fullName("Juan", 3)) # Error porque el tipo de dato no es el esperado


def add(*args) -> int: # *args: indica que se pueden recibir varios argumentos
    total = 0
    for i in args:
        total += i
    return total

result = add(1, 2, 3, 4, 5)
print("El resultado de la suma es: ", result)