# QR_Factor module

import numpy as np
def QR_Factor(A):
    (r,c) = np.shape(A)
    Q = np.identity(r)
    R= np.copy(A)
    for i in range(r - 1):
        x = R[i:,i]
        e = np.zeros_like(x)
        e[0] = np.linalg.norm(x)
        u = x - e
        v = u / np.linalg.norm(u)
        Q_i = np.identity(r)
        Q_i[i:,i:] -= 2.0 * np.outer(v,v)
        R = np.dot(Q_i,R)
        Q = np.dot(Q,Q_i)
    return (Q,R,c)