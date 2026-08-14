# Write a Python program that finds all pairs of elements in a list whose
# sum is equal to a given value.

def find_pairs(num, sum):
    seen = set()
    pairs = set()

    for num in num:
        ele = sum - num
        
        if ele in seen:
            pair = tuple(sorted((num, ele)))
            pairs.add(pair)
            
        seen.add(num)
        
    return list(pairs)

numbers_list = [2, 4, 3, 5, 7, 8, 1, 3, 2]
target = 6

result = find_pairs(numbers_list, target)
print(f"Pairs that sum up to {target}: {result}")
