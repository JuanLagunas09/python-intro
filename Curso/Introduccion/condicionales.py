x = 7

if x == 10:
    print("x es igual a 10")
else:
    print("x no es igual a 10")
    
# se puede hacer de la siguiente manera con uso de elif
# recordemos identar correctamente el código para ver los resultados dentro de los bloques de código condicionales
if x == 10:
    print("x es igual a 10")
elif x > 10:
    print("x es mayor a 20")
elif x < 10:
    print("x es menor a 10")
else:
    print("x no es igual a 10 ni a 20")
    
# se puede hacer con and y or
if x > 10 and x < 20:
    print("x es mayor a 10 y menor a 20")
elif x > 10 or x < 5:
    print("x es mayor a 10 o menor a 5")
else:
    print("x no es mayor a 10 ni menor a 5")
    
# condicionales con not
if not x == 10:
    print("x no es igual a 10")

# condicionales con booleanos y anidados
is_admin = False
if is_admin:
    print("Es administrador")
    if x == 7:
        print("x es igual a 7")
    else:
        print("x no es igual a 7")
else: 
    print("No es administrador")


# print al nivel de la raiz siempre se ejecuta
print("Fin del programa")