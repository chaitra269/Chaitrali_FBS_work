# WAP to check if a given number is Armstrong number or not. 
# for each task create separate functions 

def is_armstrong(num):
    temp = num
    count = len(str(temp))
    total = 0

    while temp > 0:
        digit = temp % 10
        total += digit ** count
        temp = temp // 10

    return total == num


# Main Program
num = int(input("Enter a number: "))

if is_armstrong(num):
    print(num, "is an Armstrong Number")
else:
    print(num, "is Not an Armstrong Number")