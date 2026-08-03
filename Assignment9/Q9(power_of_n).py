# WAP to calculate the m to the power of n using recursion 

def power(m,n):
    if n == 0:
        return 1
    return m * power(m,n-1)
m = int(input("Enter value of m : "))
n = int(input("Enter value of n : "))
result = power(m,n)
print(f'{m} raised to the power {n}  = {result}.')