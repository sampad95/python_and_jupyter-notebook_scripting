from math import *
def sum(x,n):
    sum=0
    for j in r:
        sum=sum+((x**j)/factorial(j))
    return sum
x=eval(input('Enter the value of x\n'))
n=eval(input('Enter the value of n\n'))
r=range(0,n+1)
print(sum(x,n))
