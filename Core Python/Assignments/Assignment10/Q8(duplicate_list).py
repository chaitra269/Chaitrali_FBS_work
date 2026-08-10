# WAP to create a duplicate of an exisiting list 
# it should not point to same list (Deepcopy)

original_list = [10,20,30,40]
duplicate_list = []
for ele in original_list:
    duplicate_list.append(ele)
duplicate_list[0] = 999
print("Original list(unchanged) : ",original_list)
print("Duplicate list(modified) : ",duplicate_list)