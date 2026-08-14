# Write a Python program to find all the anagrams and group them
# together from a given list of strings.

def group_anagrams(words):
    groups = {}
    
    for word in words:
        count = [0] * 26  
        
        for char in word:
            count[ord(char) - ord('a')] += 1
            
        key = tuple(count)
        
        if key not in groups:
            groups[key] = []
        groups[key].append(word)
        
    return list(groups.values())

input_list = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(group_anagrams(input_list))
