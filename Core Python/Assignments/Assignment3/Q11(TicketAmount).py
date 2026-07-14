# Accept age of five people and also per person ticket amount and then calculate 
# total amount to ticket to travel for all of them based on following condition:
# a. children below 12=30% discount 
# b. senior citizen(above 59)=50% discount 
# c. others need to pay full 

# start 
# first person ticket 
ag1 = int(input("Enter the age of first person ="))
tkprice1 = float(input("Enter the ticket price of first person = "))
totalprice = 0
if ag1<12:
    totalprice=totalprice + (tkprice1*0.30)
elif ag1>59:
    totalprice=totalprice + (tkprice1*0.50)
else:
    totalprice=totalprice + tkprice1

# first person ends here.... 

# second person ticket 
ag2 = int(input("Enter the age of second person ="))
tkprice2 = float(input("Enter the ticket price of second person = "))
totalprice = 0
if ag2<12:
    totalprice=totalprice + (tkprice2*0.30)
elif ag2>59:
    totalprice=totalprice + (tkprice2*0.50)
else:
    totalprice=totalprice + tkprice2

# second person ends here.... 

# third person ticket 
ag3 = int(input("Enter the age of third person ="))
tkprice3 = float(input("Enter the ticket price of third person = "))
totalprice = 0
if ag3<12:
    totalprice=totalprice + (tkprice3*0.30)
elif ag3>59:
    totalprice=totalprice + (tkprice3*0.50)
else:
    totalprice=totalprice + tkprice3

# third person ends here.... 

# fourth person ticket 
ag4 = int(input("Enter the age of fourth person ="))
tkprice4 = float(input("Enter the ticket price of fourth person = "))
totalprice = 0
if ag4<12:
    totalprice=totalprice + (tkprice4*0.30)
elif ag4>59:
    totalprice=totalprice + (tkprice4*0.50)
else:
    totalprice=totalprice + tkprice4

# fourth person ends here.... 

# fifth person ticket 
ag5 = int(input("Enter the age of fifth person ="))
tkprice5 = float(input("Enter the ticket price of fifth person = "))
totalprice = 0
if ag5<12:
    totalprice=totalprice + (tkprice5*0.30)
elif ag5>59:
    totalprice=totalprice + (tkprice5*0.50)
else:
    totalprice=totalprice + tkprice5
print(f"Total price to pay for the trip of five people is {totalprice}.")



