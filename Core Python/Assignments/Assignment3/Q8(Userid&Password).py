# Write a program to prompt user to enter userid and password.after verifying userid and password display 
# a 4 digit random number and ask user to enter the same.
# if user enters the same number then show him success message otherwise failed(something like captcha)

# start 
import random
userid = input("Enter the userid :")
password = input("Enter the password :")

if(userid == "admin" and password == "chaitra@123"):
    captcha = random.randint(1000,9999) #random is an built in function which gives random number from series 
    print(f"Your Captcha = {captcha}")
    chuser = int(input("Enter the captcha = "))
    if(chuser == captcha):
        print("User logged in successfully.")
    else:
        print("Invaild captcha.")
else:
    print("User is invaild")