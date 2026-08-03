# WAP to calculate Area of rectangle 

def Area_rectangle(l,b):
    return l * b 
l = float(input("Enter length of rectangle: "))
b = float(input("Enter breadth of rectangle: "))
area = Area_rectangle(l,b)
print(f'Area of rectangle is {area}')