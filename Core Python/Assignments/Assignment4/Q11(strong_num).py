# WAP to check strong number 

n = int(input("Enter number : "))
temp = n
sum = 0
while temp>0:
    d=temp%10
    fact=1

    for i in range(1,d+1):
        fact*=i

    sum += fact
    temp //= 10

if sum == n:
    print("The number is strong number.")
else:
    print("The number is not strong number.")