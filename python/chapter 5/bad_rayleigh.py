# module rayleigh
import numpy as np

def rayleigh(A,z,n,tol=0.0001):
    np.set_printoptions(precision=4)
    np.set_printoptions(suppress=True)
    print('iter       w1    r  z(x)')
    for i in range(n):

          m = np.dot(A,z)
          w1 = max(abs(m))
          z = m/w1
          w = np.dot(A,z)
          r = np.linalg.norm(w-w1*z)
          print(i+1,w1,r,z.T)
          print('===============================================')
          if( r < tol):
              print('Power Method has coverged')
              break
    return [w1,z]