# Create a class Engine and a class Car. Use composition by passing an Engine object to the Car class during initialization. Access a method of the Engine class via the Car class.


# Define the Engine class
class Engine:
    def __init__(self, engine_type):
        self.engine_type = engine_type
    
    def start_engine(self):
        return f"The {self.engine_type} engine is now running."

# Define the Car class with composition
class Car:
    def __init__(self, make, engine):
        self.make = make
        self.engine = engine  # Composing Engine object inside Car
    
    def start_car(self):
        return f"{self.make} car started. {self.engine.start_engine()}"

# Create an Engine object
engine1 = Engine("V8")

# Create a Car object and pass the Engine object to it
car1 = Car("Mustang", engine1)

# Accessing the method of Engine class via the Car class
print(car1.start_car())
