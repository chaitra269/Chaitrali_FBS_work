# WAP to find sum of n numbers using recursion 

def sum(n):
    if n >0:
        return n + sum(n-1)
    else:
        return 0
n = int(input("Enter value of n: "))
res = sum(n)
print(f'sum of 1 to {n} numbers is {res}')