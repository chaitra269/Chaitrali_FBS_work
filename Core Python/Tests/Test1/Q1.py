# Write a program to find the area and perimeter of following figure (Accept the
# length, breadth and radius from user:

length = float(input("Enter the length : "))
breadth = float(input("Enter the breadth :"))
radius = float(input("Enter the radius:"))
pi = 3.14

# calculate area & perimeter of rectangle 
rect_area = length * breadth
rect_perimeter = 2 * (length * breadth)

# calculate area & perimeter of circle 
circle_area = pi * (radius**2)
circle_perimeter = 2 * pi * radius

print(f"The area of rectangle is {rect_area:.2f} & perimeter is {rect_perimeter:.2f}")
print(f"The area of circle is {circle_area:.2f} & perimeter is {circle_perimeter:.2f}")