# Create a class Countdown that takes a start number. Implement __iter__() and __next__() to make the object iterable in a for-loop, counting down to 0.


class Countdown:
    def __init__(self, start):
        self.start = start  # Initialize with a start number
        self.current = start  # Set current to start

    # __iter__ method to return the iterator itself
    def __iter__(self):
        return self

    # __next__ method to count down
    def __next__(self):
        if self.current < 0:
            raise StopIteration  # Stop the iteration when it reaches 0
        current_value = self.current
        self.current -= 1  # Decrease the current value
        return current_value

# Create an instance of Countdown starting from 5
countdown = Countdown(5)

# Using the Countdown class in a for-loop
for number in countdown:
    print(number)
