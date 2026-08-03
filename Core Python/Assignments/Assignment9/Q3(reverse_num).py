# WAP to reverse a given number using recursive function 

def reverse(num):
    if num == 0:
        return
    print(num % 10, end="")
    reverse(num // 10)

num = int(input("Enter number: "))
reverse(num)