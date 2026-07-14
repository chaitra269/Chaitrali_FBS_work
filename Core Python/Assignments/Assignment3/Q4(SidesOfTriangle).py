# Write a program to input al sides of a triangle and check whether triangle is vaild or not 
# start 
# take three sides of triangle 
a = int(input("Enter the first side of triangle :"))
b = int(input("Enter the second side of triangle :"))
c = int(input("Enter the third side of triangle :"))

if(a + b > c) and (b + c > a) and (a + c > b):
    print("It is an vaild triangle.")
else:
    print("It is invaild triangle.")