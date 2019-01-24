# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 16:34:25 2018

@author: js
"""

import matplotlib.pyplot as plt
import numpy as np
 
L = 100 # number of cells
steps = 100 # number of time steps
density = 0.5 # density of cars
vmax = 5
p = 0.3
stepsize = int(1/density)
gammaLR=0.0
gammaRL=1

# create initial state; -1 represents an empty site; 0,1,2,3,4,5 velocities
a=np.zeros((steps,L))-1
b= np.zeros((steps,L))-1
i=0
while i < L:
    a[0,i] = 1
    b[0, i] = 1
    i += stepsize


for i in range(1,steps):
    for j in range(L):
        if a[i-1,j] > -1: # found a car
            # current velocity of car          
            velocity = a[i-1,j]
            # measure number of empty cells in front of car  
            dist = 1
            while a[i-1,(j + dist) % L] < 0:
                dist += 1
                # update velocity: increase by one but not more than distance to next car and not more than vmax   
            velupdate = min(velocity+1, dist - 1, vmax) 
            # bring in random variations in speed
            if np.random.randint(0,101) < p*100:
                v = max(velupdate - 1, 0)  
            else:
                v= velupdate
            # move all cars forward according to their velocity
            a[i,int(j + v) % L] = v
        if b[i-1,j] > -1: # found a car
            # current velocity of car
            velocity = b[i-1,j]
            # measure number of empty cells in front of car
            dist = 1
            while b[i-1,(j + dist) % L] < 0:
                dist += 1
                # update velocity: increase by one but not more than distance to next car and not more than vmax
            velupdate = min(velocity+1, dist - 1, vmax)
            # bring in random variations in speed
            if np.random.randint(0,101) < p*100:
                v = max(velupdate - 1, 0)
            else:
                v= velupdate
            # move all cars forward according to their velocity
            b[i,int(j + v) % L] = v

    for j in range(L):
        if a[i-1,j] == -1 and b[i-1,j] > -1:
            if np.random.randint(0, 101) < gammaRL * 100:
                a[i-1,j] = b[i-1,j]
                b[i - 1, j] = -1
        elif b[i-1,j] == -1 and a[i-1,j] > -1:
            if np.random.randint(0, 101) < gammaLR * 100:
                b[i - 1, j] = a[i-1,j]
                a[i - 1, j] = -1


# Prints car positions
for i in range(steps):
    for j in range(L):
        if a[i,j]== -1: 
            print(".",end='')
        else:
            print(int(a[i,j]),end='')
    print("\n")
    for j in range(L):
        if b[i,j]== -1:
            print(".",end='')
        else:
            print(int(b[i,j]),end='')
    print("\n\n-------------------------------------------------------------------------------------------\n\n")
 
# showing image
plt.figure(figsize=(10,10))
plt.title("LIFT")
plt.imshow(a, cmap='PuBu_r')
plt.show()

plt.figure(figsize=(10,10))
plt.title("RIGHT")
plt.imshow(b, cmap='PuBu_r')
plt.show()
