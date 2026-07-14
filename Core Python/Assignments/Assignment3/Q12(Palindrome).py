# write a program to check if given 3 digit number is a palindrome or not 
# start 
# take three digit number input from user 
num = int(input("Enter the 3 digit number :"))

d1 = num // 100
d2 = (num // 10) % 10
d3 = num % 10

# store the reverse value into reverse variable 
reverse = (d3 * 100) + (d2 * 10) + d1

if num == reverse:
    print(f"The given number is Palindrome.")
else:
    print("The given number is not Palindrome.")