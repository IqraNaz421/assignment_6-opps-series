# Create a class Person with a constructor that sets the name. Inherit a class Teacher from it, add a subject field, and use super() to call the base class constructor.

# Base class
class Person:
    def __init__(self, name):
        self.name = name
        print(f"Person created with name: {self.name}")

# Derived class
class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)  # Call the base class constructor
        self.subject = subject
        print(f"Teacher teaches subject: {self.subject}")

# Create an object of Teacher
teacher1 = Teacher("Mrs. Ahmed", "Mathematics")
