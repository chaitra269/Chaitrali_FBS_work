# WAP to print pattern 

# f.

for i in range(1,6):
    for j in range(1,6):
        if i==1:
            print(j,end=' ')
        elif j==1:
            print(i,end=' ')
        elif j==6-i:
            print(5,end=' ')
        else:
            print(' ',end=' ')

        
    print()