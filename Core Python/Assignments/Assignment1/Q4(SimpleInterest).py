# start 
# take input from user to calculate simple interest(P,T,R)
# P(Principal),T(Time),R(Rate)
P = int(input('Enter the Principal amount :'))
T = int(input('Enter the Time :'))
R = int(input('Enter the Rate of Interest :'))

# calculate the simple interest
SI = ( P * T * R ) / 100

# Display result
print(f'The Simple Interest is {SI}.')