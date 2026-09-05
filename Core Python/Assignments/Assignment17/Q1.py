# Create a class Student with following
# a. data members :
    # i. StudentId
    # ii. Name
    # iii. Age
    # iv. Percentage
# b. Add the following methods :
    # i. Parameterized constructor
    # ii. Display
    # iii. Accept
    # iv. Method CalculateRank
    # v. Override __str__ Method

class Student:
    def __init__(self, student_id=0, name="", age=0, percentage=0.0):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.percentage = percentage

    def accept(self):
        self.student_id = int(input("Enter Student ID: "))
        self.name = input("Enter Name: ")
        self.age = int(input("Enter Age: "))
        self.percentage = float(input("Enter Percentage: "))

    def calculate_rank(self):
        if self.percentage >= 90:
            return "Rank A"
        elif self.percentage >= 75:
            return "Rank B"
        elif self.percentage >= 50:
            return "Rank C"
        else:
            return "Pass"

    def display(self):
        print(self)

    def __str__(self):
        return f"ID: {self.student_id} | Name: {self.name} | Age: {self.age} | Percentage: {self.percentage}% | Rank: {self.calculate_rank()}"

s1=Student()
print(s1)

