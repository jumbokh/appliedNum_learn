__author__ = 'Florian Cassayre'

from copy import copy, deepcopy


def inverse(toInverse):
    size = len(toInverse)

    matrix = [[0 for j in range(size * 2)] for i in range(size)] # Matrix n x 2n

    for i in range(size): # We copy the matrix to reverse
        for j in range(size):
            matrix[i][j] = toInverse[i][j]

    for i in range(size): # We add the identity matrix
        matrix[i][i + size] = 1

    matrix = gaussJordanElimination(matrix) # We stagger

    if isZero(matrix[size - 1][size - 1]):
        return None

    inverted = [[0 for j in range(size)] for i in range(size)]
    for i in range(size): # We recover our inverse
        for j in range(size):
            inverted[i][j] = matrix[i][j + size]

    return inverted

def gaussJordanElimination(matrix):
    lines = len(matrix)
    columns = len(matrix[0])

    copy = deepcopy(matrix) # Copy the matrix to avoid changing the original

    r = -1

    for j in range(columns):

        k = r + 1

        for i in range(r + 1, lines): # Find the maximum value of the column
            if(not isZero(copy[i][j])):
                k = i
        if(k >= lines): # We go out as soon as we have done all the lines
            break

        if(not isZero(copy[k][j])):
            r += 1
            pivotDivider = copy[k][j]
            for j1 in range(columns): # Division of the line
                copy[k][j1] = copy[k][j1] / pivotDivider

            tempLine = copy[k] # Exchange of two lines in three stages
            copy[k] = copy[r]
            copy[r] = tempLine

            for i in range(lines): # Reduction of other lines
                lineDivider = copy[i][j]
                if(i != r):
                    for j1 in range(columns):
                        copy[i][j1] -= copy[r][j1] * lineDivider

    return copy

def isZero(number):
    return abs(number) < 1E-10

# Tests

size = 3

# We want to invert the following matrix:

toInverse = [[0 for j in range(size)] for i in range(size)]
toInverse[0] = [1, 2, 3]
toInverse[1] = [4, 5, 6]
toInverse[2] = [7, 8, 9]

print(inverse(toInverse)) # "None" because the matrix is not invertible!