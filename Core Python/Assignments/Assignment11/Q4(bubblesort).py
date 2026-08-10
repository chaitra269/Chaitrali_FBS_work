# python program to find the second largest number in a list using bubble sort 

nums = [45, 12, 89, 74, 23, 89, 11]

# Bubble Sort implementation
n = len(nums)
for i in range(n):
    for j in range(0, n - i - 1):
        if nums[j] > nums[j + 1]:
            # Swap elements
            nums[j], nums[j + 1] = nums[j + 1], nums[j]

# Handle potential duplicates to find the true second largest
unique_nums = list(set(nums))
unique_nums.sort()

if len(unique_nums) < 2:
    print("List is too short to find a second largest element.")
else:
    print("Sorted List:", nums)
    print("Second Largest Number:", unique_nums[-2])

