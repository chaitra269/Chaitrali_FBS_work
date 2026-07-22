""" WAP to prompt user to enter userid and password is incorrecct give him chance to re-enter the credentials.
let him try 3 times.after that program to terminate """

username="admin"
password="@12345"

for attempt in range(1,4):
    userid=input("Enter User ID:")
    pass1=input("Enter password:")
    if userid == username and pass1 == password :
        print("Login Successfully.")
        break
    else:
        remaining_attempt = 3 - attempt
        print(f"Incorrect credentials. Remaining Attempts: {remaining_attempt}")
else:
    print("Program terminated too many failed attempts.")