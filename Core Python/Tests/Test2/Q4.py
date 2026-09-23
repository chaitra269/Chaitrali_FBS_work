# Write a program to calculate the total cost of painting. The interior of building with four
# equal sized walls.

# Program to calculate wall painting costs
width = float(input("Enter the width of a wall (in meters): "))
height = float(input("Enter the height of a wall (in meters): "))
cost_per_sqm = float(input("Enter the painting cost per square meter (in Rs.): "))

# Calculate area for 4 identical walls
total_area = 4 * (width * height)
total_cost = total_area * cost_per_sqm

print(f"Total Interior Wall Area: {total_area:.2f} sq meters")
print(f"Total Painting Cost: Rs. {total_cost:.2f}")
