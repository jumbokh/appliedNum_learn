# module power_B
import numpy as np

def power_B(A,z,n):
    np.set_printoptions(precision=2)
    np.set_printoptions(suppress=True)
    for i in range(n):
          w = np.dot(A,z)
          print('w=Az=',w.T) 
          w1 = max(w)
          print('new w:',w1)
          z = w/w1
          print('z:',z.T)
          print('=====================')
    return [w1,z]