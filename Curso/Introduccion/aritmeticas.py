a = 10
b = 3
print(a + b) # Suma
print(a - b) # Resta
print(a * b) # Multiplicación
print(a / b) # División

print("{:.2f}".format((a / b))) # División con dos decimales {:.2f}
print(a // b) # División entera
print(a % b) # Módulo

print(a ** b) # Potencia
print(12 ** 0.5) # Raíz cuadrada
print(a ** (1/3)) # Raíz cúbica

print(2 + 3 * 5) # Jerarquía de operaciones primero la multiplicación
print((2 + 3) * 5) # Jerarquía de operaciones con paréntesis
print(2 ** 3 ** 2) # Jerarquía de operaciones de derecha a izquierda

print("valor", a) # Concatenación de un string con una variable numérica
print("valor " + str(a)) # Concatenación de un string con una variable numérica

print(a<b) # Menor que 
print(a>b) # Mayor que imprimirá True o False
print(a<=b) # Menor o igual que
print(a==b) # Igual que
print(a!=b) # Diferente que