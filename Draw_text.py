import numpy as np
import matplotlib.pyplot as plt

# Bezier Curves
# Define the parameter t
t = np.linspace(0, 1)

def draw(pt1, pt2, pt3, pt4, pt5, pt6, pt7, pt8):
    BASE_F = np.array(
        [ [-1, 3 ,-3 ,1],[3 ,-6 ,3 ,0],[-3, 3 ,0 ,0],[1, 0, 0, 0] ]
        )
    OBJECTS_B = np.array(
        [[pt1, pt2], [pt3, pt4], [pt5, pt6], [pt7, pt8]]
    )
    [[a,b], [c,d],[e,f],[g,h]] = np.matmul(BASE_F,OBJECTS_B)
    x = a*t*t*t + c*t*t+ e*t+ g
    y = b*t*t*t + d*t*t+ f*t + h
    plt.plot(x, y)

# D
draw(0,0,0,2,0,3,0,5)
draw(0,0,4,0,4,5,0,5)

# R
draw(4,0,4,2,4,3,4,5)
draw(4,3,8,3,8,5,4,5)
draw(4,3,5,2,6,1,7,0)

# A
draw(8,0,8.75,1.375,9.25,3.125,10,5)
draw(12,0,11.25,1.375,10.75,3.125,10,5)
draw(9,2.5,9.5,2.5,10.5,2.5,11,2.5)

# W
draw(14,0,14,2,14,3,14,5)
draw(14,0,14,0,16,2.5,16,2.5)
draw(16,2.5,16,2.5,18,0,18,0)
draw(18,0,18,2,18,3,18,5)


# Add labels and title to the plot
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Draw Text')

# Show the plot
plt.show()
