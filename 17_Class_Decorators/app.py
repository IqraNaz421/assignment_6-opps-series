# Create a class decorator add_greeting that modifies a class to add a greet() method returning "Hello from Decorator!". Apply it to a class Person.


# Class decorator
def add_greeting(cls):
    def greet(self):
        return "Hello from Decorator!"
    cls.greet = greet
    return cls

# Apply the decorator to the Person class
@add_greeting
class Person:
    def __init__(self, name):
        self.name = name

# Create an instance of Person
person1 = Person("Alice")

# Call the greet method added by the decorator
print(person1.greet())  # Output: Hello from Decorator!
