
# Create a class Student with attributes name and marks. Use the self keyword to initialize these values via a constructor. Add a method display() that prints student details.  


class Student:
    def __init__(self, name, marks):
        self.name = name        # self se instance variable set kiya
        self.marks = marks

    def display(self):
        print("Student Name:", self.name)
        print("Marks:", self.marks)


student1 = Student("Iqra", 85)
student1.display()

