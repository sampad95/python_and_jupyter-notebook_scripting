import numpy as np
from square_function import sq as f
#from inverse_function import inv as f

def simp1_3(a, b, n):
    h = (b-a)/n
#    def y(i):
#        return a + i*h

#    msum = 0
#    for k in np.arange(1, n/2+1):
#        msum += (h/3)*(f(y(2*k-2)) + 4*f(y(2*k-1)) + f(y(2*k)))

    y = np.linspace(a, b, n+1)
    msum = (h/3)*(f(a) + 4*sum(f(y[1:n:2])) + 2*sum(f(y[2:n-1:2])) + f(b))
    

    return msum
