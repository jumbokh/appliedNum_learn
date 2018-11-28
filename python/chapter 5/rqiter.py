"""
Sample code for Rayleigh quotient iteration applied to 
shift matrix.
"""

from pylab import *

A = array([[4,2/3,-4/3,4/3],[2/3,4,0,0],[-4/3,0,6,2],[4/3,0,2,6]])

print "\nA = "
print A

lam,X = eig(A)

print "\nEigenvalues: ",lam

v = randn(4)
print "\nStarting guess v: ",v
print " "

mu = 1. + 1j
print "k = %s, mu = %21.16f + %21.16fj" %  (0,mu.real,mu.imag)

for k in range(1,10):
    B = A - mu*eye(4)
    try:
        w = solve(B,v)
    except:
        print "Matrix is singular!   Converged solution"
        break
    v = w / norm(w,2)
    mu = dot(conj(v.T), dot(A,v))
    print "k = %s, mu = %21.16f + %21.16fj" %  (k,mu.real,mu.imag)


