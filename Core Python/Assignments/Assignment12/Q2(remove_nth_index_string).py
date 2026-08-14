# Python Program to Remove the nth Index Character from a Non-Empty
# String

def remove(input_string, n):
    if n < 0 or n >= len(input_string):
        return "Error: Index out of bounds."
    
    return input_string[:n] + input_string[n+1:]
text=input("Enter the string: ")
ind = int(input("Enter the index to remove:"))
result = remove(text, ind)
print(f"Original String: {text}")
print(f"Modified String: {result}")
