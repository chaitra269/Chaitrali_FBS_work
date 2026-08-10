# WAP to find second largest element in a list 

li = [2,55,22,80,95,7]
max = li[0]
second_largest_ele = li[0]
for num in range(1,len(li)):
    if(li[num] > max):
        second_largest_ele=max
        max = li[num]
    elif(li[num] > second_largest_ele and li[num]!=max):
        second_largest_ele = li[num]

print(f"The second largest element in list is {second_largest_ele}")