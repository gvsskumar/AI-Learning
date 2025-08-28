#Basic Class and Object
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def drive(self):
        print(f"The {self.year} {self.make} {self.model} is driving.")  

    def stop(self):
        print(f"The {self.year} {self.make} {self.model} has stopped.")

    def turn(self, direction):
        print(f"The {self.year} {self.make} {self.model} is turning {direction}.")

my_car = Car("Toyota", "Camry", 2022)
my_car.drive()
my_car.stop()
my_car.turn("left")

