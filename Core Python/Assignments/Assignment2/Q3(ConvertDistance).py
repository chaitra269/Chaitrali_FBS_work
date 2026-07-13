# Convert distance given in feet and inches into meter and centimeter 

# start 
# take distance as input from user 
feet = int(input('Enter Feet :'))
inches = int(input('Enter Inches :'))

# calculate total inches 
Total_inches = (feet * 12) + inches

# calculate feet and inches into meter and centimeter 
centimeter = Total_inches * 2.54 # 1 inch = 2.54 cm
meter = centimeter / 100

print(f'Meter = {meter} and Centimeter = {centimeter}')