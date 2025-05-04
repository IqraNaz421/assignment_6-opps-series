# Create a class Department and a class Employee. Use aggregation by having a Department object store a reference to an Employee object that exists independently of it.


# Define the Employee class
class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def get_employee_info(self):
        return f"Name: {self.name}, Position: {self.position}"

# Define the Department class with aggregation
class Department:
    def __init__(self, department_name, employee):
        self.department_name = department_name
        self.employee = employee  # Aggregation: Department stores reference to Employee
    
    def get_department_info(self):
        return f"Department: {self.department_name}, Employee: {self.employee.get_employee_info()}"

# Create an Employee object
employee1 = Employee("Alice", "Software Engineer")

# Create a Department object, passing the Employee object
department1 = Department("IT", employee1)

# Accessing the employee info through the department
print(department1.get_department_info())
