# Define the Employee class, representing an employee with a name and salary.
class Employee:
    def __init__(self, name, salary):
        # Initialize an Employee with a name and salary, encapsulated as private attributes.
        self.__name = name  # Private attribute for the employee's name
        self.__salary = salary  # Private attribute for the employee's salary

    @property
    def name(self):
        # Getter method for the employee's name.
        return self.__name

    @name.setter
    def name(self, value):
        # Setter method for the employee's name. Validates and sets the name.
        if not value or value.isspace():
            raise ValueError('Empty name! Please enter a name')
        self.__name = value

    @property
    def salary(self):
        # Getter method for the employee's salary.
        return self.__salary

    @salary.setter
    def salary(self, value):
        # Setter method for the employee's salary. Validates and sets the salary.
        if value < 0:
            raise ValueError('Salary has to be a positive number')
        self.__salary = value

    def increase_salary(self, amount):
        # Increase the employee's salary by the specified amount.
        if amount < 0:
            raise ValueError('Amount has to be a positive number')
        self.salary += amount