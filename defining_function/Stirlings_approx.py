#from numpy import *
from math import *
def Stir1(n):
    return log(factorial(n))
def Stir2(n):
    return n*log(n)-n
n=eval(input('Enter the value of n\n'))
print('ln(n!)=',Stir1(n))
print('n*ln(n)-n=',Stir2(n))
