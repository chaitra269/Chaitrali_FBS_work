# Python Program to Find the Intersection of Two Lists

l1 = [1, 2, 3, 4, 5]
l2 = [4, 5, 6, 7, 8]

# Using set intersection to find overlapping values
intersection_list = list(set(l1) & set(l2))

print("Intersection of lists:", intersection_list)
