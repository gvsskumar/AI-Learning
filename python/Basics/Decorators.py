# Decorators
# Decorators are functions that take another function as an argument and return a new function that wraps the original function
# A decorator is a function that takes another function (or class) as input and adds extra functionality to it without modifying its code.
# 👉 In short: “A function that wraps another function.”
# We use the @decorator_name syntax.

# Example 1: Basic Decorator
def my_decorator(func):
    def wrapper():
        print("Before function runs")
        func()
        print("After function runs")
    return wrapper

@my_decorator   # same as: say_hello = my_decorator(say_hello)
def say_hello():
    print("Hello!")

say_hello()

# Example 2: Decorator with Arguments
def repeat_decorator(func):
    def wrapper(*args, **kwargs):
        print("Running function twice...")
        func(*args, **kwargs)
        func(*args, **kwargs)
    return wrapper

@repeat_decorator
def greet(name):
    print(f"Hello, {name}!")

greet("Satya")

# Example 3: Decorator for Logging
def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with {args}, {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper

@log_decorator
def add(a, b):
    return a + b

add(5, 3)

# Example 4: Decorator with functools.wraps
# 👉 To preserve the original function’s name & docstring.

from functools import wraps

def debug(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Function: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@debug
def square(x):
    """Returns square of a number"""
    return x * x

print(square(5))        # 25
print(square.__name__)  # square (not wrapper)

# xample 5: Decorator with Arguments (Parameterized)
def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)   # Run 3 times
def hello(name):
    print(f"Hello {name}")

hello("Satya")

# Example 6: Multiple Decorators
def bold(func):
    def wrapper():
        return "<b>" + func() + "</b>"
    return wrapper

def italic(func):
    def wrapper():
        return "<i>" + func() + "</i>"
    return wrapper

@bold
@italic
def text():
    return "Python"

print(text())   # <b><i>Python</i></b>

# Example 7: Class Decorators
def decorator_class(func):
    class Wrapper:
        def __init__(self, *args, **kwargs):
            self.result = func(*args, **kwargs)

        def __str__(self):
            return f"Decorated result: {self.result}"
    return Wrapper

@decorator_class
def greet(name):
    return f"Hello {name}"

print(greet("Satya"))   # Decorated result: Hello Satya

# Example 8: Real-World → Authentication Decorator
def require_admin(func):
    def wrapper(user):
        if user != "admin":
            print("Access Denied 🚫")
        else:
            func(user)
    return wrapper

@require_admin
def delete_database(user):
    print("Database deleted ✅")

delete_database("guest")   # Access Denied
delete_database("admin")   # Database deleted

# Decorators are used for:
# Logging & debugging
# Authentication / permission checking
# Measuring execution time
# Modifying outputs (like HTML formatting)
# Retrying / repeating functions