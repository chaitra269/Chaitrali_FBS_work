# write a program to input 5 subjects marks from user and display grade(eg.First class,Second class..) 
# start 
# take marks of 5 subject from user 
m1 = int(input("Enter marks of sub1 :"))
m2 = int(input("Enter marks of sub2 :"))
m3 = int(input("Enter marks of sub3 :"))
m4 = int(input("Enter marks of sub4 :"))
m5 = int(input("Enter marks of sub5 :"))

# calculate total percentage 
percent = (m1+m2+m3+m4+m5)/500 * 100
if(percent >= 75):
    print("First class with distinction : Grade = A+")
elif(percent >= 55):
    print("Second class : Grade = B+")
elif(percent >= 35):
    print("Pass")
else:
    print("Fail")