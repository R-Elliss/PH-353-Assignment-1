import numpy as np

def trueV(n, R):  #works for any d > 0
    if n == 0:
        return 1   #0D case
    elif n == 1:
        return 2*R   #1D case
    else:
        return (2*np.pi/n * R**2 * trueV(n-2, R))

def ranradii(n,R,N):
    arr=np.zeros([N,1])
    for i in range(N):
        arr[i]=float(np.sqrt(sum(np.random.uniform(-R,R,size=(n,1))**2)))
    #print(arr)
    return arr

def volfind(n,R,N):
    xi=ranradii(n,R,N)   
    totalcount=0
    circlecount=0
    while totalcount < N:
        if xi[totalcount] <= 1:
            circlecount +=1
        totalcount += 1
    vol=circlecount/totalcount * (2*R)**n            
    #print(xi)
    print("for a sphere in",n,"dimesnions, with radius",R,"volume =",vol,"compared to the real value of,",trueV(n,R))
    return
    