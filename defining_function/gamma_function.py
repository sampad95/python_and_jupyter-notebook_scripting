#from sympy import *
import sympy as smp
def fun(n):
    fun=smp.sqrt(smp.pi)
    for i in range(1,n+1):
        fun=fun*((2*i-1)/2)
    return fun
n=eval(input('Enter the value of n\n'))
print('(n+1/2)=',(n+1/2))
print('gamma(n+1/2)=',fun(n))
