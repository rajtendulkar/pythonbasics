# Demonstration of Object-Oriented Programming in Python using Vehicle class

# Class Definition
class Vehicle:
    def __init__(self, manufacturer, model, year):
        self.manufacturer = manufacturer  # Public attribute
        self.model = model  # Public attribute
        self.year = year  # Public attribute

    # Method to display vehicle information
    def display_info(self):
        return f"Year : {self.year} Manufacturer: {self.manufacturer} Model:{self.model}"

    # Abstract method to be implemented by subclasses
    def start_engine(self):
        raise NotImplementedError("Subclass must implement abstract method")


class Bicycle(Vehicle):
    def __init__(self, manufacturer, model, year):
        super().__init__(manufacturer, model, year)  # Call the parent class constructor

    # Overriding the start_engine method
    def start_engine(self):
        raise NotImplementedError("I don't have an engine")


# Inheritance: Car class inherits from Vehicle
class Car(Vehicle):
    def __init__(self, manufacturer, model, year, doors):
        super().__init__(manufacturer, model, year)  # Call the parent class constructor
        self.__doors = doors  # Private attribute

    # Method to get the number of doors
    def get_doors(self):
        return self.__doors

    # Overriding the start_engine method
    def start_engine(self):
        return "Car engine running."


# Inheritance: Motorcycle class inherits from Vehicle
class Motorcycle(Vehicle):
    def __init__(self, manufacturer, model, year, cc):
        super().__init__(manufacturer, model, year)  # Call the parent class constructor
        self.cc = cc  # Public attribute

    # Overriding the start_engine method
    def start_engine(self):
        return "Motorcycle engine running."


# Polymorphism: Function that can start the engine of any vehicle
def start_vehicle_engine(vehicle):
    print(f"{vehicle.display_info()} - {vehicle.start_engine()}")


if __name__ == "__main__":
    # Creating instances of Car and Motorcycle
    car = Car("BMW", "318D", 2024, 4)
    motorcycle = Motorcycle("Yamaha", "GTX100", 2019, 100)
    bicycle = Bicycle("Vitus", "City Bike", 2021)

    # Accessing attributes and methods
    print(f"Car info: {car.display_info()}")
    print(f"Car doors: {car.get_doors()}")
    print(f"Motorcycle info: {motorcycle.display_info()}")
    print(f"Motorcycle cc: {motorcycle.cc}")
    print(f"Bicycle info: {bicycle.display_info()}")

    # Demonstrating polymorphism
    start_vehicle_engine(car)
    start_vehicle_engine(motorcycle)

    # should generate an exception
    start_vehicle_engine(bicycle)
