class Car:
    def __init__(self, brand, speed=0):
        self.car_brand = brand
        self.speed = speed

    def set_speed(self, speed):
        self.speed = speed

class Ferrari(Car):
    pass

mycar = Car("Renault")
yourcar = Ferrari("Ferrari")
print(yourcar.car_brand)
yourcar.set_speed(120)
print(yourcar.speed)




#classes3.py


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


#classes.py
class Car:
    def __init__(self, brand, speed = 0):    #how an object is born: init method (to move from class to object)
        self.car_brand = brand          # self is a parameter of all methods, its the object itself
        self.speed = speed

    def set_speed(self, speed):
        self.speed = speed

    def get_brand_nationality(self):
        if self.car_brand == "Renault":
            return "France"
        elif self.car_brand == "Ferrari":
            return "Italy"

    def set_age(self, age):
        self.age = age

    def set_value(self, value):
        self.value = value

mycar = Car("Renault", 30)
mycar.set_speed(80)
print(mycar.speed)

print(mycar.get_brand_nationality())

yourcar = Car("Ferrari")
print(yourcar.speed)