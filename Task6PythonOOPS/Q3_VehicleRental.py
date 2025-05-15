# Base class
class Vehicle:
    def __init__(self, model, basic_rental_rate):
        self.model = model
        self.basic_rental_rate = basic_rental_rate

    def calculate_rental(self, duration_hours):
        return self.basic_rental_rate * duration_hours


# Subclass Car
class Car(Vehicle):
    def __init__(self, model, basic_rental_rate, road_tax):
        super().__init__(model, basic_rental_rate)
        self.road_tax = road_tax

    def calculate_rental(self, duration_hours):
        rent = self.basic_rental_rate * duration_hours + self.road_tax
        return rent


# Subclass Bike
class Bike(Vehicle):
    def __init__(self, model, basic_rental_rate):
        super().__init__(model, basic_rental_rate)

    def calculate_rental(self, duration_hours):
        rent = self.basic_rental_rate * duration_hours
        return rent


# Subclass Truck
class Truck(Vehicle):
    def __init__(self, model, basic_rental_rate, road_tax, maintenance):
        super().__init__(model, basic_rental_rate)
        self.road_tax = road_tax
        self.maintenance = maintenance

    def calculate_rental(self, duration_hours):
        rent = self.basic_rental_rate * duration_hours + self.road_tax + self.maintenance
        return rent


# Polymorphism handled by calling the same method using different class objects
def vehicle_rent(vehicle, duration):
    print(f"Rent of {vehicle.model} is: {vehicle.calculate_rental(duration)}")


# Initializing objects for subclasses
car = Car("Benz", 1000, 2000)
bike = Bike("Honda Unicorn", 300)
truck = Truck("Eicher", 2000, 5000, 2000)

# Call the Vehicle rent method for different objects
vehicle_rent(car, 10)
vehicle_rent(bike, 2)
vehicle_rent(truck, 24)
