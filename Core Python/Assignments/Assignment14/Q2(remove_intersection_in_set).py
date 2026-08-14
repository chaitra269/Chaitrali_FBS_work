# Write a Python program to remove the intersection of a second set
# with a first set.

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print(f"Original Set 1: {set1}")
print(f"Original Set 2: {set2}\n")

new_set = set1.difference(set2)
print(f"New Set : {new_set}")
print(f"Original Set 1 remains unchanged: {set1}")


