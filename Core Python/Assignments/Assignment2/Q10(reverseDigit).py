# WAP to reverse three digit number 
# take input from user 
num = int(input("Enter three digit number :"))
d1 = num % 10
num = num // 10

d2 = num % 10
num = num // 10

d3 = num % 10
num = num // 10

reverse = d3 + (d2 * 10) + (d1 * 100)
print(f"The reverse number is {reverse}.")