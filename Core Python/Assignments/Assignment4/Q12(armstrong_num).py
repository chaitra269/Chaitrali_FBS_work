# WAP to check given number is armstrong number or not 

n = int(input("Enter Armstrong number you want to check :"))
count = len(str(n))
temp = n
total = 0

while n > 0:
    d = n % 10
    total = total + (d**count)
    n = n // 10
# print(total)

if total == temp:
    print("The given number is Armstrong number.")
else:
    print("The given number is not Armstrong number.")
