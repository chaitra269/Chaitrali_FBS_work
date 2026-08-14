# Python Program to Remove the Characters of Odd Index Values in a
# String


def oddIndex(str):
    result = ""
    index = 0
    
    for char in str:
        if index % 2 == 0:
            result += char
        index += 1
        
    return result
user_string = input("Enter a string: ")
    
modified_string = oddIndex(user_string)
print(f"Original String: {user_string}")
print(f"Modified String: {modified_string}")

