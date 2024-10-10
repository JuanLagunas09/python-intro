add = lambda a, b: a + b # lambda function
# a, b son los argumentos de la función lambda
# : es el separador entre los argumentos y la expresión
# a + b es la expresión que se evalúa y devuelve
substract = lambda a, b: a - b
multiply = lambda a, b: a * b
divide = lambda a, b: a / b

numbers = range(11)
squared = list(map(lambda number: number ** 2, numbers))
# squared sera una lista con los cuadrados de los números del 0 al 10
# map aplica la función lambda a cada elemento de la lista numbers 
# map espera argumentos ( función, lista ) y devuelve un iterable

print(squared)

#Pares
even = list(filter(
    lambda number: 
        number % 2 == 0, 
    numbers))
# filter espera argumentos ( función, lista ) y devuelve un iterable
print(even)
