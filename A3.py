#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 16 07:48:41 2018

@author: tanshuai
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

g=9.81
l=1.5
phi10=np.pi*(7/9)
phi1dot0=0.0
phi20=np.pi/18
phi2dot0=0.0
T=5
points=50000
dt=T/points
fac=int(points/500)

phi1=np.zeros(points)
phi1dot=np.zeros(points)
phi1[0]=phi10
phi1dot[0]=phi1dot0
phi2=np.zeros(points)
phi2dot=np.zeros(points)
phi2[0]=phi20
phi2dot[0]=phi2dot0

for i in range(1,points):
    phi1ddot=((g/l)*np.sin(phi2[i-1])*np.cos(phi1[i-1]-phi2[i-1])-(np.sin(phi1[i-1]-phi2[i-1])*(phi1dot[i-1]*phi1dot[i-1]*np.cos(phi1[i-1]-phi2[i-1])+phi2dot[i-1]*phi2dot[i-1]))-(2*g/l)*(np.sin(phi1[i-1])))/(1+(np.sin(phi1[i-1]+phi2[i-1])*np.sin(phi1[i-1]+phi2[i-1])))
    phi1dot[i]=phi1ddot*dt+phi1dot[i-1]
    phi1[i]=0.5*phi1ddot*dt**2+phi1dot[i-1]*dt+phi1[i-1]
    phi2ddot=(2*(((phi1dot[i-1]**2)*np.sin(phi1[i-1]-phi2[i-1]))-(g/l)*np.sin(phi2[i-1])+(g/l)*np.sin(phi2[i-1])*np.cos(phi1[i-1]-phi2[i-1]))+(phi2dot[i-1]**2)*np.sin(phi1[i-1]-phi2[i-1])*np.cos(phi1[i-1]-phi2[i-1]))/(1+((np.sin(phi1[i-1]-phi2[i-1]))**2))
    phi2dot[i]=phi2ddot*dt+phi2dot[i-1]
    phi2[i]=0.5*phi2ddot*dt**2+phi2dot[i-1]*dt+phi2[i-1]

x1=l*np.sin(phi1)
x2=l*np.sin(phi1)+l*np.sin(phi2)
y1=-l*np.cos(phi1)
y2=-l*np.cos(phi1)-l*np.cos(phi2)

print("oiajfiqehfioq!!!!!!!!!!!!!!!!!!")
for i in range(0,points):
    print(x1[i])


print("weqlejioqwhrio!!!!!!!!!!!!!!!!!!")
for i in range(0,points):
    print(x1[i])

#
# fig=plt.figure()
# ax=fig.add_subplot(111,autoscale_on=False,xlim=(-2*1,2*1),ylim=(-2*1,2*1))
# ax.grid()
#
# line, = ax.plot([], [], 'o-', lw=2)
# time_template = 'time = %.3f s'
# time_text = ax.text(0.05, 0.9, '', transform=ax.transAxes)
#
# def init():
#     line.set_data([],[])
#     time_text.set_text('')
#     return line,time_text
#
# def animate(i):
#     thisx1=[0,x1[fac*i]]
#     thisx2=[0,x2[fac*i]]
#     thisy1=[0,y1[fac*i]]
#     thisy2=[0,y2[fac*i]]
#
#     line.set_data(thisx1,thisy1)
#     line.set_data(thisx2,thisy2)
#     time_text.set_text(time_template % (fac*i*dt))
#     return line,time_text
#
# ani=animation.FuncAnimation(fig,animate,np.arange(points/fac),interval=1,blit=False, init_func=init)
#
# plt.show()
