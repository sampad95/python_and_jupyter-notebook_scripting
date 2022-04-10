from math import *
def sum(x,n):
    sum=x
    for j in r:
        sum=sum+(((-1)**j)*(x**((2*j)+1))/factorial((2*j)+1))
    return sum
x=eval(input('Enter the value of x\n'))
n=eval(input('Enter the value of n\n'))
r=range(1,n+1)
print(sum(x,n))
