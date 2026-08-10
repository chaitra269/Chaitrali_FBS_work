# WAP to print all numbers which are divisible by m and n in the list 

li = [2,4,33,45,90,55,60]
m = int(input("Enter value of m to divide: "))
n = int(input("Enter value of n to divide: "))
for ele in li:
    if (ele % m == 0) and (ele % n == 0):
        print(ele,end=" ")
print()