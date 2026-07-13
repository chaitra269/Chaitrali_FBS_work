# WAP to swap two numbers without using third variable 
# start 
a = int(input("Enter first number :"))
b = int(input("Enter second number :"))
a = a + b
b = a - b
a = a - b
print(f"After Swapping : A = {a}, B = {b}")