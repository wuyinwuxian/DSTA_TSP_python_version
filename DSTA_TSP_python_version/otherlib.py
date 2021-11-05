import numpy as np
import matplotlib.pyplot as plt

def distance(Best,A):
    Best = np.append(Best,Best[0])
    n = Best.size
    Dist = 0 
    for i in range(n-1):
       Dist +=  np.linalg.norm(A[Best[i],:] - A[Best[i+1],:])
    return Dist

def draw(iter_k,Best,fBest,A):
    B = A[Best,:]
    B = np.r_[B,B[0,:].reshape(1,-1)]
    plt.plot(B[:,0],B[:,1],'b-o')
    plt.title("the {0}th iteration results: {1}".format(iter_k, fBest[0]))
    plt.savefig("./picture/" + str(iter_k) + ".png")   # 在 plt.show() 之前调用 plt.savefig() 不然全是空白
    plt.show()
    plt.clf()
            
    
    