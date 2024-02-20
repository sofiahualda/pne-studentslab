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


