
# Create a class Employee with:

# a public variable name,

# a protected variable _salary, and

# a private variable __ssn.

# Try accessing all three variables from an object of the class and document what happens.

class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name         # Public variable
        self._salary = salary    # Protected variable (convention-based)
        self.__ssn = ssn         # Private variable (name mangled)

# Create an object of the class
emp = Employee("Iqra", 50000, "123-45-6789")

# Accessing the public variable
print("Public - Name:", emp.name)  # ✅ Accessible

# Accessing the protected variable
print("Protected - Salary:", emp._salary)  # ⚠️ Technically accessible, but should be treated as protected

# Accessing the private variable directly (will cause AttributeError)
try:
    print("Private - SSN:", emp.__ssn)  # ❌ Will raise AttributeError
except AttributeError as e:
    print("Private - SSN: Cannot access directly ->", e)

# Accessing private variable using name mangling
print("Private - SSN (accessed with name mangling):", emp._Employee__ssn)  # ✅ Works
