# start 
# Take input from user to calculate Compound Interest
P = int(input('Enter the Principal amount :'))
T = int(input('Enter the Time : '))
R = int(input('Enter the Rate of Interest :'))

# calculate the Amount
Amount = P * (1 + R / 100) ** T

# Calculate the Compound Interest
CI = Amount - P

# Display result
print(f'The Compound Interest is {CI}.')