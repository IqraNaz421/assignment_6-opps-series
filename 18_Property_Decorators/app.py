# Create a class Product with a private attribute _price. Use @property to get the price, @price.setter to update it, and @price.deleter to delete it.


class Product:
    def __init__(self, name, price):
        self.name = name
        self._price = price  # Private attribute
    
    # Property to get the price
    @property
    def price(self):
        return self._price
    
    # Setter to update the price
    @price.setter
    def price(self, value):
        if value >= 0:
            self._price = value
        else:
            print("Price cannot be negative.")
    
    # Deleter to delete the price
    @price.deleter
    def price(self):
        print("Deleting price...")
        del self._price

# Create an instance of Product
product1 = Product("Laptop", 1000)

# Get the price using the @property
print(f"Initial price: {product1.price}")

# Set the price using the @price.setter
product1.price = 1200
print(f"Updated price: {product1.price}")

# Try setting a negative price
product1.price = -500

# Delete the price using the @price.deleter
del product1.price
try:
    print(product1.price)  # This will raise an AttributeError since price has been deleted
except AttributeError as e:
    print("Error:", e)