# Write a program to evaluate a polynomial by using Horner's rule.

def horner(poly, n, x): 

	result = poly[0] 

	for i in range(1, n): 
		result = result*x + poly[i] 
	return result 


# Let us evaluate value of 
# 2x^3 - 6x^2 + 2x - 1 for x = 3 
poly = [2, -6, 2, -1] 
x = 3
n = len(poly) 

print("Value of polynomial is " , horner(poly, n, x)) 

