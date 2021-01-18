# Write a program to solve the following Differential Equation by using Euler’s method.
# dy / dx = 3x^2 + 1, y (1) = 2. Compute y (2) taking h = 0.25.

def func( x, y ): 
	return (3*x**2 + 1) 
	
# euler formula 
def euler( x0, y, h, x ): 
	for i in range(n): 
		y = y + h * func(x0, y) 
		x0 = x0 + h 
	print("solution at y(2) or x =", x, " is ", "%.4f"% y) 
	
x0 = 1
y0 = 2
h = 0.25
x = 2

n = int(input('Number of steps: '))
euler(x0, y0, h, n) 
