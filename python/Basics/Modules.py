# Importing a module
import math

print(math.sqrt(16))   # 4.0
print(math.pi)         # 3.141592...

# Importing a specific function
from math import sqrt

print(sqrt(16))   # 4.0

# Importing all functions
from math import *

print(sqrt(16))   # 4.0
print(pi)         # 3.141592

# Aliasing a module
import math as m

print(m.sqrt(16))   # 4.0

# Aliasing a specific function
from math import sqrt as s

print(s(16))   # 4.0

# Aliasing all functions
from math import sqrt as s, pi as p

print(s(16))   # 4.0
print(p)         # 3.141592

# Aliasing a module
import math as m

print(m.sqrt(16))   # 4.0

# Aliasing a specific function
from math import sqrt as s

print(s(16))   # 4.0

# Aliasing all functions
from math import sqrt as s, pi as p

print(s(16))   # 4.0
print(p)         # 3.141592

# Aliasing a module
import math as m

print(m.sqrt(16))   # 4.0

# Aliasing a specific function
from math import sqrt as s

print(s(16))   # 4.0

# Aliasing all functions
from math import sqrt as s, pi as p

print(s(16))   # 4.0
print(p)         # 3.141592

#Create Your Own Module
# 👉 my_module.py
def greet(name):
    return f"Hello, {name}!"

def add(a, b):
    return a + b

# 👉 main.py
import my_module

print(my_module.greet("John"))
print(my_module.add(2, 3))  # 5
