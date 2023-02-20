"""
calculate pi from a circle radius r inside a box, side length 2
if we know that x^2+y^2=1, for the circle, then generate numbers between
1 and -1, if the numbers add up to <=1 then they are part of the circle and so add one to the circle counter
otherwise just add one to the total number counter
maths:
    size of box = 2x2 = 4
    size of circle = pi, r=1
    to find r, sqrt(x^2+y^2)
    if r<=1, circlecount += 1, totalcount += 1
    else, totalcount +=1
    area of circle = circlecount/totalcount * size of box (4)
"""
import numpy as np
import random as rnd
totalcount=0
circlecount=0
N=1000000

while totalcount <N:
    x=rnd.uniform(-1,1)
    y=rnd.uniform(-1,1)
    r=np.sqrt(x**2+y**2) #gives wether the point is within the circle
    if r <=1:
        circlecount +=1 #adds a point to within the circle
    totalcount+=1 #adds a point within the square
    #print(totalcount/10000)

area = 4*(circlecount/totalcount) #gives the area of the square multiplied by the ratio of circle points to non-circle points

uncertainty_estimate = 1/np.sqrt(N)
print(area, "+/-", uncertainty_estimate)

#volume of n sphere = V_n(R)= (pi**n/2/((n/2 + 1)-1)!)*R**n
#surface area of a n sphere = (n/R)*V_n(R)
#n dimensions, R radius, 
