# 🔑 What is Inheritance?
# Inheritance allows a class (child/derived class) to reuse code from another class (parent/base class).
# It helps with code reusability, extensibility, and maintainability.

# 1. Single Level Inheritance
class Animal:   # Parent class
    def speak(self):
        return "This is an animal sound"

class Dog(Animal):   # Child class
    def speak(self):
        return "Woof! Woof!"

dog = Dog()
print(dog.speak())    # Woof! Woof!


# 2. Multiple Level Inheritance
class Animal:   # Parent class
    def speak(self):
        return "This is an animal sound"

class Dog(Animal):   # Child class
    def speak(self):
        return "Woof! Woof!"

class Poodle(Dog):   # Child class
    def speak(self):
        return "Woof! Woof! Woof!"

poodle = Poodle()
print(poodle.speak())    # Woof! Woof! Woof!


# 3. Multilevel Inheritance
class Animal:   # Parent class
    def speak(self):
        return "This is an animal sound"

class Dog(Animal):   # Child class
    def speak(self):
        return "Woof! Woof!"

class Poodle(Dog):   # Child class
    def speak(self):
        return "Woof! Woof! Woof!"

class GermanShepherd(Poodle):   # Child class
    def speak(self):
        return "Woof! Woof! Woof! Woof!"

german_shepherd = GermanShepherd()
print(german_shepherd.speak())    # Woof! Woof! Woof! Woof!

# Inheritance is a fundamental concept in object-oriented programming (OOP) that allows a new class to inherit properties and methods from an existing class.
# It promotes code reusability, maintainability, and the creation of hierarchical relationships between classes.
# It enables the creation of new classes that are based on existing classes, adding new functionality or modifying existing functionality without modifying the original class.

# 4. Hierarchical Inheritance
# Hierarchical inheritance allows multiple child classes to inherit from a single parent class.
# It promotes code reusability and allows for a more modular and flexible approach to class hierarchy.
class Vehicle:
    def fuel_type(self):
        return "Petrol or Diesel"

class Car(Vehicle):
    def wheels(self):
        return 4

class Bike(Vehicle):
    def wheels(self):
        return 2

car = Car()
bike = Bike()

print(car.fuel_type(), car.wheels())   # Petrol or Diesel 4
print(bike.fuel_type(), bike.wheels()) # Petrol or Diesel 2

# 5. Using super() in Inheritance
# The super() function is a built-in function in Python that allows you to access and call the methods of a parent class from a child class.
# It is used to inherit the attributes and methods of a parent class in a child class.
# Call parent class methods inside child class.
class Person:
    def __init__(self, name):
        self.name = name

    def show(self):
        return f"Name: {self.name}"

class Student(Person):
    def __init__(self, name, roll):
        super().__init__(name)  # call parent constructor
        self.roll = roll

    def show(self):
        return super().show() + f", Roll: {self.roll}"

s1 = Student("Satya", 101)
print(s1.show())  
# Name: Satya, Roll: 101

#✅ Types of Inheritance in Python:
# Single Inheritance
# Multilevel Inheritance
# Multiple Inheritance
# Hierarchical Inheritance
# Hybrid Inheritance (combination of above)

