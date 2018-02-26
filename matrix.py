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
	new = new_matrix(rows = len(m1[0]), cols = len(m2))
	for r in range(len(m1[0])):
		for c in range(len(m2)):
			for i in range(len(m1)):
				ans[r][c] += (m1[r][i] * m2[i][c])
	return new



def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m
