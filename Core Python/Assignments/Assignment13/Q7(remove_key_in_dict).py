# Python Program to Remove the Given Key from a Dictionary 

student_info = {"name": "Alice","age": 21,"major": "Computer Science","graduation_year": 2026}

print("Original Dictionary:", student_info)

removed_value = student_info.pop("graduation_year", None)
print(f"Removed Value: {removed_value}")

print("Updated Dictionary:", student_info)
