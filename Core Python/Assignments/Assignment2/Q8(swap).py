# WAP to swap two numbers using third variable 
# start 
# take two numbers from user 
a = int(input("Enter first number :"))
b = int(input("Enter second number :"))

# temp is used to store original value  
temp = a
a = b
b = temp
print(f"After swapping : A = {a} & B = {b}")