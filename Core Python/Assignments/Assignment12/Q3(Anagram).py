# Python Program to Detect if Two Strings are Anagrams

def IsAnagram(str1,str2):
    li1 = list(str1)
    li2 = list(str2)
    if len(li1) != len(li2):
        return False

    for char in li1:
        if char in li2:
            li2.remove(char)
        else:
            return False

    return len(li2) == 0
print(IsAnagram("listen", "silent"))
print(IsAnagram('hello','world'))


