# WAP ro print factorial of number 

n = int(input("Enter number of factorial you want : "))
fact = 1
for i in range(1,n+1):
    fact = fact*i
print("Factorial number :",fact)