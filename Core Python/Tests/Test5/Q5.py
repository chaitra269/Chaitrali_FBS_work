# Python Program to Find the Union of two Lists without
# using set concept.

def find_union(list1, list2):
    union_list = []
    
    for item in list1:
        if item not in union_list:
            union_list.append(item)
            
    for item in list2:
        if item not in union_list:
            union_list.append(item)
            
    return union_list

list_a = [1, 2, 3, 4, 3]
list_b = [3, 4, 5, 6, 1]

result = find_union(list_a, list_b)
print("Union of lists:", result)
