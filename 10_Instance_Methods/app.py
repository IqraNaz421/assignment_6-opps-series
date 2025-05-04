# Create a class Dog with instance variables name and breed. Add an instance method bark() that prints a message including the dog's name.

class Dog:
    def __init__(self, name, breed):
        self.name = name      # Instance variable
        self.breed = breed    # Instance variable

    def bark(self):
        print(f"{self.name} says: Woof! Woof!")

# Create an instance of Dog
my_dog = Dog("Buddy", "Golden Retriever")

# Call the instance method
my_dog.bark()


