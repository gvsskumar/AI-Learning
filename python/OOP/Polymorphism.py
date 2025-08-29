# 🔑 What is Polymorphism?
# 👉 Polymorphism means “many forms”.
# In Python OOP, it allows different classes to define methods with the same name but with different implementations.

# 1. Polymorphism with Functions and Objects
# 👉 Polymorphism with functions
# 👉 Polymorphism with objects
class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

def animal_sound(animal):   # generic function
    print(animal.speak())

dog = Dog()
cat = Cat()

animal_sound(dog)   # Woof!
animal_sound(cat)   # Meow!

# 2. Polymorphism with Inheritance
# 👉 Polymorphism with inheritance
class Animal:
    def speak(self):
        return "This is an animal sound"

class Dog(Animal):
    def speak(self):
        return "Woof! Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow! Meow!"

animal = Animal()
dog = Dog()
cat = Cat()

print(animal.speak())   # This is an animal sound
print(dog.speak())      # Woof! Woof!
print(cat.speak())      # Meow! Meow!

# 3. Polymorphism with Abstract Classes
# 👉 Polymorphism with abstract classes
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):
    def start(self):
        print("Car engine started")

    def stop(self):
        print("Car engine stopped")

class Bike(Vehicle):
    def start(self):
        print("Bike engine started")

    def stop(self):
        print("Bike engine stopped")

car = Car()
bike = Bike()

car.start()   # Car engine started
bike.stop()   # Bike engine stopped

# 4. Polymorphism with Interfaces
# Python doesn’t have a keyword, but abstract classes act like interfaces.

from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):
    def start(self):
        print("Car engine started")

    def stop(self):
        print("Car engine stopped")

class Bike(Vehicle):
    def start(self):
        print("Bike engine started")

    def stop(self):
        print("Bike engine stopped")

car = Car()
bike = Bike()

car.start()   # Car engine started
bike.stop()   # Bike engine stopped

# 5. Polymorphism with Generics
# 👉 Polymorphism with generics
from typing import TypeVar, Generic

T = TypeVar("T")

class Vehicle(Generic[T]):
    def __init__(self, name: T):
        self.name = name

    def start(self):
        print(f"{self.name} engine started")

    def stop(self):
        print(f"{self.name} engine stopped")

car = Vehicle("Car")
bike = Vehicle("Bike")

car.start()   # Car engine started
bike.stop()   # Bike engine stopped

# 6. Real-World Example: Payment System
# 👉 Users just call pay(), they don’t know whether it’s processed by CreditCard or PayPal
# or any other payment method
# from abc import ABC, abstractmethod

# class Payment(ABC):
#     @abstractmethod
#     def pay(self, amount):
#         pass

# class PayPalPayment(Payment):
#     def pay(self, amount):
#         print(f"Paid {amount} using PayPal")

# class CreditCardPayment(Payment):
#     def pay(self, amount):
#         print(f"Paid {amount} using Credit Card")

# payment1 = CreditCardPayment()
# payment2 = PayPalPayment()

# payment1.pay(1000)   # Paid 1000 using Credit Card
# payment2.pay(500)    # Paid 500 using PayPal



