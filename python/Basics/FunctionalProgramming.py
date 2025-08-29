# Functional Programming
#   Tool	    Purpose 	                Example
# lambda	    Small anonymous function	lambda x: x*2
# map()	        Transform each item	        map(lambda x: x*2, nums)
# filter()	Keep items that match condition	filter(lambda x: x>0, nums)
# reduce()	Reduce list → single value	    reduce(lambda x,y:x+y, nums)
# zip()	    Combine iterables	            zip(names, scores)
# List comprehension	Build list with conditions	[x*x for x in nums if x%2==0]
# Set comprehension	Build unique set	    {x*x for x in nums}
# Dict comprehension	Build dictionary	{x:x*x for x in nums}

# 1. Lambda Functions (Anonymous Functions)
# Small, one-line functions without def.

# Normal function
def square(x): return x*x

# Lambda function
square_lambda = lambda x: x*x

print(square_lambda(5))   # 25

# 2. map() → Apply a function to each element
numbers = [1, 2, 3, 4, 5]

squares = list(map(lambda x: x*x, numbers))
print(squares)   # [1, 4, 9, 16, 25]

# 3. filter() → Filter elements by condition
numbers = [10, 15, 20, 25, 30]

evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)   # [10, 20, 30]

# 4. reduce() (from functools) → Reduce to single value
from functools import reduce

numbers = [1, 2, 3, 4, 5]

product = reduce(lambda x, y: x * y, numbers)
print(product)   # 120

# 5. zip() → Combine iterables
names = ["Alice", "Bob", "Charlie"]
scores = [85, 90, 95]

zipped = list(zip(names, scores))
print(zipped)   # [('Alice', 85), ('Bob', 90), ('Charlie', 95)]

# 6. List Comprehension → Cleaner, shorter syntax
numbers = [1, 2, 3, 4, 5]

squares = [x*x for x in numbers]
print(squares)   # [1, 4, 9, 16, 25]

evens = [x for x in numbers if x % 2 == 0]
print(evens)     # [2, 4]

# 7. Set Comprehension
numbers = [1, 2, 2, 3, 4, 4, 5]

unique_squares = {x*x for x in numbers}
print(unique_squares)   # {1, 4, 9, 16, 25}

# 8. Dictionary Comprehension
numbers = [1, 2, 3, 4, 5]

squares_dict = {x: x*x for x in numbers}
print(squares_dict)   # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Real-World Example (Student Records)
students = ["Alice", "Bob", "Charlie", "David"]
marks = [85, 60, 95, 70]

# Using zip + dict comprehension
student_marks = {name: mark for name, mark in zip(students, marks)}
print(student_marks)  
# {'Alice': 85, 'Bob': 60, 'Charlie': 95, 'David': 70}

# Filter students who passed (>=70)
passed = list(filter(lambda x: x[1] >= 70, student_marks.items()))
print(passed)  
# [('Alice', 85), ('Charlie', 95), ('David', 70)]

# Increase all marks by 5 using map
updated_marks = dict(map(lambda x: (x[0], x[1] + 5), student_marks.items()))
print(updated_marks)  
# {'Alice': 90, 'Bob': 65, 'Charlie': 100, 'David': 75}
