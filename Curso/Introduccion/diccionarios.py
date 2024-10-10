numbers = {
    "one": 1, # key: value
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5
}

invert_numbers = {
    1: "one", # key: value
    2: "two",
    3: "three",
    4: "four",
    5: "five"
}

information_person = {
    "name": "Juan",
    "last_name": "Lagunas",
    "height": 1.75,
    "age": 26,
    "nationality": "Mexican",
}

dictionary_contacts = {
    "juan" : {
        "name": "Juan",
        "last_name": "Lagunas",
        "height": 1.75,
        "age": 26,
        "nationality": "Mexican",
        "phone": 1234567890,
    },
    "pedro" : {
        "name": "Pedro",
        "last_name": "Perez",
        "height": 1.70,
        "age": 30,
        "nationality": "Mexican",
        "phone": 2987654321,
    },
    "ana" : {
        "name": "Ana",
        "last_name": "Gonzalez",
        "height": 1.65,
        "age": 35,
        "nationality": "Mexican",
        "phone": 6789012345,
    },
}

print(numbers, end="\n\n")
print(numbers["one"], end="\n\n")
print(invert_numbers[1], end="\n\n")
print(information_person, end="\n\n")


keys_info_person = information_person.keys() # obtiene las llaves del diccionario
print(keys_info_person, type(keys_info_person), sep="\n", end="\n\n") # type: dict_keys o diccionario de llaves

# print(list(keys_info_person)[0], end="\n\n")
castList_keys_info_person = list(keys_info_person) # convierte las llaves en una lista
print(castList_keys_info_person[0], end="\n\n") # imprime el primer elemento de la lista de llaves

values_info_person = information_person.values() # obtiene los valores del diccionario 
print(values_info_person, type(values_info_person), sep="\n", end="\n\n") # type: dict_values o diccionario de valores

del information_person["nationality"]
print(information_person, end="\n\n")

pairs_info_person = information_person.items() # obtiene los pares de llave-valor del diccionario en tuplas
print(pairs_info_person, type(pairs_info_person), sep="\n", end="\n\n") # type: dict_items o diccionario de tuplas

print(type(dictionary_contacts), end="\n\n") # type: dict o diccionario
print(dictionary_contacts["juan"], end="\n\n")