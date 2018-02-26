import math


def print_matrix(matrix):
    for i in range(len(matrix[0])):
        row = ""
        for x in matrix:
           row += str(x[i]) + " "
        print row

def ident(matrix):
    for c in range(len(matrix)):
        for r in range(len(matrix[0])):
            if (c == r):
                matrix[c][r] = 1
            else:
                matrix[c][r] = 0
    return matrix

#m1 * m2 -> m2
def matrix_mult(m1, m2):
    m = [[] for x in range(0,4)]
    m3 = []
    row = 0
    for r in range(0,4):
        for c in range(0,len(m2[0])):
            sum = 0
            for i in range(0,len(m1[0])):
                prod = m1[i][r] * m2[c][i]
                sum += prod
            m[r].append(sum)
    m2[:] = list(m)



def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m
