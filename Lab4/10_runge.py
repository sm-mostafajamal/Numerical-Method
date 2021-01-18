# Write a program to solve the following Differential Equation by using Runge – Kutta method.
# dy / dx = x^2 + y^2 , y (0) = 0. Compute y (0.4) taking h = 0.2

def func(x, y): 
	return x**2 + y**2

def rungeKutta(x0, y0, x, h): 
	y = y0 
	for i in range(n): 
		m1 =  func(x0, y) 
		m2 =  func(x0 + h/2, y + m1*h/2) 
		m3 =  func(x0 + h/2, y + m2*h/2) 
		m4 =  func(x0 + h, y + m3*h) 
		y = y + ((m1 + 2 * m2 + 2 * m3 + m4)/6)*h 

		x0 = x0 + h 
	return y 
    
x0 = 0
y0 = 0
x = 0.4
h = 0.2
n = int(input('Number of steps: '))

print('The value of y(0.4) is:', rungeKutta(x0, y0, x, h))

