# Convert temp from celsius to fahrenhit 
# start 

# take celsius as input from user 
celsius = float(input('Enter tempersture in celsius :'))

# use (c/5 = (F-32)/9) this formula 
fahrenhit = (celsius * 9/5) + 32
print(f'The tempersture in fahrenhit = {fahrenhit}.')