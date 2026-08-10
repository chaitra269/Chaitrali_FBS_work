# WAP of having n number of elements in the list and
# find out even and odd elements in that list and
# then create separate lists  ehich will have even element & other will have odd elements

n = int(input("Enter the number of elements(n): "))
li =[]
for i in range(n):
    ele = int(input(f"enter element {i+1}:"))
    li.append(ele)

even_list = []
odd_list = []
count = 0
for ele in li:
    if ele%2==0:
        even_list.append(ele)
        count+=1
    else:
        odd_list.append(ele)
        count+=1
print("Total even elements in list = ",even_list)
print("Total odd elements in list = ",odd_list)
