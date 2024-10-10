def paresInpares(numbers):
    pares = []
    inpares = []
    for element in range(1,numbers+1):
        result = element % 2
        if result == 0:
            pares.append(element)
        else:
            inpares.append(element)
    yield {"inpares":inpares, "pares":pares} # yield devuelve un generador con los numeros pares e inpares, como iterador, se puede acceder a los elementos con next()
    
def inparesPares(numbers):
    inpares = [element for element in range(1,numbers+1) if element % 2 != 0]
    pares = [element for element in range(1,numbers+1) if element % 2 == 0]
    yield {"inpares":inpares, "pares":pares}


result = inparesPares(10)
result2 = paresInpares(10)
castResult = next(result2) # next() devuelve el siguiente elemento del generador, se debe castear para acceder a los elementos del generador

if result and ("pares" in castResult or "inpares" in castResult):
    if "pares" in castResult:
        print("Numeros pares:", castResult["pares"])
    if "inpares" in castResult:
        print("Numeros inpares:", castResult["inpares"])
else:
    print("No hay numeros pares ni inpares")
