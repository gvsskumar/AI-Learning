#🔑 What is a Pure Function?
# A Pure Function is a function that:
# Always returns the same output for the same input.
# (No randomness, no dependency on external state.)
# Has no side effects.
# (Does not modify global variables, files, databases, or change inputs.)
# 👉 In short: A pure function is predictable and does not affect the outside world.

#🔑 Why Use Pure Functions?
# Pure functions are easier to test, debug, and reason about.
# They also make the code more reusable and maintainable.

#🔑 How to Write a Pure Function?
# 👉 Always return the same output for the same input.
# 👉 No side effects.
# 👉 No randomness.
# 👉 No dependency on external state
# 👉 No global variables.

# 🚀 Why Pure Functions are Useful?
# ✅ Easier to test & debug (predictable results).
# ✅ Easier to parallelize (no shared state).
# ✅ Encourages functional programming style.
# ✅ Helps in immutability and safer code.

#✅ Example of Pure Function
def add(a, b):
    return a + b

print(add(2, 3))   # 5
print(add(2, 3))   # 5 (always same for same input)

# ✔️ Always gives the same output.
# ✔️ No side effects (does not modify anything outside).

# ❌ Example of Impure Function
total = 0

def add_to_total(x):
    global total
    total += x   # modifies global variable
    return total

print(add_to_total(5))  # 5
print(add_to_total(5))  # 10  (different result for same input)

# ⚠️ Impure because:
# Depends on external variable (total).
# Produces different results for same input.
# Modifies global variable.

# ✅ Another Pure Function Example
def square_list(numbers):
    return [n*n for n in numbers]

print(square_list([1, 2, 3]))  # [1, 4, 9]

# ✔️ No changes to the original list.
# ✔️ Always same output for same input.

# ❌ Another Impure Function Example (Randomness)
import random

def get_random_number(n):
    return random.randint(1, n)

print(get_random_number(5))  # different each time

# ⚠️ Not pure → Output changes even for same input.