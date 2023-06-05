from math import *
def exp_(x,n):
    sum1=0
    for j in range(n+1:
        sum1=sum1+(((-1)**j)*(x**j)/factorial(j))
    return sum1
x=eval(input('Enter the value of x\n'))
n=eval(input('Enter the value of n\n'))
print(exp_(x,n))
