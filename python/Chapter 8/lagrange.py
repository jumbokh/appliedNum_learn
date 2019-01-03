# module lagrange

import numpy as np
import matplotlib.pyplot as plt

def LagrangeCoef(x,y):
    n = len(x)
    c = np.zeros(n)
    d = np.zeros(n)
    for k in range(n):
        d[k] = 1.0
        for i in range(n):
            if i != k:
                d[k] = d[k]*(x[k]-x[i])
            c[k] = y[k]/d[k]
    return c

def LagrangeEval(t,x,c):
    m = len(x)
    n = len(t)
    p = np.zeros(n)
    N = np.zeros(m)
    for i in range(n):
        p[i]=0
        for j in range(m):
            N[j] = 1
            for k in range(m):
                if j != k:
                    N[j] = N[j] * (t[i] - x[k])
            p[i] = p[i] + N[j] * c[j]
    return p

def plotp(x,y,left,right,gap,c):
     t = np.arange(left,right,gap)
     p = np.zeros(len(t))
     p = LagrangeEval(t,x,c)
     plt.plot(x, y, 'o', t,p,'--')
     plt.xlabel('x')
     plt.legend(('Data','eval'),loc = 0)
     plt.grid(True)
     plt.show()