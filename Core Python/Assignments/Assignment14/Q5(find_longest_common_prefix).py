# Write a Python program to find the longest common prefix of all
# strings. Use the Python set.

def longestPrefix(str):
    if not str:
        return ""
    
    min_length = min(len(s) for s in str)
    result = []
    
    for i in range(min_length):
        char_set = set(word[i] for word in str)
        
        if len(char_set) > 1:
            break
            
        result.append(str[0][i]) 
        
    return "".join(result)

str1 = ["flower", "flow", "flight"]
print(f"Strings: {str1}")
res = longestPrefix(str1)
print(f"Longest Common Prefix: '{res}'\n")
