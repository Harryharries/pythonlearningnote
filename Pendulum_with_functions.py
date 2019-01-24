# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 18:12:38 2018

@author: js
"""

# The simple pendulum
# Equation of motion: d^2phi/dt^2 = -g/l*sin(phi)

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# command line arguments
import argparse



def printArgu(argument):
    print("Print Argument.....")
    print("l is :" +str(argument.l))
    print("point is :" +str(argument.points))
    print("Verlet is :" + str(argument.Verlet))

# define command line parser
parser = argparse.ArgumentParser(description='Pendulum using Newton or Verlet algorithm')

parser.add_argument('-Verlet', type=int, default=0,
                    help='1: Verlet, 0: Euler (default)')
parser.add_argument('-l', type=float, default=1.0,
                    help='length of pendulum in meters')
parser.add_argument('-points', type=int, default=5000,
                    help='number of time points')                    
args = parser.parse_args() 


# Define constants
g=9.81 # in m/s^2
l=args.l # pendulum length in meter
phi0 = np.pi/2 # initial angle
phidot0 = -0.0 # initial angular velocity
T = 10.5*2*np.pi*np.sqrt(l/g) # 5 oscillation periods in harmonic approximation
print(T)
points = args.points # number of time steps
dt = T/points # time step
fac = int(points/1000) # factor for animation

printArgu(args)

# Set up fields for angle and angular velocity
phi = np.zeros(points)
phidot = np.zeros(points)
phi[0] = phi0
phidot[0] = phidot0


# update positions and velocities (Euler-type algorithm)
def Euler():
    for i in range(1,points):
        phiddot = -g/l*np.sin(phi[i-1]) # angular acceleration 
        phidot[i] = phiddot*dt + phidot[i-1] # update of angular velocity
        phi[i] = 0.5*phiddot*dt**2 + phidot[i-1]*dt + phi[i-1] # update of angle

# update positions using the velocity Verlet algorithm
def Verlet():
    for i in range(1,points):
        phiddot = -g/l*np.sin(phi[i-1]) # angular acceleration 
        phi[i] = 0.5*phiddot*dt**2 + phidot[i-1]*dt + phi[i-1] # update of angle
        phiddot2 = -g/l*np.sin(phi[i]) # angular acceleration at new position
        phidot[i] = (phiddot+phiddot2)*dt/2 + phidot[i-1] # update of angular velocity


# Call either the Euler or the Verlet algorithm   
if args.Verlet: 
    Verlet()
else: 
    Euler()

# calculate x,y position of pendulum    
x = l*np.sin(phi)   
y = -l*np.cos(phi)

# Plot the result and animate
fig = plt.figure()
ax = fig.add_subplot(111, autoscale_on=False, xlim=(-2*l, 2*l), ylim=(-2*l, 2*l))
ax.grid()

line, = ax.plot([], [], 'o-', lw=2)
time_template = 'time = %.3f s'
time_text = ax.text(0.05, 0.9, '', transform=ax.transAxes)


def init():
    line.set_data([], [])
    time_text.set_text('')
    return line, time_text


def animate(i):
    thisx = [0, x[fac*i]]
    thisy = [0, y[fac*i]]
    #print(thisx)

    line.set_data(thisx, thisy)
    time_text.set_text(time_template % (fac*i*dt))
    return line, time_text

ani = animation.FuncAnimation(fig, animate, np.arange(points/fac),
                              interval=1, blit=False, init_func=init)

ani.save('double_pendulum.mp4', fps=15)
plt.show()