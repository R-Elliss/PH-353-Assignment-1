import numpy as np

"""
A test case, using a recursive function to output a highly accurate volume for any generalised radius and dimension of sphere
def trueV(r,D):  #works for any d > 0
        if D == 0:
            return 1   #0D case
        elif D == 1:
            return 2*r   #1D case
        else:
            return (2*np.pi/D * r**2 * trueV(r, D-2))
"""

def Volume(r,D):
    N = 100000 # this is incredibly accurate for N = 10,000,000 but it takes like 3 mins to run for 2d 
    
    def ranradii(r,D,N):
        arr=np.zeros([N,1])
        for i in range(N):
            arr[i]=float(np.sqrt(sum(np.random.uniform(-r,r,size=(D,1))**2))) 
        return arr

    def volfind(r,D,N):
        xi=ranradii(r,D,N)   
        count=0
        circlecount=0
        while count < N:
            if xi[count] <= r:
                circlecount +=1
            count += 1
        vol=circlecount/count * (2*r)**D
        return vol
    
    return volfind(r,D,N)

def uncertainty(r,D,N):
    uncarr=np.zeros([N])
    for i in range(N):
        uncarr[i]=Volume(r,D)
    mean=sum(uncarr)/N
    error=np.sqrt((1/(N*(N-1)))*sum((uncarr-mean)**2))
    return error

def assignment():
    dimarr=np.zeros([10,3])
    radarr=np.zeros([10,3])
    for i in range(10):
        dimarr[i,0]=i+1
        dimarr[i,1]=Volume(1,i+1)
        dimarr[i,2]=uncertainty(1,i+1,10)
        radarr[i,0]=(i+1)/2
        radarr[i,1]=Volume(((i+1)/2),3)
        radarr[i,2]=uncertainty(((i+1)/2),3,10)
    np.savetxt("dimensions1to10.txt",dimarr)
    np.savetxt("radii1to5.txt",radarr)
    return dimarr,radarr