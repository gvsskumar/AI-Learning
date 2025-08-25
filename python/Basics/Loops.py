# for loops
# Loop through a list
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)

# while loops
# Loop until a condition is met
i = 1

while i < 6:
    print(i)
    i += 1

# break statement
# Exit the loop if a condition is met
i = 1

while i < 6:
    print(i)
    if i == 3:
        break
    i += 1

# continue statement
# Skip the current iteration if a condition is met
i = 0

while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)

# else statement
# Execute a block of code when the loop is finished
i = 1

while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")

#Loop Control Statements
#break → exit the loop
#continue → skip to next iteration
#pass → do nothing (placeholder)
for i in range(1, 6):
    if i == 3:
        continue   # skip 3
    if i == 5:
        break      # stop loop
    print(i)

#Nested Loops
for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)

#Enumerate
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(index, fruit)

#Zip
fruits = ["apple", "banana", "cherry"]
colors = ["red", "yellow", "green"]
for fruit, color in zip(fruits, colors):
    print(fruit, color)         

#Looping with Dictionaries
person = {"name": "Satya", "age": 25, "city": "Hyderabad"}

for key, value in person.items():
    print(key, ":", value)

#Looping with Sets
fruits = {"apple", "banana", "cherry"}

for fruit in fruits:
    print(fruit)

#Looping with Tuples
fruits = ("apple", "banana", "cherry")

for fruit in fruits:
    print(fruit)    

    