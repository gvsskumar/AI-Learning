#Walrus Opertor
#The walrus operator := is a new assignment expression introduced in Python 3.8. It is a combination of the assignment operator (=) and the logical operator (:=).

#Syntax
#variable := expression

#Example
x = 5
print(x)

x := 10
print(x)

#Output
# 5
# 10

#In this example, the walrus operator is used to assign the value 10 to the variable x.

#The walrus operator is often used in conjunction with if statements to assign a value to a variable only if a certain condition is met.

x = 10
print(x)

if x > 5:
    x := 20
    print(x)

#Output
# 10
# 20

#In this example, the walrus operator is used to assign the value 20 to the variable x only if the condition x > 5 is met.

#The walrus operator is often used in conjunction with while loops to assign a value to a variable only if a certain condition is met.

x = 10
print(x)

while x > 5:
    x := 20
    print(x)

#Output
# 10
# 20

#In this example, the walrus operator is used to assign the value 20 to the variable x only if the condition x > 5 is met.

#The walrus operator is often used in conjunction with for loops to assign a value to a variable only if a certain condition is met.

x = 10
print(x)

for i in range(5):
    x := 20
    print(x)

#Output
# 10
# 20
# 20
# 20    
# 20    