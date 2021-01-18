# Write a program to solve the following system of linear equations by using Cramer’s Rule:
# 27x + 6y – z = 85
# 6x + 15y + 2z = 72
# x + y + 54z = 110

def determinant(mat):
	ans = (mat[0][0] * (mat[1][1] * mat[2][2] - mat[2][1] * mat[1][2]) -
		   mat[0][1] * (mat[1][0] * mat[2][2] - mat[1][2] * mat[2][0]) +
		   mat[0][2] * (mat[1][0] * mat[2][1] - mat[1][1] * mat[2][0]))
	return ans


def solution(coeff):

	d = [[coeff[0][0], coeff[0][1], coeff[0][2]],
		 [coeff[1][0], coeff[1][1], coeff[1][2]],
		 [coeff[2][0], coeff[2][1], coeff[2][2]]]
	
	d1 = [[coeff[0][3], coeff[0][1], coeff[0][2]],
		 [coeff[1][3], coeff[1][1], coeff[1][2]],
		 [coeff[2][3], coeff[2][1], coeff[2][2]]]
	
	d2 = [[coeff[0][0], coeff[0][3], coeff[0][2]],
		 [coeff[1][0], coeff[1][3], coeff[1][2]],
		 [coeff[2][0], coeff[2][3], coeff[2][2]]]
	
	d3 = [[coeff[0][0], coeff[0][1], coeff[0][3]],
		 [coeff[1][0], coeff[1][1], coeff[1][3]],
		 [coeff[2][0], coeff[2][1], coeff[2][3]]]

	# Calculating Determinant of Matrices 
	D = determinant(d)
	D1 = determinant(d1)
	D2 = determinant(d2)
	D3 = determinant(d3)
	
	print("D is : ", D)
	print("D1 is : ", D1)
	print("D2 is : ", D2)
	print("D3 is : ", D3)

	if (D != 0):
		x = D1 / D
		y = D2 / D
		z = D3 / D 
		
		print("Value of x is : ", x)
		print("Value of y is : ", y)
		print("Value of z is : ", z)

	else:
		if (D1 == 0 and D2 == 0 and D3 == 0):
			print("Infinite solutions")
		elif (D1 != 0 or D2 != 0 or D3 != 0):
			print("No solutions")

    
coeff = [[27, 6, -1, 85],
        [6, 15, 2, 72],
        [1, 1, 54, 110]]

solution(coeff)

