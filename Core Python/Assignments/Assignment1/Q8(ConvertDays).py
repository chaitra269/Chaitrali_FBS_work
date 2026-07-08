# start 
# Take input from user to calculate days,years,weeks 
Total_days = int(input('Enter total days :'))

# calculate years
Years = Total_days // 365

# calculate remaining days 
Remaining_days = Total_days % 365

# calculate weeks
weeks = Remaining_days // 7

# calculate days 
Days = Remaining_days % 7

# Display result
print(f'The years ={Years}, Weeks = {weeks}, Days = {Days} of Total Days .')