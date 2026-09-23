# 1. Find all of the Numbers from 1–1000 divisible by 8
result = [num for num in range(1, 1001) if num % 8 == 0]
print("All the numbers divisible by 8 = ",result)

# 2. find all of the Numbers from 1–1000 that have a 6 in them
numbers = [num for num in range(1, 1001) if '6' in str(num)]
print("\nAll the numbers that have 6 in them = ",numbers)

# 3. Count the number of spaces in a string
str = input("\nEnter a string: ")
space_count = len([char for char in str if char == ' '])
print("Space count of given string = ",space_count)

# 4. Remove all vowels in a string
user = input("\nEnter a string: ")
no_vowels = "".join([char for char in user if char.lower() not in 'aeiou'])
print(f"removed vowels in {user} is {no_vowels}")

# 5. Find all the words in a string that are less than 5 letters
str1 = input("\nEnter a string: ")
short_words = [word for word in str1.split() if len(word) < 5]
print(f"All the words are less than 5 letters in {str1} are {short_words}")

# 6. use a Dictionary comprehension to count the length of each word in a sentence
sentence = input("\nEnter a sentence: ")
word_lengths = {word: len(word) for word in sentence.split()}
print(f"length of {sentence} sentence is {word_lengths}")

# 7. use a Nested list comprehension to find all of the numbers from 1-1000 that are divisible by any single digit
result1 = [num for num in range(1, 1001) if any([True for divisor in range(2, 10) if num % divisor == 0])]
print(f"\n\nAll the numbers divisible by any single digit from 1-1000 = {result1}")