# Python Program to Count the Number of Vowels in a String


str1 = input("Enter a string: ")

vowels = "aeiouAEIOU"
vowel_count = 0

for char in str1:
    if char in vowels:
        vowel_count += 1

print(f"Total number of vowels: {vowel_count}")

