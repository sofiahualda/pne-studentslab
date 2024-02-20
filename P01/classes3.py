class Vehicle:
    def set_speef(slef, speed):
        self.speed = speed

class Car(Vehicle):
    def __init__(self, bran, speed=0):
        self.car_brand = brand
        self.speed = speed

class Ferrari(Car):
    def __init__(self):
        self.music = "classic"
    def make_cabrio(self):
        self.speed = 20
        self.music = "loud"
        return "Wow"

mycar = Car("Renault")
yourcar = Ferrari("Ferrari" )  # --> __init__
print(yourcar.car_brand)
yourcar.set_speed(20)
print(yourcar.speed)

print(yourcar.make_carbio(), "and music is", yourcar)



