# Write a Python program to find all the unique words and count the
# frequency of occurrence from a given list of strings. Use Python set
# data type.

def wordFrequencies(word_list):
    unique_words = set(word_list)

    frequencies = {word: word_list.count(word) for word in unique_words}
    
    return unique_words, frequencies

words = ['Red', 'Green', 'Red', 'Blue', 'Red', 'Red', 'Green', 'Blue', 'Yellow']

unique, counts = wordFrequencies(words)
print("Original List:", words)
print("Unique Words in set:", unique)
print("Word Frequencies:", counts)
