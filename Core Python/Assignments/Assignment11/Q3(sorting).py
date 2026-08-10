# python program to sort the list According to the second element in sublist 
sublists = [[1, 9], [3, 2], [5, 7], [4, 5]]

# Sort using index 1 of each sublist as the key
sorted_sublists = sorted(sublists, key=lambda x: x[1])

print("Sorted by second element:", sorted_sublists)
