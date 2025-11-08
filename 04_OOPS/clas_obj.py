class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def fullName(self):
        return f"{self.brand} {self.model}"
 

my_car = Car("BMW", "S1000")
print(my_car.brand)
print(my_car.model)
print(my_car.fullName())


my_new_car = Car("Tata", "Safari")
print(my_new_car.model)
print(my_new_car.fullName())
