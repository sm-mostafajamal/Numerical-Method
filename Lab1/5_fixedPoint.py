# Write a program to find the root of the equation x^5 + 3x^2 - 10 = 0, correct to 3 decimal places,
# by the using fixed point method.

import math

def f(x):
    return x**5 + 3*x**2 -10

# Re-writing f(x)=0 to x = g(x)
def g(x):
    return 1/math.sqrt(1+x)

# Implementing Fixed Point Iteration Method
def fixedPointIteration(x0, e, N):
    print('\n\n FIXED POINT ITERATION ')
    step = 1
    flag = 1
    condition = True
    while condition:
        x1 = g(x0)
        print('Iteration-> %d, x1 = %0.6f and f(x1) = %0.6f' % (step, x1, f(x1)))
        x0 = x1

        step = step + 1
        
        if step > N:
            flag=0
            break
        
        condition = abs(f(x1)) > e

    if flag==1:
        print('\nRequired root is: %0.3f' % x1)
    else:
        print('\nNot Convergent.')


x0 = float(input('Enter Guess: '))
e = float(input('Tolerable Error: '))
N = int(input('Maximum Step: '))

fixedPointIteration(x0,e,N)