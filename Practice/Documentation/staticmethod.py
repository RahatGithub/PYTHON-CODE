# static methods are like regular methods inside a class but these don't take 'self' or 'class' as an additional parameter/argument

class Student:
    min_attendance = 30

    def __init__(self, name, reg):
        self.name = name
        self.reg = reg

    def printDetails(self):
        print(f"name: {self.name}, reg: {self.reg}, min_attendance: {self.min_attendance}")

    @classmethod
    def changeMinAtt(cls, newAtt):
        cls.min_attendance = newAtt

    @staticmethod
    def printTestimonial():
        print("he is one of our brightest students")



class Teacher:
    base_salary = 35000

    def __init__(self, name, designation, salary):
        self.name = name
        self.designation = designation
        self.salary = salary

    def printDetails(self):
        print(
            f"name: {self.name}, designation: {self.designation}, salary: {self.salary}, basic salary: {self.base_salary}")

    @classmethod
    def changeBaseSalary(cls, newSalary):
        cls.base_salary = newSalary

    @staticmethod
    def printTestimonial():
        print("he is one of our best teachers")


omur = Student("kamrul hasan omur", "331516")
nayan = Teacher("nayan kumar", "lecturer", 35000)

# printing the results for @staticmethod
Student.printTestimonial()  # output: 'he is one of our brightest students'
Teacher.printTestimonial()  # output: 'he is one of our best teachers'
