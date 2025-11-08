class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def full_name(self):
        return f"{self.brand} {self.model}"
    
    def fuel_type(self):
        return "Petrol or disel"
    
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand,model )
        self.battery_size = battery_size
    
    def fuel_type(self):
        return "electric charge"

my_tesla = ElectricCar("Tesla", "Model s", "85kwh")
print(my_tesla.fuel_type())

safari = Car("Tata", "Safari")
print(safari.fuel_type())