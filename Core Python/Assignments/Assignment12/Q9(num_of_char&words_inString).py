# Python Program to Calculate the Number of Words and the Number of
# Characters Present in a String

str = input("Enter the string : ")
count_word = 1
count_char = 0
for char in str:
    count_char += 1
for i in str:
    if i == ' ':
        count_word +=1

print(f'Total count of words in given string = {count_word}')
print(f'Total count of characters in given string = {count_char}')

