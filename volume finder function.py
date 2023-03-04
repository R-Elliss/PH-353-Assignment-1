import numpy as np

def assignmentest():
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
    N = 10000 # this is incredibly accurate for N = 10,000,000 but it takes like 3 mins to run for 2d 
    
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
        error = float(np.sqrt((1/(N*(N-1)))*sum((xi - vol)**2)))#folded the error function into the main finder and used the array of variables used for finding the volume            
        return vol,error #print("volume =",vol,"+/-",error)
    
    #def volerr(r,D,N):
        #error = np.sqrt((1/(N*(N-1)))*sum((ranradii(r,D,N) - volfind(r,D,N))**2))
        #return float(error)

    return volfind(r,D,N)
    #print("for a sphere in",D,"dimesnions, with radius",r,", volume =",volfind(r,D,N),"+/-",volerr(r,D,N),"compared to the real value of,",trueV(r,D))


def assignment():
    dimarr=np.zeros([10,3])
    radarr=np.zeros([10,3])
    for i in range(10):
        dimarr[i,0]=i+1
        dimarr[i,1]=Volume(1,i+1)[0]
        dimarr[i,2]=Volume(1,i+1)[1]
        radarr[i,0]=(i+1)/2
        radarr[i,1]=Volume(((i+1)/2),3)[0]
        radarr[i,2]=Volume(((i+1)/2),3)[1]
    np.savetxt("dimensions1to10.txt",dimarr)
    np.savetxt("radii1to5.txt",radarr)
    return dimarr,radarr