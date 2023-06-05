from math import *
def exp(x,n):
    sum1=0
    for j in range(n+1):
        sum1+=((x**j)/factorial(j)) # takes sum upto x^n/n!
    return sum1
x=eval(input('Enter the value of x\n'))
n=eval(input('Enter the value of n\n'))
print(exp(x,n))
