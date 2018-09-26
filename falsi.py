
# coding: utf-8

# In[ ]:


## module falsi
''' root = ridder(f,a,b,tol=1.0e-9).
    Finds a root of f(x) = 0 with rule of false position method.
    The root must be bracketed in (a,b).
'''
import error
import math
from numpy import sign

def falsi(f,a,b,tol=1.0e-9):   
    fa = f(a)
    if fa == 0.0: return a
    fb = f(b)
    if fb == 0.0: return b
    if sign(fa) == sign(fb): error.err('Root is not bracketed')
    for i in range(30):
      # Compute the improved root x from falsi formula
        
        s = b - fb*(b-a)/(fb-fa)
        fx = f(s)
        if s == 0.0: return None
        
      # Test for convergence
        if i > 0:
            if abs(s - xOld) < tol*max(abs(s),1.0): return s
        xOld = s
      # Re-bracket the root as tightly as possible
        if sign(fx) == sign(fa): 
             b = s; fb = fx
        else: a = s; fa = fx
        print('{0:8.6f}'.format(a),'{0:8.6f}'.format(b),'{0:8.6f}'.format(s),'{0:8.6f}'.format(fx))    
    return None
    print('Too many iterations')

