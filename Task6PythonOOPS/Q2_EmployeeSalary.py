# Parent class Employee
class Employee:
    def __init__(self, name, basic_salary):
        self.name = name
        self.basic_salary = basic_salary

    # Method uses polymorphism
    def calculate_salary(self):
        return self.basic_salary


# Subclass RegularEmployee
class RegularEmployee(Employee):
    def __init__(self, name, basic_salary, allowance_percentage, miscellaneous):
        super().__init__(name, basic_salary)
        self.allowance_percentage = allowance_percentage
        self.miscellaneous = miscellaneous

    # Method overrides the base class method
    # Salary of regular employee calculated using base and subclass attributes
    def calculate_salary(self):
        salary = self.basic_salary + (self.allowance_percentage * self.basic_salary) / 100 + self.miscellaneous
        return salary


# Subclass ContractEmployee
class ContractEmployee(Employee):
    def __init__(self, name, basic_salary, allowance_percentage):
        super().__init__(name, basic_salary)
        self.allowance_percentage = allowance_percentage

    # Method overrides the base class method
    # Salary of contract employee calculated using base and subclass attributes
    def calculate_salary(self):
        salary = self.basic_salary + (self.allowance_percentage * self.basic_salary) / 100
        return salary


# Subclass Manager
class Manager(Employee):
    def __init__(self, name, basic_salary, allowance_percentage, miscellaneous, performance_pay):
        super().__init__(name, basic_salary)
        self.allowance_percentage = allowance_percentage
        self.miscellaneous = miscellaneous
        self.performance_pay = performance_pay

    # Method overrides the base class method
    # Salary of MANAGER is calculated using base and subclass attributes
    def calculate_salary(self):
        salary = (self.basic_salary + (
                    self.allowance_percentage * self.basic_salary) / 100 + self.miscellaneous + self.performance_pay)
        return salary


# Calling calculate_area method using objects of different subclasses
def employee_salary(employee):
    print(f"Salary of {employee.name} is: {employee.calculate_salary()}")


# initializing objects for each subclass
regular_employee = RegularEmployee("Arun", 10000, 5, 5000)
contract_employee = ContractEmployee("Babu", 8000, 5)
manager = Manager("Kavi", 15000, 10, 5000, 10000)

# Printing the salary of each employee type.
employee_salary(regular_employee)
employee_salary(contract_employee)
employee_salary(manager)
