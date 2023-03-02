import numpy as np

def Volume(r,D):
    N = 1000000
    
    def trueV(D, r):  #works for any d > 0
        if D == 0:
            return 1   #0D case
        elif D == 1:
            return 2*r   #1D case
        else:
            return (2*np.pi/D * r**2 * trueV(D-2, r))

    def ranradii(D,r,N):
        arr=np.zeros([N,1])
        for i in range(N):
            arr[i]=float(np.sqrt(sum(np.random.uniform(-r,r,size=(D,1))**2)))
        return arr

    def volfind(D,r,N):
        xi=ranradii(D,r,N)   
        totalcount=0
        circlecount=0
        while totalcount < N:
            if xi[totalcount] <= r:
                circlecount +=1
            totalcount += 1
        vol=circlecount/totalcount * (2*r)**D            
        return vol
    
    def volerr(D,r,N):
        error = np.sqrt((1/(N*(N-1)))*sum((ranradii(D,r,N) - volfind(D,r,N))**2))
        return float(error)

    print("for a sphere in",D,"dimesnions, with radius",r,", volume =",volfind(D,r,N),"+/-",volerr(D,r,N),"compared to the real value of,",trueV(D,r))
