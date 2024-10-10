# copilot: disable
# Automoviles
class Automobile: 
    def __init__(self, color, model, year, price, brand, stock):
        self.color = color
        self.model = model
        self.year = year
        self.price = price
        self.brand = brand
        self.stock = stock
        
    def print_info(self):
        print(f"Modelo: {self.model}")
        print(f"Marca: {self.brand}")
        print(f"Año: {self.year}")
        print(f"Color: {self.color}")
        print(f"Precio: {self.price}")
        print(f"Stock: {self.stock}")
        
    def sell(self):
        if self.stock > 0:
            self.stock -= 1
            print(f"Automovil {self.model} vendido")
            print(f"Nuevo stock: {self.stock}")
        else:
            print("Automovil no disponible")
            
    def show_stock(self):
        print(f"Stock: {self.stock}")
        
# Usuarios
class User:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id
        self.purchased_cars = []
        
    def purchase_car(self, car):
        if car.stock > 0:
            car.sell()
            self.purchased_cars.append(car)
        else:
            print(f"Automovil {car.model} no disponible")
            
    def show_users_cars(self):
        print(f"Automoviles de {self.name}:")
        for car in self.purchased_cars:
            print("------------------")
            print(f"{car.model} - {car.brand}")

# Consesionaria
class CarDealer:
    def __init__(self):
        self.cars = []
        self.users = []
        
    def add_car(self, car):
        self.cars.append(car)
        print(f"Automovil {car.model} añadido a la concesionaria")
    
    def add_user(self, user):
        self.users.append(user)
        print(f"Usuario {user.name} añadido a la concesionaria")
    
    def show_stock_available(self):
        print("Automoviles disponibles:")
        for car in self.cars:
            if car.stock > 0:
                print(f"{car.model} - {car.brand}")
    
    def show_stock(self):
        print("Automoviles:")
        for car in self.cars:
            print(f"{car.model} - {car.brand} - {'Disponible' if car.stock > 0 else 'No disponible'} - {car.stock}")
            
    def show_users_cars(self):
        print("Automoviles de los usuarios:")
        for user in self.users:
            user.show_users_cars()
            
    def show_car_info(self, car):
        car.print_info()
        
    def sell_car(self, car, user):
        if car.stock > 0:
            user.purchase_car(car)
        else:
            print(f"Automovil {car.model} no disponible")
            
# Se crea la concesionaria
concesionaria = CarDealer()
# Se crean los objetos de la clase Automobile
auto1 = Automobile("Rojo", "Sedan", 2021, 20000, "Toyota", 10)
auto2 = Automobile("Azul", "SUV", 2020, 25000, "Honda", 5)
auto3 = Automobile("Blanco", "Pickup", 2019, 30000, "Ford", 3)
auto4 = Automobile("Rojo", "Deportivo", 2021, 40000, "Ferrari", 1)

# Se añaden los automoviles a la concesionaria
concesionaria.add_car(auto1)
concesionaria.add_car(auto2)
concesionaria.add_car(auto3)
concesionaria.add_car(auto4)

# Se crean los objetos de la clase User
user1 = User("Juan", 1)
user2 = User("Maria", 2)
user3 = User("Pedro", 3)

# Se añaden los usuarios a la concesionaria
concesionaria.add_user(user1)
concesionaria.add_user(user2)
concesionaria.add_user(user3)

# Se muestra el stock de automoviles
print("", end="\n")
print("---------------")
concesionaria.show_stock()
print("", end="\n")
print("---------------")
concesionaria.show_car_info(auto1)
print("", end="\n")
print("---------------")
concesionaria.sell_car(auto1, user1)
concesionaria.sell_car(auto2, user1)
print("", end="\n")
print("---------------")
user1.show_users_cars()
print("", end="\n")
print("---------------")
auto3.show_stock()


            