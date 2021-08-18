# Shubham Singh
# 21250025

import math
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
import cv2


#Task_2
#Robot applying a prespecified force in the normal direction of the wall.

l1 = 5       #Length of link-1
l2 = 5       #Length of link-2
n_theta = 10
theta1 = []
theta2 = []
theta_start = 0
theta_end = math.pi/1.305
y = []


plt.ion()
plt.show()

for i in range (theta_start, n_theta):
    tmp = theta_start + i*(theta_end - theta_start) /(n_theta-1)
    theta1.append(tmp)
    theta2.append(tmp)
    y.append(i)
    
    def InverseKinematics(x, L):
        if (l1*l1 + (x*y + y*y) - l2*l2) / (2*l1*math.sqrt(x*x + y*y)) > 1:
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
            print('th2 error {}, {}'.format(x,y))

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

        def Force_control(T_1, T_2):           #defining Force Controller
            F1 = 10
            F2 = 20
            T_1 = F2*l1*math.cos(theta1)-F1*l1*math.sin(theta2)
            T_2 = F2*l2*math.cos(theta1)-F1*l2*math.sin(theta2)
            return(T_1, T_2)
           
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







