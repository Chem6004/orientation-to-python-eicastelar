#question 1
# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
from matplotlib import pyplot as plt
import time
### Number of particles will be 10
Npart = 10
### create an array 'm' and 'v' to store the masses and velocities of the 10 particles... 
### initially, each entry in 'm' and 'v' will be zero, and we will have to assign values later
m = np.zeros(Npart)
v = np.zeros(Npart)
for i in range(0,Npart):
    m[i] = 1.0
    v[i] = 2.5

### Now that values have been assigned, print to confirm they are what you expect
print("Printing array of masses: ",m)
print("Printing array of velocities: ",v)
T = 1/2 * m * v**2
### confirm that T is indeed an array with an entry for the kinetic energy of each particle
print(T)

### initialize a sum variable to zero
T_tot_loop = 0.

### loop over elements of the T array and 
### compute the sum ,
for i in range(0,Npart):
    ### add elements to the sum variable
    T_tot_loop = T_tot_loop + T[i]
    
### compute the sum using np.sum instead
T_tot_sum = np.sum(T)

### print both sums to confirm both methods give the same answer
print("Result from loop is ",T_tot_loop)
print("Result from numpy sum is ",T_tot_sum)
N_array = [1, 2, 3, 4, 5 ]
T_array = [3.125,6.25,9.375,12.5,15.625 ]      
plt.plot( N_array, T_array, 'blue')
plt.show()

