## module rayleigh
import numpy as np

def rayleigh(A,w,n,tol=0.001):
    np.set_printoptions(precision=4)
    np.set_printoptions(suppress=True)
    print('iter     m       r     z(x)')
    for i in range(n):
          # power_B
          #w0 = np.dot(A,w)
          #m0 = max(abs(w0))
          # Rayleigh
          z = w/np.linalg.norm(w)
          w = np.dot(A,z)
          m = np.dot(z.T,w)
          r = np.linalg.norm(m*z-w)
          rr = str(r)
          print('{:<5}'.format(str(i+1)),m[0],'{:.5}'.format(rr),z.T)
          print('===============================================')
          if( r < tol):
              print('Power Method has coverged')
              break
    return [m[0],z]