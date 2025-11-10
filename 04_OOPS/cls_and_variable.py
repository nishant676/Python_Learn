class Car:
    total_car = 0
    
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        Car.total_car+=1

    def full_name(self):
        return f"{self.brand} {self.model}"
    
    def fuel_type(self):
        return "Petrol or disel"
    
    @staticmethod 
    def general_description():
        return "car are means of transport"
    
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand,model )
        self.battery_size = battery_size
    
    def fuel_type(self):
        return "electric charge"

my_tesla = ElectricCar("Tesla", "Model s", "85kwh")

safari = Car("Tata", "Safari")

print(Car.total_car) #--->2
# print(my_tesla.general_description())
print(Car.general_description())




