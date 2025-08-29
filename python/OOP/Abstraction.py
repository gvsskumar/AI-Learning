# 🔑 What is Abstraction in Python (OOP)?
# Abstraction means hiding implementation details and only showing the essential features.
# It focuses on what an object does, not how it does it.
# In Python, abstraction is mostly achieved using:
# Abstract Classes (via abc module)
#Interfaces (Python doesn’t have a keyword, but abstract classes act like interfaces).

# 1. Simple Example without abc
#👉 Think of a Car: You just start() or stop(), but don’t worry about how the engine internally works.
class Car:
    def start(self):
        print("Car started")
    
    def stop(self):
        print("Car stopped")

# User only sees high-level methods
my_car = Car()
my_car.start()
my_car.stop()

# 2. Abstraction with Abstract Classes
# We use the abc (Abstract Base Class) module.

from abc import ABC, abstractmethod

class Vehicle(ABC):   # Abstract class
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


# Cannot create object of abstract class
# v = Vehicle()  ❌ Error

car = Car()
bike = Bike()

car.start()   # Car engine started
bike.stop()   # Bike engine stopped

# 3. Abstraction with Interfaces
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

# 3. Real-World Example: Payment System
# 👉 Users just call pay(), they don’t know whether it’s processed by CreditCard or PayPal.

from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


class CreditCardPayment(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using Credit Card")


class PayPalPayment(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using PayPal")


# Client code
payment1 = CreditCardPayment()
payment2 = PayPalPayment()

payment1.pay(1000)   # Paid 1000 using Credit Card
payment2.pay(500)    # Paid 500 using PayPal

