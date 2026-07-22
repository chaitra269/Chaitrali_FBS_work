""" Accept no. of passengers from user and per ticket cost. then accpet age of each passenger and
then calculate total amount to ticket to travel for all of them basede on following condition :
         a. children below 12 = 30% discount (0.7) 
         b. Senior citizen(above 59) = 50% discount (0.5) 
         c. others need to pay full."""


p_num = int(input("Enter number of passengers :"))
t_cost = float(input("Enter cost per ticket :"))
total_amount = 0

for i in range(1,p_num + 1):
    age = int(input(f"Enter age of passenger {i} :"))
    if age < 12:
        price = t_cost * 0.70
    elif age > 59:
        price = t_cost * 0.50
    else:
        price = t_cost

    total_amount = total_amount + price

print(f"Total amount to pay for all passengers : {total_amount:.2f}")
