# WAP to print first n  prime numbers 

n = int(input("Enter the number of prime numbers to print(n) : "))
count = 0
num = 2
print(f"The first {n} prime numbers are :")
while count < n:
    
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
           
            break
    else:
        print(num, end=' ')
        count += 1
    num += 1
print()