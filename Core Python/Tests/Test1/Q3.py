# Write a program to accept distance in km and convert it into meters and
# centimeters both.

km = float(input("Enter the distance in kilometres:"))

# 1 kilometer = 1,000 meters
meters = km * 1000

# 1 kilometer = 100,000 centimeters
centimeters = km * 100000

print(f"{km} km is equivalent to: {meters:.2f} meters and {centimeters:.2f} centimeters .")
