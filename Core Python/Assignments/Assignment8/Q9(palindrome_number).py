# WAP to check if entered number is palindrome or not 

def chk_palindrome(num):
    temp = num
    rev = 0
    while temp > 0:
        d = temp % 10
        rev = rev * 10 + d
        temp = temp // 10
    if num == rev:
        print('The given number is palindrome.')
    else:
        print('The given number is not palindrome.')
num = int(input("Enter the number :"))
chk_palindrome(num)
# print(res)