class Vehicle:
    vehicle_type = "none"

class Car:
    price = 1000000

    def horse_powers(self, horse):
        horse = 500
        print(horse)

class Nissan(Vehicle, Car):
    price = 500000
    vehicle_type = "sport car"
    horse = 1000


Skyline = Nissan()

print(Skyline.vehicle_type)
print(Skyline.price)
print(Skyline.horse)