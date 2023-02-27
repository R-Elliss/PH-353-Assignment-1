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
sqrt(1/(N(N-1))*sum((rnd.uniform - mean)^2))=uncertainty/error
"""
import numpy as np
import random as rnd
N=10000   #number of random numbers
totalcount=0
circlecount=0
meantot=0
uncertainty_estimate = 1/np.sqrt(N)   #estimate of the uncertainty in V, proper calculation might be needed for consistent results

# n-dimensional sphere volume/surface area calculations
n = 3    # number of dimensions
R = 1    # radius
sigmarr=np.zeros((n,1), dtype='float') #array used in error
#Recurively calculating Vn(R)
def recursive_V(n, R):  #works for any d > 0
    if n == 0:
        return 1   #0D case
    elif n == 1:
        return 2*R   #1D case
    else:
        return (2*np.pi/n * R**2 * recursive_V(n-2, R))   #equation taken from 2d recurrance relation on wikipedia page for volume of an n ball
    
        
s_Area = (n/R)*recursive_V(n, R)  #Surface area of n-d sphere, this is currently being used not entirely sure if we need it or not

while totalcount < N:
    pos_R = np.ones((n, 1), dtype='float')
    total = 0 
    for i in range(n):
        pos_R[i-1] = [rnd.uniform(-R, R)]   #creating an array with n random numbers stored
        total += float(pos_R[i-1]**2)
        sigmarr=np.append(sigmarr,np.sqrt(sum(pos_R[i-1]**2)))
        
    
    r = np.sqrt(total) #square rooting over the sum of all random numbers squared
    if r <= R:
        circlecount += 1
    totalcount += 1
mean=sum(sigmarr)/N
for i in range(N):
    meantot += (sigmarr[i+n]-mean)**2
error = np.sqrt(1/(N*(N-1))*meantot)
    
n_area = ((2*R)**n)*(circlecount/totalcount)   #area of box multiplied by the ratio of points in the sphere vs outside
print(n_area, "+/-", error, "value obtained via monte-carlo integration, compared to the actual value of", recursive_V(n, R))
