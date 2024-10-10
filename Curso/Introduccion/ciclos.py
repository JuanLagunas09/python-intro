numbers = [1, 2, 3, 4, 5]

#for element in numbers:
#    print("numero: ", element)

#for element in range(0, 10): # range va desde el 0 hasta un numero antes del 10
#    print("numero: ", element)

#for element in range(0, 10, 2): # range va desde el 0 hasta un numero antes del 10, con saltos de 2
#    print("numero: ", element)

#for element in range(9, -1, -1): # range va desde el 9 hasta un numero 0, con saltos de -1
#    print("numero: ", element)

#for element in range(0, len(numbers)): # range va desde el 0 hasta la longitud de la lista numbers
    #print("numero: ", numbers[element], element) # numbers[element] es el valor de la lista en la posicion element, element es el indice de la lista 0, 1, 2, 3, 4
    
#for element in range(3): # range va desde el 0 hasta un numero antes del 3
    #print("numero: ", element) # range va desde el 0 hasta un numero antes del 3
    
fruits = ["apple",  "cherry", "orange", "kiwi", "banana", "melon", "mango"]
for fruit in fruits:
    print(fruit) # imprime cada elemento de la lista fruits
    if fruit == "orange":
        print("Found the orange!")
        continue # salta a la siguiente iteracion y continua con el bucle
    if fruit == "banana":
        print("Found the banana!")
        break # termina el bucle
    
# WHILE
count = 0
while count < 5: # mientras count sea menor a 5
    print(count)
    if count == 3:
        break # termina el bucle cuando count sea igual a 3
    if count == 2:
        print("count is 2")
        count += 1
        continue
    count += 1 # se necesita cumplir la condicion para que el bucle se detenga, si no se incrementa count, el bucle sera infinito