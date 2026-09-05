# Create a class MedicalStudent inherited from Student with following:
    # i. Data members :Specialization
    # ii. MarksOfInternship
# b. Add the following methods :
    # i. Parameterized constructor
    # ii. Display
    # iii. Accept
    # iv. override Method CalculateRank
    # v. Override __str__ Method

from Q1 import Student
class MedicalStudent(Student):
    def __init__(self, student_id=0, name="", age=0, percentage=0.0, specialization="", marks_of_internship=0):
        super().__init__(student_id, name, age, percentage)
        self.specialization = specialization
        self.marks_of_internship = marks_of_internship

    def accept(self):
        super().accept()
        self.specialization = input("Enter Specialization: ")
        self.marks_of_internship = int(input("Enter Internship Marks: "))

    def calculate_rank(self):
        # Medical rank requires passing internship marks
        if self.marks_of_internship < 50:
            return "Internship Incomplete"
        elif self.percentage >= 80:
            return "Specialist Distinction"
        else:
            return "Medical Practitioner"

    def display(self):
        print(self)

    def __str__(self):
        base_str = super().__str__().split(" | Rank:")[0]
        return f"{base_str} | Specialization: {self.specialization} | Internship Marks: {self.marks_of_internship} | Rank: {self.calculate_rank()}"
m1=MedicalStudent()
print(m1)