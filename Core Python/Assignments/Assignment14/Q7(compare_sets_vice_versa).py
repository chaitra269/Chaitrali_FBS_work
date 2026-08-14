# Given two sets of numbers, write a Python program to find the missing
# numbers in the second set as compared to the first and vice versa.
# Use the Python set.

def findNum(set1, set2):
    missing_in_set2 = set1 - set2
    missing_in_set1 = set2 - set1
    
    return missing_in_set2, missing_in_set1

set_A = {1, 2, 3, 4, 5}
set_B = {4, 5, 6, 7, 8}

missing_B, missing_A = findNum(set_A, set_B)

print(f"Set A: {set_A}")
print(f"Set B: {set_B}")
print(f"Missing in Set B (compared to A): {missing_B}")
print(f"Missing in Set A (compared to B): {missing_A}")
