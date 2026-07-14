# write a program to input electricity unit charges and calculate total electricity bill 
# according to the given condition:
# for first 50 units Rs. 0.50/Unit 
# for next 100 units Rs. 0.75/unit 
# for next 100 units Rs. 1.20/unit 
# for unit above 250 Rs. 1.50/unit 
# an additional surcharge of 20% is added to the bill 

# start 
units = int(input("Enter electricity units : "))

if units <= 50:
    bill = units * 0.50
elif units <= 150:
    bill = (50 * 0.50) + ((units - 50) * 0.75)
elif units <= 250:
    bill = (50 * 0.50) + (100 * 0.75) + ((units - 150) * 1.20)
else:
    bill = (50 * 0.50) + (100 * 0.75) + (100 * 1.20) + ((units - 250) * 1.50)

surcharge = bill * 20 / 100
total_bill = bill + surcharge

print(f"Electricity Bill = Rs.{bill} ")
print(f"Surcharge(20%) = Rs.{surcharge}")
print(f"Total Electricity Bill = Rs.{total_bill}")