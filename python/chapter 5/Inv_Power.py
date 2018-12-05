## Inv_Power module

import numpy as np
import scipy.linalg as ALG

def inv_power(H,maxit,tol):
    n = len(H)
    L = np.eye(n)
    U = H
    #U,L = LU_Factor(H)
    P,L,U= ALG.lu(H,permute_l = False)
    w = np.ones(n)
    print('iter     m      r      z(n)')
    for i in range(maxit):
        z = w / np.linalg.norm(w)
        c = P @ z
        #w = LU_Solve(L,U,c)
        # 解 Ly = c
        y = np.linalg.solve(L,c)
        # 解 Ux = y
        w = np.linalg.solve(U,y)
        m = np.dot(z.T,w)
        r = np.linalg.norm(np.dot(m,z) - w)
        print(i+1,'%10.4f'%m,'%8.4f'%r,end='')
        for j in range(len(z)):
            print('%8.4f'%z[j],end='')
        print()
        if r < tol:
           print('Inv Power Method has coverged')
           break
    mm = 1/m
    return z,mm