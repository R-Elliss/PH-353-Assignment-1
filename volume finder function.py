import numpy as np

def Volume(r,D):
    N = 1000 # this is incredibly accurate for N = 10,000,000 but it takes like 3 mins to run for 2d 
    
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
        #error = float(np.sqrt((1/(N*(N-1)))*sum((xi - vol)**2)))#folded the error function into the main finder and used the array of variables used for finding the volume            
        error = np.sqrt((1/(N*(N-1)))*np.abs(sum(xi - (1/N*sum(xi)**2))))
        return vol,error #print("volume =",vol,"+/-",error)
    

    return volfind(r,D,N)

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