# Write a program to find the root of the equation x^3 – 5x^2 - 29 = 0, correct to 3 decimal places,
#  by using secant method.
def f(x):
    return x**3 - 5*x*2 - 0

def secant(x0,x1,e,N):
    print('\n\n SECANT METHOD IMPLEMENTATION ')
    step = 1
    condition = True
    while condition:
        if f(x0) == f(x1):
            print('Divide by zero error!')
            break
        
        x2 = x0 - (x1-x0)*f(x0)/( f(x1) - f(x0) ) 
        print('Iteration-%d, x2 = %0.6f and f(x2) = %0.6f' % (step, x2, f(x2)))
        x0 = x1
        x1 = x2
        step = step + 1
        
        if step > N:
            print('Not Convergent!')
            break
        
        condition = abs(f(x2)) > e
    print('\nRequired root is: %0.3f' % x2)

x0 = float(input('Enter First Guess: '))
x1 = float(input('Enter Second Guess: '))
e = float(input('Tolerable Error: '))
N = int(input('Maximum Step: '))

secant(x0,x1,e,N)