# Write a program to print list after removing even numbers.

li = [10, 21, 32, 45, 54, 67, 81, 92]
removed_li = []
for i in li:
    if i % 2!=0:
        removed_li.append(i)
print('Original list = ',li)
print('list after removing even numbers from original list = ',removed_li)
