#Defining & Calling a Function
def my_function():
    print("Hello from a function")  

my_function()


#Defining a Function with Parameters
def my_function(name):
    print("Hello, " + name)

my_function("Surya Kumar")


#Defining a Function with Default Parameters
def my_function(name="Guest"):
    print("Hello, " + name)

my_function("Surya Kumar")
my_function()


#Defining a Function with Keyword Arguments
def my_function(child3, child2, child1):
    print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")


#Passing a List as an Argument
def my_function(food):
    for x in food:
        print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)


#Return Values
def my_function(x):
    return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))


#Arbitrary Arguments, *args
def my_function(*kids):
    print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")


#Arbitrary Keyword Arguments, **kwargs
def my_function(**kid):
    print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")


#Passing a List as an Argument
def my_function(food):
    for x in food:
        print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)


#Lambda Functions
x = lambda a : a + 10
print(x(5))

x = lambda a, b : a * b
print(x(5, 6))

x = lambda a, b, c : a + b + c
print(x(5, 6, 2))

