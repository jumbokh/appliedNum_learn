from fractions import *
from decimal import *

def ppmat(matrix):
    size = len(matrix[0])
    #print(size)
    print()
    for a in matrix:
        for i in range(size):
            
            number = a[i]
            
            f = Fraction(Decimal(number)).limit_denominator(1000)
            fstr = str(f)
            print('{:>5}'.format(fstr),'  ',end="")

            if i < size-1 :
              print(", ",end="")
        print()