# WAP to find sum of digits using recursion 

def sum_of_digits(num):
    if num == 0:
        return 0
    return num % 10 + sum_of_digits(num // 10)

num = int(input("Enter number: "))
res = sum_of_digits(num)
print(f'Sum of digits in {num} number is {res}.')