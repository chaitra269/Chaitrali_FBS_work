# write a program to check if person is eligible to marry or not(male age >= 21 and female age >=18)
# start 
# input gender and age from user 
gender = input("Enter gender(m/f) :")
age = int(input("Enter age :"))

# check the marriage criteria 
if(gender == 'm' and age >= 21) or (gender == 'f' and age >= 18):
    print("Eligible for marriage.")
else:
    print("Not eligible for marriage.")