# WAP to calculate area of Triangle and Rectangle 

# start 
# Take input from user to calculate area of triangle 
base = float(input('enter the base of triangle :'))
height = float(input('enter the height of triangle :'))
Triangle_area = (base * height) / 2

# Take input form user to calculate area of recctangle 
length = float(input('Enter length of rectangle :'))
breadth = float(input('Enter  breadth of rectangle: '))
Rectangle_area = (length * breadth)

print(f' The Area of Trangle is {Triangle_area}. ')
print(f'The Area of Rectangle is {Rectangle_area}.')