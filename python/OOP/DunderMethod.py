# 🔑 What are Dunder (Magic) Methods?
# Dunder methods = “Double UNDerscore” methods (e.g., __init__, __str__, __len__).
# They are special methods Python uses to perform operator overloading, object representation, and built-in behaviors.
# You don’t usually call them directly → instead, Python calls them automatically.

# ✅ Summary of Useful Dunder Methods
# Dunder Method	Purpose
# __init__	Constructor (object creation)
# __str__	String representation (print(obj))
# __repr__	Developer-friendly object representation
# __len__	Define length (len(obj))
# __add__	Operator overloading (+)
# __eq__	Equality check (==)
# __getitem__	Indexing support (obj[i])
# __setitem__	Assign value by index (obj[i] = x)
# __call__	Make object callable like a function
# __del__	Destructor (called when object is deleted)

# 1. __init__ → Constructor
class Person:
    def __init__(self, name, age):  # runs when object is created
        self.name = name
        self.age = age

p = Person("Satya", 25)
print(p.name, p.age)  # Satya 25

# 2. __str__ → String Representation
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"

b = Book("Python Basics", "Guido")
print(b)   # Python Basics by Guido

# 3. __len__ → Length Support
class Team:
    def __init__(self, members):
        self.members = members

    def __len__(self):
        return len(self.members)

t = Team(["Alice", "Bob", "Charlie"])
print(len(t))   # 3

# 4. __add__ → Operator Overloading
class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __add__(self, other):   # overload + operator
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"({self.x}, {self.y})"

p1 = Point(2, 3)
p2 = Point(4, 1)
print(p1 + p2)   # (6, 4)

# 5. __eq__ → Equality Check
class Student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll

    def __eq__(self, other):  # overload ==
        return self.roll == other.roll

s1 = Student("A", 101)
s2 = Student("B", 101)
print(s1 == s2)  # True (because roll is same)

# 6. __getitem__, __setitem__ → Indexing Support
class MyList:
    def __init__(self, items):
        self.items = items

    def __getitem__(self, index):
        return self.items[index]

    def __setitem__(self, index, value):
        self.items[index] = value

lst = MyList([10, 20, 30])
print(lst[1])     # 20
lst[1] = 50
print(lst[1])     # 50

# 7. __call__ → Making Objects Callable
class Greeter:
    def __init__(self, name):
        self.name = name

    def __call__(self):
        return f"Hello, {self.name}!"

g = Greeter("Satya")
print(g())   # Hello, Satya!



