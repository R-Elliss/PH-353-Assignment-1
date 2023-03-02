import numpy as np

def assignment():
    #1) 
    results_1 = np.zeros((10,3), dtype='float')
    for D in range(1,11):
        temp = np.array_split(Volume(1,D),2)
        results_1[D-1,:] = [D,temp[0],temp[1]]
        print(results_1)
    
    #np.savetxt("D data.txt", results_1)
    '''    #unable to get this to work for now will try again soon but the need 
    # for this to be an arange is causing problems when trying to reslice the arrays back into 1 array
    #1 possible solution for this is to avoid using floats casting the loop and 
    # instead just doing 2r then doing 2r/2 where needed but this doesn't quite feel right although could be done as a last resort
    
    #2)
    results_2 = np.empty((9,3), dtype='float')
    for r in np.arange(1,5.5,0.5):
        results_2[r-1,:] = np.concatenate((results_2, np.array_split(Volume(r,3),2)),axis=1)
        #temp = np.array_split(Volume(r,3),2)   #splits output of Volume into 2 arrays, 1 for volume the other for error
        #results_2[r-1,:] = np.array([r,temp[0],temp[1]])
        print(results_2)
    '''    
    return results_1, #results_2

def Volume(r,D):
    N = 100000 # this is incredibly accurate for N = 10,000,000 but it takes like 3 mins to run for 2d 
    
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
