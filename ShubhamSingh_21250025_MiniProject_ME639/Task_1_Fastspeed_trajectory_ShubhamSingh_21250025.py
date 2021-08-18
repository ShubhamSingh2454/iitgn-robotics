# Shubham Singh
# 21250025

import math
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
import cv2

# Task_1 
# Robot following an arbitrary end-tip trajectory
# High speed Trajectory

l1 = 5   #lenght of link-1
l2 = 5   #length of link-2

n_theta = 20     
theta_start = 0
theta_end = math.pi/1.305
theta1 = []
theta2 = []
y = []


plt.ion()
plt.show()

for i in range (theta_start, n_theta+1):
    tmp = theta_start + i*(theta_end - theta_start) / (n_theta-1)
    theta1.append(tmp)
    theta2.append(tmp)
    y.append(i)
   
    def InverseKinematics(x, l):
        if (l1*l1 + (x*y + y*y) - l2*l2) / (2*l1*math*sqrt(x*x + y*y)) > 1:
            th1 = math.atan2(y, x) 
            print('th1 error {},{}'.format(x, y))
        elif ((l1*l1 + (x*x + y*y) - l2*l2) / (2*l1*math.sqrt(x*x + y*y))) < -1:
            th1 = math.atan2(y, x) - math.pi
            print('th1 error{}, {}'.format(x, y))
        else:
            th1 = math.atan2(y, x) - math.acos((l1 * l1 + (x * x + y * y) - l2 * l2) / (2 * l1 * math.sqrt(x * x + y * y)))
        if ( l1 * l1 + (x * y + y * y)) / (2 * l1 * l2) > 1:
            th2 = math.pi
            print('theta_2 error {},{}'.format(x, y))

        elif (l1 * l1 + l2 * l2 - (x * x + y * y)) / (2 * l1 * l2) < -1:
            th2 = 0.0
            print('th2 error {}, {}'.format(x, y))

        else:
            th2 = math.pi - math.acos((l1*l1+l2*l2-(x*x+y*y))/(2*l1*l2))

        return [th1, th2]

x0 = 0
y0 = 0

for t1 in theta1:
    for t2 in theta2:
        x1 = x0 + l1*math.cos(t1)
        y1 = y0 + l1*math.sin(t1)
       
        x2 = x1 + l2*math.cos(t2)
        y2 = y1 + l2*math.sin(t2)
        
        x3 = -8
        y3 = 0

        x4 = -8
        y4 = 10
    plt.clf()
    plt.xlim([-12, 12])  
    plt.ylim([-5, 12])
    plt.plot([x2],[y2],'bo') 
    plt.plot([x0,x1],[y0,y1], 'm',linewidth=3)
    plt.plot([x1,x2],[y1,y2], 'y', linewidth = 3)
    plt.plot([x3,x4], [y3,y4], 'r', linewidth=10)
   
    plt.pause(0.0001)
    

plt.ioff()
plt.show()



   
