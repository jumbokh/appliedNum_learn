## module bisectionx
''' root = bisection(f,x1,x2,switch=0,tol=1.0e-9).
    Finds a root of f(x) = 0 by bisection.
    The root must be bracketed in (x1,x2).
    Setting switch = 1 returns root = None if
    f(x) increases upon bisection.
'''    
import math
import error
from numpy import sign

def bisectionx(f,x1,x2,switch=1,tol=1.0e-9):
    logdat=[]
    f1 = f(x1)
    if f1 == 0.0: return x1,logdat
    f2 = f(x2)
    if f2 == 0.0: return x2,logdat
    if sign(f1) == sign(f2):
        error.err('Root is not bracketed')
    n = int(math.ceil(math.log(abs(x2 - x1)/tol)/math.log(2.0)))
    
    for i in range(n):
        x3 = 0.5*(x1 + x2); f3 = f(x3)
        #print('{0:6.4f}'.format(x1),'{0:8.6f}'.format(x2),'{0:8.6f}'.format(x3),'{0:8.6f}'.format(f1),'{0:8.6f}'.format(f2),'{0:8.6f}'.format(f3))
        logdat.append([round(x1,4),round(x2,4),round(x3,4),round(f1,4),round(f2,4),round(f3,4)])
        if (switch == 1) and (abs(f3) > abs(f1)) \
                         and (abs(f3) > abs(f2)):
            return None,logdat   
        if f3 == 0.0: return x3,logdat
        if sign(f2)!= sign(f3): x1 = x3; f1 = f3
        else: x2 = x3; f2 = f3
    return (x1 + x2)/2.0,logdat
