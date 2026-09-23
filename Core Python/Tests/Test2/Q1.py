# Write a program to accept year from user and check if it is a leap year or not.

# Program to check if a year is a leap year
year = int(input("Enter a year: "))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
