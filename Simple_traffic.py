# -*- coding: utf-8 -*-
"""
Created on Mon Sep 17 21:58:30 2018

@author: js
"""

# Traffic on a ring with 10 cells; cars have constant velocity
import numpy as np
import matplotlib.pyplot as plt

# cells = 10
# timeSteps = 10

cells = 100
timeSteps = 100
maxV = 5

# initial positions of cars
a=np.zeros((cells,timeSteps))
#a[0]=[0,0,0,0,0,1,0,0,0,1]
a[0]=[0,0,1,0,0,1,0,0,0,1,0,0,1,0,0,1,0,0,0,1,0,0,1,0,0,1,0,0,0,1,0,0,1,0,0,1,0,0,0,1,0,0,1,0,0,1,0,0,0,1,0,0,1,0,0,1,0,0,0,1,0,0,1,0,0,1,0,0,0,1,0,0,1,0,0,1,0,0,0,1,0,0,1,0,0,1,0,0,0,1,0,0,1,0,0,1,0,0,0,1]
# 100cells for initial state

# each car has max velocity 5 and moves forward one cell per time step
for i in range(1,timeSteps):
    for j in range(0,cells):
        if a[i-1,j]==1:
            dis = 0
            done = False
            for k in range(1,maxV+1):#check if distance between a car and the car in front
                if(not done):
                    if a[i-1, (j+1)%cells] == 1:
                        print("here is a traffic jam!!!")
                        dis = 0   #in a traffic jam car will not move anymore
                        done = True
                    if a[i - 1, (j+k)%cells] == 1:
                        dis = k-1
                        done = True
                    if k == 5:
                        dis = 5

            # For a car, dis is distance to the empty cells of the front car.
            a[i,(j+dis)%cells]=1
            #print(dis)

for i in range(timeSteps):
    for j in range(cells):
        if a[i,j]== 0: 
            print("0",end='')
        else:
            print("*",end='')
    print("\n")    
    
plt.imshow(a, cmap='gray')
#plt.colorbar()
plt.show()