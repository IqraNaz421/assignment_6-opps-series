# Create a class Car with a public variable brand and a public method start(). Instantiate the class and access both from outside the class.


# Define the Car class
class Car:
    # Constructor with a public variable 'brand'
    def __init__(self, brand):
        self.brand = brand  # public variable

    # Public method
    def start(self):
        print(f"{self.brand} is starting...")

# Instantiate the class
my_car = Car("Toyota")

# Access public variable
print("Car Brand:", my_car.brand)

# Access public method
my_car.start()