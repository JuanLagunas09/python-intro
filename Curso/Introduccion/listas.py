to_do_list = [
    "Dirigirnos al hotel",
    "Hacer el check-in",
    "Ir a almorzar",
    "Visitar el museo",
    "Descansar",
    [
        "Cenar",
        "Dormir"
    ], # Una lista dentro de otra lista
    "Desayunar",
    "Hacer el check-out",
]
numbers_list = [1, 2, 3, 4, 6]
mixed_list = [1, "Hello", 3.4, True] # Las listas pueden contener cualquier tipo de dato y son de tipo list

print(to_do_list, numbers_list, mixed_list, sep="\n")
print(len(to_do_list), len(numbers_list), len(mixed_list))
print(to_do_list[0], numbers_list[1], mixed_list[-2])

# Slicing, imprime un rango de elementos de la lista :3 significa desde el inicio hasta el índice 3 (sin incluirlo)
# 1: significa desde el índice 1 hasta el final -1 significa el penúltimo elemento 
print (to_do_list[1:3], numbers_list[:3], mixed_list[1:-1], sep="\n", end="\n\n")

to_do_list.append("Dirigirnos al aeropuerto") # Agrega un elemento al final de la lista
print(to_do_list, end="\n\n")

numbers_list.insert(4, 5) # Agrega un elemento en la posición 4 (posición, valor)
print(numbers_list, end="\n\n")

print(mixed_list.index("Hello"), end="\n\n") # Devuelve el índice del elemento buscado

print(max(numbers_list), min(numbers_list), end="\n\n") # Devuelve el valor máximo y mínimo de la lista

numbers_list.pop() # Elimina el último elemento de la lista
print(numbers_list, end="\n\n")

mixed_list.remove("Hello") # Elimina el elemento buscado
mixed_list.pop(0) # Elimina el elemento en la posición 1
print(mixed_list, end="\n\n")

del to_do_list[0] # Elimina el elemento en la posición 0
print(to_do_list, end="\n\n")

del to_do_list[:3] # Elimina los elementos en el rango de posiciones 1 a 3
print(to_do_list, end="\n\n")

to_do_list.clear() # Elimina todos los elementos de la lista
print(to_do_list, end="\n\n")

#del to_do_list # Elimina la lista
#print(to_do_list, end="\n\n") # Genera un error porque la lista ya no existe

print(type(to_do_list), type(numbers_list), type(mixed_list), end="\n\n") # Devuelve el tipo de dato de la lista

