class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        print(f"{self.name} say hello!")

class Student(Person):
    def __init__(self, name, age, id_student):
        super().__init__(name, age)
        self.id_student = id_student
    
    def greet(self):
        super().greet()
        print(f"Studend ID {self.id_student}")


student_1 = Student("ana", 20, "s123")
student_1.greet()