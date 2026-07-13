# convert the time entered in hh,min and sec in seconds 
# start 
# take input from user 
HH = int(input('Enter Hours:'))
MM = int(input('Enter Minutes:'))
Sec = int(input('Enter Seconds:'))

Total_seconds = (HH * 3600) + (MM * 60) + Sec
print(f'Total seconds = {Total_seconds}')