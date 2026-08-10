# WAP to remove all occurrences of a given elements in list 

li = [10,22,6,6,89,11,66]
print("original list with occurences: ",li)
num = int(input("Enter the element to remove completely: "))
filtered_list = []
for i in li:
    if i != num:
        filtered_list.append(i)

print("List after removing all occurences: ",filtered_list)