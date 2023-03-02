import numpy as np

def assignment():
    #1) 
    results_1 = []
    for D in range(1,11):
        results_1.append(Volume(1,D))
        #print(results_1)
        
    #2)
    results_2 = []
    for r in np.arange(1,5.5,0.5):
        results_2.append(Volume(r,3))
        
    return results_1, results_2

def Volume(r,D):
    N = 1000000 # this is incredibly accurate for N = 10,000,000 but it takes like 3 mins to run for 2d 
    
    def trueV(r,D):  #works for any d > 0
        if D == 0:
            return 1   #0D case
        elif D == 1:
            return 2*r   #1D case
        else:
            return (2*np.pi/D * r**2 * trueV(r, D-2))

    def ranradii(r,D,N):
        arr=np.zeros([N,1])
        for i in range(N):
            arr[i]=float(np.sqrt(sum(np.random.uniform(-r,r,size=(D,1))**2))) 
        return arr

    def volfind(r,D,N):
        xi=ranradii(r,D,N)   
        totalcount=0
        circlecount=0
        while totalcount < N:
            if xi[totalcount] <= r:
                circlecount +=1
            totalcount += 1
        vol=circlecount/totalcount * (2*r)**D            
        return vol
    
    def volerr(r,D,N):
        error = np.sqrt((1/(N*(N-1)))*sum((ranradii(r,D,N) - volfind(r,D,N))**2))
        return float(error)

    return [volfind(r,D,N), volerr(r,D,N)]
    #print("for a sphere in",D,"dimesnions, with radius",r,", volume =",volfind(r,D,N),"+/-",volerr(r,D,N),"compared to the real value of,",trueV(r,D))
