# Python Program to Check if a Given Key Exists in a Dictionary or Not 

dict_a = {1:'python', 2:1991, 3:'Guido Van Rossum'}
# print(dict_a.get(6,"key not present"))

key = int(input("Enter the key you want to find : "))
if key in dict_a:
    print(f"Success: '{key}' exists! value: {dict_a[key]}")
else:
    print(f"Error: '{key}' does not exist.")