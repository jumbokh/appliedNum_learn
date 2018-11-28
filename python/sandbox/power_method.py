# L-14 MCS 507 Fri 27 Sep 2013 : power_method.py

"""
The script is a very simple illustration using numpy
of the power method to compute an approximation for
the largest eigenvalue of a complex matrix.
"""

import numpy as np

def power_method(mat, start, maxit):
    """
    Does maxit iterations of the power method
    on the matrix mat starting at start.
    Returns an approximation of the largest
    eigenvector of the matrix mat.
    """
    result = start
    for i in xrange(maxit):
        result = mat*result
        result = result/np.linalg.norm(result)
    return result

def check(mat, otp):
    """
    Compares the output otp of the power
    method with the largest eigenvalue
    of the matrix mat.
    """
    prd = mat*otp
    eigval = prd[0]/otp[0]
    print 'computed eigenvalue :' , eigval
    [eigs, vecs] = np.linalg.eig(mat)
    abseigs = list(abs(eigs))
    ind = abseigs.index(max(abseigs))
    print ' largest eigenvalue :', eigs[ind]

def main():
    """
    Prompts the user for a dimension
    and the number of iterations.
    """
    print 'Running the power method...'
    dim = input('Give the dimension : ')
    nbit = input('How many iterations ? ')
    j = complex(0, 1)
    rnd = np.random.normal(0, 1, (dim, dim)) \
        + np.random.normal(0, 1, (dim, dim))*j
    nbs = np.random.normal(0, 1, (dim, 1)) \
        + np.random.normal(0, 1, (dim, 1))*j
    rndmat = np.matrix(rnd)
    rndvec = np.matrix(nbs)
    eigmax = power_method(rndmat, rndvec, nbit)
    check(rndmat, eigmax)

main()