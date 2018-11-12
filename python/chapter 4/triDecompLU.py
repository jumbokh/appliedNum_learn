### module: triDecompLU
import numpy as np
from numpy import zeros
import scipy.linalg as alg

def matrixMul(A, B):
    return [[sum(ea*eb for ea,eb in zip(a,b)) for b in B] for a in A]

def pivotize(m):
        #Creates the pivoting matrix for m.
        n = len(m)
        ID = [[float(i == j) for i in range(n)] for j in range(n)]
        for j in range(n):
            row = max(range(j, n), key=lambda i: abs(m[i][j]))
            if j != row:
                ID[j], ID[row] = ID[row], ID[j]
        return ID

def lu(A):
        #Decomposes a nxn matrix A by PA=LU and returns L, U and P.
        n = len(A)
        # create zero array

        a = [A[0][1],A[1][2],A[2][3],A[3][4],0]
        d = [A[0][0],A[1][1],A[2][2],A[3][3],A[4][4]]
        b = [      0,A[1][0],A[2][1],A[3][2],A[4][3]]
        D = zeros([n])
        B = zeros([n])
        D[0]=d[0]
        for i in range(1,n):
          B[i] = b[i]/D[i-1]
          D[i] = d[i] - B[i]*a[i-1]
            
        #print(a)
        L = np.eye(n)
        U = np.zeros(n*n).reshape(n,n)        
        #U = [[0.0] * n for i in range(n)]
        for i in range(n):
            if i<n-1:
              U[i][i+1] = a[i]
              L[i+1][i] = B[i+1]
            U[i][i] = D[i]
        return L,U,B,D

def solve(A,r):
    return np.linalg.solve(A,r)