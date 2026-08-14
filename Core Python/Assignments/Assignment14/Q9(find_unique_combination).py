# Write a Python program to find all the unique combinations of 3
# numbers from a given list of numbers, adding up to a target number.

def find_triplets(nums, target):
    triplets = []
    n = len(nums)
    
    # Check every possible combination of 3 distinct indices
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                
                # Check if the three numbers add up to the target
                if nums[i] + nums[j] + nums[k] == target:
                    combo = [nums[i], nums[j], nums[k]]
                    
                    # Manual sorting to easily check for duplication
                    for x in range(3):
                        for y in range(x + 1, 3):
                            if combo[x] > combo[y]:
                                combo[x], combo[y] = combo[y], combo[x]
                    
                    # Add to results only if we haven't seen this triplet combination yet
                    if combo not in triplets:
                        triplets.append(combo)
    return triplets

numbers = [1, 2, -1, 0, -2, 2, 3]
target = 2

print(find_triplets(numbers, target))
