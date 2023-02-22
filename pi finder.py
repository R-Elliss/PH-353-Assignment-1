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


totalcount=0
circlecount=0
while totalcount <N:
    x=rnd.uniform(-1, 1)
    y=rnd.uniform(-1, 1)
    r=np.sqrt(x**2 + y**2) #gives wether the point is within the circle
    if r <= 1:
        circlecount += 1 #adds a point to within the circle
    totalcount += 1 #adds a point within the square
    #print(totalcount/10000)

area = 4*(circlecount/totalcount) #gives the area of the square multiplied by the ratio of circle points to non-circle points
"""
import numpy as np
import random as rnd
N=1000000   #number of random numbers
totalcount=0
circlecount=0
 
uncertainty_estimate = 1/np.sqrt(N)   #estimate of the uncertainty in V, proper calculation might be needed for consistent results

# n-dimensional sphere volume/surface area calculations
n = 4    # number of dimensions
R = 1    # radius

#Recurively calculating Vn(R)
def recursive_V(n):  #works for any d > 0
    if n == 0:
        return 1   #0D case
    elif n == 1:
        return 2*R   #1D case
    else:
        return (2*np.pi/n * R**2 * recursive_V(n-2))   #equation taken from 2d recurrance relation on wikipedia page for volume of an n ball
    
#used for calculating the area of the n-dimensional box
def double(n):  #returns 2x the last value of n. i.e. n = 2 give 4, n = 3 gives 8 
    if n == 0:
        return 1
    else:
        return 2*double(n-1)
        
s_Area = (n/R)*recursive_V(n)  #Surface area of n-d sphere, this is currently being used not entirely sure if we need it or not

while totalcount < N:
    pos_R = np.ones((n, 1), dtype='float')
    total = 0 
    for i in range(n):
        pos_R[i-1] = [rnd.uniform(-1, 1)]   #creating an array with n random numbers stored
        total += float(pos_R[i-1]**2)
    r = np.sqrt(total) #square rooting over the sum of all random numbers squared
    if r <= 1:
        circlecount += 1
    totalcount += 1
    
n_area = double(n)*(circlecount/totalcount)   #area of box multiplied by the ratio of points in the sphere vs outside
print(n_area, "+/-", uncertainty_estimate, "value obtained via monte-carlo integration, compared to the actual value of", recursive_V(n))
