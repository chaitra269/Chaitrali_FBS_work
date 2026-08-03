# WAP to check if given number is an armstrong number or not using recursive function 

def armstrong(num, power):
    if num == 0:
        return 0
    return (num % 10) ** power + armstrong(num // 10, power)

num = int(input("Enter number: "))
digits = len(str(num))

if armstrong(num, digits) == num:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")