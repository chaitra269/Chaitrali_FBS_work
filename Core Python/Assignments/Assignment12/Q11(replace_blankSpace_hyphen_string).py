# Python Program to replace every blank space with hyphen in a string.

# Method : using built in method replace() 

str = input("Enter the string: ")
modified_str = " "
modified_str=str.replace(' ','-')
    
print('Modified string = ',modified_str)