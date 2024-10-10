class Person: 
    def __init__(self, name, age): # Método constructor
        # Se definen los atributos de la clase
        self.name = name
        self.age = age
    
    def great(self):
        print(f"Hola, mi nombre es {self.name} y tengo {self.age} años")

person_1 = Person("Juan", 25)
person_1.great()

person_2 = Person("Maria", 30)
person_2.great()