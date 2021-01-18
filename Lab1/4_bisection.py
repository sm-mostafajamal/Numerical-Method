# Write a program to find the root of the equation x^3 – 9x + 1 = 0, correct to 3 decimal places, by
# using the bisection method.

def func(x): 
	return x**3 - 9*x + 1

def bisection(a,b): 

	if (func(a) * func(b) >= 0): 
		print("You have not assumed right a and b\n") 
		return

	c = a 
	while ((b-a) >= 0.01): 

		# Find middle point 
		c = (a+b)/2

		# Check if middle point is root 
		if (func(c) == 0.0): 
			break

		# Decide the side to repeat the steps 
		if (func(c)*func(a) < 0): 
			b = c 
		else: 
			a = c 
			
	print("The value of root is : ","%.3f"%c) 
	
# Initial values assumed 
a = float(input("Enter value for 'a': "))
b = float(input("Enter value for 'b': "))
bisection(a, b) 

