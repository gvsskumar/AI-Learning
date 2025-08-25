#Python Conditionals

#1. if Statement
x = 10
if x > 5:
    print("x is greater than 5")
	
#2. if-else Statement
x = 3
if x > 5:
    print("x is greater than 5")
else:
    print("x is less than or equal to 5")
	
#3. if-elif-else Statement
marks = 75
if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 50:
    print("Grade: C")
else:
    print("Grade: Fail")
	
#4. Nested if
age = 20
country = "India"
if age >= 18:
    if country == "India":
        print("Eligible to vote in India")
		
#5. Logical Operators in Conditionals
#and → both must be True
#or → at least one must be True
#not → negates condition	

x = 7
if x > 5 and x < 10:
    print("x is between 5 and 10")

y = 7	
if y > 6 or y < 10:
    print("y is any one condition match then condition is True")

#6. Ternary Operator (One-line if)
age = 18
status = "Adult" if age >= 18 else "Minor"
print(status)   # Adult	
	
#7. Match-Case (Python 3.10+)
day = 3
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case _:
        print("Invalid day")
