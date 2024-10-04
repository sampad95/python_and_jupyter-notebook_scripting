import math
import numpy as np
import scipy.constants as sc
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter

def psi_n(a2, b2, nx, ny, x, y):
#     a2 = eval(input("Enter xmax\n"))
#     b2 = eval(input("Enter ymax\n"))
#     nx = eval(input("Enter nx\n"))
#     ny = eval(input("Enter nx\n"))
    
    lx = a2 - 0
    ly = b2 - 0
    if type(nx) == int and type(ny) == int and nx != 0 and ny != 0:
        psi = math.sqrt(4/lx*ly)*math.sin((nx*math.pi*x)/lx)*math.sin((ny*math.pi*y)/ly)
        return psi
        
    else:
        print("Wrong input")

        
        
def xvec(a2, h):
    return np.arange(0, a2+h, h)

def yvec(b2, h):
    return np.arange(0, b2+h, h)


xmax = 1
ymax = 1
step = 0.01

qnx = 3
qny = 3

X,Y = np.meshgrid(xvec(xmax, step), yvec(ymax, step)) # grid of point
PSI = np.array([np.array([psi_n(xmax, ymax, qnx, qny, i, j) for i in  xvec(xmax, step)]) 
                for j in yvec(ymax, step)]) 


fig = plt.figure()
ax = fig.add_subplot(projection = "3d")
surf = ax.plot_surface(X, Y, PSI, rstride=1, cstride=1, 
                      cmap=cm.hsv,linewidth=0, antialiased=False)

ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()