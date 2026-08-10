# WAP to remove duplicates from list 
li = [1,2,1,8,9,9,4,2]
li2 = []
for ele in li:
   if ele not in li2:
      li2.append(ele)
print(f'original list = {li}')
print(f'List after removing duplicates from list = {li2}')
