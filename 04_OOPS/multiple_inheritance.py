

class Battery:
    def battery_info(self):
        return "THis is battery"


class Engine:
    def engine_info():
        return "Engine smart"

class ElectricCar(Battery, Engine):
    pass

my_new_tesla = ElectricCar()

print(my_new_tesla.battery_info)
print(my_new_tesla.engine_info)