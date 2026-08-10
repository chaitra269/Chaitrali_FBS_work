# Python Program to Find the Union of two Lists

l1 = [1, 2, 3, 4, 5]
l2 = [4, 5, 6, 7, 8]

# Using set union to combine unique values
union_list = list(set(l1) | set(l2))

print("Union of lists:", union_list)
