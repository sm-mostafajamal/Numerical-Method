# Write a program to solve the following system of linear equations by using Matrix inversion
# method.
# x + y + z = 1
# x + 2y + 3z = 6
# x + 3y + 4z = 6

# Determinant 3x3
def determinant(mat):
	ans = (mat[0][0] * (mat[1][1] * mat[2][2] - mat[2][1] * mat[1][2]) -
		mat[0][1] * (mat[1][0] * mat[2][2] - mat[1][2] * mat[2][0]) +
		mat[0][2] * (mat[1][0] * mat[2][1] - mat[1][1] * mat[2][0]))
	return ans

def solution(coeff):   
	d = [[coeff[0][0], coeff[0][1], coeff[0][2]],
		 [coeff[1][0], coeff[1][1], coeff[1][2]],
		 [coeff[2][0], coeff[2][1], coeff[2][2]]]
	D = determinant(d)
	return D

# Transposing
def transpose(coeff):
	result = [[0,0,0],
			 [0,0,0],
			 [0,0,0]]

	for i in range(len(coeff)):
		# iterate through columns
		for j in range(len(coeff[0])):
			result[j][i] = coeff[i][j]
	trans=[]
	for k in result:
		trans.append(k)
	return trans

# Matrix Adjoint
def adj(mat):
    # Top
	a11 = (mat[1][1] * mat[2][2] - mat[2][1] * mat[1][2]) 
	a12 =	-(mat[1][0] * mat[2][2] - mat[1][2] * mat[2][0]) 
	a13 = (mat[1][0] * mat[2][1] - mat[1][1] * mat[2][0])
	# middle
	a21 = -(mat[0][1] * mat[2][2] - mat[2][1] * mat[0][2])
	a22 = (mat[0][0] * mat[2][2] - mat[2][0] * mat[0][2])
	a23 = -(mat[0][0] * mat[2][1] - mat[2][0] * mat[0][1])
	# last
	a31 = (mat[0][1] * mat[1][2] - mat[1][1] * mat[0][2])
	a32 = -(mat[0][0] * mat[1][2] - mat[1][0] * mat[0][2])
	a33 = (mat[0][0] * mat[1][1] - mat[1][0] * mat[0][1])

	total =[[a11,a12,a13],
			[a21,a22,a23],
			[a31,a32,a33]]
	return total


# multiplying A_inv to B 
def matmul(A, B):
    rowsA = len(A)
    colsA = len(A[0])
    rowsB = len(B)
    colsB = len(B[0])
    if colsA != rowsB:
        raise ArithmeticError('Number of A columns must equal number of B rows.')
    
    result = [[0],[0],[0]]
    for i in range(rowsA):
        for j in range(colsB):
            total = 0
            for k in range(colsA):
                total += A[i][k] * B[k][j]
            result[i][j] = total
 
    return result

# inversion
def A_inv(coeff,b):  
	total = len(coeff)
	d = [[0,0,0],
		[0,0,0],
		[0,0,0]]
	for i in range(total):
    		for j in range(total):
    				d[i][j] += coeff[i][j] / b 
	return d
    		

A = [[1, 1, 1],
    [1, 2, 3],
    [1, 3, 4]]
B =[[1],[6],[6]]

deter = solution(A)
trans = transpose(A)
adjoint = adj(trans)
A_inverse = A_inv(adjoint,deter)
X = matmul(A_inverse,B)

print(f'x={X[0]}, y={X[1]}, and z={X[2]}')