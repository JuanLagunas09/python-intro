a = [1,2,3,4,5] # Lista a
b = a # Lista b es igual a la lista a
c = a.copy() # Lista c es una copia de la lista a generando un nuevo objeto en memoria

print(a, b, c, sep="\n", end="\n\n")

del a[0] # Elimina el primer elemento de la lista a
a.append(6) # Ninguna de estas operaciones afecta a la lista c

print(a, b, c, sep="\n", end="\n\n") # La lista b también se ve afectada porque es igual a la lista a

print(id(a), id(b), id(c), end="\n\n") # id() Devuelve la dirección de memoria, en este caso de las listas a y b (son iguales)

#Todo objeto que ocupe memoria en Python tiene un identificador único que se puede obtener con la función id() por lo que si dos objetos tienen el mismo id() significa que son el mismo objeto en memoria y serán afectados por las mismas operaciones. Para evitar esto se puede utilizar el método copy() que genera un nuevo objeto en memoria.