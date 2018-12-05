## module Aitken
import numpy as np

def Aitken(A,w,n,tol=0.001):
    np.set_printoptions(precision=4)
    np.set_printoptions(suppress=True)
    print('iter     m       r     z(x)')
    m = np.zeros(n)
    for i in range(n):
          z = w/np.linalg.norm(w)
          w = np.dot(A,z)
          m[i] = np.dot(z.T,w)
          r = np.linalg.norm(m[i]*z-w)
          rr = str(r)
          print('{:<5}'.format(str(i+1)),m[0],'{:.5}'.format(rr),z.T)
          print('===============================================')
          if( r < tol):
              print('Power Method has coverged')
              break
    M = np.zeros(n)
    for k in range(3,n):
        M[k]=m[k]-np.square(m[k]-m[k-1])/((m[k]-m[k-1])-(m[k-1]-m[k-2]))
    return [m,z,M]