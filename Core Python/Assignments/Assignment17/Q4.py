# Create a class College which has collection of students. Add the
# following methods :
# a. Parameteried constructor for number of students.
# b. AddStudent
# c. GetStudent
# d. RemoveStudent
# e. Override __str__ Method

from Q1 import Student
class College:
    def __init__(self, max_students):
        self.max_students = max_students
        self.students = []

    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            print(f"Student {student.name} added successfully.")
        else:
            print("College roster is full! Cannot add more students.")

    def get_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                return student
        return None

    def remove_student(self, student_id):
        student = self.get_student(student_id)
        if student:
            self.students.remove(student)
            print(f"Student ID {student_id} removed successfully.")
            return True
        print(f"Student ID {student_id} not found.")
        return False

    def __str__(self):
        if not self.students:
            return "College is currently empty."
        
        roster = f"--- College Roster ({len(self.students)}/{self.max_students} Students) ---\n"
        for student in self.students:
            roster += str(student) + "\n"
        return roster
c1=College(1)
print(c1)