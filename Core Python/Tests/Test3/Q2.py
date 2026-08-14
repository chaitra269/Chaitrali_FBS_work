# Write a program to calculate the sum of following series
# where n is input by user.
# 1/1! + 2/2! + 3/3! + 4/4! + ... N/N!

def calculate_series_sum(n):
    total_sum = 0.0
    factorial = 1
    
    for i in range(1, n + 1):
        factorial *= i
        total_sum += i / factorial
        
    return total_sum

n = int(input("Enter the value of N: "))
if n <= 0:
    print("Please enter a positive integer greater than 0.")
else:
    result = calculate_series_sum(n)
    print(f"The sum of the series up to {n} terms is: {result:.6f}")
