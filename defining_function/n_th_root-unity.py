from numpy import *
def f(n):
    return complex(cos((2*pi*k)/n), sin((2*pi*k)/n))

n=eval(input('Enter the value of n\n'))

#k=eval(input('Enter the value of k\n'))
#print(f(n))

print('Roots for the',n,'th root of unity are:')
for k in range(n):
#    print(k,'th root for',n,'th root of unity')
    print(f(n))
