# WAP to print pattern 

# d.
for i in range(1,6):
    num=i
    for j in range(1,6-i):
        print(' ',end=' ')

    num=i
    for j in range(1,i+1):
        print(num,end=' ')
        num=num+1

    num=num-2
    for j in range(1,i):
        print(num,end=' ')
        num=num-1
    
    print()