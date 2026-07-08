# start 
# take marks of 5 subjects from user 
m1 = int(input('Enter first subject :'))
m2 = int(input('Enter second subject :'))
m3 = int(input('Enter third subject :'))
m4 = int(input('Enter fourth subject :'))
m5 = int(input('Enter fifth subject :'))

# Calculate total marks
Total_marks = (m1 + m2 + m3 + m4 + m5)

# Calculate percentage
percent = Total_marks / 500 * 100

# Display result
print(f'The Percentage of Student is {percent}.')
