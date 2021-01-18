def determinant(mat):
    ans = (mat[0][0] * (mat[1][1] * mat[2][2] - mat[2][1] * mat[1][2]) -
		mat[0][1] * (mat[1][0] * mat[2][2] - mat[1][2] * mat[2][0]) +
		mat[0][2] * (mat[1][0] * mat[2][1] - mat[1][1] * mat[2][0]))
    return ans

# def solution(coeff):   
# 	d = [[coeff[0][0], coeff[0][1], coeff[0][2]],
# 		 [coeff[1][0], coeff[1][1], coeff[1][2]],
# 		 [coeff[2][0], coeff[2][1], coeff[2][2]]]
# 	D = determinant(d)
# 	return D

A = [[3, 1, 2],
    [2, -3, -1],
    [1, 2, 1]]
deter = determinant(A)
print(deter)