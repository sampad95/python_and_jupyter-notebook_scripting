import math
import numpy as np
import scipy.constants as sc
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter

def psi_nx_ny(a2, b2, nx, ny, x, y):
    
    lx = a2 - 0
    ly = b2 - 0
    if type(nx) == int and type(ny) == int and nx > 0 and ny > 0:
        psi = math.sqrt(4/lx*ly)*math.sin((nx*math.pi*x)/lx)*math.sin((ny*math.pi*y)/ly)
        return psi
        
    else:
        print("Wrong input")
        
        
def pd_nx_ny(a2, b2, nx, ny, x, y):
    
    lx = a2 - 0
    ly = b2 - 0
    
    if type(nx) == int and type(ny) == int and nx > 0 and ny > 0:
        psi = math.sqrt(4/lx*ly)*math.sin((nx*math.pi*x)/lx)*math.sin((ny*math.pi*y)/ly)
        return psi**2
        
    else:
        print("Wrong input")

        
        
def xvec(a2, h):
    return np.arange(0, a2+h, h)

def yvec(b2, h):
    return np.arange(0, b2+h, h)


xmax = 1
ymax = 1
step = 0.01

qnx = 2
qny = 2

X,Y = np.meshgrid(xvec(xmax, step), yvec(ymax, step)) # grid of point
PSI = np.array([np.array([psi_nx_ny(xmax, ymax, qnx, qny, i, j) for i in  xvec(xmax, step)]) 
                for j in yvec(ymax, step)]) 

fig = plt.figure()
ax = fig.add_subplot(projection = "3d")
surf = ax.plot_surface(X, Y, PSI, rstride=1, cstride=1, 
                      cmap=cm.hsv,linewidth=0, antialiased=False)



#X,Y = np.meshgrid(xvec(xmax, step), yvec(ymax, step)) # grid of point
#PD = np.array([np.array([pd_nx_ny(xmax, ymax, qnx, qny, i, j) for i in  xvec(xmax, step)]) 
#                for j in yvec(ymax, step)])
#
#fig = plt.figure()
#ax = fig.add_subplot(projection = "3d")
#surf = ax.plot_surface(X, Y, PD, rstride=1, cstride=1, 
#                      cmap=cm.hsv,linewidth=0, antialiased=False)


#scale_x = xmax
#scale_y = ymax
#scale_z = 1
#ax.get_proj = lambda: np.dot(Axes3D.get_proj(ax), np.diag([scale_x, scale_y, scale_z, 1]))


ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

ax.set_xlabel('$X$', fontsize=20)
ax.set_ylabel('$Y$', fontsize=20)


fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()
