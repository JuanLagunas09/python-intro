name = input("¿Cuál es tu nombre? ")
age = input("¿Cuántos años tienes? ") # input() regresa un string por defecto
print("¡Vaya! " + name +" luces bastante joven para tener " + age + " años.")
print("-----" * 8, end="\n\n")

# Vamos a sumar dos números
num1 = input("Dame un número: ")
num2 = input("Dame otro número: ")
num3 = float(input("Tercer número: "))

# La función input() regresa un string, por lo que debemos convertirlo a un número
suma = float(num1) + float(num2) + num3
print("La suma de los números es: " + str(suma))