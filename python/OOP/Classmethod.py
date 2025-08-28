#🔑 What is @classmethod?
# A class method takes cls as the first argument (instead of self).
# It belongs to the class itself, not a specific object.
# Can be called on the class without creating an object.
# Often used as factory methods (alternative constructors).

#Basic Example
class Student:
    school_name = "ABC School"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def change_school(cls, new_name):
        cls.school_name = new_name

# Accessing class method without object
print(Student.school_name)   # ABC School
Student.change_school("XYZ School")
print(Student.school_name)   # XYZ School

# Accessing class method with object
student1 = Student("Surya", 20)
print(student1.school_name)  # ABC School
student1.change_school("XYZ School")
print(student1.school_name)  # XYZ School

# Accessing class method with class
print(Student.school_name)  # XYZ School
Student.change_school("ABC School")
print(Student.school_name)  # ABC School
