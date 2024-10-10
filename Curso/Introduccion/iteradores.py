# generadores e iteradores
my_list = [1, 2, 3, 4]
my_iter = iter(my_list) # iter() convierte un objeto en un iterador

#print(my_list)
#print(my_iter) # imprime un objeto iterador <list_iterator object at 0x0000021D3D3D3D30>
#print(type(my_iter)) # <class 'list_iterator'>

print(next(my_iter)) # next() imprime el primer elemento del iterador
print(next(my_iter)) # imprime el segundo elemento del iterador
print(next(my_iter)) # imprime el tercer elemento del iterador
print(next(my_iter), end="\n\n") # imprime el cuarto elemento del iterador
#print(next(my_iter)) # imprime el quinto elemento del iterador, pero no hay mas elementos en el iterador, por lo que arroja un error StopIteration


#Iteradores en cadenas
my_string = "Hello World"
iter_Text = iter(my_string) # convierte la cadena en un iterador, es una estructura de datos que permite recorrer los elementos de un objeto de uno en uno cada vez que se llama a la funcion next()

for element in iter_Text:
    print(element, end=" ") # imprime cada caracter de la cadena my_string
    # en este caso no se usa next() porque el bucle for se encarga de llamar a la funcion next() por nosotros

print("\n\n--------------------\n")

# Iterador numeros inpares
limit = 10
odd_iter = iter(range(1, limit+1, 2)) # crea un iterador de numeros impares del 1 al 10, se suma 2 para imprimir 1, 3, 5, 7, 9, si iniciamos en 0, se imprimiria 0, 2, 4, 6, 8
for element in odd_iter:
    print(element, end=" ") # imprime los numeros impares del 1 al 10
    
# Generadores
def my_generator():
    yield 1 # yield es una palabra clave que se utiliza como return, pero en lugar de devolver un valor, devuelve un generador
    yield 2
    yield 3
    yield 4
    yield 5
    
for value in my_generator():
    print(value, end=" ") # imprime los valores del generador
    
print("\n\n--------------------\n")

# Fibonacci 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55
def fibonacci(limit):
    a, b = 0, 1 # esto es igual a declarar las variables de esta manera a=0 y b=1
    while a < limit:
        yield a
        a, b = b, a+b # esto es igual a declarar las variables de esta manera a=b y b=a+b

for element in fibonacci(11): # se llama a la funcion fibonacci con un limite de 100
    print(element, end=" ") # imprime los numeros de la serie de fibonacci menores a 100