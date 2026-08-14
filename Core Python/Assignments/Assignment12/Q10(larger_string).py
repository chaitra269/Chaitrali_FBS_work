# Python Program to Take in Two Strings and Display the Larger String
# without Using Built-in Functions

str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")
count1 = 0
count2 = 0

for char in str1:
    count1 += 1

for char in str2:
    count2 += 1

if count1 > count2:
    print(f"The larger string is: {str1}")
elif count2 > count1:
    print(f"The larger string is: {str2}")
else:
    print("\nBoth strings are equal in length.")

