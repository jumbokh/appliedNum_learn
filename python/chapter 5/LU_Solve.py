## LU_Solve module

import numpy as np
'''
Ax=b , A=LU==> LUx=b,  Uy=b,  Lx=y
but
if Permutation
PAx=Pb, PA=LU, c=Pb

Array 切片見： http://www.zmonster.me/2016/03/09/numpy-slicing-and-indexing.html
''' 

def LU_Solve(L, U, b):
    n = len(L)
    z = np.zeros(n)
    x = np.zeros(n)
    # Lz=b  
    z[0] = b[0]
    for i in range(1,n):
        z[i] = b[i] - L[i][:i-1]* z[:i-1]
    #print(z)
    x[n-1] = z[n-1] / U[n-1][n-1]
    for i in range(1,n):
        x[i] = z[i] - U[i][i+1:n] * x[i+1:n]/U[i][i]
    return x