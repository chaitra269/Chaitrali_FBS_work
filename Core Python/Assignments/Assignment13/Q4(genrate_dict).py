# Python Program to Generate a Dictionary that Contains Numbers (between 1
# and n) in the Form (x,x*x). 

n = int(input("Enter a number (n): "))

# Initialize an empty dictionary
square_dict = {}

for i in range(1, n + 1):
    square_dict[i] = i * i

print("Generated Dictionary:", square_dict)
