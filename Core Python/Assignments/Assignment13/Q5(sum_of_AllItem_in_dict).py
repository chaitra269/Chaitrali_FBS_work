# Python Program to Sum All the Items in a Dictionary 

my_dict = {'item1': 150, 'item2': 250, 'item3': 400}

total_sum = 0

for value in my_dict.values():
    total_sum += value

print(f"The sum of all items is: {total_sum}")

