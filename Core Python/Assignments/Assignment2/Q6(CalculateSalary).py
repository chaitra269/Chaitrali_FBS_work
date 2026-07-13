# WAP to calculate total salary of employee based on basic,da=10% of basic, ta=12% of basic, hra=15% of basic 
# start 
# enter salary of employee 
Basic = int(input("Enter the basic salary of employee :"))
da = Basic * 10 / 100 #dearness allowness
ta = Basic * 12 / 100 #Travelling allowness
hra = Basic * 15 /100 #House rent allowness

Total = Basic + da + ta + hra
print(f"DA = {da}, TA = {ta}, HRA = {hra} and Total salary is {Total}.")