# WAP to calculate Area of Circle
import math
def Area_circle(r):
    return math.pi * (r ** 2)  # pi = 3.14
r = float(input("Enter the radius of circle: "))
area = Area_circle(r)
print(f'Area of circle is {area}.')