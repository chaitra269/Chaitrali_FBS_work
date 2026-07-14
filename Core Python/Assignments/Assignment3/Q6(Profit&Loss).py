# Write a program to calculate profit and loss 
# start 
# take selling price(profit) and cost price(loss) 
SP = float(input("Enter selling price :"))
CP = float(input("Enter cost price :"))

if(SP > CP):
    print(f"The profit is {SP - CP}.")
elif(CP > SP):
    print(f"The Loss is {CP - SP}.")
else:
    print("No profit No loss.")