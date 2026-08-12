# find the distance using path  
# N=north, S=south, E=east, W=west
# distance formula =sqrt(x**2 + y**2)

import math
x=0
y=0
path = "WNEENES"
for i in path:
    if i=="W":
        x-=1
    elif i=="E":
        x+=1
    elif i=="N":
        y+=1
    elif i=="S":
        y-=1
    else:
        print("Invaild path")
print('Final Coordinate :',(x,y))
distance =math.sqrt(x**2 + y**2)
print('Distance =',distance)

