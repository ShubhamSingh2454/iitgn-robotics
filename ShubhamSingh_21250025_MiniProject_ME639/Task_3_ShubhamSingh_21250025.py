# Shubham Singh
# 21250025

import numpy as np 
import scipy.integrate
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
import math
import cv2

#Control scheme for making the robot end-tip act like a virtual spring.
#centred at the mean position.


l1 = 5
l2 = 5
g = 9.81
m1 = 1
m2 = 1

theta_1 = 0
theta_2 = 90

plt.ion()
plt.show()
def Virtual_Spring(t, y):  #Tried incorporating the links as Virtual Springs using the control scheme of Inverted Pendulum
    theta_1 = y[0]
    theta_2 = y[0]
    b = 0.1
    dydt = [theta_1, -(g/l1) * np.sin(theta_2) - b*theta_1]
    return dydt
State_initial = [theta_2, theta_1]           #initial states
timestep = 0.01
time = np.linspace(0, 100, 1000) 
solution = solve_ivp(Virtual_Spring, [0, time[-1]], State_initial, t_eval= time) 

theta_2 = solution.y[0]
theta_1 = solution.y[1]

for i in range(len(theta_2)):
    theta = theta_2[i]
    Link_1Pos = (l1 * np.cos(theta - np.pi/2), l1 * np.sin(theta - np.pi/2))
    Link_2Pos = (l2 * np.sin(theta - np.pi/2), l2 * np.cos(theta - np.pi/2))
    plt.clf() 
    plt.xlim([-20, 20])
    plt.ylim([-20, 20])
    Base = (0, 0)                          
    plt.plot([Base[0], Link_1Pos[0], Link_2Pos[0]], [Base[1], Link_1Pos[1], Link_2Pos[1]], 'r')
    plt.pause(0.00001)

plt.ioff()
plt.show()


