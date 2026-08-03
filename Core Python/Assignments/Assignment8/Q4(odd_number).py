# sum of all odd numbers between 1 to n 
def sum_odd_number(n):
    return sum((i) for i in range(1,n+1) if i%2!=0)
        
n = int(input('Enter the value of n: '))
res = sum_odd_number(n)
print(f'sum of all odd numbers is {res}.')