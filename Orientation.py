# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# Print("Hello world!")
### variables for particle 1
import numpy as np
Npart = 10
### create empty list for each quantity
m = np.zeros(Npart)
v = np.zeros(Npart)
q = np.zeros(Npart)
x = np.zeros(Npart)
T = np.zeros(Npart)
print(m)

for i in range(0,Npart):
    m[i] = 1.0
    q[i] = 1.0
    x[i] = 0.5 * i
    v[i] = 0.2 * i
    ### not that i have mass and velocity for 
    ### ith particle, I can calculate kinetic energy
    ### for the ith particle 
    T[i] = 0.5 * m[i] * v[i]**2
print(T)
    
print(m)
print(q)
print(x)
print(v)
### variables for particle 2
#m2 = 1.0
#v2 = 2.5
#q2 = 1.0
#x2 = 0.5
### variable for pair of particles#
#12 = np.sqrt((x1-x2)**2)
#12 = q1*q2/r12
#rint(" separation is ",r12)
#rint (" Potential Energy is",V12)
