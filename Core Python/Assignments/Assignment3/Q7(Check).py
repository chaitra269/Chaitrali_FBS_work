# write a program to check if user has entered correct userid and password
# start
#  take userid and password from user
userid = input("Enter userid :")
password = input("Enter password :")

# check whether  userid and password is correct 
if(userid == "admin" and password == "chaitra@123"):
    print("Login successfully")
else:
    print("Login failed")