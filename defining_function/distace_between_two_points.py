from math import *
def distance(x1,y1,z1,x2,y2,z2):
    return (((x1-x2)**2)+((y1-y2)**2)+((z1-z2)**2))**(1/2)
x1,y1,z1=eval(input('Enter three coordinates of the 1st point\n')
x2,y2,z2=eval(input('Enter three coordinates of the 2nd point\n')
print(distance(x1,y1,z1,x2,y2,z2))
