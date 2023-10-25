# Create an Employee
from exerciseFive.employeeManager.employee import Employee
from exerciseFive.employeeManager.manager import Manager

employee_one = Employee("John Doe", 50000)
print(f"Employee: {employee_one.name}, Salary: {employee_one.salary}")

# Attempt to increase the salary by a positive amount
try:
    increased_salary = employee_one.increase_salary(10000)
    print(f"New Salary: {increased_salary}")
except ValueError as e:
    print(f"Error: {e}")

# Attempt to set an empty name
try:
    employee_one.name = ""
except ValueError as e:
    print(f"Error: {e}")

# Create a Manager
manager_one = Manager("Jane Smith", 70000, "HR")
manager_one.increase_salary(5000)
print(f"Manager: {manager_one.name}, Salary: {manager_one.salary}, Department: {manager_one.department_name}")

# Attempt to increase the salary by a negative amount
try:
    manager_one.increase_salary(-5000)
except ValueError as e:
    print(f"Error: {e}")