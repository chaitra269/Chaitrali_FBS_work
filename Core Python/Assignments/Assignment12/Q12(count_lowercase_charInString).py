# Python Program to count number of lowercase characters in a string.


def count_lowercase(str):
    
    for char in str:
        if 'a' <= char <= 'z':
            count += 1
            
    return count

input_text = input("Enter the string: ")
result = count_lowercase(input_text)

print(f"Original String: {input_text}")
print(f"Number of lowercase characters: {result}")
