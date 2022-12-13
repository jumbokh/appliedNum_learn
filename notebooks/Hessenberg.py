# Hessenberg module
import numpy as np
import math

def Hessenberg(A):
    (n, nn) = np.shape(A)
    np.set_printoptions(precision=4, suppress=True)
    for k in range(n-2):
        #x = np.zeros(n)
        w = np.zeros(n)
        C = np.zeros(shape=(n,nn))
        d = 0.0
        x = A[:,k]
        x = np.array([aa if i > k else 0 for i,aa in enumerate(x)])
        p = np.sign(x[k+1])
        if p == 0.0:
            p = 1
        g = np.linalg.norm(x)
        s = math.sqrt(2*g*(g+p*(x[k+1])))
        B = np.copy(A)
        if s != 0.0:
            w = x/s
            w[k+1] = (x[k+1]+p*g)/s
            w = w.reshape(-1,1)
            wt = w.reshape(1,-1)
            C = np.matmul(w,wt)
            d = np.matmul(np.matmul(wt,A),w)
            B = A - 2.0*np.dot(C,A) - 2.0 *np.dot(A,C) + 4.0 * d * C
        A = np.copy(B)
        print('k:',k+1)
        print('x = ',x.T)
        print('g = %8.4f'%g)
        print('s = %8.4f'%s)
        print('w = ',wt)
        print('d = ',d)
        print('C=',C)
        print('B=',B)
    return A