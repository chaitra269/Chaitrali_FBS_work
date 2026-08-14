# Python Program to count number of digits and letters in a string.

str = input("Enter a string: ")
letter_count = 0
digit_count = 0

for char in str:
    if char.isalpha():
        letter_count += 1
    elif char.isdigit():
        digit_count += 1

print(f"Total Letters: {letter_count}")
print(f"Total Digits: {digit_count}")




