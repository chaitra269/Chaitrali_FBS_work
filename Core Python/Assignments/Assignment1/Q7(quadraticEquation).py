# start 
import math 
# Take three values as input from user 
a = float(input('Enter num1 :'))
b = float(input('Enter num2 :'))
c = float(input('Enter num3 :'))

# calculate discriminant
D = (b ** 2) - (4 * a * c)

# Calculate the root1 and root2
R1 = (- b + math.sqrt(D)) / (2*a)
R2 = (- b - math.sqrt(D)) / (2*a)

# Display result
print(f'the roots of Quadratic equation is {R1}&{R2}.')