# Python Program to Replace all Occurrences of ‘a’ with $ in a String

def replace_char(input_string):
    modified_string = ""
    
    for char in input_string:
        if char == 'a':
            modified_string += '$'
        else:
            modified_string += char
    return modified_string

user_input = input("Enter a string: ")
result = replace_char(user_input)
print("Modified string:", result)

