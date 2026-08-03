# WAP to find sum of following series using recursive function:
#   a. 1!+2!+3!+4!+.......+n!

def fact(n):
    if n == 0 or n == 1:
        return 1
    return n * fact(n - 1)

def sum_fact(n):
    if n == 1:
        return fact(1)
    return fact(n) + sum_fact(n - 1)

n = int(input("Enter value of n: "))
res = sum_fact(n)
print("Sum =", res)