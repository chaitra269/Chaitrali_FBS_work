# Write a program to calculate simple interest based on Principal, Rate and Time
# (SI = P*R*T/100)

p = int(input("Enter principal :"))
r = int(input("Enter Rate of interrest:"))
t = int(input("Enter the time:"))
SI = (p*r*t)/100
print(f"The simple Interest  is {SI}")