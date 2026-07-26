# WAP to print pattern

# a.
for i in range(1,6):
    for j in range(1,6-i):
        print(' ',end=' ')

    for j in range(1,i):
        if(j==1 ):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    
    for j in range(1,i):
        if( j==5  or i==j ):
            print('*',end=' ')
        else:
            print(' ',end=' ')

    for j in range(1,i+1):
        if(i==j):
            print('*',end=' ')
    print()

for i in range(1,6):
    for j in range(1,i):
        print(' ',end=' ')

    for j in range(1,6-i):
        if(i==5 or j==1 ):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    
    for j in range(1,6-i):
        print(' ',end=' ')
    for j in range(1,i+1):
        if( i==j):
            print('*',end=' ')
    print()

