from fractions import *
from decimal import *

def pf(number):
              
    f = Fraction(Decimal(number)).limit_denominator(1000)
    fstr = str(f)
    print('{:>5}'.format(fstr))
