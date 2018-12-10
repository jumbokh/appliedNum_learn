# QR_eig_G Module
"""
using Givens Rotation
"""
import numpy as np
from QR import *

def QR_eig_G(A,maxit,tol):
    np.set_printoptions(precision=4, suppress=True)
    (r,c) = np.shape(A)
    #tt = np.empty(c)
    for i in range(maxit):
        Q = np.eye(r)
        R = A
        (Q, R) = givens_rotation(A)
        A = R @ Q
        t = np.empty(r)
        for j in range(c-1):
            t[j] = max(abs(A[j+1:c,j]))
        tt = max(t)
        if tt < tol:
           print("QR method coverged",'step =%'%i)
           break
        print("K: ",i+1)
        for k in range(r):
           for o in range(c):
              print('%8.4f'%A[k][o],end=', ')
           print()
        print()
    e = np.diag(A)
    return e