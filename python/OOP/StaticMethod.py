#@Static Method
class Student:
    school_name = "ABC School"

    @staticmethod
    def change_school(new_name):
        Student.school_name = new_name

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"School: {self.school_name}")

student1 = Student("Surya", 20)
student1.display()

Student.change_school("XYZ School")
student1.display()

print(Student.school_name)
