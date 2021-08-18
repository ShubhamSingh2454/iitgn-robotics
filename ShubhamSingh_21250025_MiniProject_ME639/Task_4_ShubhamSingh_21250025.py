# Shubham Singh
# 21250025

import math
import matplotlib.pyplot as plt
import cv2

# Task-4_Plot the Workspace.
#Both joints can sweep between 35 degrees and 145 degrees.

l1 = 5                      #  Length of Link-1 
l2 = 5                      # Length of Link-2 
n_theta = 5                # No. of steps 
theta_start = 35            # Initial theta
theta_end = 145             # Final theta
theta1 = []    
theta2 = []
y=[]

plt.ion()
plt.show()
for i in range (theta_start, theta_end):   
    tmp = theta_start + i*(theta_end - theta_start) / (n_theta-1)
    tmp = math.radians(i) 
    theta1.append(tmp)
    theta2.append(tmp)
    y.append(i)


x0 = 0                      #initial positions of the link-1
y0 = 0  
for t1 in theta1:
    for t2 in theta2:
        x1 = x0 + l1*math.cos(t1)
        y1 = y0 + l1*math.sin(t1)

        x2 = x1 + l2*math.cos(t2)
        y2 = y1 + l2*math.sin(t2)                  
    
        plt.plot([x0,x1],[y0,y1], linewidth =4)
        plt.plot([x1,x2],[y1,y2], linewidth =4)
        plt.xlim([-10,10])
        plt.ylim([-10,15])
        plt.pause(0.00001)
plt.ioff()
plt.show()