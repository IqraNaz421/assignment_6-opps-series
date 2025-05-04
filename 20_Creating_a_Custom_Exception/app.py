# Create a custom exception InvalidAgeError. Write a function check_age(age) that raises this exception if age < 18. Handle it with try...except.


# Define a custom exception
class InvalidAgeError(Exception):
    pass

# Function to check age
def check_age(age):
    if age < 18:
        raise InvalidAgeError("Age must be 18 or older.")
    return "Age is valid."

# Handling the exception with try...except
try:
    age = int(input("Enter your age: "))  # Taking age input from the user
    print(check_age(age))
except InvalidAgeError as e:
    print(f"Error: {e}")
except ValueError:
    print("Invalid input. Please enter a valid integer for age.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")