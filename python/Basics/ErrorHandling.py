#In Python, error handling is the process of managing exceptions (unexpected events that can cause a program to stop).
#Instead of the program crashing, you can catch and handle errors using the try-except block.

#🔹 Types of Errors
#SyntaxError: Errors in the code syntax
#Runtime Errors (Exceptions) – Happen during execution.
#NameError: Undefined variables
#ZeroDivisionError: Division by zero
#ValueError: Invalid value passed to a function
#KeyError: Key not found in a dictionary

# 🔹 How to Handle Errors
# try-except → handles errors.
# else → runs if no error occurs.
# finally → always runs (cleanup).
# raise → manually throw errors.
# Custom Exceptions → define your own error types.

# 1. Basic try-except
try:
    num = int("abc")   # invalid conversion
except ValueError:
    print("Error: Cannot convert to integer")

# 2. Catching Multiple Exceptions
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Error: Division by zero")
except ValueError:
    print("Error: Invalid value")

# 3. Catching Multiple Exceptions in One Line
try:
    num = int("xyz")
except (ValueError, TypeError) as e:
    print("Error:", e)

# 4. Using else with try-except
# The else block runs only if no exception occurs.

try:
    num = int("100")
except ValueError:
    print("Conversion failed")
else:
    print("Conversion successful:", num)

# 5. Using finally
# The finally block always runs, whether an error occurs or not.
# Useful for cleanup tasks (like closing files, database connections).

try:
    f = open("test.txt", "w")
    f.write("Hello Python")
except IOError:
    print("File error")
finally:
    f.close()
    print("File closed")    

# 6. Raising Exceptions
# You can raise an exception using the raise keyword.

try:
    age = int(input("Enter your age: "))
    if age < 0:
        raise ValueError("Age cannot be negative")
except ValueError as e:
    print("Error:", e)

# 7. Custom Exception Class
# You can define your own exception types:

class MyCustomError(Exception):
    pass

try:
    raise MyCustomError("Something went wrong!")
except MyCustomError as e:
    print("Caught custom error:", e)