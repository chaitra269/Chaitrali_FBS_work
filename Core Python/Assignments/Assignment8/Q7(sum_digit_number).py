# WAP to find sum of digits of a number 
def sum_of_digits(num):
    sum = 0

    while num > 0:
        digit = num % 10
        sum += digit
        num = num // 10

    return sum


num = int(input("Enter a number: "))
res = sum_of_digits(num)
print(f'Sum of digits is {res}.')