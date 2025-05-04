# Create a class Multiplier with an __init__() to set a factor. Define a __call__() method that multiplies an input by the factor. Test it with callable() and by calling the object like a function.



class Multiplier:
    def __init__(self, factor):
        self.factor = factor  # Set the multiplication factor
    
    def __call__(self, value):
        return value * self.factor  # Multiply the input by the factor

# Create an instance of Multiplier with a factor of 3
multiply_by_3 = Multiplier(3)

# Test with callable() function
print(callable(multiply_by_3))  # Output: True

# Call the object like a function
result = multiply_by_3(5)  # Multiply 5 by 3
print(result)  # Output: 15
