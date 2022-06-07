class employee:

    def __init__(self, name, salary, designation):
        self.name = name
        self.salary = salary
        self.designation = designation

    base_salary = 30000   # this is a class variable

    @classmethod
    def change_base_salary(cls, new_salary):
        cls.base_salary = new_salary

    def printDetails(self):
        print(f"Name: {self.name}, Salary: {self.salary}, Designation: {self.designation}")


shofiq = employee("Shofiqul Islam", 55000, "Managing director")
azad = employee("Mamun Azad", 45000, "Lead Engineer")


shofiq.printDetails()
azad.printDetails()

print("base salary (before)", shofiq.base_salary)  # it will print: base salary (before) 30000

employee.change_base_salary(40000)                 # base salary is 40000 now

print("base salary (after)", shofiq.base_salary)   # it will print: base salary (after) 40000