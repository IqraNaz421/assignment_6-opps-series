# Create four classes:

# A with a method show(),

# B and C that inherit from A and override show(),

# D that inherits from both B and C.

# Create an object of D and call show() to observe MRO.



# Base class A
class A:
    def show(self):
        print("Show method in class A")

# Class B inherits from A and overrides show()
class B(A):
    def show(self):
        print("Show method in class B")

# Class C inherits from A and overrides show()
class C(A):
    def show(self):
        print("Show method in class C")

# Class D inherits from both B and C
class D(B, C):
    pass

# Create an object of class D
obj = D()

# Call show() method on the object
obj.show()
