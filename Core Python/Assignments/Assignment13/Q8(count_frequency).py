# Python Program to Count the Frequency of Words Appearing in a String Using
# a Dictionary

text = "apple banana apple cherry banana apple"

# Convert text to lowercase and split it into individual words
words = text.lower().split()
frequencies = {}

for word in words:
    # get(word, 0) returns 0 if the word is new, otherwise returns its current count
    frequencies[word] = frequencies.get(word, 0) + 1

print(frequencies)
