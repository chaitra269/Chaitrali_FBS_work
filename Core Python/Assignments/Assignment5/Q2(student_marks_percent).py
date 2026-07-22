""" Enter numbers of students from user for those many students accept marks  of 5 subject marks 
from user and calculate percentage. diaplay all pecentage and average percentage of students."""

num = int(input("Enter total number of student :"))
percentage = []
for i in range(1,num+1):
    print(f"Enter marks for student {i} :")
    total_marks = 0
    for j in range(1,6):
        marks = float(input(f"Enter marks for subject {j} (out of 100) :"))
        total_marks = total_marks + marks

    percent = (total_marks/500)*100
    percentage.append(percent)

print("\n---- Percentage ----")
for idx, pct in enumerate(percentage,1):
    print(f"Student {idx} : {pct:.2f}%")

avg_percent = sum(percentage) / num
print(f"Average Percentage of all students: {avg_percent:.2f}%")