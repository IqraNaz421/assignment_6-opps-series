# Create a class TemperatureConverter with a static method celsius_to_fahrenheit(c) that returns the Fahrenheit value.


class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 9/5) + 32

# Example usage
celsius_value = 25
fahrenheit_value = TemperatureConverter.celsius_to_fahrenheit(celsius_value)

print(f"{celsius_value}°C is equal to {fahrenheit_value}°F")
