def add(a: float, b: float) -> float:
    return a + b

def substract(a: float, b: float) -> float:
    return a - b

def multiply(a: float, b: float) -> float:
    return a * b

def divide(a: float, b: float) -> float:
    return a / b

def power(a: float, b: float) -> float:
    return a ** b

def root(a: float, b: float) -> float:
    return a ** (1 / b)


def messageOptions():
    print("------ Calculadora ------")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Potencia")
    print("6. Raíz")
    print("7. Salir")
    return int(input("Opción: "))

def calculator():
    while True:
        print("")
        option = messageOptions()
        if option == 7:
            break
        a = float(input("Número 1: "))
        b = float(input("Número 2: "))
        if option == 1:
            print("Resultado: ", add(a, b))
        elif option == 2:
            print("Resultado: ", substract(a, b))
        elif option == 3:
            print("Resultado: ", multiply(a, b))
        elif option == 4:
            print("Resultado: ", divide(a, b))
        elif option == 5:
            print("Resultado: ", power(a, b))
        elif option == 6:
            print("Resultado: ", root(a, b))
        else:
            print("Opción no válida")
            
calculator()


