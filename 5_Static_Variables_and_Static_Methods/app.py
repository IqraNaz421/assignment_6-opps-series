# Create a class MathUtils with a static method add(a, b) that returns the sum. No class or instance variables should be used. 

class MathUtils:
    # Static method for addition
    @staticmethod
    def add(a, b):
        return a + b

# Use the static method without creating an instance
result = MathUtils.add(5, 7)

print("Sum:", result)
