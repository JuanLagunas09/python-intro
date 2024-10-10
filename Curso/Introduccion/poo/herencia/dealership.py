# Clase Vehiculo (padre)
class Vehicle:
    def __init__(self, brand, model, price):
        # Encapsulacion son los datos privados del objeto
        self.brand = brand
        self.model = model
        self.price = price
        self.is_available = True
    
    def sell(self):
        if self.is_available:
            self.is_available = False
            print(f"Vehiculo {self.brand} vendido")
        else:
            print("Vehiculo no disponible")
    
    # Abstraccion es la forma de acceder a la infomación privada de la clase
    def get_available(self):
        return self.is_available
    
    def get_price(self):
        return self.price

    # Polimorfismo
    def start_engine(self):
        raise NotImplementedError("Metodo start debe ser implementado por la subclase")
    
    def stop_engine(self):
        raise NotImplementedError("Metodo stop debe ser implementado por la subclase")

# Herencia
# Clase coche (hija)
class Car(Vehicle):
    # Polimorfismo
    def start_engine(self):
        if not self.is_available:
            return f"El motor del coche {self.brand} en marcha"
        else: 
            return f"El motor del coche {self.brand} no disponible"
        
    def stop_engine(self):
        if self.is_available:
            return f"El motor del coche {self.brand} detenido"
        else: 
            return f"El motor del coche {self.brand} no disponible"

# Clase bicicleta (hija)
class Bike(Vehicle):
    def start_engine(self):
        if not self.is_available:
            return f"La dadena de la bicicleta {self.brand} en marcha"
        else: 
            return f"La dadena de la bicicleta {self.brand} no disponible"
        
    def stop_engine(self):
        if self.is_available:
            return f"La dadena de la bicicleta {self.brand} detenida"
        else: 
            return f"La dadena de la bicicleta {self.brand} no disponible"

# Clase camión (hija)
class Truck(Vehicle):
    def start_engine(self):
        if not self.is_available:
            return f"El motor del camión {self.brand} en marcha"
        else: 
            return f"El motor del camión {self.brand} no disponible"
        
    def stop_engine(self):
        if self.is_available:
            return f"El motor del camión {self.brand} detenido"
        else: 
            return f"El motor del camión {self.brand} no disponible"
        
class Customer:
    def __init__(self,name):
        self.name = name
        self.purchased_vehicles = []
    
    def buy_vehicle(self, vehicle: Vehicle):
        if vehicle.get_available():
            vehicle.sell()
            self.purchased_vehicles.append(vehicle)
        else: 
            print(f"Vehiculo {vehicle.brand} no disponible")
    
    def inquire_vehicle(self, vehicle: Vehicle):
        if vehicle.get_available():
            availability = "Disponible"
        else:
            availability = "No disponible"
        print(f"El vehiculo {vehicle.brand} es {availability} y cuesta {vehicle.get_price()}")
        
class Dealership:
    def __init__(self):
        self.inventory = []
        self.customers = []
    
    def add_vehicles(self, vehicle: Vehicle):
        self.inventory.append(vehicle)
        print(f"Vehiculo {vehicle.brand} agregado")
    
    def add_customer(self, customer: Customer):
        self.customers.append(customer)
        print(f"Cleinte {customer.name} agregado")
    
    def show_available_vehicles(self):
        print("Vehiculos diponbles en tienda:")
        for element in self.inventory:
            if element.get_available():
                print(f"{element.brand} - {element.get_price()}")
        
car_1 = Car("Toyota", "Corolla", 2000)
bike_1 = Bike("Yamaha", "MT-07", 7000)
truck_1 = Truck("Volvo", "FH16", 80000)

customer_1 = Customer("Carlos")
dealership = Dealership()

dealership.add_vehicles(car_1)
dealership.add_vehicles(bike_1)
dealership.add_vehicles(truck_1)

# Mostrar vehiculos disponibles
dealership.show_available_vehicles()

# Cliente consulta vehiculo
customer_1.inquire_vehicle(car_1)
# Cleinte compra vehiculo
customer_1.buy_vehicle(car_1)
# Mostrar vehiculos disponibles
dealership.show_available_vehicles()