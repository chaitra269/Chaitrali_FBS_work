# WAP to solve the follwing series:
# a.1! + 2! + 3! + 4! +..........n!
# b.N + N^2 + N^3 +N^4 +..........+ N^N(here  ^ meanss Exponent)
# c.Find the sum of a geometric series from 1 to n where the commom ratio is 2.
# d.S = a +a2 / 2 + a3 /3 +.........+ a10 / 10
# e.x - x2/3 +x3/5 - x4/7 +......... to n terms

#  a.1! + 2! + 3! + 4! +..........n!
n = int(input("Enter n for series a :"))
total_sum = 0
fact = 1
for i in range(1,n+1):
    fact *= i
    total_sum = total_sum + fact
print(f"Sum of series a : {total_sum}")
print()


#  b.N + N^2 + N^3 +N^4 +..........+ N^N(here  ^ meanss Exponent)
N = int(input("Enter  N for series b :"))
total_sum = 0
for i in range(1,N+1):
    total_sum = total_sum + (N ** i)
print(f"Sum of series b : {total_sum}")
print()


#  c.Find the sum of a geometric series from 1 to n where the commom ratio is 2.
n = int(input("Enter number of terms n for geometric series c :"))
total_sum = 0
term = 1
for i in range(n):
    total_sum = total_sum + term
    term *= 2
print(f"Sum of geometric series c : {total_sum}")
print()


# d.S = a +a2 / 2 + a3 /3 +.........+ a10 / 10
a = float(input("Enter value of a for series d :"))
total_sum = 0
for i in range(1,11):
    total_sum = total_sum + (a ** i) / i
print(f"Sum of series d : {total_sum}")
print()



# e.x - x2/3 +x3/5 - x4/7 +......... to n terms
x = float(input("Enter value of x for series e: "))
n = int(input("Enter number of terms n for series e :"))
total_sum = 0
denominator = 1
for i in range(1,n+1):
    term = (x ** i) / denominator
    if i % 2 == 0:
        total_sum = total_sum - term
    else:
        total_sum = total_sum + term
    denominator += 2
print(f"Sum of series e : {total_sum}")
print()