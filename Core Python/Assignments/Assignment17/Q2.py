# Create a derived class from Student as EnggStudent with :
# a. Data members as :
    # i. Branch
    # ii. InternalMarks
# b. Add the following methods :
    # i. Parameterized constructor
    # ii. Display
    # iii. Accept
    # iv. override Method CalculateRank
    # v. Override __str__ Method

from Q1 import Student
class EnggStudent(Student):
    def __init__(self, student_id=0, name="", age=0, percentage=0.0, branch="", internal_marks=0):
        super().__init__(student_id, name, age, percentage)
        self.branch = branch
        self.internal_marks = internal_marks

    def accept(self):
        super().accept()
        self.branch = input("Enter Branch: ")
        self.internal_marks = int(input("Enter Internal Marks: "))

    def calculate_rank(self):
        # Engineering rank considers both percentage and internal marks
        combined_score = (self.percentage * 0.7) + (self.internal_marks * 0.3)
        if combined_score >= 85:
            return "Elite Engineer"
        elif combined_score >= 65:
            return "First Class Engineer"
        else:
            return "Graduate Engineer"

    def display(self):
        print(self)

    def __str__(self):
        base_str = super().__str__().split(" | Rank:")[0]
        return f"{base_str} | Branch: {self.branch} | Internal Marks: {self.internal_marks} | Rank: {self.calculate_rank()}"
e1=EnggStudent()
print(e1)
