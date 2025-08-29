# Python Object Introspection allows you to:
# Find an object’s type (type, __class__).
# Inspect attributes & methods (dir, __dict__).
# Get documentation (help).
# Check inheritance (isinstance, issubclass).
# See memory identity (id).

# Common Introspection Functions
# 1. type() → Find object’s type
x = [1, 2, 3]
print(type(x))   # <class 'list'>

y = "Hello"
print(type(y))   # <class 'str'>

# 2. id() → Get memory address (unique identifier)
a = 10
print(id(a))   # e.g., 140715334144016

# 3. dir() → List all attributes & methods
print(dir("AI"))
# ['__add__', '__class__', '__contains__', ..., 'upper', 'zfill']

# 4. help() → Documentation about object
help(str)   # shows all info about string class

# 5. isinstance() → Check if object belongs to a class
print(isinstance(5, int))        # True
print(isinstance("AI", str))     # True
print(isinstance([1,2], list))   # True

# 7. __class__ and __dict__ → Inspect class & attributes
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

car = Car("Honda", "City")

print(car.__class__)     # <class '__main__.Car'>
print(car.__dict__)      # {'brand': 'Honda', 'model': 'City'}

# 8. __doc__ → Documentation about class
print(Car.__doc__)

# 9. __name__ → Class name
print(Car.__name__)

# 10. __module__ → Module name
print(Car.__module__)

# 11. __bases__ → Parent classes
print(Car.__bases__)

# 12. __dict__ → Class attributes
print(Car.__dict__)

# 13. __class__ → Class object
print(Car.__class__)

# 14. __init__ → Constructor
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

car = Car("Honda", "City")

print(car.__class__)     # <class '__main__.Car'>
print(car.__dict__)      # {'brand': 'Honda', 'model': 'City'}

# 15. __main__ → Main module
print(__name__)


