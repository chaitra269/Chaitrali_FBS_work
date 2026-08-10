# WAP to create a new list from existing list which contains cube of each number of list 
li = [1,2,3,4,5]
li2 = []
for i in li:
    num=i**3
    li2.append(num)
print(f'New cube list from exisiting list :{li2} ')