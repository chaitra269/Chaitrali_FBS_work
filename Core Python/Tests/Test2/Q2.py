# Write a program to accept 3 digit number. If first digit is double of second digit and half of
# third digit then display “Yes, you have done it”, otherwise display “Please try next time”.
# Eg : - 428 , 214 etc.

# Program to check digit proportions
num = int(input("Enter a 3-digit number: "))

if 100 <= num <= 999:
    first_digit = num // 100
    second_digit = (num // 10) % 10
    third_digit = num % 10
    
    # Check conditions: 1st is double of 2nd AND 1st is half of 3rd
    if first_digit == (2 * second_digit) and first_digit == (third_digit / 2):
        print("Yes, you have done it")
    else:
        print("Please try next time")
else:
    print("Invalid input! Please enter a valid 3-digit number.")
