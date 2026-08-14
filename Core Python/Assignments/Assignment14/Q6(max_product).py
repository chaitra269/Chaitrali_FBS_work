# Write a Python program to find the two numbers whose product is
# maximum among all the pairs in a given list of numbers. Use the
# Python set.

def max(numbers):
    unique_num = list(set(numbers))
    
    max_prod = float('-inf')
    best_pair = None

    for i in range(len(unique_num)):
        for j in range(i + 1, len(unique_num)):
            n1, n2 = unique_num[i], unique_num[j]
            if n1 * n2 > max_prod:
                max_prod = n1 * n2
                best_pair = (n1, n2)
                
    for num in unique_num:
        if numbers.count(num) > 1 and (num * num) > max_prod:
            best_pair = (num, num)

    return best_pair

nums = [1, 10, -3, 9, 10, -10]
print("Best pair:", max(nums))
