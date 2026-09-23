# Write a program to
# 1. create a package “SY” which has class SYMARKS (Computer Total,MathsTotal, ElectronicsTotal).
# 2. Create another package “TY” which has a class TYMarks (Theory,Practical).
# 3. Create object of student class (Outside SY & TY package) having roll
# number, name, SYMakrs and TYMarks. Add the marksof SY and TY
# Computer subjects and calculate grade ("A" for >=70, "B" for >=60,
# "C" for >=50, “Pass Class” for >=40 else “Fail”) and display the result
# of the student in proper format.

# project/
# │
# ├── SY/
# │   ├── __init__.py
# │   └── symarks.py
# │
# ├── TY/
# │   ├── __init__.py
# │   └── tymarks.py
# │
# └── main.py


from Project.SY.symarks import SYMARKS
from Project.TY.tymarks import TYMarks

class Student:
    def __init__(self, roll_no, name, sy_marks, ty_marks):
        self.roll_no = roll_no
        self.name = name
        self.sy_marks = sy_marks  # Containment
        self.ty_marks = ty_marks  # Containment

    def display_result(self):
        # Adding SY Computer marks and TY Computer marks (Theory + Practical)
        total_computer_marks = (
            self.sy_marks.computer_total + 
            self.ty_marks.theory + 
            self.ty_marks.practical
        )
        
        # Assuming each of the 3 components is out of 100 (Total = 300)
        percentage = total_computer_marks / 3.0

        # Calculate Grade
        if percentage >= 70:
            grade = "A"
        elif percentage >= 60:
            grade = "B"
        elif percentage >= 50:
            grade = "C"
        elif percentage >= 40:
            grade = "Pass Class"
        else:
            grade = "Fail"

        # Format and display the result
        print("-" * 40)
        print(f"{'STUDENT RESULT':^40}")
        print("-" * 40)
        print(f"Roll Number     : {self.roll_no}")
        print(f"Student Name    : {self.name}")
        print(f"SY Computer     : {self.sy_marks.computer_total}")
        print(f"TY Theory       : {self.ty_marks.theory}")
        print(f"TY Practical    : {self.ty_marks.practical}")
        print(f"Total Comp Marks: {total_computer_marks}/300")
        print(f"Percentage      : {percentage:.2f}%")
        print(f"Grade           : {grade}")
        print("-" * 40)

# Execution block
if __name__ == "__main__":
    # Creating SYMARKS and TYMarks objects
    sy = SYMARKS(75, 80, 65)
    ty = TYMarks(70, 85)

    # Creating Student object containing SY and TY objects
    student = Student(101, "Rahul Sharma", sy, ty)

    # Displaying result
    student.display_result()
