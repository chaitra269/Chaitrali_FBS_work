# Python Program to Sort a List According to the Length of the Elements
# within the list.

words = ["Elephant", "Cat", "Crocodile", "Dog", "Giraffe"]

# Sort utilizing the length of each string
words.sort(key=len)

print("Sorted by length:", words)
