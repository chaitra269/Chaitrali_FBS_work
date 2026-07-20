# WAP to print fibonacci series upto n

n = int(input("Enter how many fibonacci numbers you want  : "))
a = -1
b = 1
for i in range(n):
    c = a + b 
    print(c)
    a = b
    b = c