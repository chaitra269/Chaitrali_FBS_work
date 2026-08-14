# Python Program to Calculate the Length of a String Without Using a
# Library Function

str = input("Enter a string: ")
count = 0

for char in str:
    count += 1

print("The length of the string is:", count)
