class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model
    
    def get_brand(self):
        return self.__brand +"!!"
    
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size

my_tesla = ElectricCar("Tesla", "Model S", "120Kwh")

# print(my_tesla.__brand)----> error cause its private
print(my_tesla.get_brand()) #--->o/p==> Tesla!!