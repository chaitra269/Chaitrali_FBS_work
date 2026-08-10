# Write a program to create three lists of numbers, their squares and cubes

# Initial range of numbers 1 through 10
numbers = list(range(1, 11))
squares = [num ** 2 for num in numbers]
cubes = [num ** 3 for num in numbers]

print("Numbers: ", numbers)
print("Squares: ", squares)
print("Cubes:   ", cubes)
