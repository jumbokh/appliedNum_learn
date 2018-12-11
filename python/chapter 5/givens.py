# givens modules
import numpy as np

def givens(A):
    """Givens变换"""
    (r, c) = np.shape(A)
    Q = np.identity(r)
    R = np.copy(A)
    (rows, cols) = np.tril_indices(r, -1, c)
    for (row, col) in zip(rows, cols):
        if R[row, col] != 0:  # R[row, col]=0则c=1,s=0,R、Q不变
            r_ = np.hypot(R[col, col], R[row, col])  # d
            c = R[col, col]/r_
            s = -R[row, col]/r_
            G = np.identity(r)
            G[[col, row], [col, row]] = c
            G[row, col] = s
            G[col, row] = -s
            R = np.dot(G, R)  # R=G(n-1,n)*...*G(2n)*...*G(23,1n)*...*G(12)*A
            Q = np.dot(Q, G.T)  # Q=G(n-1,n).T*...*G(2n).T*...*G(23,1n).T*...*G(12).T
        print('k: ',row)
        print('x = %8.4f'%R[col, col],', %8.4f'%R[row, col])
        print('c = %8.4f'%c,',s = %8.4f'%s)
        print('R:')
        for l in range(len(A)):
            for m in range(len(A)):
                print('%8.4f'%R[l][m],end=', ')
            print()
    return (Q, R)