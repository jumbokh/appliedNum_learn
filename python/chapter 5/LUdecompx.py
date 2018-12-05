## module LUdecompx
''' a = LUdecompx(a)
    LUdecomposition: [L][U] = [a]

    x = LUsolve(a,b)
    Solution phase: solves [L][U]{x} = {b}
'''
import numpy as np
#from pf import *

def LUdecompx(a):
    n = len(a)
    L = np.eye(n, dtype = 'float')
    U = a
    for k in range(0,n-1):
        for i in range(k+1,n):
           if a[i,k] != 0.0:
               lam = U[i,k]/U[k,k]
               U[i,k+1:n] = U[i,k+1:n] - lam*U[k,k+1:n]              
               #U[i,k] = lam
               L[i,k]=lam
        #print(a)
    return U,L

def LUsolve(a,b):
    n = len(a)
    for k in range(1,n):
        b[k] = b[k] - np.dot(a[k,0:k],b[0:k])
    b[n-1] = b[n-1]/a[n-1,n-1]    
    for k in range(n-2,-1,-1):
       b[k] = (b[k] - np.dot(a[k,k+1:n],b[k+1:n]))/a[k,k]
    return b
