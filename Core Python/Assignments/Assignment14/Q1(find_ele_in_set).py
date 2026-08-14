# Write a Python program to find elements in a given set that are not in
# another set.

set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

print(f"Original Set A: {set_a}")
print(f"Original Set B: {set_b}")

D = set_a.difference(set_b)
print(f"\nElements in A but not in B : {D}")
