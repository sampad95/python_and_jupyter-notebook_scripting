import numpy as np
from scipy.constants import *
def v_s(v_l,v_t):
    return ((1/3)*((1/(v_l)**3)+(2/(v_t)**3)))**(-1/3)


v_l=eval(input("Enter the longitudinal velocity in m/s\n"))
v_t=eval(input("Enter the transverse velocity in m/s\n"))

print ('Average sound velocity =',v_s(v_l,v_t),'m/s')

def theta_D(N,V,v_s):
    return ((hbar * v_s(v_l,v_t))/k)*(6*((pi)**2)*(N/V))**(1/3)

N=eval(input("Enter the number of atoms per unit cell\n"))
V=eval(input("Enter the volume in cubic meter per unit cell\n"))

print ('Debye temperature =',theta_D(N,V,v_s), 'K')
