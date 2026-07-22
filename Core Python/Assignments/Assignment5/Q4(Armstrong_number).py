# WAP to print Armstrong number within a given range 

start = int(input("Enter starting number of range :"))
end = int(input("Enter ending number of range :"))

print(f"Armstrong numbers from {start} to {end} :" )
for i in range(start,end+1):
    i_str = str(i)
    n = len(i_str)
    digit_sum = sum(int(digit)**n for digit in i_str)

    if digit_sum == i:
            print(i, end=' ')
print()
