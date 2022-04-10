from math import *
def sum(x,n):
    """This is cos(x) infinite series sum"""
    sum=0
    for j in r:
        sum=sum+(((-1)**j)*(x**(2*j))/factorial(2*j))
    return sum
x=eval(input('Enter the value of x\n'))
n=eval(input('Enter the value of n\n'))
r=range(0,n+1)
print(sum(x,n))
print(sum.__doc__)
