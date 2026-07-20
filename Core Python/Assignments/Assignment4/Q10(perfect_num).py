# WAP to check perfect number 

n = int(input("Enter number: ")) 
sum = 0
for i in range(1,n):
    if n % i == 0:
        sum += i

if sum == n:
    print("The given number is perfect number.")
else:
    print("The given number is not perfect number.")