from exerciseFive.employeeManager.employee import Employee


# Define the Manager class, which is a subclass of Employee
class Manager(Employee):
    def __init__(self, name, salary, department_name):
        # Call the constructor of the base class (Employee) to initialize name and salary
        super().__init__(name, salary)
        self.__department_name = department_name  # Additional attribute for the department

    @property
    def department_name(self):
        # Getter method for the department_name attribute
        return self.__department_name