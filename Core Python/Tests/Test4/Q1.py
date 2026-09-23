# 1. Write a function to which we pass a parameter and
# print the factors of a given number
# For Eg: Factors of 12 : 1,2,3,4,6,12

def print_factors(number):
    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(str(i))
    
    print(f"Factors of {number} : {', '.join(factors)}")

# Example usage:
print_factors(12)
