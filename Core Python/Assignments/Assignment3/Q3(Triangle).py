# Write a program to input angles of a triangle and check whether triangle is vaild or not 
# start 
angle1 = float(input("Enter first angle of triangle :"))
angle2 = float(input("Enter second angle of triangle :"))
angle3 = float(input("Enter third angle of triangle :"))

# stroe the total sum of all angles into sum variable 
sum = (angle1 + angle2 + angle3)

if(sum == 180 and angle1>0 and angle2>0 and angle3>0):
    print("It is a vaild triangle.")
else:
    print("It is invaild triangle.")
