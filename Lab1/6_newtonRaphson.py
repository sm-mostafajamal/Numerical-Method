# Write a program to find the root of the equation x^4 - 12x + 7 = 0, correct to 3 decimal places, by
# using Newton-Raphson method.

def func( x ): 
	return x**4 - 12*x + 7

# Derivative of the above function 
# which is 4*x^3 - 12 
def derivFunc( x ): 
	return 4 * x**3 - 12 

# Function to find the root 
def newtonRaphson( x ): 
	h = func(x) / derivFunc(x) 
	while abs(h) >= 0.0001: 
		h = func(x)/derivFunc(x) 
		
		# x(i+1) = x(i) - f(x) / f'(x) 
		x = x - h 
	
	print("The value of the root is : ", "%.3f"% x) 

x0 = 0 # Initial values assumed 
newtonRaphson(x0) 

