# Python Program to Take in a String and Replace Every Blank Space
# with Hyphen

def replace(str):
    modified_string = ""
    
    for char in str:
        if char == ' ':
            modified_string += '-'
        else:
            modified_string += char
    return modified_string

user_input = input("Enter a string: ")
result = replace(user_input)

print("Modified string:", result)