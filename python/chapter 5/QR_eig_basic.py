# QR_eig_basic module
###
### 用QR因式分解求特徵值
### 利用第四章的分解函數
 
import numpy as np
from QR_Factor import *

def QR_eig_basic(A,maxit):
    np.set_printoptions(precision=4, suppress=True)
    (r,c) = np.shape(A)
    for k in range(maxit):
        # A＝　ＱＲ　＝＞　Ｒ＝Ｑ’Ａ
        (Q,R,c) = QR_Factor(A)
        # 定義新的 A=RQ=Q'AQ
        A = R @ Q 
        print('K = ',k+1)
        for i in range(r):
            for j in range(c):
               print('%8.4f'%A[i][j],end=' ')
            print()
    e = np.diag(A)
    return e

