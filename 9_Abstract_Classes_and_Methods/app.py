# Use the abc module to create an abstract class Shape with an abstract method area(). Inherit a class Rectangle that implements area().


from abc import ABC, abstractmethod

# Abstract base class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

# Concrete class inheriting from Shape
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# Create an instance of Rectangle
rect = Rectangle(5, 10)
print("Area of Rectangle:", rect.area())
