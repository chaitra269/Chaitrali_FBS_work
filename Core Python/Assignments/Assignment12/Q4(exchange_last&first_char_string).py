# Python Program to Form a New String where the First Character and
# the Last Character have been Exchanged

def exchange(str1):
    if len(str1) <= 1:
        return str1
    
    return str1[-1] + str1[1:-1] + str1[0]

user_input = input("Enter a string: ")
result = exchange(user_input)

print("Original String:", user_input)
print("Modified String:", result)


