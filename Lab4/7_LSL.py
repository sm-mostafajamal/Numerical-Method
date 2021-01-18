# Write a program to find the least square line y = a + bx for the following data
# x -2 1 0 1 2
# y 1 2 3 3 4

def calculateB(x, y, n):

	# sum of array x, y, xy and x^2 
	sx = sum(x)
	sy = sum(y)
	sxsy = 0
	sx2 = 0

	for i in range(n):
		sxsy += x[i] * y[i]
		sx2 += x[i] * x[i]
	a = (sy*sx2 - sx * sxsy)/(n * sx2 - sx ** 2)
	b = (n * sxsy - sx * sy)/(n * sx2 - sx ** 2)
	return a, b

def leastSquareLine(X,Y,n):
    	
	a, b = calculateB(X, Y, n)
	
	print("Least square line is:")
	print("Y = ", '%.4f'%a, " + ", '%.4f'%b, " * X", sep="")

X = [-2, 1, 0, 1,  2]
Y = [1, 2, 3, 3, 4]
n = len(X)

leastSquareLine(X, Y, n)

