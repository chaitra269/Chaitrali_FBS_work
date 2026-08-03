# WAP to find sum of following series function 
# a.1+2+3+4+.....+n 
# b.1!+2!+3!+4!+.....+n! 
# c.1^1+2^2+3^3+......+n^n 

# a.1+2+3+4+.....+n 
def sum_series1(n):
    return sum(range(1,n+1))
n = int(input("Enter the number: "))
sum1 = sum_series1(n)
print(f'Sum of series a is {sum1}.')

print('###################################')


# b.1!+2!+3!+4!+....+n! 
import math
def sum_factorial_series(n):
    return sum(math.factorial(i) for i in range(1, n + 1))

# Example Usage
n = int(input("Enter n: "))
sum2 = sum_factorial_series(n)
print(f"Sum of series B: {sum2}.")

print('####################################')


# c.1^1+2^2+3^3+4^4+......+n^n 
def sum_powerseries(n):
    
        return sum(i ** i for i in range(1,n+1))
n = int(input("Enter the value of n : "))
sum3 = sum_powerseries(n)
print(f'Sum of series c is {sum3}.')
