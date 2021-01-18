# The following values of f (x) are given.
# x 5 6 9 11
# y = f(x) 12 13 14 16
# Write a program to find the values of x for which f (x) = 13.5 by using Lagrange’s inverse
# interpolation formula.

# Consider a structure 
# to keep each pair of 
# x and y together 
class Data: 
	def __init__(self, x, y): 
		self.x = x 
		self.y = y 

# Function to calculate the inverse interpolation 
def inv_interpolate(d: list, n: int, y: float) -> float: 
	# Initialize final x 
	x = 0
	for i in range(n): 
		# Calculate each term of the given formula 
		xi = d[i].x 
		for j in range(n): 
			if j != i: 
				xi = (xi * (y - d[j].y) /(d[i].y - d[j].y)) 

		# Add term to final result 
		x += xi 
	return x 

if __name__ == "__main__": 
	# Sample dataset of 4 points Here we find the value 
	# of x when y = 13.5 
	d = [Data(5, 12), 
		Data(6, 13), 
		Data(9, 14), 
		Data(11, 16)] 

	# Size of dataset 
	n = 4

	# Sample y value 
	y = 13.5

	# Using the Inverse Interpolation 
	print("Value of x at y = 13.5 :", round(inv_interpolate(d, n, y), 5)) 
