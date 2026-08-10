# python program to put even and odd elements of a list into two different lists 

numbers = [12, 7, 5, 64, 23, 44, 91, 18]
even_list = []
odd_list = []

for num in numbers:
    if num % 2 == 0:
        even_list.append(num)
    else:
        odd_list.append(num)

print("Original List:", numbers)
print("Even List:", even_list)
print("Odd List:", odd_list)
