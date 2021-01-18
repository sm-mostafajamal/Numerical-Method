# Consider the following ordinary differential equation.
# 10 dy/dx = x2 + y2, y (0) = 1

# for the interval 0 < x ≤ 0.4, with h = 0.1.
# Solve the equation using Fourth order Runge-Kutta method.

def func(x, y): 
	return (x**2 + y**2)/10

def rungeKutta(x0, y0, x, h):
    y = y0
    for i in range(n):
        m1 =  func(x0, y)
        m2 =  func(x0 + h/2, y + m1*h/2)
        m3 =  func(x0 + h/2, y + m2*h/2)
        m4 =  func(x0 + h, y + m3*h)
        y = y + ((m1 + 2 * m2 + 2 * m3 + m4)/6)*h
        print('At x=%.4f, y=%.4f' %(x0,y))
        x0 = x0 + h


x0 = 0
y0 = 1
x = 0.4
h = 0.1
n = int(input('Number of steps: '))
rungeKutta(x0, y0, x, h)


