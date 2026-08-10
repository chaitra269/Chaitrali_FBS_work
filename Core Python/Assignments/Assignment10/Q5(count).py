# Accept a number from user and check if this element is present in the list 
# or not also tell how many times it is present in the list 

li = [11,2,30,44,44,44,88,90,6]
num = int(input("Enter the number: "))
count = li.count(num)

if count > 0:
    print(f'{num} is present in list {count} times')
else:
    print(f'{num} is not present in list.')
