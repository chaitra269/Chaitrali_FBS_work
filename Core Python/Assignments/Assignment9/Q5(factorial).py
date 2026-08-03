# WAP to find factorial using recursion 

def factorial(num):
    if num == 0 or num == 1:
        return 1
    return num * factorial(num-1)
num = int(input("Enter value of num : "))
res = factorial(num)
print(f'Factorial of {num} is {res}.')