import math
def f(x):
#    return x**2              # composite Trapezoidal rule for function x**2
    return (2*x+1)            # composite Trapezoidal rule for function (2*x+1)
#    return math.sin(x)

a=eval(input("Enter the lower limit of the integration\n"))
b=eval(input("Enter the upper limit of the integration\n"))
N=eval(input("Enter the value of N\n"))       # larger the value of N, more accurate is the value of the integration

h=(b-a)/N
I=0.5*h*(f(a)+f(b)+2*sum([f(a+i*h) for i in range (1, N)]))

print("Value of the integration for","lower limit=",a, "and upper limit=",b, "is",I )
