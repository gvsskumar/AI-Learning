#🔑 What is Encapsulation?
# Encapsulation = Binding data (variables) + methods (functions) together inside a class.
# It helps in data hiding and controlling access.
# In Python, we don’t have strict private like Java/C++, but we use naming conventions:
# Public (normal) → accessible everywhere
# Protected (_var) → should not be accessed directly outside the class
# Private (__var) → name mangled, not easily accessible outside

# 1. Public Members (default)
class Car:
    def __init__(self, brand, model):
        self.brand = brand      # public
        self.model = model      # public

    def display(self):
        print(f"{self.brand} {self.model}")

car1 = Car("Honda", "City")
print(car1.brand)     # Accessible → Honda
car1.display()        # Honda City

# 2. Protected Members (_single_underscore)
class Student:
    def __init__(self, name, age):
        self._name = name     # protected
        self._age = age       # protected

    def show(self):
        print(f"Name: {self._name}, Age: {self._age}")

class GraduateStudent(Student):
    def display(self):
        print("Accessing protected member inside subclass:", self._name)

s1 = GraduateStudent("Satya", 22)
s1.show()             # OK
s1.display()          # OK
print(s1._name)       # ⚠️ Technically possible, but not recommended

# 3. Private Members (__double_underscore)
class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.__balance = balance   # private

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds")

    def get_balance(self):
        return self.__balance

acc = BankAccount("Kumar", 1000)
acc.deposit(500)
print(acc.get_balance())   # ✅ Safe → 1500

# print(acc.__balance)     # ❌ Error: Attribute not accessible
print(acc._BankAccount__balance)  # ⚠️ Trick: Name mangling allows access → 1500

#4. Encapsulation with Getters & Setters
# 👉 Best practice: use methods to control access to private data.

class Employee:
    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary

    # Getter
    def get_salary(self):
        return self.__salary

    # Setter
    def set_salary(self, new_salary):
        if new_salary > 0:
            self.__salary = new_salary
        else:
            print("Invalid salary")

emp = Employee("Satya", 50000)
print(emp.get_salary())   # 50000
emp.set_salary(60000)
print(emp.get_salary())   # 60000
emp.set_salary(-1000)     # Invalid salary

