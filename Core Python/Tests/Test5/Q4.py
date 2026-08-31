# There is a list with some numbers. Create a new
# dictionary using this list in such a way that key is
# number and value is frequency of occurrence of that
# number in list.

# [1,3,4,1,2,3,6,7,1,2,4]
# {1:3,3:2,2:2,

numbers = [1, 3, 4, 1, 2, 3, 6, 7, 1, 2, 4]
frequency_dict = {}

for num in numbers:
    frequency_dict[num] = frequency_dict.get(num, 0) + 1

print(frequency_dict)
# Output: {1: 3, 3: 2, 4: 2, 2: 2, 6: 1, 7: 1}
