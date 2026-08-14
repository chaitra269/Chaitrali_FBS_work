# Python Program to count the occurrences of each word in a string.

from collections import Counter

def count_words(text):
    # Convert text to lowercase and split by spaces
    words = text.lower().split()
    
    # Return the frequency mapping
    return Counter(words)

sentence = input("Enter the sentence: ")
word_counts = count_words(sentence)

print(dict(word_counts))
