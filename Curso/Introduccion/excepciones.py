try:
    divisor = int(input("Introduce un número divisor: "))
    resultado = 100 / divisor
    print(resultado)
except ZeroDivisionError as e:
    print("Error: No se puede dividir por cero")
    print(e)
except ValueError:
    print("Error: Debes introducir un número mayor a cero")
except Exception as e:
    print(e)
    print("Ha ocurrido un error no previsto", type(e).__name__) # type(e).__name__ returns the name of the exception
    
    
# IMPRIME TODAS LAS EXCEPCIONES QUE SE PUEDEN GENERAR
def print_exception_hierarchy(exception_class, ident=0):
    print(' ' * ident, exception_class.__name__)
    for subclass in exception_class.__subclasses__():
        print_exception_hierarchy(subclass, ident + 4)
        
print_exception_hierarchy(Exception)

while True:
    try: 
        divisor = int(input("Introduce un número divisor: "))
        resultado = 100 / divisor
        print(resultado)
        break
    except ValueError:
        print("Error: Debes introducir un número")
    except ZeroDivisionError:
        print("Error: No se puede dividir por cero")
    except Exception as e:
        print("Error: Ha ocurrido un error no previsto", type(e).__name__)