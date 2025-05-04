# Write a decorator function log_function_call that prints "Function is being called" before a function executes. Apply it to a function say_hello().


# Decorator function
def log_function_call(func):
    def wrapper():
        print("Function is being called")
        return func()
    return wrapper

# Function to be decorated
@log_function_call
def say_hello():
    print("Hello!")

# Call the decorated function
say_hello()
